
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from scipy import interpolate

# Adjust these paths to match project structure
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 
    # '..',
    '..'
))
sys.path.append(PROJECT_ROOT)

from numerical.solvers.dg_wave_solver_mixed import DGWaveSolverMixed
from numerical.solvers.utils import L2_err_norm

nop = 4  # Polynomial order
# xelem = np.array([-1, -0.5, 0, 0.5, 1])  # Initial element boundaries
# nelem = len(xelem) - 1

xelem = np.array([-1, -0.5,  0, 0.5, 1])  # Initial element boundaries
nelem = len(xelem) - 1
# xelem = np.array([-1, -0.6, -0.3, -0.15, 0, 0.15, 0.3, 0.6, 1])
# nelem = len(xelem) - 1

# xelem = np.array([-1, -0.4, -0.3, -0.15, 0, 0.15, 0.3, 0.4, 1])
# nelem = len(xelem) - 1

dt = 0.0001


# Initialize solver
solver = DGWaveSolverMixed(nop=4, xelem=xelem, max_elements=40, max_level=6)

print(f'solver coords shape pre-solve {np.shape(solver.coord)}')

# Compute steady solution
q_steady = solver.steady_solve()
# solver._update_matrices()
q_steady_pt = solver.pseudo_step(dt)

print(f'solver coords shape post-solve {np.shape(solver.coord)}')
print(f'solver coords: {solver.coord}')
print(f'solver f: {solver.f}')

solve_type = 2 # 1 for pseudo-timestep, 2 for steady solve


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create a figure with two subplots side by side
from matplotlib.cm import viridis, magma
viridis_colors = [viridis(0.2), viridis(0.4), viridis(0.6), viridis(0.8)]

# Magma gradient for steady plot
magma_colors = [magma(0.2), magma(0.4), magma(0.6), magma(0.8)]
# fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2, figsize=(18, 8))
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
y_bottom = -0.2
y_top = -0.3
# Setup first subplot for projection results
ax1.set_xlim([-1, 1])
ymin = np.min(solver.f)
ymax = np.max(solver.f)
ax1.set_ylim([-0.5, 1.3])
# ax1.set_ylim([ymin, ymax])
ax1.set_xticks(xelem)
ax1.tick_params(axis='x', rotation=90, labelsize=8)
ax1.set_title("Initial Steady-State solve")
# ax1.plot(solver.coord, q_steady, color=viridis_colors[0], ls='--', label='Initial numerical')
ax1.plot(solver.coord, q_steady_pt, color=viridis_colors[0], ls='--', label='Initial numerical')
# ax1.plot(solver.coord, solver.f, color = 'darkmagenta', label = 'forcing')
# ax1.plot(solver.coord, solver.get_exact_solution(), linewidth=5, alpha=0.25, label='Exact')

# Store initial coordinate data for later reference
initial_coord = solver.coord.copy()
initial_xelem = solver.xelem.copy()
ax1.plot(initial_coord, solver.get_exact_solution(), color = 'k',linewidth=1, label='Exact')
# ax2.plot(initial_coord, solver.get_exact_solution(), color = 'blue', linewidth=5, alpha=0.25, label='Exact')
fill1 = ax1.fill_betweenx([y_bottom, y_top], solver.xelem[0], solver.xelem[-1], 
                         color='yellow', alpha=0.25)

ax1.grid(True, alpha=0.3)
# ax2.grid(True, alpha=0.3)
first_legend = ax1.legend(loc='upper right')
# ax1.legend(loc='upper right')
# ax2.legend(loc='upper right')
# Create custom handles for each fill element
fill_handles = [
    Patch(facecolor='yellow', alpha=0.25, label='level 0'),
    Patch(facecolor='orange', alpha=0.5, label='level 1'),
    Patch(facecolor='indianred', alpha=0.5, label='level 2'),
    Patch(facecolor='darkmagenta', alpha=0.5, label='level 3'),
    Patch(facecolor='darkcyan', alpha=0.5, label='level 4'),
    Patch(facecolor='cyan', alpha=0.5, label='level 5'),
    
]

fill_labels = ['level 0', 'level 1', 'level 2', 'level 3', 'level 4', 'level 5']

# Add the second legend with all fill elements
second_legend = ax1.legend(handles=fill_handles, labels=fill_labels, loc='upper left', 
                          title='Refinement Levels')

# Add the first legend back
ax1.add_artist(second_legend)
ax1.add_artist(first_legend)

# solver.q = q_steady
# solver.q = q_steady_pt



# First adaptation
print("\n=== First Adaptation ===")
print(f'xelem before adaptation: {solver.xelem}')
marks_override = {1: 1}
solver.adapt_mesh(marks_override=marks_override, element_budget=8)
print(f'Mesh size after adaptation 1: {len(solver.xelem) - 1} elements, {len(solver.coord)} points')
print(f'xelem after adaptation: {solver.xelem}')

highlight_color_3 = (1.0, 0.647, 0.0, 0.25) 

adapt_coords_1 = np.zeros(len(solver.coord))-0.25
# ax3.scatter(solver.coord, adapt_coords_1, s = 1.5,color = magma_colors[1])

# Fill the area between the ticks
ax2.fill_betweenx([y_bottom, y_top], xelem[1], xelem[2], color='orange', alpha=0.5)
# ax3.set_xticks(solver.xelem)
# ax3.grid(True, alpha=0.3)

# Plot steady solution after first adaptation
q_steady_refined_1 = solver.steady_solve()
q_refined_projection_1 = solver.q.copy()
q_steady_pt_1 = solver.pseudo_step(dt)

L2_1 = L2_err_norm(nop,nelem, q_refined_projection_1, q_steady_pt_1)


ax2.set_xlim([-1, 1])
ax2.set_ylim([-0.5, 1.3])
ax2.set_xticks(solver.xelem)
ax2.tick_params(axis='x', rotation=90, labelsize=8)
ax2.set_title('Refined element 2')
# ax2.text(0.35, 1.05, 'refined element 2', transform=ax2.transAxes,
#                        ha='center', va='center', fontsize=14, color='black',
#                        bbox=dict(facecolor=highlight_color_3, alpha=0.25, edgecolor='none'))
ax2.plot(initial_coord, q_steady_pt, color = 'k', alpha = 0.25, label = 'previous solution (initial)')
# ax2.plot(solver.coord, q_steady_refined_1, color = viridis_colors[1],label='Adaptation 1 (steady)', alpha=0.7)
# ax2.plot(solver.coord, q_refined_projection_1, color = viridis_colors[1],label='Adaptation 1 (refined projection of initial)', alpha=0.7)
# ax2.plot(solver.coord, q_steady_pt_1, color = viridis_colors[2],label='Adaptation 1 (pseudo timestep)', alpha=0.7)
if solve_type == 1: 
    ax2.plot(solver.coord, q_steady_pt_1, color = 'darkmagenta',ls='--',label='Adaptation 1 (pseudo timestep)', alpha=0.7)
    ax2.plot(solver.coord, q_refined_projection_1, color = viridis_colors[1],label='Adaptation 1 (refined projection of initial)', alpha=0.7)
    ax2.text(x=-0.5, y=0.6, s = f'L2: {L2_1}')
elif solve_type == 2:
    ax2.plot(solver.coord, q_steady_refined_1, color = viridis_colors[1],label='Adaptation 1 (steady)', alpha=0.7)
# ax2.scatter(solver.coord, q_adapted, color = magma_colors[1])
ax2.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count
ax2.scatter(solver.coord, adapt_coords_1, s = 1.5,color = magma_colors[1])
# Fill the area between the ticks
fill1 = ax2.fill_betweenx([y_bottom, y_top], solver.xelem[0], solver.xelem[-1], 
                         color='yellow', alpha=0.25)
fill2 = ax2.fill_betweenx([y_bottom, y_top], xelem[1], xelem[2], color='orange', alpha=0.5)
# ax2.text(x=-0.5, y=0.6, s = f'L2: {L2_1}')
ax2.set_xticks(solver.xelem)
ax2.grid(True, alpha=0.3)
# ax3.legend(loc='upper right')
first_legend = ax2.legend(loc='upper right')
second_legend = ax2.legend(handles=fill_handles, labels=fill_labels, loc='upper left', 
                          title='Refinement Levels')

# Add the first legend back
ax2.add_artist(second_legend)
ax2.add_artist(first_legend)













fig2, ( ax3, ax4) = plt.subplots(2, 1, figsize=(12, 8))
# # Second adaptation
print("\n=== Second Adaptation ===")
print(f'xelem before adaptation: {solver.xelem}')
coord_1 = solver.coord.copy()
marks_override = {3: 1}
solver.adapt_mesh(marks_override=marks_override, element_budget=8)
print(f'xelem after adaptation: {solver.xelem}')
print(f'Mesh size after adaptation 2: {len(solver.xelem) - 1} elements, {len(solver.coord)} points')

highlight_color_3 = (0, 0.5, 0.5, 0.25) 
adapt_coords_1 = np.zeros(len(solver.coord))-0.25

# # Plot steady solution
q_steady_refined_2 = solver.steady_solve()
q_refined_projection_2 = solver.q.copy()
q_steady_pt_2 = solver.pseudo_step(dt)
print(f'second adaptation steady solve: {q_steady_refined_2}')

L2_2 = L2_err_norm(nop,nelem, q_refined_projection_2, q_steady_pt_2)


ax3.set_xlim([-1, 1])
ax3.set_ylim([-0.5, 1.3])
ax3.set_xticks(solver.xelem)
ax3.tick_params(axis='x', rotation=90, labelsize=8)
ax3.set_title('Refined element 3')
# ax3.text(0.65, 0.75, 'refined element 4', transform=ax3.transAxes,
#                        ha='center', va='center', fontsize=14, color='black',
#                        bbox=dict(facecolor=highlight_color_3, alpha=0.25, edgecolor='none'))
if solve_type == 1:
    ax3.plot(coord_1, q_steady_pt_1, color = 'k', alpha = 0.25, label = 'previous solution')
    ax3.plot(solver.coord, q_refined_projection_2, color = viridis_colors[1],label='Adaptation 2 (refined projection of previous)', alpha=0.7)
    ax3.plot(solver.coord, q_steady_pt_2, color = 'darkmagenta',ls='--',label='Adaptation 2 (pseudo timestep)', alpha=0.7)
    ax3.text(x=-0.5, y=0.6, s = f'L2: {L2_2}')
# ax2.scatter(solver.coord, q_adapted, color = magma_colors[1])
elif solve_type == 2:
    ax3.plot(coord_1, q_steady_refined_1, color = 'k', alpha = 0.25, label = 'previous solution')
    ax3.plot(solver.coord, q_steady_refined_2, color = viridis_colors[1],label='Adaptation 2 (steady)', alpha=0.7)

ax3.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count
ax3.scatter(solver.coord, adapt_coords_1, s = 1.5,color = magma_colors[1])
# Fill the area between the ticks
fill1 = ax3.fill_betweenx([y_bottom, y_top], solver.xelem[0], solver.xelem[-1], 
                         color='yellow', alpha=0.25)
fill2 = ax3.fill_betweenx([y_bottom, y_top], solver.xelem[1], solver.xelem[5], color='orange', alpha=0.5)
ax3.set_xticks(solver.xelem)
ax3.grid(True, alpha=0.3)
first_legend =ax3.legend(loc='upper right')
second_legend = ax3.legend(handles=fill_handles, labels=fill_labels, loc='upper left', 
                          title='Refinement Levels')

# Add the first legend back
ax3.add_artist(second_legend)
ax3.add_artist(first_legend)

# # Third adaptation
print("\n=== Third Adaptation ===")
print(f'xelem before adaptation: {solver.xelem}')
coord_2 = solver.coord.copy()
marks_override = {2: 1}
solver.adapt_mesh(marks_override=marks_override, element_budget=8)
print(f'xelem after adaptation: {solver.xelem}')
print(f'Mesh size after adaptation 2: {len(solver.xelem) - 1} elements, {len(solver.coord)} points')

highlight_color_4 = (1, 0.6, 1, 0.25) 
adapt_coords_1 = np.zeros(len(solver.coord))-0.25

# # Plot steady solution
q_steady_refined_3 = solver.steady_solve()
q_refined_projection_3 = solver.q.copy()
q_steady_pt_3 = solver.pseudo_step(dt)

L2_3 = L2_err_norm(nop,nelem, q_refined_projection_3, q_steady_pt_3)
# ax4.text(x=-0.5, y=0.6, s = f'L2: {L2_3}')

# interp_func = interpolate.interp1d(coord_2, q_steady_refined_2, 
#                                   kind='linear',  # You can use 'cubic' for smoother interpolation
#                                   bounds_error=False, 
#                                   fill_value='extrapolate') 

# q_steady_refined_2_interpolated = interp_func(solver.coord)


ax4.set_xlim([-1, 1])
ax4.set_ylim([-0.5, 1.3])
ax4.set_xticks(solver.xelem)
ax4.tick_params(axis='x', rotation=90, labelsize=8)
ax4.set_title('Refined element 8')
# ax4.text(0.30, -0.80, 'refined element 3', transform=ax3.transAxes,
#                        ha='left', va='center', fontsize=14, color='black',
#                        bbox=dict(facecolor=highlight_color_4, alpha=0.25, edgecolor='none'))
# ax4.plot(coord_2, q_steady_refined_2, color = 'k', alpha = 0.25, label = 'previous solution')
# ax4.plot(solver.coord, q_steady_refined_3, color = viridis_colors[1],label='Adaptation 3 (steady)', alpha=0.7)
if solve_type == 1:
    ax4.plot(coord_2, q_steady_pt_2, color = 'k', alpha = 0.25, label = 'previous solution')
    ax4.plot(solver.coord, q_refined_projection_3, color = viridis_colors[1],label='Adaptation 3 (refined projection of previous)', alpha=0.7)
    ax4.plot(solver.coord, q_steady_pt_3, color = 'darkmagenta',ls='--',label='Adaptation 3 (pseudo timestep)', alpha=0.7)
    ax4.text(x=-0.5, y=0.6, s = f'L2: {L2_3}')
# ax2.scatter(solver.coord, q_adapted, color = magma_colors[1])
elif solve_type == 2:
    ax4.plot(coord_2, q_steady_refined_2, color = 'k', alpha = 0.25, label = 'previous solution')
    ax4.plot(solver.coord, q_steady_refined_3, color = viridis_colors[1],label='Adaptation 3 (steady)', alpha=0.7)

# ax4.plot(coord_2, q_steady_pt_2, color = 'k', alpha = 0.25, label = 'previous solution')
# ax4.plot(solver.coord, q_steady_pt_3, color = 'darkmagenta',ls = '--',label='Adaptation 3 (steady)', alpha=0.7)
# ax2.scatter(solver.coord, q_adapted, color = magma_colors[1])
ax4.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count
ax4.scatter(solver.coord, adapt_coords_1, s = 1.5,color = magma_colors[1])
# Fill the area between the ticks
fill1 = ax4.fill_betweenx([y_bottom, y_top], solver.xelem[0], solver.xelem[-1], 
                         color='yellow', alpha=0.25)
fill2 = ax4.fill_betweenx([y_bottom, y_top], solver.xelem[1], solver.xelem[6], color='orange', alpha=0.5)
fill3 = ax4.fill_betweenx([y_bottom, y_top], solver.xelem[2], solver.xelem[4], color='indianred', alpha=0.5)

# fill_between = ax4.fill_between(solver.coord, q_steady_refined_2_interpolated, q_steady_refined_3, 
#                                color='green', alpha=0.3, label='difference')
ax4.set_xticks(solver.xelem)
ax4.grid(True, alpha=0.3)
first_legend = ax4.legend(loc='upper right')
second_legend = ax4.legend(handles=fill_handles, labels=fill_labels, loc='upper left', 
                          title='Refinement Levels')

# Add the first legend back
ax4.add_artist(second_legend)
ax4.add_artist(first_legend)





fig3, (ax5, ax6) = plt.subplots(2, 1, figsize=(12, 8))

# # Fourth adaptation
print("\n=== Fourth Adaptation ===")
print(f'xelem before adaptation: {solver.xelem}')
coord_3 = solver.coord.copy()
marks_override = {4: 1}
solver.adapt_mesh(marks_override=marks_override, element_budget=8)
print(f'xelem after adaptation: {solver.xelem}')
print(f'Mesh size after adaptation 2: {len(solver.xelem) - 1} elements, {len(solver.coord)} points')

highlight_color_4 = (1, 0.6, 1, 0.25) 
adapt_coords_1 = np.zeros(len(solver.coord))-0.25

# # Plot steady solution
q_steady_refined_4 = solver.steady_solve()
q_refined_projection_4 = solver.q.copy()
q_steady_pt_4 = solver.pseudo_step(dt)

L2_4 = L2_err_norm(nop,nelem, q_refined_projection_4, q_steady_pt_4)
# ax5.text(x=-0.5, y=0.6, s = f'L2: {L2_4}')

ax5.set_xlim([-1, 1])
ax5.set_ylim([-0.5, 1.3])
ax5.set_xticks(solver.xelem)
ax5.tick_params(axis='x', rotation=90, labelsize=8)
ax5.set_title('Refined element 9')
# ax4.text(0.30, -0.80, 'refined element 3', transform=ax3.transAxes,
#                        ha='left', va='center', fontsize=14, color='black',
#                        bbox=dict(facecolor=highlight_color_4, alpha=0.25, edgecolor='none'))
# ax5.plot(coord_3, q_steady_refined_3, color = 'k', alpha = 0.25, label = 'previous solution')
# ax5.plot(solver.coord, q_steady_refined_4, color = viridis_colors[1],label='Adaptation 3 (steady)', alpha=0.7)
if solve_type == 1:
    ax5.plot(coord_3, q_steady_pt_3, color = 'k', alpha = 0.25, label = 'previous solution')
    ax5.plot(solver.coord, q_refined_projection_4, color = viridis_colors[1],label='Adaptation 4 (refined projection of previous)', alpha=0.7)
    ax5.plot(solver.coord, q_steady_pt_4, color = 'darkmagenta',ls='--',label='Adaptation 4 (pseudo timestep)', alpha=0.7)
    ax5.text(x=-0.5, y=0.6, s = f'L2: {L2_4}')
# ax2.scatter(solver.coord, q_adapted, color = magma_colors[1])
elif solve_type == 2:
    ax5.plot(coord_3, q_steady_refined_3, color = 'k', alpha = 0.25, label = 'previous solution')
    ax5.plot(solver.coord, q_steady_refined_4, color = viridis_colors[1],label='Adaptation 4 (steady)', alpha=0.7)
# ax5.plot(coord_3, q_steady_pt_3, color = 'k', alpha = 0.25, label = 'previous solution')
# ax5.plot(solver.coord, q_steady_pt_4, color = 'darkmagenta',ls = '--', label='Adaptation 3 (steady)', alpha=0.7)
# ax5.plot(solver.coord, solver.get_exact_solution(), color = 'k',linewidth=1, label='Exact')
# ax2.scatter(solver.coord, q_adapted, color = magma_colors[1])
ax5.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count
ax5.scatter(solver.coord, adapt_coords_1, s = 1.5,color = magma_colors[1])
# Fill the area between the ticks
fill1 = ax5.fill_betweenx([y_bottom, y_top], solver.xelem[0], solver.xelem[-1], 
                         color='yellow', alpha=0.25)
fill2 = ax5.fill_betweenx([y_bottom, y_top], solver.xelem[1], solver.xelem[8], color='orange', alpha=0.5)
fill3 = ax5.fill_betweenx([y_bottom, y_top], solver.xelem[2], solver.xelem[6], color='indianred', alpha=0.5)
ax5.set_xticks(solver.xelem)
ax5.grid(True, alpha=0.3)
first_legend = ax5.legend(loc='upper right')
second_legend = ax5.legend(handles=fill_handles, labels=fill_labels, loc='upper left', 
                          title='Refinement Levels')

# Add the first legend back
ax5.add_artist(second_legend)
ax5.add_artist(first_legend)

# # Fifth adaptation
print("\n=== Fifth Adaptation ===")
print(f'xelem before adaptation: {solver.xelem}')
coord_4 = solver.coord.copy()
marks_override = {4: 1}
solver.adapt_mesh(marks_override=marks_override, element_budget=12)
print(f'xelem after adaptation: {solver.xelem}')
print(f'Mesh size after adaptation 2: {len(solver.xelem) - 1} elements, {len(solver.coord)} points')

marks_override = {3: 1}
solver.adapt_mesh(marks_override=marks_override, element_budget=12)
print(f'xelem after adaptation: {solver.xelem}')
print(f'Mesh size after adaptation 2: {len(solver.xelem) - 1} elements, {len(solver.coord)} points')

highlight_color_4 = (1, 0.6, 1, 0.25) 
adapt_coords_1 = np.zeros(len(solver.coord))-0.25

# # Plot steady solution
q_steady_refined_5 = solver.steady_solve()
q_refined_projection_5 = solver.q.copy()
q_steady_pt_5 = solver.pseudo_step(dt)
L2_5 = L2_err_norm(nop,nelem, q_refined_projection_5, q_steady_pt_5)
# ax6.text(x=-0.5, y=0.6, s = f'L2: {L2_5}')

ax6.set_xlim([-1, 1])
ax6.set_ylim([-0.5, 1.3])
ax6.set_xticks(solver.xelem)
ax6.tick_params(axis='x', rotation=90, labelsize=8)
ax6.set_title('Refined elements 20 and 21')
# ax4.text(0.30, -0.80, 'refined element 3', transform=ax3.transAxes,
#                        ha='left', va='center', fontsize=14, color='black',
#                        bbox=dict(facecolor=highlight_color_4, alpha=0.25, edgecolor='none'))
# ax6.plot(coord_4, q_steady_refined_4, color = 'k', alpha = 0.25, label = 'previous solution')
# ax6.plot(solver.coord, q_steady_refined_5, color = viridis_colors[1],label='Adaptation 3 (steady)', alpha=0.7)
if solve_type == 1:
    ax6.plot(coord_4, q_steady_pt_4, color = 'k', alpha = 0.25, label = 'previous solution')
    ax6.plot(solver.coord, q_refined_projection_5, color = viridis_colors[1],label='Adaptation 5 (refined projection of previous)', alpha=0.7)
    ax6.plot(solver.coord, q_steady_pt_5, color = 'darkmagenta',ls='--',label='Adaptation 5 (pseudo timestep)', alpha=0.7)
    ax6.text(x=-0.5, y=0.6, s = f'L2: {L2_5}')
# ax2.scatter(solver.coord, q_adapted, color = magma_colors[1])
elif solve_type == 2:
    ax6.plot(coord_4, q_steady_refined_4, color = 'k', alpha = 0.25, label = 'previous solution')
    ax6.plot(solver.coord, q_steady_refined_5, color = viridis_colors[1],label='Adaptation 5 (steady)', alpha=0.7)
# ax6.plot(coord_4, q_steady_pt_4, color = 'k', alpha = 0.25, label = 'previous solution')
# ax6.plot(solver.coord, q_steady_pt_5, color = 'darkmagenta',ls = '--', label='Adaptation 3 (steady)', alpha=0.7)
# ax2.scatter(solver.coord, q_adapted, color = magma_colors[1])
ax6.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count
ax6.scatter(solver.coord, adapt_coords_1, s = 1.5,color = magma_colors[1])
# Fill the area between the ticks
fill1 = ax6.fill_betweenx([y_bottom, y_top], solver.xelem[0], solver.xelem[-1], 
                         color='yellow', alpha=0.25)
fill2 = ax6.fill_betweenx([y_bottom, y_top], solver.xelem[1], solver.xelem[9], color='orange', alpha=0.5)
fill3 = ax6.fill_betweenx([y_bottom, y_top], solver.xelem[2], solver.xelem[8], color='indianred', alpha=0.5)
fill4 = ax6.fill_betweenx([y_bottom, y_top], solver.xelem[3], solver.xelem[7], color='darkmagenta', alpha=0.5)
ax6.set_xticks(solver.xelem)
ax6.grid(True, alpha=0.3)
first_legend = ax6.legend(loc='upper right')
second_legend = ax6.legend(handles=fill_handles, labels=fill_labels, loc='upper left', 
                          title='Refinement Levels')

# Add the first legend back
ax6.add_artist(second_legend)
ax6.add_artist(first_legend)


fig4, (ax7, ax8) = plt.subplots(2, 1, figsize=(12, 8))

# # Sixth adaptation
print("\n=== Sixh Adaptation ===")
print(f'xelem before adaptation: {solver.xelem}')
coord_5 = solver.coord.copy()
marks_override = {5: 1}
solver.adapt_mesh(marks_override=marks_override, element_budget=14)
print(f'xelem after adaptation: {solver.xelem}')
print(f'Mesh size after adaptation 2: {len(solver.xelem) - 1} elements, {len(solver.coord)} points')

marks_override = {4: 1}
solver.adapt_mesh(marks_override=marks_override, element_budget=14)
print(f'xelem after adaptation: {solver.xelem}')
print(f'Mesh size after adaptation 2: {len(solver.xelem) - 1} elements, {len(solver.coord)} points')

highlight_color_4 = (1, 0.6, 1, 0.25) 
adapt_coords_1 = np.zeros(len(solver.coord))-0.25

# # Plot steady solution
q_steady_refined_6 = solver.steady_solve()
q_refined_projection_6 = solver.q.copy()
q_steady_pt_6 = solver.pseudo_step(dt)
L2_6 = L2_err_norm(nop,nelem, q_refined_projection_6, q_steady_pt_6)
# ax7.text(x=-0.5, y=0.6, s = f'L2: {L2_6}')

ax7.set_xlim([-0.5, 0.5])
ax7.set_ylim([-0.5, 1.3])
ax7.set_xticks(solver.xelem)[3:-3]
ax7.tick_params(axis='x', rotation=90, labelsize=8)
ax7.set_title('Refined elements 43, 44, 45, and 46')
# ax4.text(0.30, -0.80, 'refined element 3', transform=ax3.transAxes,
#                        ha='left', va='center', fontsize=14, color='black',
#                        bbox=dict(facecolor=highlight_color_4, alpha=0.25, edgecolor='none'))
# ax7.plot(coord_5, q_steady_refined_5, color = 'k', alpha = 0.25, label = 'previous solution')
# ax7.plot(solver.coord, q_steady_refined_6, color = viridis_colors[1],label='Adaptation 3 (steady)', alpha=0.7)
if solve_type == 1:
    ax7.plot(coord_5, q_steady_pt_5, color = 'k', alpha = 0.25, label = 'previous solution')
    ax7.plot(solver.coord, q_refined_projection_6, color = viridis_colors[1],label='Adaptation 6 (refined projection of previous)', alpha=0.7)
    ax7.plot(solver.coord, q_steady_pt_6, color = 'darkmagenta',ls='--',label='Adaptation 6 (pseudo timestep)', alpha=0.7)
    ax7.text(x=-0.5, y=0.6, s = f'L2: {L2_6}')
# ax2.scatter(solver.coord, q_adapted, color = magma_colors[1])
elif solve_type == 2:
    ax7.plot(coord_5, q_steady_refined_5, color = 'k', alpha = 0.25, label = 'previous solution')
    ax7.plot(solver.coord, q_steady_refined_6, color = viridis_colors[1],label='Adaptation 6 (steady)', alpha=0.7)
# ax7.plot(coord_5, q_steady_pt_5, color = 'k', alpha = 0.25, label = 'previous solution')
# ax7.plot(solver.coord, q_steady_pt_6, color = 'darkmagenta',ls = '--',label='Adaptation 3 (steady)', alpha=0.7)
# ax2.scatter(solver.coord, q_adapted, color = magma_colors[1])
ax7.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count
ax7.scatter(solver.coord, adapt_coords_1, s = 1.5,color = magma_colors[1])
# Fill the area between the ticks
fill1 = ax7.fill_betweenx([y_bottom, y_top], solver.xelem[0], solver.xelem[-1], 
                         color='yellow', alpha=0.25)
fill2 = ax7.fill_betweenx([y_bottom, y_top], solver.xelem[1], solver.xelem[11], color='orange', alpha=0.5)
fill3 = ax7.fill_betweenx([y_bottom, y_top], solver.xelem[2], solver.xelem[10], color='indianred', alpha=0.5)
fill4 = ax7.fill_betweenx([y_bottom, y_top], solver.xelem[3], solver.xelem[9], color='darkmagenta', alpha=0.5)
fill5 = ax7.fill_betweenx([y_bottom, y_top], solver.xelem[4], solver.xelem[8], color='darkcyan', alpha=0.75)
# ax7.set_xticks(solver.xelem)
ax7.grid(True, alpha=0.3)
first_legend = ax7.legend(loc='upper right')
second_legend = ax7.legend(handles=fill_handles, labels=fill_labels, loc='upper left', 
                          title='Refinement Levels')

# Add the first legend back
ax7.add_artist(second_legend)
ax7.add_artist(first_legend)



# solver.q = q_steady_refined_6
# q_steady_refined_6_stepped = solver.q


for i in range (20):
    solver.step(dt=0.02)
# # Seventh adaptation
print("\n=== Seventh Adaptation ===")
print(f'xelem before adaptation: {solver.xelem}')
coord_6 = solver.coord.copy()
marks_override = {6: 1}
solver.adapt_mesh(marks_override=marks_override, element_budget=16)
print(f'xelem after adaptation: {solver.xelem}')
print(f'Mesh size after adaptation 2: {len(solver.xelem) - 1} elements, {len(solver.coord)} points')

marks_override = {5: 1}
solver.adapt_mesh(marks_override=marks_override, element_budget=16)
print(f'xelem after adaptation: {solver.xelem}')
print(f'Mesh size after adaptation 2: {len(solver.xelem) - 1} elements, {len(solver.coord)} points')

highlight_color_4 = (1, 0.6, 1, 0.25) 
adapt_coords_1 = np.zeros(len(solver.coord))-0.25

# # Plot steady solution
q_steady_refined_7 = solver.steady_solve()
q_refined_projection_7 = solver.q.copy()
q_steady_pt_7 = solver.pseudo_step(dt=0.000001)

ax8.set_xlim([-1, 1])
ax8.set_ylim([-0.5, 1.3])
ax8.set_xticks(solver.xelem)
ax8.tick_params(axis='x', rotation=90, labelsize=8)
ax8.set_title('Refined center elements')
# ax4.text(0.30, -0.80, 'refined element 3', transform=ax3.transAxes,
#                        ha='left', va='center', fontsize=14, color='black',
#                        bbox=dict(facecolor=highlight_color_4, alpha=0.25, edgecolor='none'))
# ax8.plot(coord_6, q_steady_refined_6_stepped, color = 'k', alpha = 0.25, label = 'previous solution')
# ax8.plot(solver.coord, q_steady_refined_7, color = viridis_colors[1],label='Adaptation 3 (steady)', alpha=0.7)
if solve_type == 1:
    ax8.plot(coord_6, q_steady_pt_6, color = 'k', alpha = 0.25, label = 'previous solution')
    ax8.plot(solver.coord, q_refined_projection_7, color = viridis_colors[1],label='Adaptation 7 (refined projection of previous)', alpha=0.7)
    ax8.plot(solver.coord, q_steady_pt_7, color = 'darkmagenta',ls='--',label='Adaptation 7 (pseudo timestep)', alpha=0.7)
    # ax6.text(x=-0.5, y=0.6, s = f'L2: {L2_5}')
# ax2.scatter(solver.coord, q_adapted, color = magma_colors[1])
elif solve_type == 2:
    ax8.plot(coord_6, q_steady_refined_6, color = 'k', alpha = 0.25, label = 'previous solution')
    ax8.plot(solver.coord, q_steady_refined_7, color = viridis_colors[1],label='Adaptation 7 (steady)', alpha=0.7)
# ax8.plot(coord_6, q_steady_pt_6, color = 'k', alpha = 0.25, label = 'previous solution')
# ax8.plot(solver.coord, q_steady_pt_7, color = 'darkmagenta',ls = '--',label='Adaptation 3 (steady)', alpha=0.7)
# ax8.plot(solver.coord, q_refined_projection_7, color = 'darkmagenta',ls = '--',label='Adaptation 3 (steady)', alpha=0.7)
# ax2.scatter(solver.coord, q_adapted, color = magma_colors[1])
ax8.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count
ax8.scatter(solver.coord, adapt_coords_1, s = 1.5,color = magma_colors[1])
# Fill the area between the ticks
fill1 = ax8.fill_betweenx([y_bottom, y_top], solver.xelem[0], solver.xelem[-1], 
                         color='yellow', alpha=0.25)
fill2 = ax8.fill_betweenx([y_bottom, y_top], solver.xelem[1], solver.xelem[13], color='orange', alpha=0.5)
fill3 = ax8.fill_betweenx([y_bottom, y_top], solver.xelem[2], solver.xelem[12], color='indianred', alpha=0.5)
fill4 = ax8.fill_betweenx([y_bottom, y_top], solver.xelem[3], solver.xelem[11], color='darkmagenta', alpha=0.5)
fill5 = ax8.fill_betweenx([y_bottom, y_top], solver.xelem[4], solver.xelem[10], color='darkcyan', alpha=0.75)
fill6 = ax8.fill_betweenx([y_bottom, y_top], solver.xelem[5], solver.xelem[9], color='cyan', alpha=0.85, label = 'refinement level 5')
ax8.set_xticks(solver.xelem)
first_legend = ax8.legend(loc='upper right')
second_legend = ax8.legend(handles=fill_handles, labels=fill_labels, loc='upper left', 
                          title='Refinement Levels')



# Add the first legend back
ax8.add_artist(second_legend)
ax8.add_artist(first_legend)

custom_lines = [Line2D([0], [0], color='magenta', lw=4, alpha=0.25)]
custom_labels = ['refinement level 4','refinement level 5']

# Add the second legend
second_legend = ax8.legend(custom_lines, custom_labels, loc='upper left')

# Add the first legend back (otherwise it gets overwritten)
ax8.add_artist(first_legend)
ax8.grid(True, alpha=0.3)
ax8.legend(loc='upper right')









# # First adaptation
# print("\n=== First Adaptation ===")
# print(f'xelem before adaptation: {solver.xelem}')
# marks_override = {1: 1}
# solver.adapt_mesh(marks_override=marks_override, element_budget=8)
# print(f'Mesh size after adaptation 1: {len(solver.xelem) - 1} elements, {len(solver.coord)} points')
# print(f'xelem after adaptation: {solver.xelem}')

# highlight_color_3 = (1.0, 0.647, 0.0, 0.25) 

# adapt_coords_1 = np.zeros(len(solver.coord))-0.25
# # ax3.scatter(solver.coord, adapt_coords_1, s = 1.5,color = magma_colors[1])
# y_bottom = -0.2
# y_top = -0.3
# # Fill the area between the ticks
# ax2.fill_betweenx([y_bottom, y_top], xelem[1], xelem[2], color='orange', alpha=0.5)
# # ax3.set_xticks(solver.xelem)
# # ax3.grid(True, alpha=0.3)

# # Plot steady solution after first adaptation
# q_steady_refined_1 = solver.steady_solve()
# ax2.set_xlim([-1, 1])
# ax2.set_ylim([-0.5, 1.3])
# ax2.set_xticks(solver.xelem)
# ax2.tick_params(axis='x', rotation=90, labelsize=8)
# ax2.set_title('Refined element 2')
# # ax2.text(0.35, 1.05, 'refined element 2', transform=ax2.transAxes,
# #                        ha='center', va='center', fontsize=14, color='black',
# #                        bbox=dict(facecolor=highlight_color_3, alpha=0.25, edgecolor='none'))
# ax2.plot(initial_coord, q_steady, color = 'k', alpha = 0.25, label = 'previous solution')
# ax2.plot(solver.coord, q_steady_refined_1, color = viridis_colors[1],label='Adaptation 1 (steady)', alpha=0.7)
# # ax2.scatter(solver.coord, q_adapted, color = magma_colors[1])
# ax2.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count
# ax2.scatter(solver.coord, adapt_coords_1, s = 1.5,color = magma_colors[1])
# # Fill the area between the ticks
# ax2.fill_betweenx([y_bottom, y_top], xelem[1], xelem[2], color='orange', alpha=0.5)
# ax2.set_xticks(solver.xelem)
# ax2.grid(True, alpha=0.3)
# # ax3.legend(loc='upper right')
# ax2.legend(loc='upper right')


# # # Second adaptation
# print("\n=== Second Adaptation ===")
# print(f'xelem before adaptation: {solver.xelem}')
# coord_1 = solver.coord.copy()
# marks_override = {3: 1}
# solver.adapt_mesh(marks_override=marks_override, element_budget=8)
# print(f'xelem after adaptation: {solver.xelem}')
# print(f'Mesh size after adaptation 2: {len(solver.xelem) - 1} elements, {len(solver.coord)} points')

# highlight_color_3 = (0, 0.5, 0.5, 0.25) 
# adapt_coords_1 = np.zeros(len(solver.coord))-0.25

# # # Plot steady solution
# q_steady_refined_2 = solver.steady_solve()
# print(f'second adaptation steady solve: {q_steady_refined_2}')

# ax3.set_xlim([-1, 1])
# ax3.set_ylim([-0.5, 1.3])
# ax3.set_xticks(solver.xelem)
# ax3.tick_params(axis='x', rotation=90, labelsize=8)
# ax3.set_title('Refined element 4')
# # ax3.text(0.65, 0.75, 'refined element 4', transform=ax3.transAxes,
# #                        ha='center', va='center', fontsize=14, color='black',
# #                        bbox=dict(facecolor=highlight_color_3, alpha=0.25, edgecolor='none'))
# ax3.plot(coord_1, q_steady_refined_1, color = 'k', alpha = 0.25, label = 'previous solution')
# ax3.plot(solver.coord, q_steady_refined_2, color = viridis_colors[1],label='Adaptation 2 (steady)', alpha=0.7)
# # ax2.scatter(solver.coord, q_adapted, color = magma_colors[1])
# ax3.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count
# ax3.scatter(solver.coord, adapt_coords_1, s = 1.5,color = magma_colors[1])
# # Fill the area between the ticks
# ax3.fill_betweenx([y_bottom, y_top], solver.xelem[3], solver.xelem[5], color='teal', alpha=0.5)
# ax3.set_xticks(solver.xelem)
# ax3.grid(True, alpha=0.3)
# ax3.legend(loc='upper right')

# # # Third adaptation
# print("\n=== Third Adaptation ===")
# print(f'xelem before adaptation: {solver.xelem}')
# coord_2 = solver.coord.copy()
# marks_override = {2: 1}
# solver.adapt_mesh(marks_override=marks_override, element_budget=8)
# print(f'xelem after adaptation: {solver.xelem}')
# print(f'Mesh size after adaptation 2: {len(solver.xelem) - 1} elements, {len(solver.coord)} points')

# highlight_color_4 = (1, 0.6, 1, 0.25) 
# adapt_coords_1 = np.zeros(len(solver.coord))-0.25

# # # Plot steady solution
# q_steady_refined_3 = solver.steady_solve()

# ax4.set_xlim([-1, 1])
# ax4.set_ylim([-0.5, 1.3])
# ax4.set_xticks(solver.xelem)
# ax4.tick_params(axis='x', rotation=90, labelsize=8)
# ax4.set_title('Refined element 3')
# # ax4.text(0.30, -0.80, 'refined element 3', transform=ax3.transAxes,
# #                        ha='left', va='center', fontsize=14, color='black',
# #                        bbox=dict(facecolor=highlight_color_4, alpha=0.25, edgecolor='none'))
# ax4.plot(coord_2, q_steady_refined_2, color = 'k', alpha = 0.25, label = 'previous solution')
# ax4.plot(solver.coord, q_steady_refined_3, color = viridis_colors[1],label='Adaptation 3 (steady)', alpha=0.7)
# # ax2.scatter(solver.coord, q_adapted, color = magma_colors[1])
# ax4.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count
# ax4.scatter(solver.coord, adapt_coords_1, s = 1.5,color = magma_colors[1])
# # Fill the area between the ticks
# ax4.fill_betweenx([y_bottom, y_top], solver.xelem[2], solver.xelem[4], color='magenta', alpha=0.5)
# ax4.set_xticks(solver.xelem)
# ax4.grid(True, alpha=0.3)
# ax4.legend(loc='upper right')



# fig2, (ax10,ax12,ax14,ax16) = plt.subplots(4, 1, figsize=(10, 8))
# fig2, (ax10,ax12) = plt.subplots(2, 1, figsize=(10, 8))
# # Forth adaptation
# print("\n=== Fourth Adaptation ===")
# print(f'xelem before adaptation: {solver.xelem}')
# coord_3 = solver.coord.copy()
# marks_override = {4: 1}
# solver.adapt_mesh(marks_override=marks_override, element_budget=8)
# print(f'xelem after adaptation: {solver.xelem}')
# print(f'Mesh size after adaptation 2: {len(solver.xelem) - 1} elements, {len(solver.coord)} points')

# # Plot projected solution
# # q_adapted_4 = solver.q.copy()
# # ax9.set_xlim([-1, 1])
# # ax9.set_ylim([-0.5, 1.3])
# # ax9.set_xticks(solver.xelem)
# # ax9.tick_params(axis='x', rotation=90, labelsize=8)
# # highlight_color_7 = (1, 0.6, 1, 0.25) 
# # # ax9.set_title('Fourth adaptation')
# # # ax3.text(0.5, 1.05, 'solution after adapting element 1', transform=ax3.transAxes,
# # #                        ha='right', va='center', fontsize=14, color='black')
# # ax9.text(0.75, 2.55, 'refined element 4', transform=ax3.transAxes,
# #                        ha='center', va='center', fontsize=14, color='black',
# #                        bbox=dict(facecolor=highlight_color_7, alpha=0.25, edgecolor='none'))
# # ax9.plot(coord_3, q_adapted_3, color = 'k', alpha = 0.25, label = 'previous solution')
# # ax9.plot(solver.coord,  q_adapted_4, color = viridis_colors[1], label='adapted solution (projection)', alpha=0.7)
# # # ax1.scatter(solver.coord, q_adapted, color = magma_colors[1])
# # ax9.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count
# adapt_coords_1 = np.zeros(len(solver.coord))-0.25
# # ax9.scatter(solver.coord, adapt_coords_1, s = 1.5,color = magma_colors[1])
# # y_bottom = -0.2
# # y_top = -0.3
# # # Fill the area between the ticks
# # ax9.fill_betweenx([y_bottom, y_top], solver.xelem[4], solver.xelem[6], color='magenta', alpha=0.5)
# # ax9.set_xticks(solver.xelem)
# # ax9.grid(True, alpha=0.3)
# # ax9.legend(loc='upper right')
# # ax5.plot(solver.coord, q_adapted_2, color = viridis_colors[2],label='Adaptation 2 (projection)', alpha=0.7)
# # ax5.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count

# # Plot steady solution
# q_steady_refined_4 = solver.steady_solve()

# ax10.set_xlim([-0.5, 0.5])
# ax10.set_ylim([-0.5, 1.3])
# ax10.set_xticks(solver.xelem)
# ax10.tick_params(axis='x', rotation=90, labelsize=8)
# ax10.text(0.60, 2.55, 'refined element 4', transform=ax3.transAxes,
#                        ha='left', va='center', fontsize=14, color='black',
#                        bbox=dict(facecolor=highlight_color_7, alpha=0.25, edgecolor='none'))
# ax10.plot(coord_3, q_steady_refined_3, color = 'k', alpha = 0.25, label = 'previous solution')
# ax10.plot(solver.coord, q_steady_refined_4, color = viridis_colors[1],label='Adaptation 3 (steady)', alpha=0.7)
# # ax2.scatter(solver.coord, q_adapted, color = magma_colors[1])
# ax10.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count
# ax10.scatter(solver.coord, adapt_coords_1, s = 1.5,color = magma_colors[1])
# # Fill the area between the ticks
# ax10.fill_betweenx([y_bottom, y_top], solver.xelem[4], solver.xelem[6], color='magenta', alpha=0.5)
# ax10.set_xticks(solver.xelem)
# ax10.grid(True, alpha=0.3)
# ax10.legend(loc='upper right')



# # Fifth adaptation
# print("\n=== Fifth Adaptation ===")
# print(f'xelem before adaptation: {solver.xelem}')
# coord_4 = solver.coord.copy()
# marks_override = {4: 1}
# solver.adapt_mesh(marks_override=marks_override, element_budget=12)
# print(f'xelem after adaptation: {solver.xelem}')
# print(f'Mesh size after adaptation 2: {len(solver.xelem) - 1} elements, {len(solver.coord)} points')
# adapt_coords_1 = np.zeros(len(solver.coord))-0.25

# # Plot steady solution
# q_steady_refined_5 = solver.steady_solve()

# ax12.set_xlim([-0.25, 0.25])
# ax12.set_ylim([-0.5, 1.3])
# ax12.set_xticks(solver.xelem[2:-2])
# ax12.tick_params(axis='x', rotation=90, labelsize=8)
# ax12.text(0.60, -1.05, 'refined element 4', transform=ax3.transAxes,
#                        ha='left', va='center', fontsize=14, color='black',
#                        bbox=dict(facecolor=highlight_color_7, alpha=0.25, edgecolor='none'))
# ax12.plot(coord_4, q_steady_refined_4, color = 'k', alpha = 0.25, label = 'previous solution')
# ax12.plot(solver.coord, q_steady_refined_5, color = viridis_colors[1],label='Adaptation 5 (steady)', alpha=0.7)
# # ax2.scatter(solver.coord, q_adapted, color = magma_colors[1])
# ax12.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count
# ax12.scatter(solver.coord, adapt_coords_1, s = 1.5,color = magma_colors[1])
# # Fill the area between the ticks
# ax12.fill_betweenx([y_bottom, y_top], solver.xelem[4], solver.xelem[6], color='magenta', alpha=0.5)
# ax12.set_xticks(solver.xelem[2:-2])
# ax12.grid(True, alpha=0.3)
# ax12.legend(loc='upper right')
# # ax6.plot(solver.coord, q_steady_refined_2, color = viridis_colors[2],label='Adaptation 2 (steady)', alpha=0.7)
# # ax6.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count

# # Third adaptation
# print("\n=== Third Adaptation ===")
# marks_override = {2: 1}
# solver.adapt_mesh(marks_override=marks_override, element_budget=8)
# print(f'Mesh size after adaptation 3: {len(solver.xelem) - 1} elements, {len(solver.coord)} points')

# # Plot projected solution
# q_adapted = solver.q.copy()
# ax1.plot(solver.coord, q_adapted, color = viridis_colors[3],label='Adaptation 3 (projection)', alpha=0.7)
# ax1.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count



# # Plot steady solution
# q_steady_refined = solver.steady_solve()
# ax2.plot(solver.coord, q_steady_refined, color = viridis_colors[3],label='Adaptation 3 (steady)', alpha=0.7)
# ax2.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count


# ax1.plot(initial_coord, solver.get_exact_solution(), color = 'blue',linewidth=5, alpha=0.25, label='Exact')
# ax2.plot(initial_coord, solver.get_exact_solution(), color = 'blue', linewidth=5, alpha=0.25, label='Exact')

# Update tick marks to show element boundaries
# ax1.set_xticks(solver.xelem)
# ax2.set_xticks(solver.xelem)

# Add legends
ax1.legend(loc='upper right')
# ax2.legend(loc='upper right')

# Add grid lines

# ax3.grid(True, alpha=0.3)

# Adjust layout and show



# x = np.linspace(0, 2 * np.pi, 400)
# y = np.sin(x ** 2)

# # Create a 4x2 grid of subplots
# fig1, axs = plt.subplots(4, 2, figsize=(10, 8))

# # Plot on each subplot
# for i in range(4):
#     for j in range(2):
#         axs[i, j].plot(x, y)
#         axs[i, j].set_title(f"Plot {i * 2 + j + 1}")

# Adjust layout
# plt.tight_layout()
plt.tight_layout()
plt.show()













#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``
# # fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2, figsize=(18, 8))
# fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2, figsize=(18, 8))

# # Setup first subplot for projection results
# ax1.set_xlim([-1, 1])
# ax1.set_ylim([-0.5, 1.3])
# ax1.set_xticks(xelem)
# ax1.tick_params(axis='x', rotation=90, labelsize=8)
# ax1.set_title("Initial Steady-State solve")
# ax1.plot(solver.coord, q_steady, color=viridis_colors[0], ls='--', label='Initial numerical')
# # ax1.plot(solver.coord, solver.get_exact_solution(), linewidth=5, alpha=0.25, label='Exact')

# # Setup second subplot for steady solutions
# ax2.set_xlim([-1, 1])
# ax2.set_ylim([-0.5, 1.3])
# ax2.set_xticks(xelem)
# ax2.tick_params(axis='x', rotation=90, labelsize=8)
# ax2.set_title("Initial Steady-State solve")
# ax2.plot(solver.coord, q_steady, color=viridis_colors[0], ls='--', label='Initial numerical')
# # ax2.plot(solver.coord, solver.get_exact_solution(), linewidth=5, alpha=0.25, label='Exact')

# # Store initial coordinate data for later reference
# initial_coord = solver.coord.copy()
# initial_xelem = solver.xelem.copy()
# ax1.plot(initial_coord, solver.get_exact_solution(), color = 'k',linewidth=1, label='Exact')
# ax2.plot(initial_coord, solver.get_exact_solution(), color = 'blue', linewidth=5, alpha=0.25, label='Exact')

# ax1.grid(True, alpha=0.3)
# ax2.grid(True, alpha=0.3)
# ax1.legend(loc='upper right')
# ax2.legend(loc='upper right')

# solver.q = q_steady



# # First adaptation
# print("\n=== First Adaptation ===")
# print(f'xelem before adaptation: {solver.xelem}')
# marks_override = {1: 1}
# solver.adapt_mesh(marks_override=marks_override, element_budget=8)
# print(f'Mesh size after adaptation 1: {len(solver.xelem) - 1} elements, {len(solver.coord)} points')
# print(f'xelem after adaptation: {solver.xelem}')

# # Plot projected solution
# q_adapted_1 = solver.q.copy()
# ax3.set_xlim([-1, 1])
# ax3.set_ylim([-0.5, 1.3])
# ax3.set_xticks(solver.xelem)
# ax3.tick_params(axis='x', rotation=90, labelsize=8)
# highlight_color_3 = (1.0, 0.647, 0.0, 0.25) 
# # ax3.set_title('Solution after adapting')
# # ax3.text(0.5, 1.05, 'solution after adapting element 1', transform=ax3.transAxes,
# #                        ha='right', va='center', fontsize=14, color='black')
# ax3.text(0.5, 1.05, 'refined element 2', transform=ax3.transAxes,
#                        ha='center', va='center', fontsize=14, color='black',
#                        bbox=dict(facecolor=highlight_color_3, alpha=0.25, edgecolor='none'))
# ax3.plot(initial_coord, q_steady, color = 'k', alpha = 0.25, label = 'previous solution')
# ax3.plot(solver.coord,  q_adapted_1,color = viridis_colors[1], label='adapted solution (projection)', alpha=0.7)
# # ax1.scatter(solver.coord, q_adapted, color = magma_colors[1])
# ax3.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count
# adapt_coords_1 = np.zeros(len(solver.coord))-0.25
# ax3.scatter(solver.coord, adapt_coords_1, s = 1.5,color = magma_colors[1])
# y_bottom = -0.2
# y_top = -0.3
# # Fill the area between the ticks
# ax3.fill_betweenx([y_bottom, y_top], xelem[1], xelem[2], color='orange', alpha=0.5)
# ax3.set_xticks(solver.xelem)
# ax3.grid(True, alpha=0.3)

# # Plot steady solution after first adaptation
# q_steady_refined_1 = solver.steady_solve()
# ax4.set_xlim([-1, 1])
# ax4.set_ylim([-0.5, 1.3])
# ax4.set_xticks(solver.xelem)
# ax4.tick_params(axis='x', rotation=90, labelsize=8)
# ax4.text(1.5, 1.05, 'refined element 2', transform=ax3.transAxes,
#                        ha='center', va='center', fontsize=14, color='black',
#                        bbox=dict(facecolor=highlight_color_3, alpha=0.25, edgecolor='none'))
# ax4.plot(initial_coord, q_steady, color = 'k', alpha = 0.25, label = 'previous solution')
# ax4.plot(solver.coord, q_steady_refined_1, color = viridis_colors[1],label='Adaptation 1 (steady)', alpha=0.7)
# # ax2.scatter(solver.coord, q_adapted, color = magma_colors[1])
# ax4.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count
# ax4.scatter(solver.coord, adapt_coords_1, s = 1.5,color = magma_colors[1])
# # Fill the area between the ticks
# ax4.fill_betweenx([y_bottom, y_top], xelem[1], xelem[2], color='orange', alpha=0.5)
# ax4.set_xticks(solver.xelem)
# ax4.grid(True, alpha=0.3)
# ax3.legend(loc='upper right')
# ax4.legend(loc='upper right')

# # Second adaptation
# print("\n=== Second Adaptation ===")
# print(f'xelem before adaptation: {solver.xelem}')
# coord_1 = solver.coord.copy()
# marks_override = {2: 1}
# solver.adapt_mesh(marks_override=marks_override, element_budget=8)
# print(f'xelem after adaptation: {solver.xelem}')
# print(f'Mesh size after adaptation 2: {len(solver.xelem) - 1} elements, {len(solver.coord)} points')

# # Plot projected solution
# q_adapted_2 = solver.q.copy()

# ax5.set_xlim([-1, 1])
# ax5.set_ylim([-0.5, 1.3])
# ax5.set_xticks(solver.xelem)
# ax5.tick_params(axis='x', rotation=90, labelsize=8)
# highlight_color_5 = (0, 0.5, 0.5, 0.25) 
# # ax3.set_title('Solution after adapting')
# # ax3.text(0.5, 1.05, 'solution after adapting element 1', transform=ax3.transAxes,
# #                        ha='right', va='center', fontsize=14, color='black')
# ax5.text(0.5, -0.35, 'refined element 3', transform=ax3.transAxes,
#                        ha='center', va='center', fontsize=14, color='black',
#                        bbox=dict(facecolor=highlight_color_5, alpha=0.25, edgecolor='none'))
# ax5.plot(coord_1, q_adapted_1, color = 'k', alpha = 0.25, label = 'previous solution')
# ax5.plot(solver.coord,  q_adapted_2, color = viridis_colors[1], label='adapted solution (projection)', alpha=0.7)
# # ax1.scatter(solver.coord, q_adapted, color = magma_colors[1])
# ax5.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count
# adapt_coords_1 = np.zeros(len(solver.coord))-0.25
# ax5.scatter(solver.coord, adapt_coords_1, s = 1.5,color = magma_colors[1])
# y_bottom = -0.2
# y_top = -0.3
# # Fill the area between the ticks
# ax5.fill_betweenx([y_bottom, y_top], solver.xelem[2], solver.xelem[4], color='teal', alpha=0.5)
# ax5.set_xticks(solver.xelem)
# ax5.grid(True, alpha=0.3)
# ax5.legend(loc='upper right')
# # ax5.plot(solver.coord, q_adapted_2, color = viridis_colors[2],label='Adaptation 2 (projection)', alpha=0.7)
# # ax5.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count

# # Plot steady solution
# q_steady_refined_2 = solver.steady_solve()
# print(f'second adaptation steady solve: {q_steady_refined_2}')

# ax6.set_xlim([-1, 1])
# ax6.set_ylim([-0.5, 1.3])
# ax6.set_xticks(solver.xelem)
# ax6.tick_params(axis='x', rotation=90, labelsize=8)
# ax6.text(1.5, -0.45, 'refined element 3', transform=ax3.transAxes,
#                        ha='center', va='center', fontsize=14, color='black',
#                        bbox=dict(facecolor=highlight_color_5, alpha=0.25, edgecolor='none'))
# ax6.plot(coord_1, q_steady_refined_1, color = 'k', alpha = 0.25, label = 'previous solution')
# ax6.plot(solver.coord, q_steady_refined_2, color = viridis_colors[1],label='Adaptation 2 (steady)', alpha=0.7)
# # ax2.scatter(solver.coord, q_adapted, color = magma_colors[1])
# ax6.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count
# ax6.scatter(solver.coord, adapt_coords_1, s = 1.5,color = magma_colors[1])
# # Fill the area between the ticks
# ax6.fill_betweenx([y_bottom, y_top], solver.xelem[2], solver.xelem[4], color='teal', alpha=0.5)
# ax6.set_xticks(solver.xelem)
# ax6.grid(True, alpha=0.3)
# ax6.legend(loc='upper right')

# # Third adaptation
# print("\n=== Third Adaptation ===")
# print(f'xelem before adaptation: {solver.xelem}')
# coord_2 = solver.coord.copy()
# marks_override = {4: 1}
# solver.adapt_mesh(marks_override=marks_override, element_budget=8)
# print(f'xelem after adaptation: {solver.xelem}')
# print(f'Mesh size after adaptation 2: {len(solver.xelem) - 1} elements, {len(solver.coord)} points')

# # Plot projected solution
# q_adapted_3 = solver.q.copy()
# ax7.set_xlim([-1, 1])
# ax7.set_ylim([-0.5, 1.3])
# ax7.set_xticks(solver.xelem)
# ax7.tick_params(axis='x', rotation=90, labelsize=8)
# highlight_color_7 = (1, 0.6, 1, 0.25) 
# # ax3.set_title('Solution after adapting')
# # ax3.text(0.5, 1.05, 'solution after adapting element 1', transform=ax3.transAxes,
# #                        ha='right', va='center', fontsize=14, color='black')
# ax7.text(0.65, -1.80, 'refined element 4', transform=ax3.transAxes,
#                        ha='center', va='center', fontsize=14, color='black',
#                        bbox=dict(facecolor=highlight_color_7, alpha=0.25, edgecolor='none'))
# ax7.plot(coord_2, q_adapted_2, color = 'k', alpha = 0.25, label = 'previous solution')
# ax7.plot(solver.coord,  q_adapted_3, color = viridis_colors[1], label='adapted solution (projection)', alpha=0.7)
# # ax1.scatter(solver.coord, q_adapted, color = magma_colors[1])
# ax7.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count
# adapt_coords_1 = np.zeros(len(solver.coord))-0.25
# ax7.scatter(solver.coord, adapt_coords_1, s = 1.5,color = magma_colors[1])
# y_bottom = -0.2
# y_top = -0.3
# # Fill the area between the ticks
# ax7.fill_betweenx([y_bottom, y_top], solver.xelem[4], solver.xelem[6], color='magenta', alpha=0.5)
# ax7.set_xticks(solver.xelem)
# ax7.grid(True, alpha=0.3)
# ax7.legend(loc='upper right')
# # ax5.plot(solver.coord, q_adapted_2, color = viridis_colors[2],label='Adaptation 2 (projection)', alpha=0.7)
# # ax5.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count

# # Plot steady solution
# q_steady_refined_3 = solver.steady_solve()

# ax8.set_xlim([-1, 1])
# ax8.set_ylim([-0.5, 1.3])
# ax8.set_xticks(solver.xelem)
# ax8.tick_params(axis='x', rotation=90, labelsize=8)
# ax8.text(1.60, -2.00, 'refined element 4', transform=ax3.transAxes,
#                        ha='left', va='center', fontsize=14, color='black',
#                        bbox=dict(facecolor=highlight_color_7, alpha=0.25, edgecolor='none'))
# ax8.plot(coord_2, q_steady_refined_2, color = 'k', alpha = 0.25, label = 'previous solution')
# ax8.plot(solver.coord, q_steady_refined_3, color = viridis_colors[1],label='Adaptation 3 (steady)', alpha=0.7)
# # ax2.scatter(solver.coord, q_adapted, color = magma_colors[1])
# ax8.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count
# ax8.scatter(solver.coord, adapt_coords_1, s = 1.5,color = magma_colors[1])
# # Fill the area between the ticks
# ax8.fill_betweenx([y_bottom, y_top], solver.xelem[4], solver.xelem[6], color='magenta', alpha=0.5)
# ax8.set_xticks(solver.xelem)
# ax8.grid(True, alpha=0.3)
# ax8.legend(loc='upper right')


# # fig2, (ax10,ax12,ax14,ax16) = plt.subplots(4, 1, figsize=(10, 8))
# fig2, (ax10,ax12) = plt.subplots(2, 1, figsize=(10, 8))
# # Forth adaptation
# print("\n=== Fourth Adaptation ===")
# print(f'xelem before adaptation: {solver.xelem}')
# coord_3 = solver.coord.copy()
# marks_override = {4: 1}
# solver.adapt_mesh(marks_override=marks_override, element_budget=8)
# print(f'xelem after adaptation: {solver.xelem}')
# print(f'Mesh size after adaptation 2: {len(solver.xelem) - 1} elements, {len(solver.coord)} points')

# # Plot projected solution
# # q_adapted_4 = solver.q.copy()
# # ax9.set_xlim([-1, 1])
# # ax9.set_ylim([-0.5, 1.3])
# # ax9.set_xticks(solver.xelem)
# # ax9.tick_params(axis='x', rotation=90, labelsize=8)
# # highlight_color_7 = (1, 0.6, 1, 0.25) 
# # # ax9.set_title('Fourth adaptation')
# # # ax3.text(0.5, 1.05, 'solution after adapting element 1', transform=ax3.transAxes,
# # #                        ha='right', va='center', fontsize=14, color='black')
# # ax9.text(0.75, 2.55, 'refined element 4', transform=ax3.transAxes,
# #                        ha='center', va='center', fontsize=14, color='black',
# #                        bbox=dict(facecolor=highlight_color_7, alpha=0.25, edgecolor='none'))
# # ax9.plot(coord_3, q_adapted_3, color = 'k', alpha = 0.25, label = 'previous solution')
# # ax9.plot(solver.coord,  q_adapted_4, color = viridis_colors[1], label='adapted solution (projection)', alpha=0.7)
# # # ax1.scatter(solver.coord, q_adapted, color = magma_colors[1])
# # ax9.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count
# adapt_coords_1 = np.zeros(len(solver.coord))-0.25
# # ax9.scatter(solver.coord, adapt_coords_1, s = 1.5,color = magma_colors[1])
# # y_bottom = -0.2
# # y_top = -0.3
# # # Fill the area between the ticks
# # ax9.fill_betweenx([y_bottom, y_top], solver.xelem[4], solver.xelem[6], color='magenta', alpha=0.5)
# # ax9.set_xticks(solver.xelem)
# # ax9.grid(True, alpha=0.3)
# # ax9.legend(loc='upper right')
# # ax5.plot(solver.coord, q_adapted_2, color = viridis_colors[2],label='Adaptation 2 (projection)', alpha=0.7)
# # ax5.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count

# # Plot steady solution
# q_steady_refined_4 = solver.steady_solve()

# ax10.set_xlim([-0.5, 0.5])
# ax10.set_ylim([-0.5, 1.3])
# ax10.set_xticks(solver.xelem)
# ax10.tick_params(axis='x', rotation=90, labelsize=8)
# ax10.text(0.60, 2.55, 'refined element 4', transform=ax3.transAxes,
#                        ha='left', va='center', fontsize=14, color='black',
#                        bbox=dict(facecolor=highlight_color_7, alpha=0.25, edgecolor='none'))
# ax10.plot(coord_3, q_steady_refined_3, color = 'k', alpha = 0.25, label = 'previous solution')
# ax10.plot(solver.coord, q_steady_refined_4, color = viridis_colors[1],label='Adaptation 3 (steady)', alpha=0.7)
# # ax2.scatter(solver.coord, q_adapted, color = magma_colors[1])
# ax10.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count
# ax10.scatter(solver.coord, adapt_coords_1, s = 1.5,color = magma_colors[1])
# # Fill the area between the ticks
# ax10.fill_betweenx([y_bottom, y_top], solver.xelem[4], solver.xelem[6], color='magenta', alpha=0.5)
# ax10.set_xticks(solver.xelem)
# ax10.grid(True, alpha=0.3)
# ax10.legend(loc='upper right')



# # Fifth adaptation
# print("\n=== Fifth Adaptation ===")
# print(f'xelem before adaptation: {solver.xelem}')
# coord_4 = solver.coord.copy()
# marks_override = {4: 1}
# solver.adapt_mesh(marks_override=marks_override, element_budget=12)
# print(f'xelem after adaptation: {solver.xelem}')
# print(f'Mesh size after adaptation 2: {len(solver.xelem) - 1} elements, {len(solver.coord)} points')
# adapt_coords_1 = np.zeros(len(solver.coord))-0.25

# # Plot steady solution
# q_steady_refined_5 = solver.steady_solve()

# ax12.set_xlim([-0.25, 0.25])
# ax12.set_ylim([-0.5, 1.3])
# ax12.set_xticks(solver.xelem[2:-2])
# ax12.tick_params(axis='x', rotation=90, labelsize=8)
# ax12.text(0.60, -1.05, 'refined element 4', transform=ax3.transAxes,
#                        ha='left', va='center', fontsize=14, color='black',
#                        bbox=dict(facecolor=highlight_color_7, alpha=0.25, edgecolor='none'))
# ax12.plot(coord_4, q_steady_refined_4, color = 'k', alpha = 0.25, label = 'previous solution')
# ax12.plot(solver.coord, q_steady_refined_5, color = viridis_colors[1],label='Adaptation 5 (steady)', alpha=0.7)
# # ax2.scatter(solver.coord, q_adapted, color = magma_colors[1])
# ax12.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count
# ax12.scatter(solver.coord, adapt_coords_1, s = 1.5,color = magma_colors[1])
# # Fill the area between the ticks
# ax12.fill_betweenx([y_bottom, y_top], solver.xelem[4], solver.xelem[6], color='magenta', alpha=0.5)
# ax12.set_xticks(solver.xelem[2:-2])
# ax12.grid(True, alpha=0.3)
# ax12.legend(loc='upper right')
# # ax6.plot(solver.coord, q_steady_refined_2, color = viridis_colors[2],label='Adaptation 2 (steady)', alpha=0.7)
# # ax6.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count

# # # Third adaptation
# # print("\n=== Third Adaptation ===")
# # marks_override = {2: 1}
# # solver.adapt_mesh(marks_override=marks_override, element_budget=8)
# # print(f'Mesh size after adaptation 3: {len(solver.xelem) - 1} elements, {len(solver.coord)} points')

# # # Plot projected solution
# # q_adapted = solver.q.copy()
# # ax1.plot(solver.coord, q_adapted, color = viridis_colors[3],label='Adaptation 3 (projection)', alpha=0.7)
# # ax1.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count



# # # Plot steady solution
# # q_steady_refined = solver.steady_solve()
# # ax2.plot(solver.coord, q_steady_refined, color = viridis_colors[3],label='Adaptation 3 (steady)', alpha=0.7)
# # ax2.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')  # Empty plot for displaying element count


# # ax1.plot(initial_coord, solver.get_exact_solution(), color = 'blue',linewidth=5, alpha=0.25, label='Exact')
# # ax2.plot(initial_coord, solver.get_exact_solution(), color = 'blue', linewidth=5, alpha=0.25, label='Exact')

# # Update tick marks to show element boundaries
# # ax1.set_xticks(solver.xelem)
# # ax2.set_xticks(solver.xelem)

# # Add legends
# ax1.legend(loc='upper right')
# ax2.legend(loc='upper right')

# # Add grid lines

# # ax3.grid(True, alpha=0.3)

# # Adjust layout and show



# # x = np.linspace(0, 2 * np.pi, 400)
# # y = np.sin(x ** 2)

# # # Create a 4x2 grid of subplots
# # fig1, axs = plt.subplots(4, 2, figsize=(10, 8))

# # # Plot on each subplot
# # for i in range(4):
# #     for j in range(2):
# #         axs[i, j].plot(x, y)
# #         axs[i, j].set_title(f"Plot {i * 2 + j + 1}")

# # Adjust layout
# # plt.tight_layout()
# plt.tight_layout()
# plt.show()