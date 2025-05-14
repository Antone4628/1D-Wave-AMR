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
    '..',
))
sys.path.append(PROJECT_ROOT)

# from numerical.solvers.dg_wave_solver_mixed import DGWaveSolverMixed
from numerical.solvers.dg_wave_solver_mixed_clean import DGWaveSolverMixed




def calculate_delta_u(old_solution, new_solution, old_grid, new_grid):
    """
    Calculate the L1 norm of the difference between solutions according to equation 3.
    
    Args:
        old_solution: Solution before adaptation
        new_solution: Solution after adaptation
        old_grid: Grid coordinates before adaptation
        new_grid: Grid coordinates after adaptation
        
    Returns:
        float: The integral of absolute difference between solutions
    """
    # Interpolate the solution with fewer points onto the grid with more points
    if len(new_solution) >= len(old_solution):
        old_interpolated = np.interp(new_grid, old_grid, old_solution)
        # Calculate element-wise differences
        point_differences = np.abs(new_solution - old_interpolated)
        # Calculate approximate element widths for integration
        element_widths = np.diff(np.append(new_grid, new_grid[-1] + (new_grid[-1] - new_grid[-2])))
        # Approximate the integral using element widths
        delta_u = np.sum(point_differences * element_widths)
    else:
        new_interpolated = np.interp(old_grid, new_grid, new_solution)
        point_differences = np.abs(new_interpolated - old_solution)
        element_widths = np.diff(np.append(old_grid, old_grid[-1] + (old_grid[-1] - old_grid[-2])))
        delta_u = np.sum(point_differences * element_widths)
        
    return delta_u

# Then add this line to store delta_u values
delta_u_values = []

# Initial setup
nop = 4  # Polynomial order
xelem = np.array([-1, -0.5, 0, 0.5, 1])  # Initial element boundaries
nelem = len(xelem) - 1

# Initialize solver
solver = DGWaveSolverMixed(nop=4, xelem=xelem, max_elements=40, max_level=6)

# Compute initial steady solution
q_steady = solver.steady_solve_improved()

# Store initial coordinate data for later reference
initial_coord = solver.coord.copy()
initial_xelem = solver.xelem.copy()

# Create fill handles for refinement level visualization
# fill_handles = [
#     Patch(facecolor='yellow', alpha=0.25, label='level 0'),
#     Patch(facecolor='orange', alpha=0.5, label='level 1'),
#     Patch(facecolor='indianred', alpha=0.5, label='level 2'),
#     Patch(facecolor='darkmagenta', alpha=0.5, label='level 3'),
#     Patch(facecolor='darkcyan', alpha=0.5, label='level 4'),
#     Patch(facecolor='cyan', alpha=0.5, label='level 5'),
# ]
# fill_labels = ['level 0', 'level 1', 'level 2', 'level 3', 'level 4', 'level 5']

# Create fill handles for refinement level visualization
colors = ['yellow', 'orange', 'indianred', 'darkmagenta', 'darkcyan', 'cyan']
fill_handles = []
for i, color in enumerate(colors):
    fill_handles.append(Patch(facecolor=color, alpha=0.85, edgecolor='black', linewidth=0.5, label=f'level {i}'))
fill_labels = [f'level {i}' for i in range(len(colors))]

# Settings for all plots
y_bottom = -0.2
y_top = -0.3
from matplotlib.cm import viridis, magma
viridis_colors = [viridis(0.2), viridis(0.4), viridis(0.6), viridis(0.8)]
magma_colors = [magma(0.2), magma(0.4), magma(0.6), magma(0.8)]

# Define refinement steps - each tuple contains (element_to_refine, title, element_budget)
refinement_steps = [
    (1, "Refined element 2", 8),
    (3, "Refined element 3", 8),
    (2, "Refined element 8", 8),
    (4, "Refined element 9", 8),
    ([4, 3], "Refined elements 20 and 21", 12),  # Multiple refinements
    ([5, 4], "Refined center elements", 14),
    ([6, 5], "Refined center elements", 16)
]

# Create first figure with initial solution
fig1, ax1 = plt.subplots(1, 1, figsize=(12, 5))
ax1.set_xlim([-1, 1])
ax1.set_ylim([-0.5, 1.3])
ax1.set_xticks(xelem)
ax1.tick_params(axis='x', rotation=90, labelsize=8)
ax1.set_title("Initial Steady-State solve")
ax1.plot(solver.coord, q_steady, color=viridis_colors[0], ls='--', label='Initial numerical')
ax1.plot(initial_coord, solver.get_exact_solution(), color='k', linewidth=1, label='Exact')
fill1 = ax1.fill_betweenx([y_bottom, y_top], solver.xelem[0], solver.xelem[-1], 
                       color='yellow', alpha=0.25)
ax1.grid(True, alpha=0.3)
first_legend = ax1.legend(loc='upper right')
second_legend = ax1.legend(handles=fill_handles, labels=fill_labels, loc='upper left', 
                          title='Refinement Levels')
ax1.add_artist(first_legend)
ax1.add_artist(second_legend)

# Store solution history for plotting comparisons
solution_history = [(solver.coord.copy(), q_steady.copy())]
xelem_history = [solver.xelem.copy()]

# Create a figure for each pair of refinement steps (2 per figure)
n_refinements = len(refinement_steps)
n_figures = (n_refinements + 1) // 2  # Round up division

# Set the current solution for refinement
solver.q = q_steady.copy()

# Loop through refinement steps
for i, (element_to_refine, title, element_budget) in enumerate(refinement_steps):
    # Create a new figure every 2 refinements
    if i % 2 == 0:
        fig, axes = plt.subplots(2, 1, figsize=(12, 8))
        current_fig_idx = i // 2
    
    # Get the current axis to plot on
    ax = axes[i % 2]
    
    print(f"\n=== Refinement Step {i+1}: {title} ===")
    print(f'xelem before adaptation: {solver.xelem}')
    
    # Store current coordinates for plotting
    current_coord = solver.coord.copy()
    current_q = solution_history[-1][1].copy()
    
    # Apply mesh refinement - handle single or multiple elements to refine
    if isinstance(element_to_refine, list):
        for elem in element_to_refine:
            marks_override = {elem: 1}
            solver.adapt_mesh(marks_override=marks_override, element_budget=element_budget)
    else:
        marks_override = {element_to_refine: 1}
        solver.adapt_mesh(marks_override=marks_override, element_budget=element_budget)
    
    print(f'xelem after adaptation: {solver.xelem}')
    print(f'dt after adaptation: {solver.dt}')
    print(f'Mesh size after adaptation: {len(solver.xelem) - 1} elements, {len(solver.coord)} points')
    print(f'active elements after adaptation: {solver.active}')
    print(f'active levels: {solver.get_active_levels()}')
    
    # Compute steady solution after refinement
    q_steady_refined = solver.steady_solve_improved()

        # Calculate delta_u between solutions before and after adaptation
    delta_u = calculate_delta_u(current_q, q_steady_refined, current_coord, solver.coord)
    delta_u_values.append(delta_u)
    print(f"Delta U for refinement step {i+1}: {delta_u:.6e}")
    
    # Set for next refinement
    solver.q = q_steady_refined.copy()
    
    # Store for history
    solution_history.append((solver.coord.copy(), q_steady_refined.copy()))
    xelem_history.append(solver.xelem.copy())
    
    # Create dots at bottom of plot for visualization
    adapt_coords = np.zeros(len(solver.coord)) - 0.25
    
    # Set plot limits and labels
    ax.set_xlim([-1, 1])
    ax.set_ylim([-0.5, 1.3])
    ax.set_xticks(solver.xelem)
    ax.tick_params(axis='x', rotation=90, labelsize=8)
    ax.set_title(title)
    
    # Plot previous solution, new solution, and reference dots
    ax.plot(current_coord, current_q, color='k', alpha=0.25, label='previous solution')
    ax.plot(solver.coord, q_steady_refined, color=viridis_colors[1], label='Refined solution (steady)', alpha=0.7)
    ax.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')
    ax.scatter(solver.coord, adapt_coords, s=1.5, color=magma_colors[1])
    
    # Add fill areas to show refinement levels
    # Base level (always present)
    # Get actual refinement levels for each element
    active_levels = solver.get_active_levels()
    colors = ['yellow', 'orange', 'indianred', 'darkmagenta', 'darkcyan', 'cyan']

    # Clear any existing fill areas
    for artist in ax.patches:
        if isinstance(artist, plt.matplotlib.patches.Rectangle):
            artist.remove()

    # Create a fill patch for each element with the color corresponding to its level
    for j in range(len(solver.xelem) - 1):  # For each element
        if j < len(active_levels):  # Safety check
            level = active_levels[j]
            level_color = colors[min(level, len(colors)-1)]  # Use the last color if level exceeds color list
            
            # Create a fill patch for this element
            ax.fill_betweenx(
                [y_bottom, y_top],
                solver.xelem[j],
                solver.xelem[j+1],
                color=level_color,
                alpha=0.85,
                edgecolor='black',
                linewidth=0.5
            )
    # fill1 = ax.fill_betweenx([y_bottom, y_top], solver.xelem[0], solver.xelem[-1], 
    #                     color='yellow', alpha=0.25)
    
    # # Add additional fill areas based on refinement level
    # # This is a simplified version - you may need to adjust based on the specific refinement pattern
    # colors = ['orange', 'indianred', 'darkmagenta', 'darkcyan', 'cyan']
    # for level in range(min(5, i+1)):
    #     if level < len(colors) and level+1 < len(solver.xelem) // 2:
    #         ax.fill_betweenx([y_bottom, y_top], 
    #                         solver.xelem[level+1], 
    #                         solver.xelem[-(level+2)], 
    #                         color=colors[level], alpha=0.5)
            


    
    # Grid and legend
    ax.grid(True, alpha=0.3)
    first_legend = ax.legend(loc='upper right')
    second_legend = ax.legend(handles=fill_handles, labels=fill_labels, loc='upper left', 
                            title='Refinement Levels')
    ax.add_artist(second_legend)
    ax.add_artist(first_legend)
    
    # If this is the last refinement and odd number, adjust layout
    if i == n_refinements - 1 and i % 2 == 0:
        axes[1].set_visible(False)
    
    # Adjust layout every 2 refinements or at the end
    if i % 2 == 1 or i == n_refinements - 1:
        plt.tight_layout()



# After all refinement steps, plot the delta_u values
fig_delta, ax_delta = plt.subplots(figsize=(10, 6))
ax_delta.plot(range(1, len(delta_u_values)+1), delta_u_values, 'o-', linewidth=2)
ax_delta.set_xlabel('Refinement Step')
ax_delta.set_ylabel('Δu (L1 norm of solution difference)')
ax_delta.set_title('Solution Change After Each Refinement Step')
ax_delta.grid(True)
ax_delta.set_xticks(range(1, len(delta_u_values)+1))


plt.show()






# ===========================================================================
# Add timestepping on the final refined solution
# ===========================================================================
print("\n=== Time Evolution of Final Solution ===")

# Store the final refined solution and grid before timestepping
final_refined_solution = solver.q.copy()
final_refined_grid = solver.xelem.copy()
final_refined_coord = solver.coord.copy()

# Number of timesteps to run
num_timesteps = 300
# dt = 0.01  # Time step size
dt = solver.dt

# Create arrays to store solutions at different timesteps
timestep_solutions = [final_refined_solution.copy()]
timestep_times = [solver.time]

# Run the specified number of timesteps
for i in range(num_timesteps):
    solver.step(dt)
    timestep_solutions.append(solver.q.copy())
    timestep_times.append(solver.time)
    print(f"Completed timestep {i+1}/{num_timesteps}, t = {solver.time:.3f}")

# Create a figure to show time evolution
fig_time, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Plot the initial refined solution
ax1.set_xlim([-1, 1])
ax1.set_ylim([-0.5, 1.3])
ax1.set_title(f"Initial Refined Solution (t = {timestep_times[0]:.3f})")
ax1.plot(final_refined_coord, final_refined_solution, color=viridis_colors[0], ls='-', label='Initial refined solution')
ax1.plot(final_refined_coord, solver.get_exact_solution(), color='k', linewidth=1, label='Exact solution')
ax1.scatter(final_refined_coord, np.zeros(len(final_refined_coord))-0.25, s=1.5, color=magma_colors[1])
ax1.set_xticks(final_refined_grid)
ax1.tick_params(axis='x', rotation=90, labelsize=8)
ax1.grid(True, alpha=0.3)
ax1.legend(loc='upper right')

# Plot the final solution after timestepping
ax2.set_xlim([-1, 1])
ax2.set_ylim([-0.5, 1.3])
ax2.set_title(f"Solution After {num_timesteps} Timesteps (t = {timestep_times[-1]:.3f})")
ax2.plot(final_refined_coord, final_refined_solution, color='k', alpha=0.25, label=f'Initial (t = {timestep_times[0]:.3f})')
ax2.plot(solver.coord, solver.q, color=viridis_colors[2], label=f'After {num_timesteps} timesteps')

# Get and plot exact solution at final time
original_time = solver.time
solver.time = timestep_times[-1]
exact_final = solver.get_exact_solution()
solver.time = original_time  # Restore original time
ax2.plot(solver.coord, exact_final, color='r', linewidth=1, linestyle='--', label=f'Exact at t = {timestep_times[-1]:.3f}')

ax2.set_xticks(solver.xelem)
ax2.tick_params(axis='x', rotation=90, labelsize=8)
ax2.grid(True, alpha=0.3)
ax2.legend(loc='upper right')

plt.tight_layout()

# Optional: Create an animation of the solution over time
if False:  # Set to True to create animation
    from matplotlib.animation import FuncAnimation
    
    fig_anim, ax_anim = plt.subplots(figsize=(10, 6))
    ax_anim.set_xlim([-1, 1])
    ax_anim.set_ylim([-0.5, 1.3])
    ax_anim.grid(True, alpha=0.3)
    
    line, = ax_anim.plot([], [], lw=2)
    time_text = ax_anim.text(0.02, 0.95, '', transform=ax_anim.transAxes)
    
    def init():
        line.set_data([], [])
        time_text.set_text('')
        return line, time_text
    
    def animate(i):
        line.set_data(solver.coord, timestep_solutions[i])
        time_text.set_text(f'Time: {timestep_times[i]:.3f}')
        return line, time_text
    
    anim = FuncAnimation(fig_anim, animate, init_func=init,
                         frames=len(timestep_solutions), interval=200, blit=True)
    ax_anim.set_title('Solution Evolution Over Time')
    plt.tight_layout()

# Show all plots
plt.show()



# ===========================================================================
# Second round of adaptations after time evolution
# ===========================================================================
print("\n=== Second Round of Adaptations (After Time Evolution) ===")

# Define refinement steps for the second round
refinement_steps_second_round = [
    (11, "Refined element 2", 40),
    (13, "Refined element 3", 40),
    (12, "Refined element 8", 40),
    (14, "Refined element 9", 40),
    ([13, 14], "Refined elements 20 and 21", 40),  # Multiple refinements
    ([14, 15], "Refined center elements", 40),
    ([16, 15], "Refined center elements", 40)
]

# Create new figures for the second round
n_refinements_second = len(refinement_steps_second_round)
n_figures_second = (n_refinements_second + 1) // 2  # Round up division

# Store current solution for comparison
post_timestepping_solution = solver.q.copy()
post_timestepping_coord = solver.coord.copy()
post_timestepping_xelem = solver.xelem.copy()

# Store solution history for the second round
solution_history_second = [(solver.coord.copy(), solver.q.copy())]
xelem_history_second = [solver.xelem.copy()]

# Loop through second round refinement steps
for i, (element_to_refine, title, element_budget) in enumerate(refinement_steps_second_round):
    # Create a new figure every 2 refinements
    if i % 2 == 0:
        fig, axes = plt.subplots(2, 1, figsize=(12, 8))
        current_fig_idx = i // 2
    
    # Get the current axis to plot on
    ax = axes[i % 2]
    
    print(f"\n=== Second Round Refinement Step {i+1}: {title} ===")
    print(f'xelem before adaptation: {solver.xelem}')
    
    # Store current coordinates for plotting
    current_coord = solver.coord.copy()
    current_q = solution_history_second[-1][1].copy()
    
    # Apply mesh refinement - handle single or multiple elements to refine
    if isinstance(element_to_refine, list):
        for elem in element_to_refine:
            marks_override = {elem: 1}
            solver.adapt_mesh(marks_override=marks_override, element_budget=element_budget)
    else:
        marks_override = {element_to_refine: 1}
        solver.adapt_mesh(marks_override=marks_override, element_budget=element_budget)
    
    print(f'xelem after adaptation: {solver.xelem}')
    print(f'Mesh size after adaptation: {len(solver.xelem) - 1} elements, {len(solver.coord)} points')
    print(f'active elements after adaptation: {solver.active}')
    print(f'active levels: {solver.get_active_levels()}')
    
    # Compute steady solution after refinement
    q_steady_refined = solver.steady_solve_improved()
    
    # Calculate delta_u between solutions before and after adaptation
    # Continue using the same delta_u_values list from the first round
    delta_u = calculate_delta_u(current_q, q_steady_refined, current_coord, solver.coord)
    delta_u_values.append(delta_u)
    print(f"Delta U for second round refinement step {i+1}: {delta_u:.6e}")
    
    # Set for next refinement
    solver.q = q_steady_refined.copy()
    
    # Store for history
    solution_history_second.append((solver.coord.copy(), q_steady_refined.copy()))
    xelem_history_second.append(solver.xelem.copy())
    
    # Create dots at bottom of plot for visualization
    adapt_coords = np.zeros(len(solver.coord)) - 0.25
    
    # Set plot limits and labels
    ax.set_xlim([-1, 1])
    ax.set_ylim([-0.5, 1.3])
    ax.set_xticks(solver.xelem)
    ax.tick_params(axis='x', rotation=90, labelsize=8)
    ax.set_title(f"Second Round: {title}")
    
    # Plot previous solution, new solution, and reference dots
    ax.plot(current_coord, current_q, color='k', alpha=0.25, label='Previous solution')
    ax.plot(solver.coord, q_steady_refined, color=viridis_colors[1], label='Refined solution (steady)', alpha=0.7)
    ax.plot([], [], ' ', label=f'Elements: {len(solver.xelem) - 1}')
    ax.scatter(solver.coord, adapt_coords, s=1.5, color=magma_colors[1])
    
    # Add fill areas to show refinement levels
    # Base level (always present)
    # Get actual refinement levels for each element
    active_levels = solver.get_active_levels()
    colors = ['yellow', 'orange', 'indianred', 'darkmagenta', 'darkcyan', 'cyan']

    # Clear any existing fill areas
    for artist in ax.patches:
        if isinstance(artist, plt.matplotlib.patches.Rectangle):
            artist.remove()

    # Create a fill patch for each element with the color corresponding to its level
    for j in range(len(solver.xelem) - 1):  # For each element
        if j < len(active_levels):  # Safety check
            level = active_levels[j]
            level_color = colors[min(level, len(colors)-1)]  # Use the last color if level exceeds color list
            
            # Create a fill patch for this element
            ax.fill_betweenx(
                [y_bottom, y_top],
                solver.xelem[j],
                solver.xelem[j+1],
                color=level_color,
                alpha=0.85,
                edgecolor='black',
                linewidth=0.5
            )
    # fill1 = ax.fill_betweenx([y_bottom, y_top], solver.xelem[0], solver.xelem[-1], 
    #                     color='yellow', alpha=0.25)
    
    # # Add additional fill areas based on refinement level
    # # This is a simplified version - you may need to adjust based on the specific refinement pattern
    # colors = ['orange', 'indianred', 'darkmagenta', 'darkcyan', 'cyan']
    # for level in range(min(5, i+1)):
    #     if level < len(colors) and level+1 < len(solver.xelem) // 2:
    #         ax.fill_betweenx([y_bottom, y_top], 
    #                         solver.xelem[level+1], 
    #                         solver.xelem[-(level+2)], 
    #                         color=colors[level], alpha=0.5)
            


    
    # Grid and legend
    ax.grid(True, alpha=0.3)
    first_legend = ax.legend(loc='upper right')
    second_legend = ax.legend(handles=fill_handles, labels=fill_labels, loc='upper left', 
                            title='Refinement Levels')
    ax.add_artist(second_legend)
    ax.add_artist(first_legend)
    
    # If this is the last refinement and odd number, adjust layout
    if i == n_refinements_second - 1 and i % 2 == 0:
        axes[1].set_visible(False)
    
    # Adjust layout every 2 refinements or at the end
    if i % 2 == 1 or i == n_refinements_second - 1:
        plt.tight_layout()

# Plot the combined delta_u values (from both rounds)
fig_delta, ax_delta = plt.subplots(figsize=(10, 6))
ax_delta.plot(range(1, len(delta_u_values)+1), delta_u_values, 'o-', linewidth=2)
ax_delta.set_xlabel('Refinement Step')
ax_delta.set_ylabel('Δu (L1 norm of solution difference)')
ax_delta.set_title('Solution Change After Each Refinement Step (Both Rounds)')
ax_delta.grid(True)
ax_delta.set_xticks(range(1, len(delta_u_values)+1))

# Add a vertical line to separate first and second rounds
first_round_steps = len(refinement_steps)
if first_round_steps < len(delta_u_values):
    ax_delta.axvline(x=first_round_steps + 0.5, color='r', linestyle='--', 
                    label='Start of second round (after timestepping)')
    ax_delta.legend()

plt.tight_layout()

# Create a final comparison figure showing initial, after first round, 
# after timestepping, and final solutions
fig_comparison, ax_comparison = plt.subplots(figsize=(12, 8))
ax_comparison.set_xlim([-1, 1])
ax_comparison.set_ylim([-0.5, 1.3])
ax_comparison.set_title("Comparison of Solutions Through All Stages")

# Initial solution
ax_comparison.plot(initial_coord, q_steady, color='gray', alpha=0.5, 
                  label='Initial solution')

# After first round refinements (before timestepping)
first_round_final_coords, first_round_final_q = solution_history[-1]
ax_comparison.plot(first_round_final_coords, first_round_final_q, color=viridis_colors[0], 
                 label='After first round refinements')

# After timestepping
ax_comparison.plot(post_timestepping_coord, post_timestepping_solution, color=viridis_colors[2], 
                 label='After timestepping')

# Final solution after second round
ax_comparison.plot(solver.coord, solver.q, color=magma_colors[2], linewidth=2,
                 label='Final solution after second round')

# Exact solution
ax_comparison.plot(solver.coord, solver.get_exact_solution(), color='r', linestyle='--',
                 label='Exact solution')

ax_comparison.grid(True, alpha=0.3)
ax_comparison.legend(loc='upper right')
plt.tight_layout()

plt.show()