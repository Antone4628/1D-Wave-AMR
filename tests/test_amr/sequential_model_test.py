"""
1D Wave Equation Solver with Sequential RL-AMR

This script solves the 1D wave equation using a Discontinuous Galerkin method 
with sequential adaptive mesh refinement guided by a trained reinforcement learning model.
It follows Foucart's approach of processing elements one by one in order of non-conformity.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os
import sys

# Get absolute path to project root
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 
    '..',
    '..'
))
sys.path.append(PROJECT_ROOT)

ANIMATIONS_DIR = os.path.join(PROJECT_ROOT, 'animations')
os.makedirs(ANIMATIONS_DIR, exist_ok=True)

# Import the sequential solver and adapter
from numerical.solvers.dg_wave_solver_model_sequential import DGWaveSolverSequential
from numerical.amr.model_adapt_sequential import ModelMarkerSequential

def main():
    """Run the sequential RL-AMR simulation"""
    
    # Define initial mesh
    xelem = np.array([-1, -0.4, 0, 0.4, 1])
    nelem = len(xelem) - 1

    # Print initial mesh information
    differences = np.diff(xelem)
    print(f'Initial element sizes: {differences}')
    print(f'Smallest initial element has dx: {np.min(differences)}')

    # Solver parameters
    max_level = 8       # Max level of refinement
    nop = 4             # Polynomial order
    courant_max = 0.1   # CFL number
    time_final = 0.03    # Final time
    icase = 1           # Test case number (1: Gaussian)
    periodic = True
    max_elements = 30   # Maximum number of elements
    verbose = True      # Print detailed logs

    # Calculate smallest possible element size after refinement
    dx_min = np.min(differences)/(2**max_level)
    print(f'Smallest possible refined element: {dx_min}')

    # Initialize sequential solver
    solver = DGWaveSolverSequential(
        nop=nop,
        xelem=xelem,
        max_elements=max_elements,
        max_level=max_level,
        courant_max=courant_max,
        icase=icase,
        periodic=periodic,
        verbose=verbose
    )

    # Path to the trained model
    model_path = os.path.join(PROJECT_ROOT, 'experiments', 'results', 'gamma_c_100.0', 
                              'run_20250521_141716', 'models', 'final_model.zip')

    # Initialize ModelMarkerSequential with trained model
    model_adapter = ModelMarkerSequential(
        model_path=model_path,
        solver=solver,
        element_budget=max_elements,
        verbose=True
    )

    # Solve and collect results
    times = []
    solutions = []
    grids = []
    coords = []

    # Store initial state
    times.append(solver.time)
    solutions.append(solver.q.copy())
    grids.append(solver.xelem.copy())
    coords.append(solver.coord.copy())

    # Solve the PDE with sequential RL-based AMR
    step_count = 0
    while solver.time < time_final:
        dt = min(solver.dt, time_final - solver.time)
        print(f"\nTimestep {step_count}, Time: {solver.time:.3f}")
        
        # Process elements using fixed-priority single round approach
        adaptations_made = model_adapter.mark_and_adapt_single_round()
        print(f"Made {adaptations_made} adaptations in this timestep")
        
        # Take time step
        solver.step(dt)
        
        # Store results
        times.append(solver.time)
        solutions.append(solver.q.copy())
        grids.append(solver.xelem.copy())
        coords.append(solver.coord.copy())
        step_count += 1

    # Create animation
    create_animation(times, solutions, grids, coords, solver, xelem, nelem, max_level)

def create_animation(times, solutions, grids, coords, solver, xelem, nelem, max_level):
    """Create and save animation of the simulation results"""
    
    plt.rcParams['animation.html'] = 'jshtml'
    plt.style.use('ggplot')

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim([-1, 1])
    ax.set_ylim([-0.1, 1.2])
    ax.set_xticks(xelem)
    ax.tick_params(axis='x', rotation=90, labelsize=8)
    ax.set_title(f'{nelem} initial elements, Sequential RL-AMR (Single Round) to level {max_level}, dt = {solver.dt:.6f}')

    # Add text annotations
    frame_text = ax.text(0.05, 0.95, '',
                       horizontalalignment='left',
                       verticalalignment='top',
                       transform=ax.transAxes)
    time_text = ax.text(0.05, 0.90, '',
                      horizontalalignment='left',
                      verticalalignment='top',
                      transform=ax.transAxes)
    elements_text = ax.text(0.05, 0.85, '',
                          horizontalalignment='left',
                          verticalalignment='top',
                          transform=ax.transAxes)

    # Initialize plot
    animated_plot = ax.plot(coords[0], solutions[0], color='darkblue')[0]

    def update_data(frame):
        """Update function for animation."""
        animated_plot.set_ydata(solutions[frame])
        animated_plot.set_xdata(coords[frame])
        ax.set_xticks(grids[frame])
        frame_text.set_text(f'frame: {frame}')
        time_text.set_text(f'time: {times[frame]:.2f}')
        # Calculate number of elements in this frame
        n_elements = len(grids[frame]) - 1
        elements_text.set_text(f'elements: {n_elements}')

    # Create animation
    anim = FuncAnimation(
        fig=fig,
        func=update_data,
        frames=len(solutions),
        interval=10
    )

    # Save animation
    gif_title = os.path.join(ANIMATIONS_DIR, 'Sequential_RL_AMR_Single_Round_1D_Wave_GIF.gif')
    anim.save(gif_title, writer="pillow", fps=50)
    print(f"Animation saved to {gif_title}")

    plt.show()

if __name__ == "__main__":
    main()