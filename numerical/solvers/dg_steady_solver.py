"""
Discontinuous Galerkin Steady-State Solver

This module implements a high-order Discontinuous Galerkin (DG) solver for the 1D steady-state advection problem
with h-adaptation capabilities using hierarchical mesh refinement. The solver uses:
- Legendre-Gauss-Lobatto (LGL) nodal basis functions
- Upwind numerical fluxes for interface treatment
- Low-storage Runge-Kutta pseudo-time integration to steady state
- Hierarchical mesh refinement with solution projection
"""

import numpy as np
import os
import sys

# Adjust these paths to match project structure
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 
    '..',
    '..'
))
sys.path.append(PROJECT_ROOT)

from ..dg.basis import lgl_gen, Lagrange_basis
from ..dg.matrices import (create_mass_matrix, create_diff_matrix, 
                      Fmatrix_upwind_flux, Matrix_DSS, create_RM_matrix)
from ..grid.mesh import create_grid_us
from ..amr.forest import forest
from ..amr.adapt import adapt_mesh, adapt_sol, mark, check_balance, enforce_balance
from ..amr.projection import projections
from .utils import exact_solution, eff

class DGSteadySolver:
    """
    Discontinuous Galerkin solver for 1D steady-state advection problem with Adaptive Mesh Refinement (AMR).
    
    This solver implements:
    - Modal DG discretization with LGL nodes
    - Hierarchical h-refinement for mesh adaptation
    - Solution projection between refined/coarsened elements
    - Low-storage RK pseudo-time integration to steady state
    
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
        f (array): Source term / forcing function
        advection_speed (float): Advection speed for the equation
    """
    def __init__(self, nop, xelem, max_elements, max_level, courant_max=0.1, icase=7, periodic = False, verbose=False):
        """
        Initialize the DG steady-state solver with AMR capabilities.
        
        Args:
            nop (int): Polynomial order for basis functions
            xelem (array): Element boundary coordinates
            max_elements (int): Maximum number of elements allowed
            max_level (int): Maximum refinement level allowed
            courant_max (float): Maximum Courant number for time step calculation
            icase (int): Test case identifier (default is 7 for tanh solution)
            verbose (bool): Whether to print detailed diagnostic information
        """
        self.nop = nop
        self.xelem = xelem.copy()
        self.max_elements = max_elements 
        self.ngl = nop + 1
        self.nelem = len(xelem) - 1
        self.max_level = max_level
        self.icase = icase
        self.time = 0.0
        self.residual_history = []
        self.dx_min = np.min(np.diff(xelem)) / (2**max_level)
        self.xgl, self.wgl = lgl_gen(self.ngl)
        self.nq = self.nop + 2
        self.xnq, self.wnq = lgl_gen(self.nq)
        self.psi, self.dpsi = Lagrange_basis(self.ngl, self.nq, self.xgl, self.xnq)
        self.verbose = verbose
        self.periodic = periodic
        self.criterion = 1  # Default marking criterion
        
        self._initialize_mesh()
        self.q, self.advection_speed = self._initialize_solution()
        self.f = self._initialize_source_term()
        self._compute_timestep(courant_max)
        self._initialize_matrices()
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
        
        # For non-periodic boundary conditions - modify periodicity array
        self.periodicity_non_periodic = np.arange(self.npoin_dg)  # Identity mapping (no periodicity)
        
    def _initialize_solution(self):
        """Initialize the solution based on test case."""
        q, advection_speed = exact_solution(
            self.coord, self.npoin_dg, self.time, self.icase
        )
        return q, advection_speed
    
    def _initialize_source_term(self):
        """Initialize the source term / forcing function."""
        f = eff(self.coord, self.npoin_dg, self.icase, self.advection_speed)
        return f
        
    def _compute_timestep(self, courant_max):
        """Compute time step size based on Courant condition."""
        dx_min = np.min(np.diff(self.xelem)) / (2**self.max_level)
        self.dt = courant_max * dx_min / self.advection_speed
        
    def _initialize_projections(self):
        """Initialize projection matrices for AMR operations."""
        RM = create_RM_matrix(self.ngl, self.nq, self.wnq, self.psi)
        self.PS1, self.PS2, self.PG1, self.PG2 = projections(
            RM, self.ngl, self.nq, self.wnq, self.xgl, self.xnq
        )

    def _initialize_matrices(self):
        """
        Initialize mass and differentiation matrices with condition number checking.
        
        Raises:
            ValueError: If mass matrix condition number is too high or matrix solve fails
        """
        self._update_matrices()

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
        
        # For steady-state advection, use non-periodic boundary conditions
        self.M, self.D = Matrix_DSS(
            self.Me, self.De, self.advection_speed, self.intma, 
            self.periodicity_non_periodic, self.ngl, self.nelem, self.npoin_dg
        )
        
        # Check condition number before proceeding
        cond_num = np.linalg.cond(self.M)
        if self.verbose:
            print(f"Mass matrix condition number: {cond_num}")
        
        if cond_num > 1e12:  # Choose appropriate threshold
            raise ValueError(f"Mass matrix condition number too high: {cond_num}")
            
        self.F = Fmatrix_upwind_flux(
            self.intma, self.nelem, self.npoin_dg, self.ngl, self.advection_speed, self.periodic
        )
        
        # For the steady state problem, R = D - F
        self.R = self.D - self.F
        
        try:
            # Solve M^{-1}R for the steady state operator
            self.Dhat = np.linalg.solve(self.M, self.R)
        except np.linalg.LinAlgError:
            if self.verbose:
                print("Matrix solve failed. Current mesh configuration:")
                print(f"Number of elements: {self.nelem}")
                print(f"Element sizes: {np.diff(self.xelem)}")
            raise

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
        if size_ratio > 250:
            issues.append(f"Element size ratio too large: {size_ratio:.2f}")
        
        # Check for very small elements with relative threshold
        min_size = np.min(element_sizes)
        domain_size = grid[-1] - grid[0]
        if min_size < domain_size * 1e-6:  # Relative threshold
            issues.append(f"Elements too small: {min_size:.2e}")
                
        # Check for rapid size changes between neighbors
        neighbor_ratios = element_sizes[1:] / element_sizes[:-1]
        if len(neighbor_ratios) > 0:  # Ensure not empty
            max_neighbor_ratio = max(max(neighbor_ratios), max(1.0/np.where(neighbor_ratios > 0, neighbor_ratios, float('inf'))))
            if max_neighbor_ratio > 6:  # Was 4, now 6
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

    def adapt_mesh(self, criterion=None, marks_override=None, element_budget=None):
        """
        Perform mesh adaptation based on solution properties.
        Respects element_budget constraint.
        
        Args:
            criterion (int, optional): Marking criterion to use
            marks_override (dict): Override marking for specific elements
            element_budget (int): Maximum allowed number of elements
            
        Returns:
            None
            
        Raises:
            ValueError: If adaptation would exceed element budget
        """
        # Use instance criterion if not specified
        if criterion is None:
            criterion = self.criterion
            
        # Initialize marks based on override or criterion
        if marks_override is not None:
            marks = np.zeros(len(self.active), dtype=int)
            for idx, mark_val in marks_override.items():
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
        pre_q = self.q.copy()
        pre_f = self.f.copy()
        pre_grid = self.xelem.copy()
        pre_active = self.active.copy()
        pre_nelem = self.nelem
        pre_intma = self.intma.copy()
        pre_coord = self.coord.copy()
        pre_npoin_dg = self.npoin_dg
        pre_periodicity = self.periodicity.copy()
        
        # Check if any adaptations are needed
        if not np.any(marks):
            if self.verbose:
                print("No adaptations needed.")
            return
        
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
            pre_q, pre_coord, marks, pre_active, self.label_mat,
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
        self.periodicity_non_periodic = np.arange(self.npoin_dg)  # Update non-periodic mapping

        # Update source term on new grid
        self.f = eff(self.coord, self.npoin_dg, self.icase, self.advection_speed)

        # Add balancing loop
        if not check_balance(self.active, self.label_mat):
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
            self.periodicity_non_periodic = np.arange(self.npoin_dg)  # Update non-periodic mapping
            
            # Update source term on balanced grid
            self.f = eff(self.coord, self.npoin_dg, self.icase, self.advection_speed)

        # Update matrices
        self._update_matrices()
        self.verify_state() 

    def step(self, dt=None):
        """
        Take single time step using low-storage Runge-Kutta method.
        
        Args:
            dt (float, optional): Time step size. If None, use the solver's dt
            
        Returns:
            float: Residual norm (measure of convergence to steady state)
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
            # For steady state, include the source term in the RHS
            R = self.Dhat @ qp + np.linalg.solve(self.M, self.f)
            
            for i in range(self.npoin_dg):
                dq[i] = RKA[s]*dq[i] + dt*R[i]
                qp[i] = qp[i] + RKB[s]*dq[i]
                
            if self.periodicity[-1] == self.periodicity[0]:
                qp[-1] = qp[0]
        
        # Compute residual as norm of update
        residual = np.linalg.norm(qp - self.q) / np.linalg.norm(self.q) if np.linalg.norm(self.q) > 0 else np.linalg.norm(qp - self.q)
        
        self.q = qp
        self.time += dt
        self.residual_history.append(residual)
        
        return residual

    def solve_to_steady_state(self, max_iter=1000, tol=1e-8, adapt_frequency=10):
        """
        Solve the steady-state problem using pseudo-time stepping.
        
        Args:
            max_iter (int): Maximum number of iterations
            tol (float): Convergence tolerance for residual
            adapt_frequency (int): Frequency of mesh adaptation
            
        Returns:
            tuple: (residual_history, times, solutions, grids, coords) containing convergence history and snapshots
        """
        times = [self.time]
        solutions = [self.q.copy()]
        grids = [self.xelem.copy()]
        coords = [self.coord.copy()]
        
        for iter_count in range(max_iter):
            # Adapt mesh periodically
            if iter_count % adapt_frequency == 0 and iter_count > 0:
                if self.verbose:
                    print(f"\nIteration {iter_count}, adapting mesh")
                self.adapt_mesh()
            
            # Take time step
            residual = self.step()
            
            # Store results periodically
            if iter_count % 10 == 0 or residual < tol:
                times.append(self.time)
                solutions.append(self.q.copy())
                grids.append(self.xelem.copy())
                coords.append(self.coord.copy())
            
            # Check for convergence
            if residual < tol:
                if self.verbose:
                    print(f"Converged to residual {residual:.3e} in {iter_count+1} iterations")
                break
                
            if self.verbose and iter_count % 10 == 0:
                print(f"Iteration {iter_count}, residual: {residual:.3e}")
                
        # If we didn't converge, print a warning
        if iter_count == max_iter-1 and residual > tol:
            print(f"Warning: Did not converge to tolerance {tol}. Final residual: {residual:.3e}")
            
        return self.residual_history, times, solutions, grids, coords

    def get_exact_solution(self):
        """
        Get exact solution.
        
        Returns:
            array: Exact solution values at grid points
        """
        qe, _ = exact_solution(self.coord, self.npoin_dg, self.time, self.icase)
        return qe
    
    def compute_error_norm(self):
        """
        Compute L2 error norm between numerical and exact solutions.
        
        Returns:
            float: L2 error norm
        """
        qe = self.get_exact_solution()
        error = self.q - qe
        # Compute L2 norm using mass matrix for proper weighting
        l2_error = np.sqrt(np.dot(error, self.M @ error))
        l2_exact = np.sqrt(np.dot(qe, self.M @ qe))
        return l2_error / l2_exact if l2_exact > 0 else l2_error
    
    def reset(self):
        """
        Reset solver to initial state.
        
        Returns:
            array: Initial solution
            
        Raises:
            ValueError: If initial mesh quality is poor
        """
        # Reset to initial grid
        self.xelem = np.array([-1, -0.5, 0, 0.5, 1])  # Reset to original grid
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
        self.periodicity_non_periodic = np.arange(self.npoin_dg)  # Reset non-periodic mapping
        
        # Reset solution to initial condition
        self.q, self.advection_speed = exact_solution(self.coord, self.npoin_dg, 0.0, self.icase)
        self.time = 0.0
        self.residual_history = []
        
        # Reset source term
        self.f = eff(self.coord, self.npoin_dg, self.icase, self.advection_speed)
        
        # Verify mesh quality before updating matrices
        quality_ok, issues = self.check_mesh_quality(self.xelem)
        if not quality_ok:
            raise ValueError(f"Initial mesh quality issues: {issues}")
        
        # Update matrices
        self._update_matrices()
        self.verify_state()
        return self.q