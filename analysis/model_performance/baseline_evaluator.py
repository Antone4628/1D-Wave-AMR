#!/usr/bin/env python3
"""
Baseline AMR Evaluator

Generates baseline performance data for comparison with DRL-AMR models.
Supports no-AMR and conventional threshold-based AMR modes.
"""

import argparse
import os
import sys
import numpy as np
import pandas as pd
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parents[2]
sys.path.append(str(project_root))

from numerical.solvers.dg_wave_solver_baseline import DGWaveSolverBaseline
from numerical.solvers.utils import calculate_grid_normalized_l2_error

def extract_configuration_from_sweep(sweep_name):
    """
    Extract default configuration from sweep name.
    For session3_100k_uniform, use standard test case parameters.
    """
    # Default configuration matching existing setups
    config = {
        'nop': 3,
        'xelem': np.array([-1, -0.4, 0, 0.4, 1]),
        'max_level': 5,
        'icase': 1,
        'courant_max': 0.1,
        'periodic': True,
        'verbose': False,
        'balance': False
    }
    
    return config

def run_baseline_evaluation(args):
    """
    Run baseline evaluation and return metrics.
    """
    # Extract configuration
    config = extract_configuration_from_sweep(args.sweep_name)
    
    # Calculate max_elements from element_budget (generous upper bound)
    max_elements = args.element_budget * 20
    
    # Set max_level to prevent refinement beyond initial level
    max_level_for_baseline = max(args.initial_refinement, 1)  # Minimum level 1 for safety

        # DEBUG: Add these lines
    # print(f"DEBUG CLI: args.mode = {args.mode}")
    # print(f"DEBUG CLI: args.threshold = {args.threshold}")

    # Initialize solver
    solver = DGWaveSolverBaseline(
        nop=config['nop'],
        xelem=config['xelem'].copy(),
        max_elements=max_elements,
        max_level=max_level_for_baseline,
        courant_max=config['courant_max'],
        icase=config['icase'],
        periodic=config['periodic'],
        verbose=args.verbose,
        balance=config['balance'],
        amr_mode=args.mode,  # ← This should be 'conventional-amr'
        threshold=args.threshold
    )
    
    # DEBUG: Add this line
    # print(f"DEBUG CLI: After creation, solver.amr_mode = {solver.amr_mode}")
    
    # Apply initial refinement if specified
    if args.initial_refinement > 0:
        solver.initialize_with_refinement(
            refinement_mode='fixed',
            refinement_level=args.initial_refinement
        )
        # Store for metrics
        solver.initial_refinement = args.initial_refinement
    else:
        solver.initial_refinement = 0

    # SAVE INITIAL COORDINATE STATE FOR GRID-NORMALIZED L2
    initial_coord = solver.coord.copy()
    
    if args.verbose:
        print(f"Running {args.mode} evaluation:")
        print(f"  Initial refinement: {args.initial_refinement}")
        print(f"  Max refinement level: {max_level_for_baseline}")
        print(f"  Element budget: {args.element_budget}")
        print(f"  Time final: {args.time_final}")
        if args.mode == 'conventional-amr':
            print(f"  Threshold: {args.threshold}")
    
    # Run simulation
    metrics = solver.run_simulation(
        time_final=args.time_final,
        # element_budget=args.element_budget
        element_budget = None
    )
    # ADD GRID-NORMALIZED L2 ERROR FOR CONVENTIONAL-AMR CASES
    if args.mode == 'conventional-amr':
        # Need to access final solution from solver
        grid_normalized_l2_error = calculate_grid_normalized_l2_error(
            solver.q, solver.coord, initial_coord, solver.time, solver.icase
        )
        metrics['grid_normalized_l2_error'] = grid_normalized_l2_error
    else:
        # For no-amr, the error is already on the reference grid
        metrics['grid_normalized_l2_error'] = metrics.get('final_l2_error', 0.0)

    
    return metrics

def generate_baseline_data(args):
    """
    Generate baseline data for specified configuration.
    """
    results = []
    
    if args.mode == 'no-amr':
        # Single no-AMR run
        if args.verbose:
            print("Generating no-AMR baseline...")
        
        metrics = run_baseline_evaluation(args)
        results.append(metrics)
        
    elif args.mode == 'conventional-amr':
        # Run with specified threshold(s)
        if args.threshold_list:
            # Parse comma-separated threshold values
            thresholds = [float(t.strip()) for t in args.threshold_list.split(',')]
            if args.verbose:
                print(f"Using multiple thresholds: {thresholds}")
        else:
            # Single threshold
            thresholds = [args.threshold]
            if args.verbose:
                print(f"Using single threshold: {args.threshold}")
        
        for threshold in thresholds:
            if args.verbose:
                print(f"Generating conventional-AMR baseline with threshold {threshold}...")
            
            # Update threshold for this run
            args.threshold = threshold
            metrics = run_baseline_evaluation(args)
            results.append(metrics)
    
    return results

def save_results(results, args):
    """
    Save results to CSV file matching model evaluation format.
    """
    # Convert to DataFrame
    df = pd.DataFrame(results)
    
    # Ensure output directory exists
    output_dir = Path(f"analysis/data/model_performance/{args.sweep_name}")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Determine output filename
    if args.output_file:
        output_path = output_dir / args.output_file
    else:
        # Auto-generate filename with mode
        filename = f"baseline_results_{args.mode}_ref{args.initial_refinement}_budget{args.element_budget}.csv"
        output_path = output_dir / filename
    
    # Save CSV
    df.to_csv(output_path, index=False)
    
    if args.verbose:
        print(f"Results saved to: {output_path}")
        print(f"Generated {len(results)} baseline data points")
    
    return output_path

def main():
    parser = argparse.ArgumentParser(
        description="Generate baseline AMR performance data",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
        Examples:
        # No-AMR baseline
        python baseline_evaluator.py session3_100k_uniform --mode no-amr \\
            --initial-refinement 3 --element-budget 50

        # Single threshold conventional AMR
        python baseline_evaluator.py session3_100k_uniform --mode conventional-amr \\
            --initial-refinement 3 --element-budget 50 --threshold 0.5

        # Multiple thresholds conventional AMR
        python baseline_evaluator.py session3_100k_uniform --mode conventional-amr \\
            --initial-refinement 3 --element-budget 50 \\
            --threshold-list "0.5,0.4,0.3,0.2,0.1,0.05,0.01"
                """
    )
    
    # Required arguments
    parser.add_argument('sweep_name', 
                       help='Name of parameter sweep (e.g., session3_100k_uniform)')
    
    # Mode selection
    parser.add_argument('--mode', choices=['no-amr', 'conventional-amr'], 
                       required=True,
                       help='Baseline evaluation mode')
    
    # Configuration parameters
    parser.add_argument('--initial-refinement', type=int, default=0,
                       help='Initial mesh refinement level (default: 0)')
    parser.add_argument('--element-budget', type=int, default=None,
                       help='Maximum number of elements (default: 50)')
    parser.add_argument('--time-final', type=float, default=1.0,
                       help='Final simulation time (default: 1.0)')
    
    # Conventional AMR parameters
    parser.add_argument('--threshold', type=float, default=0.5,
                       help='Adaptation threshold for conventional AMR (default: 0.5)')
    # parser.add_argument('--multiple-thresholds', action='store_true',
    #                    help='Run multiple thresholds [0.3, 0.5, 0.7] for conventional AMR')

    parser.add_argument('--threshold-list', type=str,
                   help='Comma-separated threshold values for conventional AMR (e.g., "0.5,0.4,0.3,0.2,0.1,0.05,0.01")')


    
    # Output parameters
    parser.add_argument('--output-file', type=str,
                       help='Output CSV filename (auto-generated if not specified)')
    parser.add_argument('--verbose', action='store_true',
                       help='Enable verbose output')
    
    args = parser.parse_args()
    
    # Validate arguments
    if args.mode == 'conventional-amr' and args.threshold_list and args.threshold != 0.5:
        print("Warning: --threshold ignored when using --threshold-list")
    
    try:
        # Generate baseline data
        results = generate_baseline_data(args)
        
        # Save results
        output_path = save_results(results, args)
        
        print(f"Baseline evaluation complete: {output_path}")
        
    except Exception as e:
        print(f"Error during baseline evaluation: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()