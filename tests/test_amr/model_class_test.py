"""
1D Wave Equation Solver with RL-Driven AMR

This script solves the 1D wave equation using a DG method with RL-driven adaptive mesh refinement.
Uses the DGWaveSolver class for the core numerical solution and a trained RL model for adaptation decisions.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os
import sys
import argparse

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
from numerical.amr.model_marker import RLModelMarker

def solve_with_custom_marker(solver, time_final, marker=None, monitor_interval=10):
    """
    Solve the wave equation up to time_final with optional custom marker.
    
    Args:
        solver (DGWaveSolver): The initialized solver
        time_final (float): Final simulation time
        marker (callable, optional): Custom marking function. If None, use default.
        monitor_interval (int): How often to print monitoring information
        
    Returns:
        tuple: (times, solutions, grids, coords, metrics) containing:
            - times: Simulation times at each step
            - solutions: Solution values at each step
            - grids: Mesh grid at each step
            - coords: Node coordinates at each step 
            - metrics: Dictionary of simulation metrics
    """
    times = [solver.time]
    solutions = [solver.q.copy()]
    grids = [solver.xelem.copy()]
    coords = [solver.coord.copy()]
    
    element_counts = [len(solver.active)]
    step_count = 0
    
    metrics = {
        'max_elements': 0,
        'min_elements': float('inf'),
        'avg_elements': 0,
        'budget_violations': 0,
        'timesteps': 0
    }
    
    print(f"Starting simulation with {'RL-driven' if marker else 'traditional'} AMR")
    print(f"Initial elements: {len(solver.active)}, Budget: {solver.max_elements}")
    
    while solver.time < time_final:
        dt = min(solver.dt, time_final - solver.time)
        
        # Print progress every monitor_interval steps
        if step_count % monitor_interval == 0:
            print(f"\nTimestep {step_count}, Time: {solver.time:.3f}, Elements: {len(solver.active)}/{solver.max_elements}")
        
        # Use the provided marker or fall back to default
        if marker is not None:
            marks = marker(solver.active, solver.label_mat, solver.intma, solver.q)
            try:
                solver.adapt_mesh(criterion=None, marks_override={i: m for i, m in enumerate(marks)})
            except ValueError as e:
                print(f"⚠️ Error during adapt_mesh: {e}")
                metrics['budget_violations'] += 1
                # Continue with the simulation despite the error
        else:
            # Original code path
            try:
                solver.adapt_mesh()
            except ValueError as e:
                print(f"⚠️ Error during adapt_mesh: {e}")
                metrics['budget_violations'] += 1
                # Continue with the simulation
        
        # Track element count
        current_elements = len(solver.active)
        element_counts.append(current_elements)
        
        # Update metrics
        metrics['max_elements'] = max(metrics['max_elements'], current_elements)
        metrics['min_elements'] = min(metrics['min_elements'], current_elements)
        
        # Take time step
        solver.step(dt)
        
        # Store results
        times.append(solver.time)
        solutions.append(solver.q.copy())
        grids.append(solver.xelem.copy())
        coords.append(solver.coord.copy())
        step_count += 1
    
    # Calculate final metrics
    metrics['timesteps'] = step_count
    metrics['avg_elements'] = sum(element_counts) / len(element_counts)
    
    # Report metrics
    print("\n--- Simulation Metrics ---")
    print(f"Timesteps: {metrics['timesteps']}")
    print(f"Max Elements: {metrics['max_elements']}")
    print(f"Min Elements: {metrics['min_elements']}")
    print(f"Avg Elements: {metrics['avg_elements']:.2f}")
    print(f"Budget Violations: {metrics['budget_violations']}")
    
    if marker and hasattr(marker, 'get_statistics'):
        model_stats = marker.get_statistics()
        print("\n--- RL Model Statistics ---")
        print(f"Total Decisions: {model_stats['total_decisions']}")
        print(f"Refinements: {model_stats['decisions']['refine']}")
        print(f"Coarsenings: {model_stats['decisions']['coarsen']}")
        print(f"No Changes: {model_stats['decisions']['no_change']}")
        print(f"Detected Violations: {model_stats['violations']}")
    
    return times, solutions, grids, coords, metrics

def create_animation(times, solutions, grids, coords, title, filename, metrics=None):
    """
    Create and save an animation of the solution evolution.
    
    Args:
        times: List of simulation times
        solutions: List of solution arrays
        grids: List of grid arrays
        coords: List of coordinate arrays
        title: Animation title
        filename: Output filename
        metrics: Optional metrics dictionary for annotations
        
    Returns:
        animation: The created animation
    """
    plt.rcParams['animation.html'] = 'jshtml'
    plt.style.use('ggplot')

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim([-1, 1])
    ax.set_ylim([-0.1, 2.2])
    ax.set_xticks(grids[0])
    ax.tick_params(axis='x', rotation=90, labelsize=8)
    ax.set_title(title)

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

    # Add grid lines at initial positions
    grid_lines = []
    for x in grids[0]:
        line = ax.axvline(x=x, color='gray', linestyle='--', alpha=0.3)
        grid_lines.append(line)

    def update_data(frame):
        """Update function for animation."""
        # Update solution
        animated_plot.set_ydata(solutions[frame])
        animated_plot.set_xdata(coords[frame])
        
        # Update grid lines
        for line in grid_lines:
            line.remove()
        grid_lines.clear()
        
        for x in grids[frame]:
            line = ax.axvline(x=x, color='gray', linestyle='--', alpha=0.3)
            grid_lines.append(line)
            
        # Update text annotations
        frame_text.set_text(f'Frame: {frame}')
        time_text.set_text(f'Time: {times[frame]:.3f}')
        elements_text.set_text(f'Elements: {len(grids[frame])-1}')
        
        # Adjust x-ticks to match current grid
        ax.set_xticks(grids[frame])

    # Create animation
    anim = FuncAnimation(
        fig=fig,
        func=update_data,
        frames=len(solutions),
        interval=100,
        blit=False  # Need this to be False for grid lines to update properly
    )

    # Save animation
    print(f"Saving animation to {filename}...")
    anim.save(filename, writer="pillow", fps=30)
    print(f"Animation saved successfully!")
    
    plt.close(fig)
    return anim

def compare_amr_approaches(time_final=0.2, nelem=4, max_level=4, nop=4, element_budget=40, icase=1, 
                          model_path=None, verbose=False):
    """
    Run comparison between traditional and RL-driven AMR.
    
    Args:
        time_final: Final simulation time
        nelem: Initial number of elements
        max_level: Maximum refinement level
        nop: Polynomial order
        element_budget: Maximum allowed elements
        icase: Test case ID
        model_path: Path to trained RL model
        verbose: Whether to print detailed logs
        
    Returns:
        dict: Comparison metrics
    """
    # Initial mesh
    xelem = np.array([-1, -0.4, 0, 0.4, 1])
    
    # Parameters
    courant_max = 0.1
    
    # Traditional approach
    solver_trad = DGWaveSolver(
        nop=nop,
        xelem=xelem.copy(),
        max_elements=element_budget,
        max_level=max_level,
        courant_max=courant_max,
        icase=icase,
        verbose=verbose
    )
    
    # RL approach
    solver_rl = DGWaveSolver(
        nop=nop,
        xelem=xelem.copy(),
        max_elements=element_budget,
        max_level=max_level,
        courant_max=courant_max,
        icase=icase,
        verbose=verbose
    )
    
    # Initialize RL model marker
    rl_marker = RLModelMarker(model_path, element_budget, verbose=verbose)
    
    # Run simulations
    print("Running traditional AMR simulation...")
    times_trad, solutions_trad, grids_trad, coords_trad, metrics_trad = solve_with_custom_marker(
        solver_trad, time_final
    )
    
    print("\nRunning RL-driven AMR simulation...")
    times_rl, solutions_rl, grids_rl, coords_rl, metrics_rl = solve_with_custom_marker(
        solver_rl, time_final, marker=rl_marker
    )
    
    # Create animations
    create_animation(
        times_trad, solutions_trad, grids_trad, coords_trad,
        f"Traditional AMR: {nelem} initial elements, max level {max_level}",
        os.path.join(ANIMATIONS_DIR, 'Traditional_AMR_Wave_Solver.gif'),
        metrics_trad
    )
    
    create_animation(
        times_rl, solutions_rl, grids_rl, coords_rl,
        f"RL-driven AMR: {nelem} initial elements, max level {max_level}",
        os.path.join(ANIMATIONS_DIR, 'RL_Driven_AMR_Wave_Solver.gif'),
        metrics_rl
    )
    
    # Compare results
    element_counts_trad = [grid.shape[0]-1 for grid in grids_trad]
    element_counts_rl = [grid.shape[0]-1 for grid in grids_rl]
    
    # Calculate error against exact solution at final time
    solver_trad.time = times_trad[-1]
    exact_trad = solver_trad.get_exact_solution()
    error_trad = np.linalg.norm(solutions_trad[-1] - exact_trad) / np.linalg.norm(exact_trad)
    
    solver_rl.time = times_rl[-1]
    exact_rl = solver_rl.get_exact_solution()
    error_rl = np.linalg.norm(solutions_rl[-1] - exact_rl) / np.linalg.norm(exact_rl)
    
    # Generate comparison plots
    fig, axs = plt.subplots(2, 2, figsize=(15, 10))
    
    # Plot solution at final time
    axs[0, 0].plot(coords_trad[-1], solutions_trad[-1], 'b-', label='Traditional')
    axs[0, 0].plot(coords_rl[-1], solutions_rl[-1], 'r-', label='RL-driven')
    axs[0, 0].plot(coords_trad[-1], exact_trad, 'k--', label='Exact')
    axs[0, 0].set_title('Solution at Final Time')
    axs[0, 0].legend()
    
    # Plot element count evolution
    axs[0, 1].plot(times_trad, element_counts_trad, 'b-', label='Traditional')
    axs[0, 1].plot(times_rl, element_counts_rl, 'r-', label='RL-driven')
    axs[0, 1].set_title('Element Count Evolution')
    axs[0, 1].set_xlabel('Time')
    axs[0, 1].set_ylabel('Number of Elements')
    axs[0, 1].legend()
    
    # Plot final mesh for traditional AMR
    axs[1, 0].plot(coords_trad[-1], solutions_trad[-1], 'b-')
    for x in grids_trad[-1]:
        axs[1, 0].axvline(x=x, color='b', linestyle='--', alpha=0.3)
    axs[1, 0].set_title(f'Traditional AMR Mesh (Error: {error_trad:.6f})')
    
    # Plot final mesh for RL-driven AMR
    axs[1, 1].plot(coords_rl[-1], solutions_rl[-1], 'r-')
    for x in grids_rl[-1]:
        axs[1, 1].axvline(x=x, color='r', linestyle='--', alpha=0.3)
    axs[1, 1].set_title(f'RL-driven AMR Mesh (Error: {error_rl:.6f})')
    
    plt.tight_layout()
    plt.savefig(os.path.join(PROJECT_ROOT, "plots", "amr_comparison.png"))
    plt.close(fig)
    
    # Create element efficiency metric: ratio of errors weighted by element counts
    # Higher values mean the RL approach is more efficient
    if element_counts_trad[-1] > 0 and element_counts_rl[-1] > 0:
        element_efficiency = error_trad / error_rl * element_counts_rl[-1] / element_counts_trad[-1]
    else:
        element_efficiency = float('nan')
    
    # Compile comparison metrics
    comparison = {
        'traditional': {
            'final_elements': element_counts_trad[-1],
            'max_elements': metrics_trad['max_elements'],
            'avg_elements': metrics_trad['avg_elements'],
            'error': error_trad,
            'violations': metrics_trad['budget_violations']
        },
        'rl_driven': {
            'final_elements': element_counts_rl[-1],
            'max_elements': metrics_rl['max_elements'],
            'avg_elements': metrics_rl['avg_elements'],
            'error': error_rl,
            'violations': metrics_rl['budget_violations']
        },
        'element_efficiency': element_efficiency,
        'error_ratio': error_trad / error_rl if error_rl > 0 else float('inf')
    }
    
    # Print summary
    print("\n--- Comparison Summary ---")
    print(f"Final time: {time_final}")
    print(f"Traditional AMR: {element_counts_trad[-1]} elements, error = {error_trad:.6f}")
    print(f"RL-driven AMR: {element_counts_rl[-1]} elements, error = {error_rl:.6f}")
    print(f"Error ratio (Traditional/RL): {comparison['error_ratio']:.2f}x")
    print(f"Element efficiency: {element_efficiency:.2f}x")
    
    return comparison

def run_rl_only(time_final=0.2, nelem=4, max_level=4, nop=4, element_budget=40, icase=1, 
               model_path=None, verbose=False):
    """
    Run only the RL-driven AMR approach.
    
    Args:
        time_final: Final simulation time
        nelem: Initial number of elements
        max_level: Maximum refinement level
        nop: Polynomial order
        element_budget: Maximum allowed elements
        icase: Test case ID
        model_path: Path to trained RL model
        verbose: Whether to print detailed logs
    """
    # Initial mesh
    xelem = np.array([-1, -0.4, 0, 0.4, 1])
    
    # Parameters
    courant_max = 0.1
    
    # Initialize solver
    solver = DGWaveSolver(
        nop=nop,
        xelem=xelem,
        max_elements=element_budget,
        max_level=max_level,
        courant_max=courant_max,
        icase=icase,
        verbose=verbose
    )
    
    # Initialize RL model marker
    rl_marker = RLModelMarker(model_path, element_budget, verbose=verbose)
    
    # Solve and collect results
    times, solutions, grids, coords, metrics = solve_with_custom_marker(
        solver, time_final, marker=rl_marker
    )
    
    # Create animation
    create_animation(
        times, solutions, grids, coords,
        f"RL-driven AMR: {nelem} initial elements, max level {max_level}",
        os.path.join(ANIMATIONS_DIR, 'RL_Driven_AMR_Wave_Solver.gif'),
        metrics
    )
    
    # Calculate final error
    solver.time = times[-1]
    exact = solver.get_exact_solution()
    error = np.linalg.norm(solutions[-1] - exact) / np.linalg.norm(exact)
    
    # Print final summary
    print("\n--- RL-driven AMR Summary ---")
    print(f"Final time: {time_final}")
    print(f"Final elements: {len(grids[-1])-1}")
    print(f"Error: {error:.6f}")
    
    return times, solutions, grids, coords, metrics

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run RL-driven AMR simulations')
    parser.add_argument('--model_path', type=str, required=True, 
                        help='Path to trained RL model')
    parser.add_argument('--compare', action='store_true',
                        help='Compare traditional and RL-driven AMR')
    parser.add_argument('--time_final', type=float, default=0.2,
                        help='Final simulation time')
    parser.add_argument('--max_level', type=int, default=4,
                        help='Maximum refinement level')
    parser.add_argument('--nop', type=int, default=4,
                        help='Polynomial order')
    parser.add_argument('--element_budget', type=int, default=40,
                        help='Maximum allowed elements')
    parser.add_argument('--icase', type=int, default=1,
                        help='Test case ID')
    parser.add_argument('--verbose', action='store_true',
                        help='Print detailed logs')
    args = parser.parse_args()
    
    # Verify model path exists
    if not os.path.exists(args.model_path):
        print(f"Error: Model path '{args.model_path}' does not exist.")
        sys.exit(1)
    
    # Print simulation parameters
    print("--- Simulation Parameters ---")
    print(f"Model path: {args.model_path}")
    print(f"Final time: {args.time_final}")
    print(f"Max refinement level: {args.max_level}")
    print(f"Polynomial order: {args.nop}")
    print(f"Element budget: {args.element_budget}")
    print(f"Test case: {args.icase}")
    print(f"Verbose: {args.verbose}")
    print(f"Compare: {args.compare}")
    print("----------------------------")
    
    # Create plots directory if it doesn't exist
    plots_dir = os.path.join(PROJECT_ROOT, "plots")
    os.makedirs(plots_dir, exist_ok=True)
    
    # Run appropriate simulation
    if args.compare:
        compare_amr_approaches(
            time_final=args.time_final,
            max_level=args.max_level,
            nop=args.nop,
            element_budget=args.element_budget,
            icase=args.icase,
            model_path=args.model_path,
            verbose=args.verbose
        )
    else:
        run_rl_only(
            time_final=args.time_final,
            max_level=args.max_level,
            nop=args.nop,
            element_budget=args.element_budget,
            icase=args.icase,
            model_path=args.model_path,
            verbose=args.verbose
        )