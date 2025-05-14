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

from numerical.solvers.dg_steady_solver import DGSteadySolver

def main():
    # Set up the problem
    nop = 4  # Polynomial order
    xelem = np.array([-1, -0.5, 0, 0.5, 1])  # Initial element boundaries
    nelem = len(xelem) - 1
    
    max_level = 4  # Maximum refinement level
    max_elements = 100  # Maximum number of elements
    courant_max = 0.1  # CFL condition
    icase = 7  # Test case (7 is the tanh solution)
    
    # Create the solver
    solver = DGSteadySolver(
        nop=nop,
        xelem=xelem,
        max_elements=max_elements,
        max_level=max_level,
        courant_max=courant_max,
        icase=icase,
        verbose=True
    )
    
    # Print initial information
    print(f"Initial number of elements: {solver.nelem}")
    print(f"Element sizes: {np.diff(solver.xelem)}")
    print(f"Smallest element size after max refinement: {solver.dx_min}")
    print(f"Time step: {solver.dt}")
    
    # Solve to steady state
    residual_history, times, solutions, grids, coords = solver.solve_to_steady_state(
        max_iter=1000, 
        tol=1e-6,
        adapt_frequency=10
    )
    
    # Get exact solution for comparison
    qe = solver.get_exact_solution()
    error_norm = solver.compute_error_norm()
    print(f"Final L2 error norm: {error_norm}")
    
    # ================= Plotting Results =================
    # Plot convergence history
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Plot residual history
    ax1.semilogy(residual_history)
    ax1.set_xlabel('Iteration')
    ax1.set_ylabel('Residual (log scale)')
    ax1.set_title('Convergence History')
    ax1.grid(True)
    
    # Plot final solution
    ax2.plot(solver.coord, qe, 'b--', label='Exact Solution')
    ax2.plot(solver.coord, solver.q, 'r-', label='Computed Solution')
    ax2.set_xlabel('x')
    ax2.set_ylabel('u(x)')
    ax2.set_title(f'Final Solution (Error: {error_norm:.2e})')
    
    # Add vertical lines for element boundaries
    for x in solver.xelem:
        ax2.axvline(x, color='gray', linestyle=':')
    
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    plt.savefig('steady_solution.png')
    plt.show()
    
    # Create animation of adaptation process
    if len(solutions) > 1:
        fig, ax = plt.subplots(figsize=(10, 6))
        plt.tight_layout()
        
        # Plot the initial solution
        exact_line, = ax.plot(coords[0], qe, 'b--', label='Exact Solution')
        computed_line, = ax.plot(coords[0], solutions[0], 'r-', label='Computed Solution')
        
        # Add vertical lines for element boundaries
        element_lines = []
        for x in grids[0]:
            line = ax.axvline(x, color='gray', linestyle=':')
            element_lines.append(line)
        
        ax.set_xlabel('x')
        ax.set_ylabel('u(x)')
        ax.set_title(f'Solution and Mesh Evolution (Iteration: 0)')
        ax.legend()
        ax.grid(True)
        ax.set_xlim([-1, 1])
        ax.set_ylim([-0.5, 1.5])  # Adjust based on your solution range
        
        # Save frames
        plt.savefig('frame_0.png')
        
        for i in range(1, len(solutions)):
            # Update plot data
            computed_line.set_xdata(coords[i])
            computed_line.set_ydata(solutions[i])
            
            # Clear old element lines
            for line in element_lines:
                line.remove()
            
            # Add new element lines
            element_lines = []
            for x in grids[i]:
                line = ax.axvline(x, color='gray', linestyle=':')
                element_lines.append(line)
            
            ax.set_title(f'Solution and Mesh Evolution (Iteration: {i*10})')
            
            plt.savefig(f'frame_{i}.png')
        
        print(f"Generated {len(solutions)} frames for animation")
        print("You can create a GIF using tools like ImageMagick or use plt.animation.FuncAnimation in a more advanced script")
        
    # ================= Manual Adaptation Test =================
    print("\nTesting manual mesh adaptation...")
    
    # Reset the solver
    solver.reset()
    
    # Take a few steps to get an initial solution
    for _ in range(10):
        solver.step()
    
    # Get error before adaptation
    error_before = solver.compute_error_norm()
    print(f"Error before manual adaptation: {error_before}")
    
    # Save state before adaptation
    q_before = solver.q.copy()
    xelem_before = solver.xelem.copy()
    
    # Create manual adaptation marks (refine around the steep gradient)
    marks_override = {}
    for i, elem in enumerate(solver.active):
        # Find elements in the transition region (around x=0.25)
        # This is where the tanh function has its steep gradient
        elem_indices = solver.intma[:, i]
        elem_coords = solver.coord[elem_indices]
        elem_center = np.mean(elem_coords)
        
        # Refine elements near the transition
        if 0.0 < elem_center < 0.5:
            marks_override[i] = 1  # Mark for refinement
            
    # Apply manual adaptation
    solver.adapt_mesh(marks_override=marks_override)
    print(f"Number of elements after manual adaptation: {solver.nelem}")
    
    # Take more steps to converge on the adapted mesh
    for _ in range(50):
        residual = solver.step()
    
    # Get error after adaptation
    error_after = solver.compute_error_norm()
    print(f"Error after manual adaptation and reconvergence: {error_after}")
    print(f"Error reduction factor: {error_before/error_after:.2f}x")
    
    # Plot the results of manual adaptation
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))
    
    # Before adaptation
    ax1.plot(solver.coord, solver.get_exact_solution(), 'b--', label='Exact Solution')
    ax1.plot(solver.coord, q_before, 'r-', label='Computed Solution')
    for x in xelem_before:
        ax1.axvline(x, color='gray', linestyle=':')
    ax1.set_title(f'Before Manual Adaptation (Error: {error_before:.2e})')
    ax1.legend()
    ax1.grid(True)
    
    # After adaptation
    ax2.plot(solver.coord, solver.get_exact_solution(), 'b--', label='Exact Solution')
    ax2.plot(solver.coord, solver.q, 'r-', label='Computed Solution')
    for x in solver.xelem:
        ax2.axvline(x, color='gray', linestyle=':')
    ax2.set_title(f'After Manual Adaptation (Error: {error_after:.2e})')
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    plt.savefig('manual_adaptation.png')
    plt.show()
    
    print("\nAll tests completed successfully!")

if __name__ == "__main__":
    main()