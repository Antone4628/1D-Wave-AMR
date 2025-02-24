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
    def __init__(self, nop, xelem, max_elements, max_level, courant_max=0.1, icase=1):
        self.nop = nop
        self.xelem = xelem
        self.max_elements = max_elements 
        self.ngl = nop + 1
        self.nelem = len(xelem) - 1
        self.max_level = max_level
        self.icase = icase
        self.time = 0.0
        self.dx_min = np.min(np.diff(xelem)) / (2**max_level)
        self.xgl, self.wgl = lgl_gen(self.ngl)
        self.nq = self.nop + 2
        self.xnq, self.wnq = lgl_gen(self.nq)
        self.psi, self.dpsi = Lagrange_basis(self.ngl, self.nq, self.xgl, self.xnq)
        self._initialize_mesh()
        self.q = self._initialize_solution()
        self._compute_timestep(courant_max)
        self._initialize_projections()
        
    def _initialize_mesh(self):
        self.npoin_cg = self.nop * self.nelem + 1
        self.npoin_dg = self.ngl * self.nelem
        self.label_mat, self.info_mat, self.active = forest(self.xelem, self.max_level)
        self.coord, self.intma, self.periodicity = create_grid_us(
            self.ngl, self.nelem, self.npoin_cg, self.npoin_dg, 
            self.xgl, self.xelem
        )
        
    def _initialize_solution(self):
        q, self.wave_speed = exact_solution(
            self.coord, self.npoin_dg, self.time, self.icase
        )
        return q
        
    def _compute_timestep(self, courant_max):
        dx_min = np.min(np.diff(self.xelem)) / (2**self.max_level)
        self.dt = courant_max * dx_min / self.wave_speed
        
    def _initialize_projections(self):
        RM = create_RM_matrix(self.ngl, self.nq, self.wnq, self.psi)
        self.PS1, self.PS2, self.PG1, self.PG2 = projections(
            RM, self.ngl, self.nq, self.wnq, self.xgl, self.xnq
        )





    # def _update_matrices(self):
    #     self.Me = create_mass_matrix(
    #         self.intma, self.coord, self.nelem, self.ngl, 
    #         self.nq, self.wnq, self.psi
    #     )
    #     self.De = create_diff_matrix(self.ngl, self.nq, self.wnq, self.psi, self.dpsi)
    #     self.M, self.D = Matrix_DSS(
    #         self.Me, self.De, self.wave_speed, self.intma, 
    #         self.periodicity, self.ngl, self.nelem, self.npoin_dg
    #     )
    #     self.F = Fmatrix_upwind_flux(
    #         self.intma, self.nelem, self.npoin_dg, self.ngl, self.wave_speed
    #     )
    #     R = self.D - self.F
    #     self.Dhat = np.linalg.solve(self.M, R)
    def _update_matrices(self):
        """Update mass and differentiation matrices with condition number checking"""
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
        print(f"Mass matrix condition number: {cond_num}")
        
        if cond_num > 1e10:  # Choose appropriate threshold
            raise ValueError(f"Mass matrix condition number too high: {cond_num}")
            
        self.F = Fmatrix_upwind_flux(
            self.intma, self.nelem, self.npoin_dg, self.ngl, self.wave_speed
        )
        R = self.D - self.F
        
        try:
            self.Dhat = np.linalg.solve(self.M, R)
        except np.linalg.LinAlgError:
            print("Matrix solve failed. Current mesh configuration:")
            print(f"Number of elements: {self.nelem}")
            print(f"Element sizes: {np.diff(self.xelem)}")
            raise    
  



    # def adapt_mesh(self, criterion=1, marks_override=None, element_budget=None):
    #     """
    #     Perform mesh adaptation based on solution properties.
    #     Respects element_budget constraint.
    #     """
    #     # Get refinement marks based on solution properties
    #     marks = mark(self.active, self.label_mat, self.intma, self.q, criterion)

    #     if marks_override is not None:
    #         for idx, mark_val in marks_override.items():
    #             # Check budget before refinement
    #             if mark_val == 1 and element_budget is not None:
    #                 if len(self.active) >= element_budget:
    #                     print(f"Budget limit reached ({element_budget} elements). Canceling refinement.")
    #                     marks[idx] = 0
    #                     continue
    #             marks[idx] = mark_val

        
    #     # Store pre-adaptation state
    #     pre_grid = self.xelem
    #     pre_active = self.active
    #     pre_nelem = self.nelem
    #     pre_coord = self.coord
    #     pre_npoin_dg = self.npoin_dg
        
    #     # Adapt mesh
    #     new_grid, new_active, _, new_nelem, npoin_cg, new_npoin_dg = adapt_mesh(
    #         self.nop, pre_grid, pre_active, self.label_mat, 
    #         self.info_mat, marks
    #     )

    #     # Create new grid
    #     new_coord, new_intma, new_periodicity = create_grid_us(
    #         self.ngl, new_nelem, npoin_cg, new_npoin_dg, 
    #         self.xgl, new_grid
    #     )

    #     # Project solution
    #     q_new = adapt_sol(
    #         self.q, pre_coord, marks, pre_active, self.label_mat,
    #         self.PS1, self.PS2, self.PG1, self.PG2, self.ngl
    #     )

    #     # Update solver state
    #     self.q = q_new
    #     self.active = new_active
    #     self.nelem = new_nelem
    #     self.intma = new_intma
    #     self.coord = new_coord
    #     self.xelem = new_grid
    #     self.npoin_dg = new_npoin_dg
    #     self.periodicity = new_periodicity

    #     # Add balancing loop here
    #     if not check_balance(self.active, self.label_mat):
    #         bal_q, bal_active, bal_nelem, bal_intma, bal_coord, bal_grid, bal_npoin_dg, bal_periodicity = enforce_balance(self.active, 
    #                                                                                             self.label_mat, 
    #                                                                                             self.xelem, 
    #                                                                                             self.info_mat, 
    #                                                                                             self.nop, 
    #                                                                                             self.coord, 
    #                                                                                             self.PS1, self.PS2, self.PG1, self.PG2, 
    #                                                                                             self.ngl, self.xgl, 
    #                                                                                             self.q, self.max_level)

        
    #         self.q = bal_q
    #         self.active = bal_active
    #         self.nelem = bal_nelem
    #         self.intma = bal_intma
    #         self.coord = bal_coord
    #         self.xelem = bal_grid
    #         self.npoin_dg = bal_npoin_dg
    #         self.periodicity = bal_periodicity


        
    #     # Update matrices
    #     self._update_matrices()

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
        
        # Check size ratio
        if size_ratio > 100:
            issues.append(f"Element size ratio too large: {size_ratio:.2f}")
        
        # Check for very small elements
        min_size = np.min(element_sizes)
        if min_size < 1e-5:
            issues.append(f"Elements too small: {min_size:.2e}")
            
        # Check for rapid size changes between neighbors
        neighbor_ratios = element_sizes[1:] / element_sizes[:-1]
        max_neighbor_ratio = max(max(neighbor_ratios), max(1/neighbor_ratios))
        if max_neighbor_ratio > 4:  # Even stricter than 2:1
            issues.append(f"Rapid size change between neighbors: ratio {max_neighbor_ratio:.2f}")
        
        return len(issues) == 0, "; ".join(issues)
    
    def verify_state(self):
        """Verify solver state is valid"""
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

    def adapt_mesh(self, criterion=1, marks_override=None, element_budget=None):
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
        # Get refinement marks based on solution properties
        # Check for marks_override first
        # if marks_override is not None:
        #     # Create zero marks array
        #     marks = np.zeros(len(self.active), dtype=int)
        #     print(f'verify marks array is resetting before applying override values: {marks}')
            
        #     # Apply override values
        #     for idx, mark_val in marks_override.items():
        #         # Check budget before refinement
        #         if mark_val == 1 and element_budget is not None:
        #             if len(self.active) >= element_budget:
        #                 print(f"Budget limit reached ({element_budget} elements). Canceling refinement.")
        #                 continue
        #         marks[idx] = mark_val
        #         print(f'verify marks array is applying override values: {marks}')
        if marks_override is not None:
                #     # Create zero marks array
                marks = np.zeros(len(self.active), dtype=int)
                # print(f'verify marks array is resetting before applying override values: {marks}')
                for idx, mark_val in marks_override.items():
                    # Handle refinement case with budget check
                    if mark_val == 1 and element_budget is not None:
                        if len(self.active) >= element_budget:
                            print(f"Budget limit reached ({element_budget} elements). Canceling refinement.")
                            continue
                        # print(f'refining element at index: {idx}')
                        marks[idx] = mark_val
                        # print(f'marks for refining: {marks}')
                        
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
                                    print(f"Marking element {elem} and sibling {sibling} for coarsening")
                                    marks[idx] = -1
                                    marks[sibling_idx] = -1
                                else:
                                    print(f"No valid sibling found for element {elem}, skipping coarsening")
                
        else:
            # If no override, get marks from criterion
            marks = mark(self.active, self.label_mat, self.intma, self.q, criterion)
        # marks = mark(self.active, self.label_mat, self.intma, self.q, criterion)

       
        # Store pre-adaptation state
        pre_q = self.q
        pre_grid = self.xelem
        pre_active = self.active
        pre_nelem = self.nelem
        pre_intma = self.intma
        pre_coord = self.coord
        pre_npoin_dg = self.npoin_dg
        pre_periodicity = self.periodicity
        # print(f'marks being passed into adapt_mesh(): {marks}')
        # Adapt mesh
        new_grid, new_active, _, new_nelem, npoin_cg, new_npoin_dg = adapt_mesh(
            self.nop, pre_grid, pre_active, self.label_mat, 
            self.info_mat, marks
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
        if not check_balance(self.active, self.label_mat):
            # Store state before balance enforcement
            pre_balance_elements = len(self.active)
            print(f'balancing.....')
            
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
            
            # # Check if balance enforcement would exceed budget
            # if element_budget is not None and len(bal_active) > element_budget:
            #     print(f"Balance enforcement would exceed budget ({len(bal_active)} > {element_budget})")
            #     # Revert to pre-adaptation state
            #     self.q = pre_q
            #     self.active = pre_active
            #     self.nelem = pre_nelem
            #     self.intma = pre_intma
            #     self.coord = pre_coord
            #     self.xelem = pre_grid
            #     self.npoin_dg = pre_npoin_dg
            #     self.periodicity = pre_periodicity
            #     raise ValueError("Balance enforcement would exceed element budget")
                
            # Update with balanced state
            self.q = bal_q
            self.active = bal_active
            self.nelem = bal_nelem
            self.intma = bal_intma
            self.coord = bal_coord
            self.xelem = bal_grid
            self.npoin_dg = bal_npoin_dg
            self.periodicity = bal_periodicity

        
        # Update matrices
        self._update_matrices()
        self.verify_state() 


    
    def step(self, dt=None):
        """
        Take single time step with balance verification.
        """
        if dt is None:
            dt = self.dt
                
        # Check balance before step
        
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

        # Check balance after step  

    def solve(self, time_final):
        times = [self.time]
        solutions = [self.q.copy()]
        grids = [self.xelem.copy()]
        coords = [self.coord.copy()]
        
        step_count = 0
        while self.time < time_final:
            dt = min(self.dt, time_final - self.time)
            # print(f"\nTimestep {step_count}, Time: {self.time:.3f}")
            
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
    # def solve(self, time_final):
    #     times = [self.time]
    #     solutions = [self.q.copy()]
    #     grids = [self.xelem.copy()]
    #     coords = [self.coord.copy()]
        
    #     step_count = 0
    #     while self.time < time_final:
    #         dt = min(self.dt, time_final - self.time)
            
    #         print(f"\nTimestep {step_count}, Time: {self.time:.3f}")
        
    #         # Check balance before adaptation
    #         violations = check_2_1_balance(self.active, self.label_mat, debug=True)
    #         if violations:
    #             print("Pre-adaptation violations found:")
    #             for elem, neighbor, level1, level2 in violations:
    #                 print(f"Elements {elem}({level1}) and {neighbor}({level2})")

    #         self.adapt_mesh()

    #                 # Check balance after adaptation
    #         violations = check_2_1_balance(self.active, self.label_mat, debug=True)
    #         if violations:
    #             print("Post-adaptation violations found:")
    #             for elem, neighbor, level1, level2 in violations:
    #                 print(f"Elements {elem}({level1}) and {neighbor}({level2})")
                
    #             # Print detailed mesh state when violation found
    #             print("\nDetailed mesh state at violation:")
    #             # print_mesh_state(self.active, self.label_mat)
            
    #         self.step(dt)
            
    #         times.append(self.time)
    #         solutions.append(self.q.copy())
    #         grids.append(self.xelem.copy())
    #         coords.append(self.coord.copy())
    #         step_count += 1
            
    #     return times, solutions, grids, coords

    def get_exact_solution(self):
        qe, _ = exact_solution(self.coord, self.npoin_dg, self.time, self.icase)
        return qe
    

    def reset(self):
        """Reset solver to initial state"""
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
        self.verify_state()  # Add verification after reset
        return self.q
    # def reset(self):
    #     self.nelem = len(self.xelem) - 1
    #     self.npoin_cg = self.nop * self.nelem + 1
    #     self.npoin_dg = self.ngl * self.nelem
    #     self.label_mat, self.info_mat, self.active = forest(self.xelem, self.max_level)
    #     self.coord, self.intma, self.periodicity = create_grid_us(
    #         self.ngl, self.nelem, self.npoin_cg, self.npoin_dg, self.xgl, self.xelem
    #     )
    #     self.q, _ = exact_solution(self.coord, self.npoin_dg, 0.0, self.icase)
    #     self.time = 0.0
    #     self._update_matrices()
    #     return self.q
