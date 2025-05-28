"""
1D Wave Equation Solver with RL-AMR using Mixed Approach

This script solves the 1D wave equation using a Discontinuous Galerkin method 
with adaptive mesh refinement guided by a trained reinforcement learning model.
It utilizes the mixed approach with steady-state solving between adaptations.
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

# Import the mixed solver
from numerical.solvers.dg_wave_solver_mixed_model import DGWaveSolverMixed
from numerical.amr.model_marker import ModelMarker

# Define initial mesh
xelem = np.array([-1, -0.4, 0, 0.4, 1])
nelem = len(xelem) - 1
# xelem = np.array([-1, -0.4, -0.2, 0, 0.2, 0.4, 1])
# nelem = len(xelem) - 1

# Print initial mesh information
differences = np.diff(xelem)
print(f'Initial element sizes: {differences}')
print(f'Smallest initial element has dx: {np.min(differences)}')

# Solver parameters
max_level = 8       # Max level of refinement
nop = 4             # Polynomial order
courant_max = 0.1   # CFL number
time_final = 0.02   # Final time
icase = 1           # Test case number (1: Gaussian)
periodic = True
max_elements = 50   # Maximum number of elements

# Calculate smallest possible element size after refinement
dx_min = np.min(differences)/(2**max_level)
print(f'Smallest possible refined element: {dx_min}')

# Initialize solver
solver = DGWaveSolverMixed(
    nop=nop,
    xelem=xelem,
    max_elements=max_elements,
    max_level=max_level,
    courant_max=courant_max,
    icase=icase,
    periodic=periodic
)

# Path to the trained model
# Use the model trained with the mixed approach
# model_path = os.path.join(PROJECT_ROOT, 'experiments', 'results', 'gamma_c_50.0', 'run_20250514_090135', 'models', 'final_model.zip')
model_path = os.path.join(PROJECT_ROOT, 'models', 'transferred', 'step_domain_0.05_final_model.zip')

# Initialize ModelMarker with trained model
model_marker = ModelMarker(
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

# Solve the PDE with RL-based AMR
step_count = 0
while solver.time < time_final:
    dt = min(solver.dt, time_final - solver.time)
    print(f"\nTimestep {step_count}, Time: {solver.time:.3f}")
    
    # Get marking decisions from the RL model
    marks = model_marker.mark(
        solver.active, 
        solver.label_mat, 
        solver.intma,
        solver.q
    )
    
    # Convert marks array to dictionary for compatibility with mixed solver
    marks_dict = {i: mark for i, mark in enumerate(marks) if mark != 0}
    print(f'marks: {marks}')
    
    # Apply adaptation with model-generated marks
    solver.adapt_mesh(marks)
    
    # KEY DIFFERENCE: Solve for steady-state after adaptation
    # This matches what happens in the DGAMREnvMixed environment
    improved_steady_solution = solver.steady_solve_improved()
    solver.q = improved_steady_solution
    
    # Take time step
    solver.step(dt)
    
    # Store results
    times.append(solver.time)
    solutions.append(solver.q.copy())
    grids.append(solver.xelem.copy())
    coords.append(solver.coord.copy())
    step_count += 1

# Create animation (same as before)
plt.rcParams['animation.html'] = 'jshtml'
plt.style.use('ggplot')

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim([-1, 1])
ax.set_ylim([-0.1, 1.2])
ax.set_xticks(xelem)
ax.tick_params(axis='x', rotation=90, labelsize=8)
ax.set_title(f'{nelem} initial elements, Mixed RL-AMR to level {max_level}, dt = {solver.dt:.6f}')

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
animated_plot = ax.plot(coords[0], solutions[0], color='darkmagenta')[0]

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
gif_title = os.path.join(ANIMATIONS_DIR, 'Mixed_model_RL_AMR_1D_Wave_GIF.gif')
anim.save(gif_title, writer="pillow", fps=50)

plt.show()