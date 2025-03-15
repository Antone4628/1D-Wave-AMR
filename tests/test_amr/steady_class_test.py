"""
1D Wave Equation Steady State Solver with AMR

This script solves the steady-state version of the 1D wave equation 
using a DG method with adaptive mesh refinement.
Uses the DGWaveSolver class for the core numerical solution.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import os
import sys
import os.path
# Get absolute path to project root

PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 
    '..',
    '..'
))
sys.path.append(PROJECT_ROOT)

RESULTS_DIR = os.path.join(PROJECT_ROOT, 'results')
os.makedirs(RESULTS_DIR, exist_ok=True)

# Import the steady state solver
from numerical.solvers.dg_steady_solver import DGWaveSolver

# Define initial mesh
xelem = np.array([-1, -0.4, 0, 0.4, 1])
nelem = len(xelem) - 1

# Print initial mesh information
differences = np.diff(xelem)
print(f'Initial element sizes: {differences}')
print(f'Smallest initial element has dx: {np.min(differences)}')

# Solver parameters
max_level = 4         # Max level of refinement
nop = 4               # Polynomial order
icase = 7             # Test case number (7: Tanh function)

# Calculate smallest possible element size after refinement
dx_min = np.min(differences)/(2**max_level)
print(f'Smallest possible refined element: {dx_min}')

# Initialize solver
solver = DGWaveSolver(
    nop=nop,
    xelem=xelem,
    max_elements=40,
    max_level=max_level,
    icase=icase
)

print(f'Initializing solver with element budget: {solver.max_elements}')

# Solve and collect results - for steady case, this performs the adaptation
solutions, grids, coords = solver.solve()

# Create simple visualization with just two frames - initial and final solutions
plt.style.use('ggplot')

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
fig.tight_layout(pad=4)

# First frame - initial solution
ax1.set_xlim([-1, 1])
ax1.set_ylim([-0.1, 2.2])
ax1.set_xticks(grids[0])
ax1.tick_params(axis='x', rotation=90, labelsize=8)
ax1.set_title(f'Initial solution with {nelem} elements')
ax1.plot(coords[0], solutions[0], color='darkmagenta')
ax1.plot(coords[0], solver.get_exact_solution(), color='black', linestyle='--')

# Mark mesh points
for x in grids[0]:
    ax1.axvline(x, color='gray', linestyle='-', alpha=0.3, linewidth=0.5)

# Second frame - final adapted solution
ax2.set_xlim([-1, 1])
ax2.set_ylim([-0.1, 2.2])
ax2.set_xticks(grids[-1])
ax2.tick_params(axis='x', rotation=90, labelsize=8)
ax2.set_title(f'Final solution after adaptation with {len(grids[-1])-1} elements')
ax2.plot(coords[-1], solutions[-1], color='darkmagenta')
ax2.plot(coords[-1], solver.get_exact_solution(), color='black', linestyle='--')

# Mark mesh points
for x in grids[-1]:
    ax2.axvline(x, color='gray', linestyle='-', alpha=0.3, linewidth=0.5)

# Save the figure
filename = os.path.join(RESULTS_DIR, 'steady_wave_amr_comparison.png')
plt.savefig(filename, dpi=300, bbox_inches='tight')
print(f"Saved comparison figure to {filename}")

# Create animation showing adaptation process
plt.style.use('ggplot')
fig_anim, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim([-1, 1])
ax.set_ylim([-0.1, 2.2])
ax.set_title(f'{nelem} initial elements, AMR to level {max_level}')

# Add text annotations
frame_text = ax.text(0.05, 0.95, '',
                    horizontalalignment='left',
                    verticalalignment='top',
                    transform=ax.transAxes)
elements_text = ax.text(0.05, 0.90, '',
                   horizontalalignment='left',
                   verticalalignment='top',
                   transform=ax.transAxes)

# Initialize plot with both numerical and exact solution
num_solution_line, = ax.plot([], [], color='darkmagenta', label='Numerical')
exact_solution_line, = ax.plot([], [], color='black', linestyle='--', label='Exact')
ax.legend()

def update_data(frame):
    """Update function for animation."""
    # Update tick marks for grid
    ax.set_xticks(grids[frame])
    ax.tick_params(axis='x', rotation=90, labelsize=8)
    
    # Update solution data
    num_solution_line.set_data(coords[frame], solutions[frame])
    
    # Get exact solution on current grid
    exact_sol = solver.get_exact_solution()
    exact_solution_line.set_data(coords[frame], exact_sol)
    
    # Update text info
    frame_text.set_text(f'Adaptation step: {frame}')
    elements_text.set_text(f'Elements: {len(grids[frame])-1}')
    
    # Add vertical lines for mesh points with alpha=0.3
    for line in ax.get_lines():
        if line not in [num_solution_line, exact_solution_line]:
            line.remove()
    
    for x in grids[frame]:
        ax.axvline(x, color='gray', linestyle='-', alpha=0.3, linewidth=0.5)
    
    return num_solution_line, exact_solution_line, frame_text, elements_text

# Create animation
anim = FuncAnimation(
    fig=fig_anim,
    func=update_data,
    frames=len(solutions),
    interval=1000,  # Slower for steady case visualization
    blit=False      # Set to False to allow dynamic grid lines
)

# Save animation
gif_title = os.path.join(RESULTS_DIR, 'Steady_Wave_AMR_Solution.gif')
anim.save(gif_title, writer="pillow", fps=1)
print(f"Saved animation to {gif_title}")

plt.close('all')
print("Completed steady-state solution visualization")