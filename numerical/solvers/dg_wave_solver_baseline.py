"""
Discontinuous Galerkin Wave Solver with Adaptive Mesh Refinement

This module implements a high-order Discontinuous Galerkin (DG) solver for the 1D wave equation
with h-adaptation capabilities using hierarchical mesh refinement. The solver uses:
- Legendre-Gauss-Lobatto (LGL) nodal basis functions
- Upwind numerical fluxes for interface treatment
- Low-storage Runge-Kutta time integration
- Hierarchical mesh refinement with solution projection
"""

import numpy as np
from scipy.sparse.linalg import gmres
from ..dg.basis import lgl_gen, Lagrange_basis
# from ..dg.matrices import (create_mass_matrix, create_diff_matrix, 
#                       Fmatrix_upwind_flux, Matrix_DSS, create_RM_matrix, Fmatrix_centered_flux, Fmatrix_upwind_flux_bc)
from ..dg.matrices import *
from ..grid.mesh import create_grid_us
from ..amr.forest import forest
from ..amr.adapt import adapt_mesh, adapt_sol, mark, check_balance, enforce_balance
from ..amr.projection import projections
from .utils import exact_solution, eff

class DGWaveSolverBaseline:
    """
    Discontinuous Galerkin solver for baseline AMR evaluation.
    
    Supports two modes:
    - no-amr: Fixed mesh at specified refinement level
    - conventional-amr: Threshold-based adaptation using criterion=1
    
    
    This solver implements:
    - Modal DG discretization with LGL nodes
    - Hierarchical h-refinement for mesh adaptation
    - Solution projection between refined/coarsened elements
    - Low-storage RK time integration
    
    Attributes:
        nop (int): Polynomial order for the DG basis functions
        ngl (int): Number of LGL points per element (nop + 1)
        nelem (int): Current number of elements in mesh
        xelem (array): Element boundary coordinates
        max_level (int): Maximum allowed refinement level
        max_elements (int): Maximum allowed number of elements
        dt (float): Current time step size
        time (float): Current simulation time
        icase (int): Test case identifier for initial/exact solutions
        dx_min (float): Minimum element size based on max refinement
        q (array): Current solution vector
        wave_speed (float): Wave propagation speed for the equation
    """
    def __init__(self, nop, xelem, max_elements, max_level, courant_max=0.1, 
             icase=1, periodic=True, verbose=False, balance=False,
             amr_mode='no-amr', threshold=0.5):
        """
        Initialize the DG wave solver with AMR capabilities.
        
        Args:
            nop (int): Polynomial order for basis functions
            xelem (array): Element boundary coordinates
            max_elements (int): Maximum number of elements allowed
            max_level (int): Maximum refinement level allowed
            courant_max (float): Maximum Courant number for time step calculation
            icase (int): Test case identifier
            verbose (bool): Whether to print detailed diagnostic information
        """
        self.nop = nop
        self.xelem = xelem
        self.max_elements = max_elements 
        self.ngl = nop + 1
        self.nelem = len(xelem) - 1
        self.max_level = max_level
        self.icase = icase
        self.time = 0.0
        self.dx_min = np.min(np.diff(xelem)) / (2**max_level)
        self.courant_max = courant_max
        self.xgl, self.wgl = lgl_gen(self.ngl)
        self.nq = self.nop + 2
        self.xnq, self.wnq = lgl_gen(self.nq)
        self.psi, self.dpsi = Lagrange_basis(self.ngl, self.nq, self.xgl, self.xnq)
        self.periodic = periodic
        self.balance = balance
        self.verbose = verbose
        self.amr_mode = amr_mode
        self.threshold = threshold
        
        self._initialize_mesh()
        self.q = self._initialize_solution()

        # self.q = np.zeros(len(self.coord))
        # self.wave_speed = 2.0

        self.qe =self.get_exact_solution()
        self._compute_timestep(use_actual_max_level=True)
        # self._compute_timestep(courant_max)
        self._initialize_projections()
        self.f = self._initialize_forcing()
        self._update_matrices()
        self.q = self.steady_solve_improved()
        
    def _initialize_mesh(self):
        """Initialize the mesh and grid structures."""
        self.npoin_cg = self.nop * self.nelem + 1
        self.npoin_dg = self.ngl * self.nelem
        self.label_mat, self.info_mat, self.active = forest(self.xelem, self.max_level)
        self.coord, self.intma, self.periodicity = create_grid_us(
            self.ngl, self.nelem, self.npoin_cg, self.npoin_dg, 
            self.xgl, self.xelem
        )
        
    def _initialize_solution(self):
        """Initialize the solution based on test case."""
        q, self.wave_speed = exact_solution(
            self.coord, self.npoin_dg, self.time, self.icase
        )
        return q
        # return self.steady_solve_improved()
    
    # def _initialize_forcing(self):
    #     """Initialize the forcing function based on test case."""
    #     f = eff(self.coord, self.npoin_dg, self.icase, self.wave_speed)
    #     return f
    def _initialize_forcing(self):
        """Initialize the forcing function based on test case."""
        self.f = eff(self.coord, self.npoin_dg, self.icase, self.wave_speed, self.time)
        return self.f
    
    def _update_forcing(self):
        self.f = eff(self.coord, self.npoin_dg, self.icase, self.wave_speed, self.time)
        return self.f

    
    # def _compute_timestep(self, courant_max):
    #     """Compute time step size based on Courant condition."""
    #     dx_min = np.min(np.diff(self.xelem)) / (2**self.max_level)
    #     self.dt = courant_max * dx_min / self.wave_speed
    #     # self.dt = 0.003
        
    def _initialize_projections(self):
        """Initialize projection matrices for AMR operations."""
        RM = create_RM_matrix(self.ngl, self.nq, self.wnq, self.psi)
        self.PS1, self.PS2, self.PG1, self.PG2 = projections(
            RM, self.ngl, self.nq, self.wnq, self.xgl, self.xnq
        )
    def _compute_timestep(self, use_actual_max_level=False):
        """
        Compute time step size based on Courant condition.
        
        Args:
            use_actual_max_level (bool): If True, use actual maximum refinement level
                                        present in the mesh instead of max_level
        """
        if use_actual_max_level:
            current_max_level = self.get_current_max_refinement_level()
            # print(f'current max level = {current_max_level}')
            if current_max_level == 0:
                dx_min = np.min(np.diff(self.xelem))/2
            #     # dx_min = np.min(np.diff(self.xelem)) 
            else:
                # dx_min = np.min(np.diff(self.xelem)) / (2**current_max_level)
                dx_min = np.min(np.diff(self.xelem))/2

            if self.verbose:
                print(f"Using max refinement level: {current_max_level}/{self.max_level}")
        else:
            dx_min = np.min(np.diff(self.xelem)) / (2**self.max_level)
            
        old_dt = getattr(self, 'dt', None)
        self.dt = self.courant_max * dx_min / self.wave_speed
        if use_actual_max_level == False:
            print(f'dt: {self.dt}')
        # if old_dt is not None and abs(old_dt - self.dt) > 1e-10:
        #     print(f"\nTime step updated: {old_dt:.6e} -> {self.dt:.6e}")
        #     print(f'current max level: {current_max_level}, dx_min: {dx_min}\n')
        if self.verbose and old_dt is not None and abs(old_dt - self.dt) > 1e-10:
            print(f"Time step updated: {old_dt:.6e} -> {self.dt:.6e}")

    def _update_matrices(self):
        """
        Update mass and differentiation matrices with condition number checking.
        
        Raises:
            ValueError: If mass matrix condition number is too high or matrix solve fails
        """
        self.Me = create_mass_matrix(
            self.intma, self.coord, self.nelem, self.ngl, 
            self.nq, self.wnq, self.psi
        )
        self.De = create_diff_matrix(self.ngl, self.nq, self.wnq, self.psi, self.dpsi)
        
        self.M, self.D = Matrix_DSS(
            self.Me, self.De, self.wave_speed, self.intma, 
            self.periodicity, self.ngl, self.nelem, self.npoin_dg
        )
        
        # Check condition number before proceeding
        cond_num = np.linalg.cond(self.M)
        # if self.verbose:
        #     print(f"Mass matrix condition number: {cond_num}")
        
        if cond_num > 1e10:  # Choose appropriate threshold
            raise ValueError(f"Mass matrix condition number too high: {cond_num}")
            
        self.F = Fmatrix_upwind_flux_bc(
            self.intma, self.nelem, self.npoin_dg, self.ngl, self.wave_speed, self.periodic
        )
        R = self.D - self.F

        self.Fcent = Fmatrix_centered_flux(
            self.intma, self.nelem, self.npoin_dg, self.ngl, self.wave_speed
        )
        
        
        try:
            self.Dhat = np.linalg.solve(self.M, R)
        except np.linalg.LinAlgError:
            if self.verbose:
                print("Matrix solve failed. Current mesh configuration:")
                print(f"Number of elements: {self.nelem}")
                print(f"Element sizes: {np.diff(self.xelem)}")
            raise

    def get_current_max_refinement_level(self):
        """
        Determine the maximum refinement level currently present in the active mesh.
        
        Returns:
            int: Maximum refinement level among active elements
        """
        active_levels = np.zeros(len(self.active), dtype=int)
        
        for i, elem in enumerate(self.active):
            # Element IDs in label_mat are 1-indexed, hence elem-1
            active_levels[i] = self.label_mat[elem-1][4]  # Level is in column 4
            
        return np.max(active_levels) if len(active_levels) > 0 else 0
    
    def get_active_levels(self):
        """
        Determine the maximum refinement level currently present in the active mesh.
        
        Returns:
            int: Maximum refinement level among active elements
        """
        active_levels = np.zeros(len(self.active), dtype=int)
        
        for i, elem in enumerate(self.active):
            # Element IDs in label_mat are 1-indexed, hence elem-1
            active_levels[i] = self.label_mat[elem-1][4]  # Level is in column 4

        return active_levels
    

    
    def balance_mesh(self, balance=None):
        """
        Check and enforce mesh balance in the current adaptive mesh.
        
        This method checks if the current mesh satisfies the 2:1 balance constraint,
        and if not, enforces balance by refining elements as needed.
        
        Args:
            balance (bool, optional): Whether to enforce balance. If None, uses the 
                                    instance's balance attribute.
                                    
        Returns:
            bool: Whether balancing was performed
        """
        # Use the method parameter if provided, otherwise use the instance variable
        use_balance = self.balance if balance is None else balance
        
        # Check if we need to enforce balance
        if use_balance and not check_balance(self.active, self.label_mat):
            print("Enforcing mesh balance...")
            if self.verbose:
                print("Enforcing mesh balance...")
                print(f'Pre-balance active elements: {len(self.active)}')
            
            # Enforce balance
            bal_q, bal_active, bal_nelem, bal_intma, bal_coord, bal_grid, bal_npoin_dg, bal_periodicity = enforce_balance(
                self.active, 
                self.label_mat, 
                self.xelem, 
                self.info_mat, 
                self.nop, 
                self.coord, 
                self.PS1, self.PS2, self.PG1, self.PG2, 
                self.ngl, self.xgl, 
                self.q, 
                self.max_level
            )
            
            # Update solver state with balanced state
            self.q = bal_q
            self.active = bal_active
            self.nelem = bal_nelem
            self.intma = bal_intma
            self.coord = bal_coord
            self.xelem = bal_grid
            self.npoin_dg = bal_npoin_dg
            self.periodicity = bal_periodicity
            
            if self.verbose:
                print(f'Post-balance active elements: {len(self.active)}')
            
            return True  # Balancing was performed
        
        return False  # No balancing needed
    
    def initialize_with_refinement(self, refinement_mode='none', refinement_level=2, refinement_probability=0.5):
        """
        Initialize the solver with a mesh at various refinement levels.
        
        Args:
            refinement_mode (str): Mode for initial refinement
                - 'fixed': Refine all elements to specified level
                - 'random': Randomly refine elements with given probability
                - 'none': No refinement (default behavior)
            refinement_level (int): Maximum refinement level for fixed mode
            refinement_probability (float): Probability of refining an element in random mode
        
        Returns:
            None
        """
        # First create the base forest structure as normal
        self._initialize_mesh()
        
        # If no refinement requested, return early
        if refinement_mode == 'none':
            return
            
        # Skip refinement if already at max level
        if refinement_level > self.max_level:
            refinement_level = self.max_level
            
        # Store original active elements
        original_active = self.active.copy()
        
        # Perform the initial refinement based on mode
        if refinement_mode == 'fixed':
            # Refine all elements to the specified level
            self._perform_fixed_refinement(refinement_level)
        elif refinement_mode == 'random':
            # Randomly refine elements
            
            self._perform_random_refinement(refinement_level, refinement_probability)
        
        # After refinement, re-initialize the solution on the refined mesh
        self.q = self._initialize_solution()
        
        # Update matrices for the new mesh
        self._update_matrices()
        
        # Recalculate time step
        self._compute_timestep(use_actual_max_level=True)
        
        # Verify state is valid
        self.verify_state()


    def _perform_fixed_refinement(self, target_level):
        """
        Refine all elements to a fixed level.
        
        Args:
            target_level (int): Target refinement level
        """
        for level in range(target_level):
            # In each iteration, refine all currently active elements
            marks = np.ones(len(self.active), dtype=int)
            
            # Apply refinement
            new_grid, new_active, _, new_nelem, npoin_cg, new_npoin_dg = adapt_mesh(
                self.nop, self.xelem, self.active, self.label_mat, 
                self.info_mat, marks, self.max_level
            )
            
            # Create new grid
            new_coord, new_intma, new_periodicity = create_grid_us(
                self.ngl, new_nelem, npoin_cg, new_npoin_dg, 
                self.xgl, new_grid
            )
            
            # Project solution (starting with zeros since we'll reinitialize)
            zero_q = np.zeros_like(self.q)
            q_new = adapt_sol(
                zero_q, self.coord, marks, self.active, self.label_mat,
                self.PS1, self.PS2, self.PG1, self.PG2, self.ngl
            )
            
            # Update solver state
            self.q = q_new
            self.active = new_active
            self.nelem = new_nelem
            self.intma = new_intma
            self.coord = new_coord
            self.xelem = new_grid
            self.npoin_dg = new_npoin_dg
            self.periodicity = new_periodicity
            


    def _perform_random_refinement(self, max_initial_level, probability):
        """
        Randomly refine elements up to a maximum level.
        
        Args:
            max_level (int): Maximum refinement level
            probability (float): Probability of refining an element at each level
        """
        for level in range(max_initial_level):
            # Create random refinement markers
            n_active = len(self.active)
            marks = (np.random.random(n_active) < probability).astype(int)
            
            # Skip if no elements marked
            if not np.any(marks):
                continue
                
            # Apply refinement
            new_grid, new_active, _, new_nelem, npoin_cg, new_npoin_dg = adapt_mesh(
                self.nop, self.xelem, self.active, self.label_mat, 
                self.info_mat, marks, self.max_level
            )
            
            # Create new grid
            new_coord, new_intma, new_periodicity = create_grid_us(
                self.ngl, new_nelem, npoin_cg, new_npoin_dg, 
                self.xgl, new_grid
            )
            
            # Project solution (starting with zeros since we'll reinitialize)
            zero_q = np.zeros_like(self.q)
            q_new = adapt_sol(
                zero_q, self.coord, marks, self.active, self.label_mat,
                self.PS1, self.PS2, self.PG1, self.PG2, self.ngl
            )
            
            # Update solver state
            self.q = q_new
            self.active = new_active
            self.nelem = new_nelem
            self.intma = new_intma
            self.coord = new_coord
            self.xelem = new_grid
            self.npoin_dg = new_npoin_dg
            self.periodicity = new_periodicity

            
            
            # Enforce 2:1 balance
            self.balance_mesh(self.balance)


    def check_mesh_quality(self, grid):
        """
        Check if proposed mesh would be numerically stable.
        
        Args:
            grid: Proposed grid coordinates
                
        Returns:
            bool: True if mesh quality is acceptable
            str: Description of any quality issues found
        """
        element_sizes = np.diff(grid)
        size_ratio = np.max(element_sizes) / np.min(element_sizes)
        
        issues = []
        
        # More permissive size ratio check (was 100, now 250)
        if size_ratio > 500:
            issues.append(f"Element size ratio too large: {size_ratio:.2f}")
        
        # Check for very small elements with relative threshold
        min_size = np.min(element_sizes)
        domain_size = grid[-1] - grid[0]
        if min_size < domain_size * 1e-6:  # Relative threshold
            issues.append(f"Elements too small: {min_size:.2e}")
                
        # More permissive neighbor ratio check
        neighbor_ratios = element_sizes[1:] / element_sizes[:-1]
        max_neighbor_ratio = max(max(neighbor_ratios), max(1/neighbor_ratios))
        if max_neighbor_ratio > 512:  # Was 4, now 32
            issues.append(f"Rapid size change between neighbors: ratio {max_neighbor_ratio:.2f}")
        
        return len(issues) == 0, "; ".join(issues)
    
    def verify_state(self):
        """
        Verify solver state is valid.
        
        Raises:
            ValueError: If element count, sizes, mesh quality, or solution values are invalid
        """
        # Check element count
        if len(self.active) > self.max_elements:
            raise ValueError(f"Element count {len(self.active)} exceeds maximum {self.max_elements}")
        
        # Check element sizes
        element_sizes = np.diff(self.xelem)
        if np.any(element_sizes <= 0):
            raise ValueError("Invalid element sizes detected")
        
        # Check mesh quality
        quality_ok, issues = self.check_mesh_quality(self.xelem)
        if not quality_ok:
            raise ValueError(f"Mesh quality issues: {issues}")
        
        # Check solution values
        if np.any(~np.isfinite(self.q)):
            raise ValueError("Invalid solution values detected")
        
    def get_exact_solution(self):
        """
        Get exact solution at current time.
        
        Returns:
            array: Exact solution values at grid points
        """
        qe, _ = exact_solution(self.coord, self.npoin_dg, self.time, self.icase)
        return qe
    
    def get_forcing(self):
        """
        Get exact solution at current time.
        
        Returns:
            array: Exact solution values at grid points
        """
        f = eff(self.coord, self.npoin_dg, self.icase, self.wave_speed)
        return f

    

    def step(self, dt=None):
        """
        Take single time step using low-storage Runge-Kutta method.
        
        Args:
            dt (float, optional): Time step size. If None, use the solver's dt
        """
        if dt is None:
            dt = self.dt
                
        # Low-storage Runge-Kutta coefficients
        RKA = np.array([0,
                    -567301805773.0/1357537059087,
                    -2404267990393.0/2016746695238,
                    -3550918686646.0/2091501179385,
                    -1275806237668.0/842570457699])
        
        RKB = np.array([1432997174477.0/9575080441755,
                    5161836677717.0/13612068292357,
                    1720146321549.0/2090206949498,
                    3134564353537.0/4481467310338,
                    2277821191437.0/14882151754819])
        
        dq = np.zeros(self.npoin_dg)
        qp = self.q.copy()
        
        for s in range(len(RKA)):
            R = self.Dhat @ qp
            
            for i in range(self.npoin_dg):
                dq[i] = RKA[s]*dq[i] + dt*R[i]
                qp[i] = qp[i] + RKB[s]*dq[i]
                
            if self.periodicity[-1] == self.periodicity[0]:
                qp[-1] = qp[0]
                
        self.q = qp
        self.time += dt

    
    def pseudo_step(self, dt=None):
        """
        Take single time step using low-storage Runge-Kutta method.
        
        Args:
            dt (float, optional): Time step size. If None, use the solver's dt
        """
        if dt is None:
            dt = self.dt

        self._update_matrices()
        # self._initialize_forcing()
        # f = self.f
        self._update_forcing()
                
        # Low-storage Runge-Kutta coefficients
        RKA = np.array([0,
                    -567301805773.0/1357537059087,
                    -2404267990393.0/2016746695238,
                    -3550918686646.0/2091501179385,
                    -1275806237668.0/842570457699])
        
        RKB = np.array([1432997174477.0/9575080441755,
                    5161836677717.0/13612068292357,
                    1720146321549.0/2090206949498,
                    3134564353537.0/4481467310338,
                    2277821191437.0/14882151754819])
        
        dq = np.zeros(self.npoin_dg)
        qp = self.q.copy()
        
        for s in range(len(RKA)):
            R = self.Dhat @ qp + self.f
            
            for i in range(self.npoin_dg):
                dq[i] = RKA[s]*dq[i] + dt*R[i]
                qp[i] = qp[i] + RKB[s]*dq[i]
                
            if self.periodicity[-1] == self.periodicity[0]:
                qp[-1] = qp[0]
                
        self.q = qp
        self.time += dt
        return qp

    def run_simulation(self, time_final=1.0, element_budget=None):
        """
        Run complete baseline simulation and return performance metrics.
        
        Args:
            time_final (float): Final simulation time
            element_budget (int): Maximum allowed elements
            
        Returns:
            dict: Performance metrics matching model evaluation format
        """
        import time
        start_time = time.time()

        # print(f"DEBUG: self.amr_mode = {self.amr_mode}")
        # print(f"DEBUG: self.threshold = {self.threshold}")

        # if self.verbose:
        #     print(f"Starting {self.amr_mode} simulation to time {time_final}")
        #     print(f"Initial elements: {len(self.active)}")
        #     print(f"Initial time: {self.time}")           # ADD THIS
        #     print(f"Initial dt: {self.dt}")               # ADD THIS
        #     print(f"Initial solution norm: {np.linalg.norm(self.q)}")  # ADD THIS
     
        
        # Initialize tracking
        total_cost = 0
        adaptation_count = 0
        
        # step_counter = 0 
        if self.verbose:
            print(f"Starting {self.amr_mode} simulation to time {time_final}")
            print(f"Initial elements: {len(self.active)}")
            
        # Main simulation loop
        while self.time < time_final:
            # print(f"Loop iteration {step_counter}, time={self.time}, dt={self.dt}")
            # Conventional AMR adaptation (every timestep to match model evaluation)
            if self.amr_mode == 'conventional-amr':
                # print(f"DEBUG: About to call conventional_amr_step at time {self.time}")  # ADD THIS
                pre_elements = len(self.active)
                self.conventional_amr_step()
                if len(self.active) != pre_elements:
                    adaptation_count += 1
                    # print(f"DEBUG: Adaptation occurred! {pre_elements} -> {len(self.active)}")  # ADD THIS
                    
            # Check budget constraint
            # if len(self.active) > element_budget:
            #     if self.verbose:
            #         print(f"Budget exceeded: {len(self.active)} > {element_budget}")
            #     break
                
            # Take physics time step
            dt = min(self.dt, time_final - self.time)
            self.step(dt)
            
            # Update cost tracking
            total_cost += len(self.active)
            # step_counter += 1  # ADD THIS
            # if step_counter > 10:  # Safety break
            #     print("Breaking after 10 steps for debugging")
            #     break
            
        # Calculate final metrics
        simulation_time = time.time() - start_time
        qe = self.get_exact_solution()
        final_l2_error = np.sqrt(np.sum((self.q - qe)**2) / np.sum(qe**2))
        
        metrics = {
            'method': self.amr_mode,
            'initial_refinement': getattr(self, 'initial_refinement', 0),
            'evaluation_element_budget': element_budget,
            'final_l2_error': final_l2_error,
            'total_cost': total_cost,
            'final_elements': len(self.active),
            'simulation_time': simulation_time,
            'threshold_value': self.threshold if self.amr_mode == 'conventional-amr' else 'N/A',
            'adaptation_count': adaptation_count
        }
        
        if self.verbose:
            print(f"Simulation complete:")
            print(f"  Final L2 error: {final_l2_error:.6f}")
            print(f"  Total cost: {total_cost}")
            print(f"  Final elements: {len(self.active)}")
            print(f"  Adaptations: {adaptation_count}")
            
        return metrics
    

    def conventional_amr_step(self, element_budget=None):
        """
        Perform conventional AMR adaptation using threshold-based marking.
        
        Args:
            element_budget (int): Maximum allowed elements
        """
        if self.amr_mode != 'conventional-amr':
            return  # No adaptation in no-amr mode
            
        # Get marks using threshold-based criterion
        marks = mark(self.active, self.label_mat, self.intma, self.q, 
                    criterion=1, threshold=self.threshold)
        
        # Skip if no adaptation needed
        if not np.any(marks):
            return
            
        # Check budget before applying refinements
        if element_budget is not None:
            refinement_count = np.sum(marks == 1)
            if len(self.active) + refinement_count > element_budget:
                if self.verbose:
                    print(f"Budget limit would be exceeded. Skipping adaptation.")
                return
        
        # Store pre-adaptation state
        pre_q = self.q
        pre_grid = self.xelem  
        pre_active = self.active
        pre_nelem = self.nelem
        pre_intma = self.intma
        pre_coord = self.coord
        pre_npoin_dg = self.npoin_dg
        pre_periodicity = self.periodicity
        
        # Adapt mesh
        new_grid, new_active, _, new_nelem, npoin_cg, new_npoin_dg = adapt_mesh(
            self.nop, pre_grid, pre_active, self.label_mat, 
            self.info_mat, marks, self.max_level
        )
        
        # Create new grid
        new_coord, new_intma, new_periodicity = create_grid_us(
            self.ngl, new_nelem, npoin_cg, new_npoin_dg, 
            self.xgl, new_grid
        )
        
        # Project solution
        q_new = adapt_sol(
            self.q, pre_coord, marks, pre_active, self.label_mat,
            self.PS1, self.PS2, self.PG1, self.PG2, self.ngl
        )
        
        # Update solver state
        self.q = q_new
        self.active = new_active
        self.nelem = new_nelem
        self.intma = new_intma
        self.coord = new_coord
        self.xelem = new_grid
        self.npoin_dg = new_npoin_dg
        self.periodicity = new_periodicity
        
        # Apply mesh balancing if needed
        self.balance_mesh(self.balance)
        
        # Update matrices and forcing
        self._update_matrices()
        self._update_forcing()
        self.verify_state()
        self._compute_timestep(use_actual_max_level=True) 

    def solve(self, time_final):
        """
        Solve the wave equation up to time_final.
        
        Args:
            time_final (float): Final simulation time
            
        Returns:
            tuple: (times, solutions, grids, coords) containing snapshots at each time step
        """
        times = [self.time]
        solutions = [self.q.copy()]
        grids = [self.xelem.copy()]
        coords = [self.coord.copy()]
        
        step_count = 0
        while self.time < time_final:
            dt = min(self.dt, time_final - self.time)
            if self.verbose:
                print(f"\nTimestep {step_count}, Time: {self.time:.3f}")
            
            # Single adapt_mesh call 
            self.adapt_mesh()
            
            # Take time step
            self.step(dt)
            
            # Store results
            times.append(self.time)
            solutions.append(self.q.copy())
            grids.append(self.xelem.copy())
            coords.append(self.coord.copy())
            step_count += 1
            
        return times, solutions, grids, coords
    

    def steady_solve(self):
        """
        Solve the steady-state advection equation u∂q/∂x = f using direct solve.
        
        Args:
            beta (float): Parameter controlling solution steepness
            
        Returns:
            array: Steady-state solution
        """
        # Create non-periodic boundary handling
        periodicity_non_periodic = np.arange(self.npoin_dg)
        
        # Update matrices with non-periodic boundaries
        self.Me = create_mass_matrix(
            self.intma, self.coord, self.nelem, self.ngl, 
            self.nq, self.wnq, self.psi
        )
        self.De = create_diff_matrix(self.ngl, self.nq, self.wnq, self.psi, self.dpsi)
        
        # Create mass and differentiation matrices
        M, D = Matrix_DSS(
            self.Me, self.De, self.wave_speed, self.intma, 
            periodicity_non_periodic, self.ngl, self.nelem, self.npoin_dg
        )
        
        # Create both centered and upwind flux matrices
        F_centered = Fmatrix_centered_flux(
            self.intma, self.nelem, self.npoin_dg, self.ngl, self.wave_speed
        )
        F_upwind = Fmatrix_upwind_flux_bc(
            self.intma, self.nelem, self.npoin_dg, self.ngl, self.wave_speed, periodic=False
        )
        
        # Create forcing vector
        self._update_forcing()
        
        # Create boundary condition vector
        b = np.zeros(self.npoin_dg)
        # For positive wave speed, inflow is at the leftmost point
        # inflow_idx = np.argmin(self.coord)
        # inflow_sol = self.q[inflow_idx]
        inflow_value = exact_solution(np.array([-1]), 1, self.time, self.icase)[0]
        # outflow_value = exact_solution(np.array([-1]), 1, self.time, self.icase)[-1]
        # # inflow_x = self.coord[inflow_idx]
        b[0] = inflow_value # Exact solution at inflow
        # b[-1] = outflow_value
        
         
        
        # Form the linear system
        rhs = M @ self.f - F_upwind @ b
        # rhs = M @ f - F_centered @ b
        
        # Add small regularization to improve conditioning
        epsilon = 1e-12
        # A = F_upwind - D + epsilon * np.eye(self.npoin_dg)
        A = F_upwind - D
        # A = F_centered - D + epsilon * np.eye(self.npoin_dg)

        



        
        # Solve the linear system
        try:
            q_steady = np.linalg.solve(A, rhs)
            # q_steady, info = gmres(A, rhs, rtol=1e-5, maxiter=1000)
        except np.linalg.LinAlgError:
            # Fall back to pseudoinverse for highly ill-conditioned systems
            # from scipy.linalg import pinv
            # q_steady = pinv(A, cond=1e-10) @ rhs
            print(f'using speudoinverse')
            q_steady = np.linalg.pinv(A, rcond=1e-10) @ rhs
            
            if self.verbose:
                print("Warning: Using pseudoinverse due to ill-conditioning")
        
        # Store solution
        self.q_steady = q_steady
        
        if self.verbose:
            # Calculate L2 error against exact solution
            qe, _ = exact_solution(self.coord, self.npoin_dg, 0.0, 1)  # icase=1
            l2_error = np.sqrt(np.sum((q_steady - qe)**2) / np.sum(qe**2))
            print(f"Steady-state solution computed with L2 error: {l2_error:.2e}")
        
        return q_steady
    
    def steady_solve_improved(self):
        """
        Solve the steady-state advection equation with strong boundary conditions
        """
        # Create matrices as before
        periodicity_non_periodic = np.arange(self.npoin_dg)
        self.Me = create_mass_matrix(
            self.intma, self.coord, self.nelem, self.ngl, 
            self.nq, self.wnq, self.psi
        )
        self.De = create_diff_matrix(self.ngl, self.nq, self.wnq, self.psi, self.dpsi)
        
        # Create mass and differentiation matrices
        M, D = Matrix_DSS(
            self.Me, self.De, self.wave_speed, self.intma, 
            periodicity_non_periodic, self.ngl, self.nelem, self.npoin_dg
        )
        
        F_upwind = Fmatrix_upwind_flux_bc(
            self.intma, self.nelem, self.npoin_dg, self.ngl, self.wave_speed, periodic=False
        )

            # Use Rusanov flux instead of upwind flux
        F_rusanov = Fmatrix_rusanov_flux(
            self.intma, self.nelem, self.npoin_dg, self.ngl, 
            self.wave_speed, periodic=False
        )

        
        # Identify boundary nodes
        left_boundary_idx = self.intma[0, 0]
        inflow_value = exact_solution(np.array([-1]), 1, self.time, self.icase)[0]
        
        # Create system
        A = F_upwind - D
        # A = F_rusanov - D
        rhs = M @ self.f
        
        # Strongly enforce the inflow boundary condition
        A[left_boundary_idx, :] = 0.0
        A[left_boundary_idx, left_boundary_idx] = 1.0
        rhs[left_boundary_idx] = inflow_value

        
        # Solve the system
        q_steady = np.linalg.solve(A, rhs)
         # Store solution
        self.q_steady = q_steady
        
        return q_steady
    

    def steady_solve_direct(self):
        """
        Solve the steady-state advection equation u∂q/∂x = f using direct integration.
        """
        # Update forcing function
        self._update_forcing()
        f = self.f
        
        # Get coordinates and prepare solution array
        x = self.coord
        q_steady = np.zeros_like(x)
        
        # Set the inflow boundary condition
        left_boundary_idx = self.intma[0, 0]
        inflow_value = exact_solution(np.array([-1]), 1, self.time, self.icase)[0]
        
        # Sort points by x-coordinate for integration
        sort_idx = np.argsort(x)
        x_sorted = x[sort_idx]
        f_sorted = f[sort_idx]
        
        # Start with inflow boundary condition
        q_sorted = np.zeros_like(x_sorted)
        q_sorted[0] = inflow_value
        
        # Integrate along characteristics
        for i in range(1, len(x_sorted)):
            # Integrate f from previous point to current point
            dx = x_sorted[i] - x_sorted[i-1]
            f_avg = 0.5 * (f_sorted[i] + f_sorted[i-1])
            q_sorted[i] = q_sorted[i-1] + (dx/self.wave_speed) * f_avg
        
        # Map back to original ordering
        for i, idx in enumerate(sort_idx):
            q_steady[idx] = q_sorted[i]
        
        return q_steady


        
    
    

