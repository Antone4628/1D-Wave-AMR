#!/usr/bin/env python3
"""
Baseline Simulation Runner for Visualization

This script runs baseline AMR simulations (no-amr, conventional-amr) on the 1D wave equation
using Discontinuous Galerkin method for comparison with DRL-AMR models.

Key features for baseline evaluation:
- Supports no-amr and conventional threshold-based AMR modes
- Multiple plotting modes: animate, snapshot, final
- Optional exact solution comparison
- Comprehensive metrics collection for accuracy vs cost analysis
- Enhanced parameter display for baseline configurations

Usage:
    python baseline_simulation_runner.py --mode conventional-amr --threshold 0.5 --plot-mode animate
    python baseline_simulation_runner.py --mode no-amr --initial-refinement 3 --plot-mode final
    python baseline_simulation_runner.py --mode conventional-amr --threshold 0.2 --plot-mode snapshot
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os
import sys
import argparse
import time
from pathlib import Path

# Get absolute path to project root
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 
    '..',
    '..'
))
sys.path.append(PROJECT_ROOT)

# Import the baseline solver
from numerical.solvers.dg_wave_solver_baseline import DGWaveSolverBaseline
from numerical.solvers.utils import exact_solution

def extract_baseline_configuration(args):
    """
    Extract baseline configuration parameters from arguments.
    
    Args:
        args: Parsed command line arguments
        
    Returns:
        dict: Baseline configuration parameters
    """
    config = {
        'mode': args.mode,
        'initial_refinement': args.initial_refinement,
        'element_budget': args.element_budget,
        'time_final': args.time_final,
        'max_level': args.max_level,
        'nop': args.nop,
        'courant_max': args.courant_max,
        'icase': args.icase
    }
    
    # Add threshold for conventional-amr mode
    if args.mode == 'conventional-amr':
        config['threshold'] = args.threshold
    
    return config

def create_baseline_directory(baseline_config, base_dir=None):
    """
    Create organized directory structure for baseline outputs.
    
    Args:
        baseline_config (dict): Baseline configuration parameters
        base_dir (str): Base directory (defaults to PROJECT_ROOT/animations/baselines)
        
    Returns:
        str: Path to baseline-specific directory
    """
    if base_dir is None:
        base_dir = os.path.join(PROJECT_ROOT, 'animations', 'baselines')
    
    # Create baseline-specific directory name
    mode = baseline_config['mode']
    ref = baseline_config['initial_refinement']
    budget = baseline_config['element_budget']
    
    if mode == 'conventional-amr':
        threshold = baseline_config['threshold']
        baseline_dir_name = f"{mode}_ref{ref}_budget{budget}_t{threshold}"
    else:
        baseline_dir_name = f"{mode}_ref{ref}_budget{budget}"
    
    baseline_output_dir = os.path.join(base_dir, baseline_dir_name)
    
    # Create directory if it doesn't exist
    os.makedirs(baseline_output_dir, exist_ok=True)
    
    return baseline_output_dir

def generate_filename(baseline_config, plot_mode, extension='png'):
    """
    Generate descriptive filename with baseline parameters and mode.
    
    Args:
        baseline_config (dict): Baseline configuration parameters
        plot_mode (str): Plotting mode (animate, snapshot, final)
        extension (str): File extension
        
    Returns:
        str: Generated filename
    """
    mode = baseline_config['mode']
    ref = baseline_config['initial_refinement']
    budget = baseline_config['element_budget']
    
    if mode == 'conventional-amr':
        threshold = baseline_config['threshold']
        filename = f"baseline_{mode}_ref{ref}_budget{budget}_t{threshold}_{plot_mode}.{extension}"
    else:
        filename = f"baseline_{mode}_ref{ref}_budget{budget}_{plot_mode}.{extension}"
    
    return filename

def create_parameter_title(baseline_config):
    """Create formatted parameter string for titles."""
    mode = baseline_config['mode']
    ref = baseline_config['initial_refinement']
    budget = baseline_config['element_budget']
    time_final = baseline_config['time_final']
    
    if mode == 'conventional-amr':
        threshold = baseline_config['threshold']
        return f"Baseline: {mode.upper()}, ref={ref}, budget={budget}, t={time_final}, threshold={threshold}"
    else:
        return f"Baseline: {mode.upper()}, ref={ref}, budget={budget}, t={time_final}"

def create_animation(times, solutions, grids, coords, solver, baseline_config, 
                    include_exact=True, output_dir=None):
    """
    Create and save animation of the simulation results.
    
    Args:
        times (list): Time history
        solutions (list): Solution history  
        grids (list): Grid boundary history
        coords (list): Coordinate history
        solver: Solver instance for parameters
        baseline_config (dict): Baseline configuration information
        include_exact (bool): Whether to include exact solution
        output_dir (str): Directory to save animation
        
    Returns:
        str: Path to saved animation file
    """
    # Set up plot
    plt.rcParams['animation.html'] = 'jshtml'
    plt.style.use('ggplot')
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Create title
    param_str = create_parameter_title(baseline_config)
    title = f'Baseline Simulation Animation\n{param_str}'
    fig.suptitle(title, fontsize=14, fontweight='bold')
    
    ax.set_xlim([-1, 1])
    ax.set_ylim([-0.1, 1.2])
    ax.set_xlabel('Domain Position')
    ax.set_ylabel('Solution Value')
    
    # Add text annotations
    frame_text = ax.text(0.02, 0.98, '', transform=ax.transAxes, 
                        verticalalignment='top', fontsize=10,
                        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
    time_text = ax.text(0.02, 0.90, '', transform=ax.transAxes,
                       verticalalignment='top', fontsize=10,
                       bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
    elements_text = ax.text(0.02, 0.82, '', transform=ax.transAxes,
                           verticalalignment='top', fontsize=10,
                           bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
    
    # Initialize solution plots with baseline-specific styling
    mode = baseline_config['mode']
    if mode == 'conventional-amr':
        solution_line = ax.plot(coords[0], solutions[0], 'orange', linewidth=2, 
                               label='Conventional-AMR Solution')[0]
    else:
        solution_line = ax.plot(coords[0], solutions[0], 'purple', linewidth=2, 
                               label='No-AMR Solution')[0]
    
    if include_exact:
        # Calculate initial exact solution
        exact_sol_0 = exact_solution(coords[0], len(coords[0]), times[0], solver.icase)[0]
        exact_line = ax.plot(coords[0], exact_sol_0, 'r--', linewidth=2, label='Exact Solution')[0]
    
    # Add vertical lines for element boundaries
    boundary_lines = []
    for x in grids[0]:
        boundary_lines.append(ax.axvline(x, color='darkmagenta', linestyle=':', alpha=0.7, linewidth=1))
    
    ax.legend()
    
    def update_data(frame):
        """Update function for animation."""
        # Update solution plot
        solution_line.set_ydata(solutions[frame])
        solution_line.set_xdata(coords[frame])
        
        # Update exact solution if included
        if include_exact:
            exact_sol = exact_solution(coords[frame], len(coords[frame]), times[frame], solver.icase)[0]
            exact_line.set_ydata(exact_sol)
            exact_line.set_xdata(coords[frame])
        
        # Update element boundaries
        for line in boundary_lines:
            line.remove()
        boundary_lines.clear()
        
        for x in grids[frame]:
            boundary_lines.append(ax.axvline(x, color='darkmagenta', linestyle=':', alpha=0.7, linewidth=1))
        
        # Update tick marks
        ax.set_xticks(grids[frame])
        
        # Update text
        frame_text.set_text(f'Frame: {frame}/{len(solutions)-1}')
        time_text.set_text(f'Time: {times[frame]:.3f}')
        n_elements = len(grids[frame]) - 1
        elements_text.set_text(f'Elements: {n_elements}')
    
    # Create animation
    anim = FuncAnimation(
        fig=fig,
        func=update_data,
        frames=len(solutions),
        interval=50,  # 50ms between frames
        blit=False
    )
    
    # Save animation
    if output_dir:
        filename = generate_filename(baseline_config, 'animate', 'mp4')
        animation_path = os.path.join(output_dir, filename)
        
        try:
            anim.save(animation_path, writer="ffmpeg", fps=20, dpi=100)
            print(f"Animation saved to {animation_path}")
        except Exception as e:
            print(f"Warning: Could not save animation: {e}")
            animation_path = None
    else:
        animation_path = None
    
    plt.close(fig)  # Close figure to free memory
    return animation_path

def create_snapshot(times, solutions, grids, coords, solver, baseline_config,
                   include_exact=True, output_dir=None, n_snapshots=5):
    """
    Create snapshot plot with multiple timesteps.
    
    Args:
        times (list): Time history
        solutions (list): Solution history
        grids (list): Grid boundary history
        coords (list): Coordinate history
        solver: Solver instance
        baseline_config (dict): Baseline configuration information
        include_exact (bool): Whether to include exact solution
        output_dir (str): Directory to save plot
        n_snapshots (int): Number of snapshots to show
        
    Returns:
        str: Path to saved plot file
    """
    # Select snapshot indices
    total_frames = len(times)
    snapshot_indices = np.linspace(0, total_frames-1, n_snapshots, dtype=int)
    
    # Set up plot
    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Create title
    param_str = create_parameter_title(baseline_config)
    title = f'Baseline Simulation Snapshots\n{param_str}'
    fig.suptitle(title, fontsize=14, fontweight='bold')
    
    ax.set_xlim([-1, 1])
    ax.set_ylim([-0.1, 1.2])
    ax.set_xlabel('Domain Position')
    ax.set_ylabel('Solution Value')
    
    # Color scheme for different times
    colors = plt.cm.viridis(np.linspace(0, 1, n_snapshots))
    
    # Plot solutions at different times
    mode = baseline_config['mode']
    for i, idx in enumerate(snapshot_indices):
        alpha = 0.8 if i == len(snapshot_indices) - 1 else 0.6  # Highlight final
        linewidth = 2.5 if i == len(snapshot_indices) - 1 else 1.5
        
        label = f'{mode} t={times[idx]:.3f}'
        ax.plot(coords[idx], solutions[idx], color=colors[i], linewidth=linewidth,
                alpha=alpha, label=label)
        
        # Add element boundaries for final timestep
        if i == len(snapshot_indices) - 1:
            for x in grids[idx]:
                ax.axvline(x, color='darkmagenta', linestyle=':', alpha=0.7, linewidth=1)
    
    # Add exact solution at final time if requested
    if include_exact:
        final_idx = snapshot_indices[-1]
        exact_sol = exact_solution(coords[final_idx], len(coords[final_idx]), times[final_idx], solver.icase)[0]
        ax.plot(coords[final_idx], exact_sol, 'r--', linewidth=2, alpha=0.9, label='Exact (final)')
    
    ax.legend(fontsize=10)
    plt.tight_layout()
    
    # Save plot
    plot_path = None
    if output_dir:
        filename = generate_filename(baseline_config, 'snapshot', 'png')
        plot_path = os.path.join(output_dir, filename)
        
        try:
            plt.savefig(plot_path, dpi=150, bbox_inches='tight')
            print(f"Snapshot plot saved to {plot_path}")
        except Exception as e:
            print(f"Warning: Could not save snapshot plot: {e}")
    
    plt.close(fig)  # Close figure to free memory
    return plot_path

def create_final_plot(solver, results, baseline_config, include_exact=True, output_dir=None):
    """
    Create final solution plot with comprehensive metrics.
    
    Args:
        solver: Solver instance
        results (dict): Evaluation results
        baseline_config (dict): Baseline configuration information
        include_exact (bool): Whether to include exact solution
        output_dir (str): Directory to save plot
        
    Returns:
        str: Path to saved plot file
    """
    # Set up plot
    plt.style.use('ggplot')
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Create title
    param_str = create_parameter_title(baseline_config)
    title = f'Baseline Simulation Final Results\n{param_str}'
    fig.suptitle(title, fontsize=14, fontweight='bold')
    
    # Top plot: Final solution
    mode = baseline_config['mode']
    if mode == 'conventional-amr':
        color = 'orange'
        label = 'Conventional-AMR Solution'
    else:
        color = 'purple'
        label = 'No-AMR Solution'
    
    ax1.plot(solver.coord, solver.q, color=color, linewidth=2, label=label)
    
    if include_exact:
        exact_sol = exact_solution(solver.coord, len(solver.coord), solver.time, solver.icase)[0]
        ax1.plot(solver.coord, exact_sol, 'r--', linewidth=2, label='Exact Solution')
    
    # Add element boundaries
    for x in solver.xelem:
        ax1.axvline(x, color='darkmagenta', linestyle=':', alpha=0.7, linewidth=1)
    
    ax1.set_xlim([-1, 1])
    ax1.set_ylim([-0.1, 1.2])
    ax1.set_xlabel('Domain Position')
    ax1.set_ylabel('Solution Value')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Bottom plot: Metrics summary
    ax2.axis('off')
    
    # Create metrics text
    metrics_text = f"""
BASELINE SIMULATION METRICS
{'='*50}
Configuration:
  • Mode: {mode.upper()}
  • Initial Refinement: {baseline_config['initial_refinement']}
  • Element Budget: {baseline_config['element_budget']}
  • Time Final: {baseline_config['time_final']:.3f}"""
    
    if mode == 'conventional-amr':
        metrics_text += f"\n  • Threshold: {baseline_config['threshold']}"
    
    metrics_text += f"""

Performance Metrics:
  • Final L2 Error: {results['final_l2_error']:.6e}
  • Total Cost: {results['total_cost']}
  • Final Elements: {results['final_elements']}
  • Total Adaptations: {results['total_adaptations']}
  • Simulation Time: {results['simulation_time']:.6f} s
  • Final Time: {results['final_time']:.3f}
  • Method: {results['method']}
"""
    
    ax2.text(0.02, 0.98, metrics_text, transform=ax2.transAxes, fontsize=11,
            verticalalignment='top', fontfamily='monospace',
            bbox=dict(boxstyle="round,pad=0.5", facecolor="lightgray", alpha=0.8))
    
    plt.tight_layout()
    
    # Save plot
    plot_path = None
    if output_dir:
        filename = generate_filename(baseline_config, 'final', 'png')
        plot_path = os.path.join(output_dir, filename)
        
        try:
            plt.savefig(plot_path, dpi=150, bbox_inches='tight')
            print(f"Final plot saved to {plot_path}")
        except Exception as e:
            print(f"Warning: Could not save final plot: {e}")
    
    plt.close(fig)  # Close figure to free memory
    return plot_path

def run_baseline_evaluation(baseline_config, verbose=False):
    """
    Run baseline simulation and collect results.
    
    Args:
        baseline_config (dict): Baseline configuration parameters
        verbose (bool): Whether to print detailed logs
        
    Returns:
        dict: Evaluation results
    """
    # Extract configuration from baseline_config dict
    # Default configuration matching existing setups
    default_config = {
        'nop': 3,
        'xelem': np.array([-1, -0.4, 0, 0.4, 1]),
        'max_level': 5,
        'icase': 1,
        'courant_max': 0.1,
        'periodic': True,
        'verbose': False,
        'balance': False
    }
    
    # Override with provided config values
    for key in ['nop', 'max_level', 'icase', 'courant_max']:
        if key in baseline_config:
            default_config[key] = baseline_config[key]
    
    default_config['verbose'] = verbose
    
    # Calculate max_elements from element_budget (generous upper bound)
    max_elements = baseline_config['element_budget'] * 3
    
    # Set max_level to prevent refinement beyond initial level for baseline consistency
    max_level_for_baseline = max(baseline_config['initial_refinement'], 1)
    
    # Initialize baseline solver with proper interface
    solver = DGWaveSolverBaseline(
        nop=default_config['nop'],
        xelem=default_config['xelem'].copy(),
        max_elements=max_elements,
        max_level=max_level_for_baseline,
        courant_max=default_config['courant_max'],
        icase=default_config['icase'],
        periodic=default_config['periodic'],
        verbose=verbose,
        balance=default_config['balance'],
        amr_mode=baseline_config['mode'],
        threshold=baseline_config.get('threshold', 0.5)  # Default threshold for conventional-amr
    )
    
    # Apply initial refinement if specified
    if baseline_config['initial_refinement'] > 0:
        if verbose:
            print(f"Applying initial refinement level {baseline_config['initial_refinement']}")
        solver.initialize_with_refinement(
            refinement_mode='fixed',
            refinement_level=baseline_config['initial_refinement']
        )
        solver.initial_refinement = baseline_config['initial_refinement']
    else:
        solver.initial_refinement = 0
    
    if verbose:
        print(f"Running {baseline_config['mode']} evaluation:")
        print(f"  Initial refinement: {baseline_config['initial_refinement']}")
        print(f"  Max refinement level: {max_level_for_baseline}")
        print(f"  Element budget: {baseline_config['element_budget']}")
        print(f"  Time final: {baseline_config['time_final']}")
        if baseline_config['mode'] == 'conventional-amr':
            print(f"  Threshold: {baseline_config.get('threshold', 0.5)}")
    
    # Run simulation using our own loop (since solver.solve() has bugs)
    time_final = baseline_config['time_final']
    simulation_start_time = time.time()
    
    # Initialize result arrays
    times = [solver.time]
    solutions = [solver.q.copy()]
    grids = [solver.xelem.copy()]
    coords = [solver.coord.copy()]
    
    # Main simulation loop
    step_count = 0
    while solver.time < time_final:
        dt = min(solver.dt, time_final - solver.time)
        
        if verbose:
            print(f"  Timestep {step_count}, Time: {solver.time:.3f}")
        
        # Apply adaptation based on mode
        if baseline_config['mode'] == 'conventional-amr':
            # Use the baseline solver's conventional AMR method
            pre_elements = len(solver.active)
            solver.conventional_amr_step(baseline_config['element_budget'])
            
        # No adaptation needed for no-amr mode
        
        # Take time step
        solver.step(dt)
        
        # Store results
        times.append(solver.time)
        solutions.append(solver.q.copy())
        grids.append(solver.xelem.copy())
        coords.append(solver.coord.copy())
        step_count += 1
    
    simulation_time = time.time() - simulation_start_time
    
    # Calculate metrics from the solve results
    final_exact = exact_solution(coords[-1], len(coords[-1]), times[-1], solver.icase)[0]
    # l2_error = np.sqrt(np.sum((solutions[-1] - final_exact)**2) * solver.dx_min)
    l2_error = np.sqrt(np.sum((solutions[-1] - final_exact)**2) / np.sum(final_exact**2))
    
    # Create metrics dictionary (matching baseline_evaluator.py format)
    metrics = {
        'method': baseline_config['mode'],
        'initial_refinement': baseline_config['initial_refinement'],
        'evaluation_element_budget': baseline_config['element_budget'],
        'final_l2_error': l2_error,
        'total_cost': (len(times) - 1) * (len(grids[-1]) - 1),
        'final_elements': len(grids[-1]) - 1,  # Final number of elements
        'simulation_time': simulation_time,
        'threshold_value': baseline_config.get('threshold', 'N/A'),
        'adaptation_count': 0,  # Will be updated based on mode
        'final_time': times[-1]
    }
    
    # Count adaptations by tracking element count changes
    adaptation_count = 0
    if len(grids) > 1:
        for i in range(1, len(grids)):
            if len(grids[i]) != len(grids[i-1]):
                adaptation_count += 1
    metrics['adaptation_count'] = adaptation_count
    
    # Create comprehensive results
    results = {
        'solver': solver,
        'times': times,
        'solutions': solutions,
        'grids': grids,
        'coords': coords,
        'metrics': metrics,
        'final_l2_error': metrics['final_l2_error'],
        'total_cost': metrics['total_cost'],
        'final_elements': metrics['final_elements'],
        'total_adaptations': metrics['adaptation_count'],
        'simulation_time': metrics['simulation_time'],
        'final_time': metrics['final_time'],
        'method': metrics['method']
    }
    
    return results

def main():
    """Main function with argument parsing for command line usage"""
    parser = argparse.ArgumentParser(description='Run baseline AMR simulation with visualization')
    
    # Required arguments
    parser.add_argument('--mode', choices=['no-amr', 'conventional-amr'], 
                       required=True, help='Baseline simulation mode')
    
    # Simulation parameters
    parser.add_argument('--time-final', type=float, default=1.0, help='Final simulation time')
    parser.add_argument('--element-budget', type=int, default=150, help='Maximum number of elements')
    parser.add_argument('--max-level', type=int, default=5, help='Maximum refinement level')
    parser.add_argument('--nop', type=int, default=3, help='Polynomial order')
    parser.add_argument('--courant-max', type=float, default=0.1, help='CFL number')
    parser.add_argument('--icase', type=int, default=1, help='Test case identifier')
    parser.add_argument('--initial-refinement', type=int, default=5, 
                       help='Initial refinement level (0=base mesh, >0 refines all elements)')
    
    # Conventional AMR parameters
    parser.add_argument('--threshold', type=float, default=0.5,
                       help='Adaptation threshold for conventional AMR (default: 0.5)')
    
    # Plotting options
    parser.add_argument('--plot-mode', choices=['animate', 'snapshot', 'final'], 
                       help='Plotting mode: animate (full animation), snapshot (multiple timesteps), final (final timestep only)')
    parser.add_argument('--include-exact', action='store_true', default=True, 
                       help='Include exact solution in plots (default: True)')
    parser.add_argument('--no-exact', dest='include_exact', action='store_false', 
                       help='Disable exact solution in plots')
    
    # Output options
    parser.add_argument('--verbose', action='store_true', help='Print detailed progress logs')
    
    args = parser.parse_args()
    
    # Validate arguments
    if args.mode == 'conventional-amr' and not hasattr(args, 'threshold'):
        args.threshold = 0.5  # Default threshold
    
    try:
        # Extract baseline configuration
        baseline_config = extract_baseline_configuration(args)
        
        if args.verbose:
            print("=== BASELINE SIMULATION RUNNER ===")
            print(f"Mode: {args.mode}")
            if args.mode == 'conventional-amr':
                print(f"Threshold: {args.threshold}")
            print(f"Initial Refinement: {args.initial_refinement}")
            print(f"Element Budget: {args.element_budget}")
            print(f"Time Final: {args.time_final}")
            if args.plot_mode:
                print(f"Plot Mode: {args.plot_mode}")
            print()
        
        # Run baseline evaluation
        results = run_baseline_evaluation(baseline_config, verbose=args.verbose)
        
        # Create visualization if plot mode specified
        if args.plot_mode:
            output_dir = create_baseline_directory(baseline_config)
            
            if args.plot_mode == 'animate':
                animation_path = create_animation(
                    results['times'], results['solutions'], results['grids'], 
                    results['coords'], results['solver'], baseline_config,
                    include_exact=args.include_exact, output_dir=output_dir
                )
                if animation_path:
                    print(f"Animation created: {animation_path}")
                    
            elif args.plot_mode == 'snapshot':
                plot_path = create_snapshot(
                    results['times'], results['solutions'], results['grids'], 
                    results['coords'], results['solver'], baseline_config,
                    include_exact=args.include_exact, output_dir=output_dir
                )
                if plot_path:
                    print(f"Snapshot plot created: {plot_path}")
                    
            elif args.plot_mode == 'final':
                plot_path = create_final_plot(
                    results['solver'], results, baseline_config,
                    include_exact=args.include_exact, output_dir=output_dir
                )
                if plot_path:
                    print(f"Final plot created: {plot_path}")
        
        # Print final summary
        if args.verbose:
            print("\n=== BASELINE EVALUATION COMPLETE ===")
            print(f"Configuration: {create_parameter_title(baseline_config)}")
            print(f"Final L2 Error: {results['final_l2_error']:.6e}")
            print(f"Total Cost: {results['total_cost']}")
            print(f"Final Elements: {results['final_elements']}")
            print(f"Total Adaptations: {results['total_adaptations']}")
            print(f"Final Time: {results['final_time']:.3f}")
    
    except Exception as e:
        print(f"Error during baseline evaluation: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()