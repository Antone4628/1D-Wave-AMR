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
from ..dg.basis import lgl_gen, Lagrange_basis
from ..dg.matrices import (create_mass_matrix, create_diff_matrix, 
                      Fmatrix_upwind_flux, Matrix_DSS, create_RM_matrix)
from ..grid.mesh import create_grid_us
from ..amr.forest import forest
from ..amr.adapt import adapt_mesh, adapt_sol, mark, check_balance, enforce_balance
from ..amr.projection import projections
from .utils import exact_solution

class DGWaveSolver:
    """
    Discontinuous Galerkin solver for 1D wave equation with Adaptive Mesh Refinement (AMR).
    
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
    def __init__(self, nop, xelem, max_elements, max_level, courant_max=0.1, icase=1, periodic = True, verbose=False):
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
        self.verbose = verbose
        
        self._initialize_mesh()
        self.q = self._initialize_solution()
        self._compute_timestep(use_actual_max_level=True)
        # self._compute_timestep(courant_max)
        self._initialize_projections()
        
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
        if self.verbose:
            print(f"Mass matrix condition number: {cond_num}")
        
        if cond_num > 1e10:  # Choose appropriate threshold
            raise ValueError(f"Mass matrix condition number too high: {cond_num}")
            
        self.F = Fmatrix_upwind_flux(
            self.intma, self.nelem, self.npoin_dg, self.ngl, self.wave_speed, self.periodic
        )
        R = self.D - self.F
        
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

    # def check_mesh_quality(self, grid):
    #     """
    #     Check if proposed mesh would be numerically stable.
        
    #     Args:
    #         grid: Proposed grid coordinates
            
    #     Returns:
    #         bool: True if mesh quality is acceptable
    #         str: Description of any quality issues found
    #     """
    #     element_sizes = np.diff(grid)
    #     size_ratio = np.max(element_sizes) / np.min(element_sizes)
        
    #     issues = []
        
    #     # Check size ratio
    #     if size_ratio > 100:
    #         issues.append(f"Element size ratio too large: {size_ratio:.2f}")
        
    #     # Check for very small elements
    #     min_size = np.min(element_sizes)
    #     if min_size < 1e-5:
    #         issues.append(f"Elements too small: {min_size:.2e}")
            
    #     # Check for rapid size changes between neighbors
    #     neighbor_ratios = element_sizes[1:] / element_sizes[:-1]
    #     max_neighbor_ratio = max(max(neighbor_ratios), max(1/neighbor_ratios))
    #     if max_neighbor_ratio > 4:  # Even stricter than 2:1
    #         issues.append(f"Rapid size change between neighbors: ratio {max_neighbor_ratio:.2f}")
        
    #     return len(issues) == 0, "; ".join(issues)
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

    def adapt_mesh(self, criterion=1, marks_override=None, element_budget=None, update_dt = True, balance = True):
        """
        Perform mesh adaptation based on solution properties.
        Respects element_budget constraint.
        
        Args:
            criterion (int): Marking criterion to use
            marks_override (dict): Override marking for specific elements
            element_budget (int): Maximum allowed number of elements
            
        Returns:
            None
            
        Raises:
            ValueError: If adaptation would exceed element budget
        """
        # Initialize marks based on override or criterion
        if marks_override is not None:
            marks = np.zeros(len(self.active), dtype=int)
            for idx, mark_val in marks_override.items():
                if idx >= len(self.active):
                    raise ValueError(f"Index error: {idx} out of bounds for active array with length {len(self.active)} ->SOLVER ADAPT MESH")
                # Handle refinement case with budget check
                if mark_val == 1 and element_budget is not None:
                    if len(self.active) >= element_budget:
                        if self.verbose:
                            print(f"Budget limit reached ({element_budget} elements). Canceling refinement.")
                        continue
                    marks[idx] = mark_val
                    
                # Enhanced coarsening logic
                elif mark_val == -1:
                    elem = self.active[idx]  # Get actual element number
                    if elem > 0:  # Safety check
                        parent = self.label_mat[elem-1][1]
                        
                        # Only proceed if element has a parent (level > 0)
                        if parent != 0:
                            # Find sibling by checking neighboring elements
                            sibling = None
                            sibling_idx = None
                            
                            # Check element before current one
                            if elem > 1 and idx > 0 and self.label_mat[elem-2][1] == parent:
                                sibling = elem - 1
                                sibling_idx = idx - 1
                                
                            # Check element after current one
                            elif elem < len(self.label_mat) and idx < len(self.active)-1 and self.label_mat[elem][1] == parent:
                                sibling = elem + 1
                                sibling_idx = idx + 1
                            
                            # Mark both elements for coarsening if sibling found
                            if sibling is not None and sibling in self.active:
                                if self.verbose:
                                    print(f"Marking element {elem} and sibling {sibling} for coarsening")
                                marks[idx] = -1
                                marks[sibling_idx] = -1
                            elif self.verbose:
                                print(f"No valid sibling found for element {elem}, skipping coarsening")
                
        else:
            # If no override, get marks from criterion
            marks = mark(self.active, self.label_mat, self.intma, self.q, criterion)
       
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

        # Add balancing loop here
        if balance:
            if not check_balance(self.active, self.label_mat):
                # print("Enforcing mesh balance...")
                # print(f'pre-balance active elements: {len(self.active)}')
                if self.verbose:
                    print("Enforcing mesh balance...")
                
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
                
                # Update with balanced state
                self.q = bal_q
                self.active = bal_active
                self.nelem = bal_nelem
                self.intma = bal_intma
                self.coord = bal_coord
                self.xelem = bal_grid
                self.npoin_dg = bal_npoin_dg
                self.periodicity = bal_periodicity
                # print(f'post-balance active elements: {len(self.active)}')

        # Update matrices
        self._update_matrices()
        self.verify_state() 

        if update_dt:
            self._compute_timestep(use_actual_max_level=True)

    # def step(self, dt=None):
    #     """
    #     Take single time step using low-storage Runge-Kutta method.
        
    #     Args:
    #         dt (float, optional): Time step size. If None, use the solver's dt
    #     """
    #     if dt is None:
    #         dt = self.dt
                
    #     # Low-storage Runge-Kutta coefficients
    #     RKA = np.array([0,
    #                 -567301805773.0/1357537059087,
    #                 -2404267990393.0/2016746695238,
    #                 -3550918686646.0/2091501179385,
    #                 -1275806237668.0/842570457699])
        
    #     RKB = np.array([1432997174477.0/9575080441755,
    #                 5161836677717.0/13612068292357,
    #                 1720146321549.0/2090206949498,
    #                 3134564353537.0/4481467310338,
    #                 2277821191437.0/14882151754819])
        
    #     dq = np.zeros(self.npoin_dg)
    #     qp = self.q.copy()
        
    #     for s in range(len(RKA)):
    #         R = self.Dhat @ qp
            
    #         for i in range(self.npoin_dg):
    #             dq[i] = RKA[s]*dq[i] + dt*R[i]
    #             qp[i] = qp[i] + RKB[s]*dq[i]
                
    #         # Enforce periodicity after EACH RK stage
    #         if self.periodic:
    #             # Find matching nodes at domain boundaries
    #             for i in range(self.ngl):
    #                 left_bdry_idx = self.intma[i, 0]  # First element, all nodes
    #                 right_bdry_idx = self.intma[i, -1]  # Last element, all nodes
    #                 if left_bdry_idx == right_bdry_idx:
    #                     # These are the same point in the mesh, enforce equality
    #                     avg_val = 0.5 * (qp[left_bdry_idx] + qp[right_bdry_idx])
    #                     qp[left_bdry_idx] = avg_val
    #                     qp[right_bdry_idx] = avg_val
        
    #     self.q = qp
    #     self.time += dt


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

    def get_exact_solution(self):
        """
        Get exact solution at current time.
        
        Returns:
            array: Exact solution values at grid points
        """
        qe, _ = exact_solution(self.coord, self.npoin_dg, self.time, self.icase)
        return qe
    
    def reset(self):
        """
        Reset solver to initial state.
        
        Returns:
            array: Initial solution
            
        Raises:
            ValueError: If initial mesh quality is poor
        """
        # Reset to initial number of elements and grid
        self.xelem = np.array([-1, -0.4, 0, 0.4, 1])  # Reset to original grid
        self.nelem = len(self.xelem) - 1
        
        # Recalculate grid parameters
        self.npoin_cg = self.nop * self.nelem + 1
        self.npoin_dg = self.ngl * self.nelem
        
        # Reset AMR structures
        self.label_mat, self.info_mat, self.active = forest(self.xelem, self.max_level)
        
        # Create fresh grid
        self.coord, self.intma, self.periodicity = create_grid_us(
            self.ngl, self.nelem, self.npoin_cg, self.npoin_dg, self.xgl, self.xelem
        )
        
        # Reset solution to initial condition
        self.q, _ = exact_solution(self.coord, self.npoin_dg, 0.0, self.icase)
        self.time = 0.0
        
        # Verify mesh quality before updating matrices
        quality_ok, issues = self.check_mesh_quality(self.xelem)
        if not quality_ok:
            raise ValueError(f"Initial mesh quality issues: {issues}")
        
        # Update matrices
        self._update_matrices()
        # Calculate time step based on actual refinement level
        self._compute_timestep(use_actual_max_level=True)
        self.verify_state()
        return self.q