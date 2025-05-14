import numpy as np
import matplotlib.pyplot as plt
import os
import sys

# Adjust these paths to match project structure
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 
    '..',
    '..'
))
sys.path.append(PROJECT_ROOT)

# from numerical.solvers.dg_steady_solver import DGSteadySolver
from numerical.dg.matrices import *
from numerical.solvers.dg_wave_solver_mixed import DGWaveSolverMixed

def analyze_solver(solver):
    """Print diagnostic information about solver state."""
    # Identify boundary nodes
    left_idx = solver.intma[0, 0]
    right_idx = solver.intma[solver.ngl-1, solver.nelem-1]
    
    print(f"Left boundary index: {left_idx}")
    print(f"Right boundary index: {right_idx}")
    
    # Create flux matrix
    F_upwind = Fmatrix_upwind_flux_bc(
        solver.intma, solver.nelem, solver.npoin_dg, solver.ngl, 
        solver.wave_speed, periodic=False
    )
    
    # Examine boundary rows
    print(f"Flux matrix at left boundary: {F_upwind[left_idx, :]}")
    print(f"Flux matrix at right boundary: {F_upwind[right_idx, :]}")
    
    # Create and solve the system using both approaches
    q_matrix = solver.steady_solve_improved()
    q_direct = solver.steady_solve_direct()
    # q_direct = steady_solve_direct(solver)
    
    # Compare solutions
    plt.figure(figsize=(10, 6))
    plt.plot(solver.coord, q_matrix, 'r-', label='Matrix approach')
    plt.plot(solver.coord, q_direct, 'b--', label='Direct integration')
    plt.plot(solver.coord, solver.get_exact_solution(), 'k:', label='Exact')
    plt.legend()
    plt.title(f"Solution with {solver.nelem} elements")
    plt.grid(True)
    plt.show()
    
    return q_matrix, q_direct

# Initialize solver
nop = 4
xelem = np.array([-1, -0.5, 0, 0.5, 1])
solver = DGWaveSolverMixed(nop=nop, xelem=xelem, max_elements=40, max_level=6)

# Analyze initial solver state
print("=== Initial Solver Analysis ===")
q_init_matrix, q_init_direct = analyze_solver(solver)

# First refinement
print("\n=== First Refinement (Element on left) ===")
marks_override = {1: 1}
solver.adapt_mesh(marks_override=marks_override,element_budget=28)
q_left_matrix, q_left_direct = analyze_solver(solver)

# Second refinement
print("\n=== Second Refinement (Element on right) ===")
marks_override = {3: 1}
solver.adapt_mesh(marks_override=marks_override,element_budget=28)
q_right_matrix, q_right_direct = analyze_solver(solver)


# Post-adaptation visualization (FIXED VERSION)
# Create a comprehensive figure showing solution evolution
plt.figure(figsize=(15, 10))

# Plot 1: Solution evolution through refinements
plt.subplot(2, 2, 1)
plt.plot(solver.coord, q_init_matrix, 'k--', label='Initial')
plt.plot(solver.coord, q_left_matrix, 'r-', label='After left refinement')
plt.plot(solver.coord, q_right_matrix, 'b-', label='After right refinement')
plt.plot(solver.coord, solver.get_exact_solution(), 'g:', label='Exact')
plt.title('Solution Evolution')
plt.xlabel('x')
plt.ylabel('q')
plt.grid(True)
plt.legend()

# Plot 2: Error comparison
plt.subplot(2, 2, 2)
exact = solver.get_exact_solution()
plt.plot(solver.coord, np.abs(q_init_matrix - exact), 'k--', label='Initial')
plt.plot(solver.coord, np.abs(q_left_matrix - exact), 'r-', label='After left refinement')
plt.plot(solver.coord, np.abs(q_right_matrix - exact), 'b-', label='After right refinement')
plt.title('Absolute Error')
plt.xlabel('x')
plt.ylabel('|Error|')
plt.yscale('log')
plt.grid(True)
plt.legend()

# Create a focused visualization of the boundary condition issue
plt.subplot(2, 2, 3)
plt.plot(solver.coord, q_init_matrix, 'k--', label='Initial')
plt.plot(solver.coord, q_left_matrix, 'r-', label='After left refinement')
plt.plot(solver.coord, q_right_matrix, 'b-', label='After right refinement')
plt.plot(solver.coord, solver.get_exact_solution(), 'g:', label='Exact')
plt.title('Left Boundary Region')
plt.xlabel('x')
plt.ylabel('q')
plt.xlim(-1, -0.5)  # Zoom on left boundary
plt.ylim(-0.1, 0.2)  # Adjust as needed
plt.grid(True)
plt.legend()

# Right side zoom
plt.subplot(2, 2, 4)
plt.plot(solver.coord, q_init_matrix, 'k--', label='Initial')
plt.plot(solver.coord, q_left_matrix, 'r-', label='After left refinement')
plt.plot(solver.coord, q_right_matrix, 'b-', label='After right refinement')
plt.plot(solver.coord, solver.get_exact_solution(), 'g:', label='Exact')
plt.title('Right Boundary Region')
plt.xlabel('x')
plt.ylabel('q')
plt.xlim(0.5, 1)  # Zoom on right boundary
plt.ylim(-0.1, 0.2)  # Adjust as needed
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig('solution_evolution.png')
plt.show()

# Create mesh visualization
plt.figure(figsize=(15, 5))

# Function to visualize mesh with element refinement levels
def plot_mesh(ax, xelem, title):
    ax.set_xlim(-1, 1)
    ax.set_ylim(0, 1)
    for i in range(len(xelem)-1):
        ax.axvline(x=xelem[i], color='k', linestyle='-')
    ax.axvline(x=xelem[-1], color='k', linestyle='-')
    
    # Add element numbers
    for i in range(len(xelem)-1):
        center = (xelem[i] + xelem[i+1])/2
        ax.text(center, 0.5, str(i), 
                horizontalalignment='center', 
                verticalalignment='center',
                bbox=dict(facecolor='white', alpha=0.7))
    
    ax.set_yticks([])
    ax.set_title(title)
    ax.set_xlabel('x')

# Get mesh data from each stage
xelem_init = np.array([-1, -0.5, 0, 0.5, 1])  # Initial mesh

# Create 3 subplots for each mesh stage
plt.subplot(1, 3, 1)
plot_mesh(plt.gca(), xelem_init, 'Initial Mesh')

plt.subplot(1, 3, 2)
# This would be the mesh after first refinement
# You'd need to store this information earlier in the original code
plot_mesh(plt.gca(), solver.xelem, 'After Refinements')

plt.tight_layout()
plt.savefig('mesh_evolution.png')
plt.show()

# Examine flux matrix behavior
plt.figure(figsize=(12, 5))

# Get flux matrices for analysis
def create_flux_matrix(solver):
    return Fmatrix_upwind_flux_bc(
        solver.intma, solver.nelem, solver.npoin_dg, solver.ngl, 
        solver.wave_speed, periodic=False
    )

F_final = create_flux_matrix(solver)

# Plot flux matrix as a heatmap for visualization
plt.subplot(1, 2, 1)
plt.imshow(F_final, cmap='RdBu', interpolation='nearest')
plt.colorbar(label='Flux value')
plt.title('Flux Matrix Structure')
plt.xlabel('Column index')
plt.ylabel('Row index')

# Plot diagonals of flux matrix - FIXED VERSION
plt.subplot(1, 2, 2)
diag_vals = np.diag(F_final)
plt.plot(range(len(diag_vals)), diag_vals, 'o-', label='Diagonal')
# Fix: Use proper range for superdiagonal (one element shorter)
plt.plot(range(len(diag_vals)-1), np.diag(F_final, k=1), 's-', label='Superdiagonal')
# Fix: Use proper range for subdiagonal (one element shorter)
plt.plot(range(1, len(diag_vals)), np.diag(F_final, k=-1), '^-', label='Subdiagonal')
plt.title('Flux Matrix Diagonals')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('flux_analysis.png')
plt.show()

# Print summary statistics
print("\n=== Summary Statistics ===")
print(f"Matrix approach L2 error:")
print(f"  Initial: {np.sqrt(np.mean((q_init_matrix - exact)**2)):.6e}")
print(f"  After left refinement: {np.sqrt(np.mean((q_left_matrix - exact)**2)):.6e}")
print(f"  After right refinement: {np.sqrt(np.mean((q_right_matrix - exact)**2)):.6e}")

# Conservation check
def check_conservation(q, coord):
    # Basic check: integral of solution should be conserved
    # Use trapezoidal rule for integration
    return np.trapz(q, coord)

print("\nSolution integral (conservation check):")
print(f"  Exact: {check_conservation(exact, solver.coord):.6f}")
print(f"  Initial (matrix): {check_conservation(q_init_matrix, solver.coord):.6f}")
print(f"  After left refinement: {check_conservation(q_left_matrix, solver.coord):.6f}")
print(f"  After right refinement: {check_conservation(q_right_matrix, solver.coord):.6f}")






# # Post-adaptation visualization
# # Create a comprehensive figure showing solution evolution
# plt.figure(figsize=(15, 10))

# # Plot 1: Solution evolution through refinements (matrix approach)
# plt.subplot(2, 2, 1)
# plt.plot(solver.coord, q_init_matrix, 'k--', label='Initial')
# plt.plot(solver.coord, q_left_matrix, 'r-', label='After left refinement')
# plt.plot(solver.coord, q_right_matrix, 'b-', label='After right refinement')
# plt.plot(solver.coord, solver.get_exact_solution(), 'g:', label='Exact')
# plt.title('Solution Evolution (Matrix Approach)')
# plt.xlabel('x')
# plt.ylabel('q')
# plt.grid(True)
# plt.legend()

# # Plot 2: Solution evolution through refinements (direct integration)
# plt.subplot(2, 2, 2)
# plt.plot(solver.coord, q_init_direct, 'k--', label='Initial')
# plt.plot(solver.coord, q_left_direct, 'r-', label='After left refinement')
# plt.plot(solver.coord, q_right_direct, 'b-', label='After right refinement')
# plt.plot(solver.coord, solver.get_exact_solution(), 'g:', label='Exact')
# plt.title('Solution Evolution (Direct Integration)')
# plt.xlabel('x')
# plt.ylabel('q')
# plt.grid(True)
# plt.legend()

# # Plot 3: Error comparison for matrix approach
# plt.subplot(2, 2, 3)
# exact = solver.get_exact_solution()
# plt.plot(solver.coord, np.abs(q_init_matrix - exact), 'k--', label='Initial')
# plt.plot(solver.coord, np.abs(q_left_matrix - exact), 'r-', label='After left refinement')
# plt.plot(solver.coord, np.abs(q_right_matrix - exact), 'b-', label='After right refinement')
# plt.title('Absolute Error (Matrix Approach)')
# plt.xlabel('x')
# plt.ylabel('|Error|')
# plt.yscale('log')
# plt.grid(True)
# plt.legend()

# # Plot 4: Error comparison for direct integration
# plt.subplot(2, 2, 4)
# plt.plot(solver.coord, np.abs(q_init_direct - exact), 'k--', label='Initial')
# plt.plot(solver.coord, np.abs(q_left_direct - exact), 'r-', label='After left refinement')
# plt.plot(solver.coord, np.abs(q_right_direct - exact), 'b-', label='After right refinement')
# plt.title('Absolute Error (Direct Integration)')
# plt.xlabel('x')
# plt.ylabel('|Error|')
# plt.yscale('log')
# plt.grid(True)
# plt.legend()

# plt.tight_layout()
# plt.savefig('solution_evolution.png')
# plt.show()

# # Create a focused visualization of the boundary condition issue
# plt.figure(figsize=(12, 8))

# # Left side zoom
# plt.subplot(1, 2, 1)
# plt.plot(solver.coord, q_init_matrix, 'k--', label='Initial')
# plt.plot(solver.coord, q_left_matrix, 'r-', label='After left refinement')
# plt.plot(solver.coord, q_right_matrix, 'b-', label='After right refinement')
# plt.plot(solver.coord, solver.get_exact_solution(), 'g:', label='Exact')
# plt.title('Left Boundary Region')
# plt.xlabel('x')
# plt.ylabel('q')
# plt.xlim(-1, -0.5)  # Zoom on left boundary
# plt.ylim(-0.1, 0.2)  # Adjust as needed
# plt.grid(True)
# plt.legend()

# # Right side zoom
# plt.subplot(1, 2, 2)
# plt.plot(solver.coord, q_init_matrix, 'k--', label='Initial')
# plt.plot(solver.coord, q_left_matrix, 'r-', label='After left refinement')
# plt.plot(solver.coord, q_right_matrix, 'b-', label='After right refinement')
# plt.plot(solver.coord, solver.get_exact_solution(), 'g:', label='Exact')
# plt.title('Right Boundary Region')
# plt.xlabel('x')
# plt.ylabel('q')
# plt.xlim(0.5, 1)  # Zoom on right boundary
# plt.ylim(-0.1, 0.2)  # Adjust as needed
# plt.grid(True)
# plt.legend()

# plt.tight_layout()
# plt.savefig('boundary_condition_analysis.png')
# plt.show()

# # Create mesh visualization
# plt.figure(figsize=(15, 5))

# # Function to visualize mesh with element refinement levels
# def plot_mesh(ax, xelem, title):
#     ax.set_xlim(-1, 1)
#     ax.set_ylim(0, 1)
#     for i in range(len(xelem)-1):
#         ax.axvline(x=xelem[i], color='k', linestyle='-')
#     ax.axvline(x=xelem[-1], color='k', linestyle='-')
    
#     # Add element numbers
#     for i in range(len(xelem)-1):
#         center = (xelem[i] + xelem[i+1])/2
#         ax.text(center, 0.5, str(i), 
#                 horizontalalignment='center', 
#                 verticalalignment='center',
#                 bbox=dict(facecolor='white', alpha=0.7))
    
#     ax.set_yticks([])
#     ax.set_title(title)
#     ax.set_xlabel('x')

# # Get mesh data from each stage
# xelem_init = np.array([-1, -0.5, 0, 0.5, 1])  # Initial mesh

# # Create 3 subplots for each mesh stage
# plt.subplot(1, 3, 1)
# plot_mesh(plt.gca(), xelem_init, 'Initial Mesh')

# plt.subplot(1, 3, 2)
# # This would be the mesh after first refinement
# # You'd need to store this information earlier in the original code
# plot_mesh(plt.gca(), solver.xelem, 'After Refinements')

# plt.tight_layout()
# plt.savefig('mesh_evolution.png')
# plt.show()

# # Examine flux matrix behavior
# plt.figure(figsize=(12, 5))

# # Get flux matrices for analysis
# def create_flux_matrix(solver):
#     return Fmatrix_upwind_flux_bc(
#         solver.intma, solver.nelem, solver.npoin_dg, solver.ngl, 
#         solver.wave_speed, periodic=False
#     )

# F_final = create_flux_matrix(solver)

# # Plot flux matrix as a heatmap for visualization
# plt.subplot(1, 2, 1)
# plt.imshow(F_final, cmap='RdBu', interpolation='nearest')
# plt.colorbar(label='Flux value')
# plt.title('Flux Matrix Structure')
# plt.xlabel('Column index')
# plt.ylabel('Row index')

# # Plot diagonals of flux matrix
# plt.subplot(1, 2, 2)
# diag_vals = np.diag(F_final)
# plt.plot(range(len(diag_vals)), diag_vals, 'o-', label='Diagonal')
# plt.plot(range(len(diag_vals)), np.diag(F_final, k=1), 's-', label='Superdiagonal')
# plt.plot(range(len(diag_vals)-1), np.diag(F_final, k=-1), '^-', label='Subdiagonal')
# plt.title('Flux Matrix Diagonals')
# plt.xlabel('Index')
# plt.ylabel('Value')
# plt.legend()
# plt.grid(True)

# plt.tight_layout()
# plt.savefig('flux_analysis.png')
# plt.show()

# # Print summary statistics
# print("\n=== Summary Statistics ===")
# print(f"Matrix approach L2 error:")
# print(f"  Initial: {np.sqrt(np.mean((q_init_matrix - exact)**2)):.6e}")
# print(f"  After left refinement: {np.sqrt(np.mean((q_left_matrix - exact)**2)):.6e}")
# print(f"  After right refinement: {np.sqrt(np.mean((q_right_matrix - exact)**2)):.6e}")

# print(f"\nDirect integration L2 error:")
# print(f"  Initial: {np.sqrt(np.mean((q_init_direct - exact)**2)):.6e}")
# print(f"  After left refinement: {np.sqrt(np.mean((q_left_direct - exact)**2)):.6e}")
# print(f"  After right refinement: {np.sqrt(np.mean((q_right_direct - exact)**2)):.6e}")

# # Conservation check
# def check_conservation(q, coord):
#     # Basic check: integral of solution should be conserved
#     # Use trapezoidal rule for integration
#     return np.trapz(q, coord)

# print("\nSolution integral (conservation check):")
# print(f"  Exact: {check_conservation(exact, solver.coord):.6f}")
# print(f"  Initial (matrix): {check_conservation(q_init_matrix, solver.coord):.6f}")
# print(f"  After left refinement: {check_conservation(q_left_matrix, solver.coord):.6f}")
# print(f"  After right refinement: {check_conservation(q_right_matrix, solver.coord):.6f}")
# print(f"  Initial (direct): {check_conservation(q_init_direct, solver.coord):.6f}")
# print(f"  After left refinement: {check_conservation(q_left_direct, solver.coord):.6f}")
# print(f"  After right refinement: {check_conservation(q_right_direct, solver.coord):.6f}")