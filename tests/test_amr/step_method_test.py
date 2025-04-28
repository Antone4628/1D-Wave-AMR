import numpy as np
import os
import sys
import os.path
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 
    '..',
    '..'
))
sys.path.append(PROJECT_ROOT)

ANIMATIONS_DIR = os.path.join(PROJECT_ROOT, 'animations')
os.makedirs(ANIMATIONS_DIR, exist_ok=True)

from numerical.solvers.dg_wave_solver_mixed import DGWaveSolverMixed


def test_step_method():
    # Initialize the solver
    nop = 3  # Polynomial order
    xelem = np.array([-1, -0.4, 0, 0.4, 1])  # Element boundaries
    max_elements = 20  # Maximum number of elements
    max_level = 2  # Maximum refinement level
    
    # Create solver instance
    solver = DGWaveSolverMixed(
        nop=nop,
        xelem=xelem,
        max_elements=max_elements,
        max_level=max_level,
        icase=1,  # Using test case 1
        courant_max=0.1,
        periodic=True
    )
    
    # Number of time steps to take
    num_steps = 50
    
    # Create figure for visualization
    plt.figure(figsize=(12, 8))
    
    # Capture initial solution
    solutions = [solver.q.copy()]
    times = [solver.time]
    coords = [solver.coord.copy()]
    
    # Take multiple steps and store solutions
    for i in range(num_steps):
        solver.step()
        solutions.append(solver.q.copy())
        times.append(solver.time)
        coords.append(solver.coord.copy())
        
        # Print progress
        if (i+1) % 10 == 0:
            print(f"Completed {i+1}/{num_steps} steps, time: {solver.time:.4f}")
    
    # Create animation
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1.5, 1.5)
    line, = ax.plot([], [], 'o-', lw=2)
    title = ax.set_title("")
    
    def init():
        line.set_data([], [])
        return line,
    
    def animate(i):
        x = coords[i]
        y = solutions[i]
        line.set_data(x, y)
        title.set_text(f'Time: {times[i]:.4f}')
        return line, title
    
    ani = FuncAnimation(fig, animate, frames=len(solutions),
                        init_func=init, blit=True, interval=100)
    
    # Save animation
    ani.save('wave_propagation.mp4', fps=10, extra_args=['-vcodec', 'libx264'])
    
    # Plot selected frames for static visualization
    plt.figure(figsize=(15, 10))
    frame_indices = [0, 10, 20, 30, 40, 49]  # Selected frames to display
    
    for i, idx in enumerate(frame_indices):
        plt.subplot(2, 3, i+1)
        plt.plot(coords[idx], solutions[idx], 'o-')
        plt.grid(True)
        plt.title(f'Time: {times[idx]:.4f}')
        plt.xlim(-1, 1)
        plt.ylim(-1.5, 1.5)
    
    plt.tight_layout()
    plt.savefig('wave_propagation_frames.png')
    plt.show()
    
    # Compute solution differences between consecutive steps
    step_differences = []
    for i in range(1, len(solutions)):
        # Use min length for comparison since mesh might change
        min_len = min(len(solutions[i]), len(solutions[i-1]))
        diff = np.linalg.norm(solutions[i][:min_len] - solutions[i-1][:min_len])
        step_differences.append(diff)
    
    plt.figure(figsize=(10, 6))
    plt.plot(times[1:], step_differences, '-o')
    plt.grid(True)
    plt.xlabel('Time')
    plt.ylabel('Solution Change (L2 Norm)')
    plt.title('Solution Change Between Steps')
    plt.savefig('solution_differences.png')
    plt.show()
    
    # Check if solution is changing
    avg_diff = np.mean(step_differences)
    print(f"Average solution change between steps: {avg_diff:.6f}")
    
    if avg_diff < 1e-10:
        print("WARNING: Solution is not changing significantly between steps!")
    else:
        print("Solution is changing between steps as expected.")
        
    return solver, solutions, coords, times

if __name__ == "__main__":
    solver, solutions, coords, times = test_step_method()