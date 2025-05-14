"""
1D Wave Equation Solver with AMR - Testing Gaussian Pulse Advection (icase=9)

This script simulates the unsteady 1D advection case described in Section 4.3 of the paper
by Foucart et al. (2023), using a DG method with adaptive mesh refinement.
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

ANIMATIONS_DIR = os.path.join(PROJECT_ROOT, 'animations')
os.makedirs(ANIMATIONS_DIR, exist_ok=True)

from numerical.solvers.dg_wave_solver_clean import DGWaveSolver

# Define initial mesh for domain [-4, 4]
xelem = np.array([-4.0, -2.0, 0.0, 2.0, 4.0])
nelem = len(xelem) - 1

# Print initial mesh information
differences = np.diff(xelem)
print(f'Initial element sizes: {differences}')
print(f'Smallest initial element has dx: {np.min(differences)}')

# Solver parameters
max_level = 4         # Max level of refinement
nop = 3               # Polynomial order
courant_max = 0.1     # CFL number
time_final = 8.0      # Run for 8 time units to see pulse go full circle
icase = 9             # Test case number (9: Gaussian pulse advection)
periodic = True       # Use periodic boundary conditions

# Calculate smallest possible element size after refinement
dx_min = np.min(differences)/(2**max_level)
print(f'Smallest possible refined element: {dx_min}')

# Initialize solver
solver = DGWaveSolver(
    nop=nop,
    xelem=xelem,
    max_elements=40,
    max_level=max_level,
    courant_max=courant_max,
    icase=icase,
    periodic=periodic
)

print(f'Courant: {solver.wave_speed*solver.dt/dx_min:.6f}')
print(f'dt = {solver.dt:.6f}')
print(f'time_final = {time_final}')
print(f'timesteps = {time_final/solver.dt:.1f}')

# Solve and collect results
times, solutions, grids, coords = solver.solve(time_final)

# Create animation
plt.rcParams['animation.html'] = 'jshtml'
plt.style.use('ggplot')

fig, ax = plt.subplots(figsize=(12, 6))
ax.set_xlim([-4, 4])
ax.set_ylim([-0.1, 1.1])  # Gaussian function ranges from 0 to 1
ax.set_xticks(xelem)
ax.tick_params(axis='x', rotation=90, labelsize=8)
ax.set_title(f'Gaussian Pulse Advection (icase=9) with AMR - velocity=1.0')

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

# Plot exact solution for comparison
def exact_gaussian(x, t):
    """Get exact solution for the Gaussian pulse at time t"""
    mu = -4
    sigma_sq = 0.25
    c = 1.0
    
    # Apply periodic boundary conditions on domain [-4, 4] by summing contributions
    # from the main pulse and its periodic images
    x_shifted = x - c*t
    domain_length = 8
    
    # Sum contributions from the main pulse and one periodic image on each side
    main_pulse = np.exp(-1/(2*sigma_sq)*((x_shifted - mu)**2))
    left_image = np.exp(-1/(2*sigma_sq)*((x_shifted - mu + domain_length)**2))
    right_image = np.exp(-1/(2*sigma_sq)*((x_shifted - mu - domain_length)**2))
    
    # The final solution is the sum of all contributions
    return main_pulse + left_image + right_image
# def exact_gaussian(x, t):
#     """Get exact solution for the Gaussian pulse at time t"""
#     mu = -4
#     sigma_sq = 0.25
#     c = 1.0
    
#     # Apply periodic boundary conditions on domain [-4, 4]
#     x_shifted = x - c*t
#     domain_length = 8
    
#     # Handle periodicity for visualization
#     x_periodic = np.copy(x_shifted)
#     for i in range(len(x_periodic)):
#         if x_periodic[i] < -4:
#             x_periodic[i] += domain_length
#         elif x_periodic[i] > 4:
#             x_periodic[i] -= domain_length
    
#     return np.exp(-1/(2*sigma_sq)*(x_periodic - mu)**2)

# Initialize plots - numerical solution and exact solution
x_fine = np.linspace(-4, 4, 500)  # Fine grid for exact solution
numerical_plot = ax.plot(coords[0], solutions[0], 'b-', label='Numerical')[0]
exact_plot = ax.plot(x_fine, exact_gaussian(x_fine, 0), 'r--', label='Exact')[0]
ax.legend()

def update_data(frame):
    """Update function for animation."""
    # Update numerical solution
    numerical_plot.set_ydata(solutions[frame])
    numerical_plot.set_xdata(coords[frame])
    
    # Update exact solution
    exact_plot.set_ydata(exact_gaussian(x_fine, times[frame]))
    
    # Update mesh ticks
    ax.set_xticks(grids[frame])
    
    # Update text annotations
    frame_text.set_text(f'Frame: {frame}')
    time_text.set_text(f'Time: {times[frame]:.2f}')
    elements_text.set_text(f'Elements: {len(grids[frame])-1}')
    
    return numerical_plot, exact_plot

# Create animation
anim = FuncAnimation(
    fig=fig,
    func=update_data,
    frames=len(solutions),
    interval=50,
    blit=False  # Set to True for better performance, but might not work with text updates
)

# Save animation
gif_title = os.path.join(ANIMATIONS_DIR, 'Gaussian_Pulse_Advection_AMR.gif')
anim.save(gif_title, writer="pillow", fps=10)  # Reduced fps for better visualization

# Create snapshots at specific times
snapshot_times = [0.0, 2.0, 4.0, 6.0, 8.0]
fig2, axes = plt.subplots(len(snapshot_times), 1, figsize=(10, 10), sharex=True)
fig2.suptitle('Gaussian Pulse Advection with AMR - Snapshots')

for i, target_time in enumerate(snapshot_times):
    # Find closest time index
    time_idx = np.abs(np.array(times) - target_time).argmin()
    
    # Plot numerical solution
    axes[i].plot(coords[time_idx], solutions[time_idx], 'b-', label='Numerical')
    
    # Plot exact solution
    axes[i].plot(x_fine, exact_gaussian(x_fine, times[time_idx]), 'r--', label='Exact')
    
    # Add grid lines
    for x in grids[time_idx]:
        axes[i].axvline(x, color='gray', linestyle=':', alpha=0.5)
    
    # Label and configure subplot
    axes[i].set_title(f'Time: {times[time_idx]:.2f}')
    axes[i].set_ylim([-0.1, 1.1])
    axes[i].set_ylabel('u')
    axes[i].legend()

axes[-1].set_xlabel('x')
axes[-1].set_xlim([-4, 4])

# Save snapshot figure
plt.tight_layout()
snapshot_file = os.path.join(ANIMATIONS_DIR, 'Gaussian_Pulse_Advection_Snapshots.png')
plt.savefig(snapshot_file)

print(f"Animation saved to {gif_title}")
print(f"Snapshots saved to {snapshot_file}")

# plt.show()  # Uncomment to display plots