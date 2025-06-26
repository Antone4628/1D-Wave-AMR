"""
Batch Model Evaluator for AMR Parameter Sweep Analysis

This script evaluates all 81 trained RL models systematically for accuracy vs cost analysis.
Produces CSV with core metrics and JSON files with detailed results for each model.

Usage:
    python batch_model_evaluator.py session3_100k_uniform --time-final 1.0 --element-budget 50 --verbose
"""

import numpy as np
import os
import sys
import argparse
import csv
import json
import gc
from pathlib import Path
from datetime import datetime

# Get absolute path to project root
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 
    '..',
    '..'
))
sys.path.append(PROJECT_ROOT)

# Import the evaluation components (from single_model_runner.py)
from dg_wave_solver_evaluation import DGWaveSolverEvaluation
from model_marker_evaluation import ModelMarkerEvaluation
from numerical.solvers.utils import exact_solution, calculate_grid_normalized_l2_error

def extract_training_parameters(model_path):
    """
    Extract training parameters from the standardized model path.
    
    Expected path format: .../gamma_{value}_step_{value}_rl_{value}_budget_{value}/final_model.zip
    
    Args:
        model_path (str): Path to the model file
        
    Returns:
        dict: Extracted training parameters or None if parsing fails
    """
    try:
        # Extract the parent directory name
        parent_dir = Path(model_path).parent.name
        
        # Split by underscores and parse
        parts = parent_dir.split('_')
        
        # Expected format: ['gamma', '25.0', 'step', '0.025', 'rl', '10', 'budget', '25']
        if len(parts) == 8 and parts[0] == 'gamma' and parts[2] == 'step' and parts[4] == 'rl' and parts[6] == 'budget':
            return {
                'gamma_c': float(parts[1]),
                'step_domain_fraction': float(parts[3]),
                'rl_iterations_per_timestep': int(parts[5]),
                'element_budget': int(parts[7])  # This is the TRAINING budget
            }
        else:
            print(f"Warning: Model path doesn't match expected pattern: {parent_dir}")
            return None
            
    except Exception as e:
        print(f"Warning: Could not extract parameters from path: {e}")
        return None

def discover_models(models_directory):
    """
    Auto-discover all model files in the specified directory.
    
    Args:
        models_directory (str): Path to directory containing model subdirectories
        
    Returns:
        list: List of paths to final_model.zip files
    """
    models_dir = Path(models_directory)
    if not models_dir.exists():
        raise FileNotFoundError(f"Models directory not found: {models_directory}")
    
    model_paths = []
    
    # Look for final_model.* files in each subdirectory (handles transfer naming issues)
    for subdir in models_dir.iterdir():
        if subdir.is_dir():
            # Look for any file starting with "final_model"
            model_files = list(subdir.glob("final_model.*"))
            if model_files:
                # Use the first match (should only be one)
                model_paths.append(str(model_files[0]))
            else:
                print(f"Warning: No final_model.* found in {subdir}")
    
    model_paths.sort()  # Ensure consistent ordering
    return model_paths

def evaluate_single_model_batch(model_path, time_final=1.0, element_budget=50, max_level=5, 
                               nop=4, courant_max=0.1, icase=1, initial_refinement=0, verbose=False):
    """
    Evaluate a single model for batch processing (no visualization).
    
    This is a stripped-down version of run_single_model() from single_model_runner.py
    that focuses purely on metrics collection.
    
    Args:
        model_path (str): Path to the trained model file
        time_final (float): Final simulation time
        element_budget (int): Maximum number of elements allowed
        max_level (int): Maximum refinement level
        nop (int): Polynomial order
        courant_max (float): CFL number
        icase (int): Test case identifier
        initial_refinement (int): Initial refinement level
        verbose (bool): Whether to print detailed logs
        
    Returns:
        dict: Evaluation results with metrics
    """
    
    # Validate model path
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    
    # Extract training parameters from model path
    training_params = extract_training_parameters(model_path)
    
    # Define initial mesh
    xelem = np.array([-1, -0.4, 0, 0.4, 1])

    # Initialize evaluation solver
    solver = DGWaveSolverEvaluation(
        nop=nop,
        xelem=xelem,
        max_elements=element_budget,
        max_level=max_level,
        courant_max=courant_max,
        icase=icase,
        periodic=True,
        verbose=verbose
    )

    # Initialize ModelMarkerEvaluation with trained model
    model_adapter = ModelMarkerEvaluation(
        model_path=model_path,
        solver=solver,
        element_budget=element_budget,
        verbose=verbose
    )

    if verbose:
        print(f"Evaluating: {Path(model_path).parent.name}")

    # Apply initial refinement if requested
    if initial_refinement > 0:
        if verbose:
            print(f"Applying initial refinement level {initial_refinement}")
        solver._perform_fixed_refinement(initial_refinement)

    # SAVE INITIAL COORDINATE STATE FOR GRID-NORMALIZED L2
    initial_coord = solver.coord.copy()  # Save initial coordinates after refinement
    actual_initial_elements = len(solver.active)
    
    # Initialize metrics tracking
    element_counts = [len(solver.active)]
    adaptation_counts = [0]

    # Solve the PDE with sequential RL-based AMR
    step_count = 0
    total_adaptations = 0
    
    while solver.time < time_final:
        dt = min(solver.dt, time_final - solver.time)
        
        if verbose:
            print(f"  Timestep {step_count}, Time: {solver.time:.3f}")
        
        # Apply mesh adaptation using single round approach
        adaptations_made = model_adapter.mark_and_adapt_single_round()
        total_adaptations += adaptations_made
        
        # Take normal time step
        solver.step(dt)
        
        # Track element counts for cost calculation
        element_counts.append(len(solver.active))
        adaptation_counts.append(adaptations_made)
        step_count += 1

    # Calculate final metrics
    final_exact_solution = exact_solution(solver.coord, solver.npoin_dg, solver.time, solver.icase)[0]
    final_l2_error = np.sqrt(np.sum((solver.q - final_exact_solution)**2) / np.sum(final_exact_solution**2))

    # Calculate grid-normalized L2 error for fair comparison
    grid_normalized_l2_error = calculate_grid_normalized_l2_error(
        solver.q, solver.coord, initial_coord, solver.time, solver.icase
    )
    
    # Calculate total computational cost
    total_cost = sum(element_counts)
    
    # Create simulation config hash for reproducibility
    config_data = f"{time_final}_{element_budget}_{max_level}_{nop}_{courant_max}_{icase}_{initial_refinement}"
    simulation_config_hash = str(hash(config_data))[:8]
    
    # Prepare results dictionary
    results = {
        'final_l2_error': final_l2_error,
        'grid_normalized_l2_error': grid_normalized_l2_error,
        'total_cost': total_cost,
        'final_elements': len(solver.active),
        'total_adaptations': total_adaptations,
        'training_parameters': training_params,
        'simulation_metrics': {
            'initial_elements': actual_initial_elements,
            'max_elements': max(element_counts),
            'min_elements': min(element_counts),
            'total_timesteps': step_count,
            'final_time': solver.time,
            'average_elements': np.mean(element_counts),
            'element_count_history': element_counts,
            'adaptation_count_history': adaptation_counts,
            'model_path': model_path,
            'simulation_config_hash': simulation_config_hash,
            'evaluation_timestamp': datetime.now().isoformat()
        }
    }
    
    if verbose:
        print(f"  Final L2 Error: {final_l2_error:.6e}")
        print(f"  Total Cost: {total_cost}")
        print(f"  Final Elements: {len(solver.active)}")
    
    return results

def run_batch_evaluation(sweep_name, time_final=1.0, element_budget=50, max_level=5, 
                        nop=4, courant_max=0.1, icase=1, initial_refinement=0, verbose=False):
    """
    Run batch evaluation of all models in the specified sweep.
    
    Args:
        sweep_name (str): Name of the sweep (e.g., 'session3_100k_uniform')
        time_final (float): Final simulation time
        element_budget (int): Maximum number of elements allowed
        max_level (int): Maximum refinement level
        nop (int): Polynomial order
        courant_max (float): CFL number
        icase (int): Test case identifier
        initial_refinement (int): Initial refinement level
        verbose (bool): Whether to print detailed logs
        
    Returns:
        tuple: (csv_path, json_dir, metadata)
    """
    
    # Set up paths
    models_directory = os.path.join(PROJECT_ROOT, 'analysis', 'data', 'models', sweep_name)
    output_directory = os.path.join(PROJECT_ROOT, 'analysis', 'data', 'model_performance', sweep_name)
    
    # Create output directory
    os.makedirs(output_directory, exist_ok=True)
    
    # Discover all models
    model_paths = discover_models(models_directory)
    
    if not model_paths:
        raise ValueError(f"No models found in {models_directory}")
    
    print(f"Found {len(model_paths)} models to evaluate")
    
    # Set up CSV output
    csv_path = os.path.join(output_directory, f'model_results_ref{initial_refinement}_budget{element_budget}.csv')
    json_dir = os.path.join(output_directory, 'individual_results')
    os.makedirs(json_dir, exist_ok=True)
    
    # CSV headers matching the specification
    csv_headers = [
        'gamma_c', 'step_domain_fraction', 'rl_iterations_per_timestep', 'element_budget',
        'final_l2_error', 'grid_normalized_l2_error', 'total_cost', 'final_elements', 'total_adaptations', 
        'final_time', 'initial_elements', 'simulation_config_hash', 'model_path'
    ]
    
    # Initialize tracking
    successful_runs = 0
    failed_runs = 0
    failed_models = []
    start_time = datetime.now()
    
    # Open CSV file for writing
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_headers)
        
        for i, model_path in enumerate(model_paths):
            try:
                if verbose:
                    print(f"\n[{i+1}/{len(model_paths)}] Processing {Path(model_path).parent.name}")
                
                # Evaluate the model
                results = evaluate_single_model_batch(
                    model_path=model_path,
                    time_final=time_final,
                    element_budget=element_budget,
                    max_level=max_level,
                    nop=nop,
                    courant_max=courant_max,
                    icase=icase,
                    initial_refinement=initial_refinement,
                    verbose=verbose
                )
                
                # Extract data for CSV row
                training_params = results['training_parameters']
                if training_params:
                    csv_row = [
                        training_params['gamma_c'],
                        training_params['step_domain_fraction'],
                        training_params['rl_iterations_per_timestep'],
                        training_params['element_budget'],
                        results['final_l2_error'],
                        results['grid_normalized_l2_error'],  # Add this line
                        results['total_cost'],
                        results['final_elements'],
                        results['total_adaptations'],
                        results['simulation_metrics']['final_time'],
                        results['simulation_metrics']['initial_elements'],
                        results['simulation_metrics']['simulation_config_hash'],
                        model_path
                    ]
                    
                    # Write CSV row
                    writer.writerow(csv_row)
                    
                    # Save detailed JSON results
                    model_name = Path(model_path).parent.name
                    json_path = os.path.join(json_dir, f"{model_name}_detailed_results.json")
                    
                    with open(json_path, 'w') as jsonfile:
                        json.dump(results, jsonfile, indent=2, default=str)
                    
                    successful_runs += 1
                    
                    # Show progress after successful completion
                    if not verbose:
                        print(f"[{i+1}/{len(model_paths)}] Completed: {model_name} (L2: {results['final_l2_error']:.2e}, Cost: {results['total_cost']})")
                    
                else:
                    print(f"Warning: Could not extract training parameters from {model_path}")
                    failed_runs += 1
                    failed_models.append(str(model_path))
                    
            except Exception as e:
                print(f"Error evaluating {model_path}: {e}")
                failed_runs += 1
                failed_models.append(str(model_path))
                
            finally:
                # Memory cleanup after each model
                try:
                    del results, model_adapter, solver
                    gc.collect()
                except:
                    pass
    
    # Create metadata
    end_time = datetime.now()
    runtime_hours = (end_time - start_time).total_seconds() / 3600
    
    metadata = {
        "batch_config": {
            "sweep_name": sweep_name,
            "time_final": time_final,
            "element_budget": element_budget,
            "max_level": max_level,
            "nop": nop,
            "courant_max": courant_max,
            "icase": icase,
            "initial_refinement": initial_refinement
        },
        "run_timestamp": start_time.isoformat(),
        "completion_timestamp": end_time.isoformat(),
        "total_models": len(model_paths),
        "successful_runs": successful_runs,
        "failed_runs": failed_runs,
        "failed_models": failed_models,
        "estimated_runtime_hours": runtime_hours
    }
    
    # Save metadata
    metadata_path = os.path.join(output_directory, 'batch_metadata.json')
    with open(metadata_path, 'w') as f:
        json.dump(metadata, f, indent=2)
    
    # Save failed models log if any
    if failed_models:
        failed_log_path = os.path.join(output_directory, 'failed_models.log')
        with open(failed_log_path, 'w') as f:
            f.write(f"Failed models ({len(failed_models)}):\n")
            for model in failed_models:
                f.write(f"{model}\n")
    
    print(f"\n=== BATCH EVALUATION COMPLETE ===")
    print(f"Successful runs: {successful_runs}/{len(model_paths)}")
    print(f"Failed runs: {failed_runs}")
    print(f"Runtime: {runtime_hours:.2f} hours")
    print(f"Results saved to: {csv_path}")
    print(f"Detailed JSON results: {json_dir}")
    
    return csv_path, json_dir, metadata

def main():
    """Main function with argument parsing for command line usage"""
    parser = argparse.ArgumentParser(description='Batch evaluate all RL models for accuracy vs cost analysis')
    
    # Required arguments
    parser.add_argument('sweep_name', help='Name of the sweep (e.g., session3_100k_uniform)')
    
    # Simulation parameters
    parser.add_argument('--time-final', type=float, default=1.0, help='Final simulation time')
    parser.add_argument('--element-budget', type=int, default=50, help='Maximum number of elements')
    parser.add_argument('--max-level', type=int, default=5, help='Maximum refinement level')
    parser.add_argument('--nop', type=int, default=4, help='Polynomial order')
    parser.add_argument('--courant-max', type=float, default=0.1, help='CFL number')
    parser.add_argument('--icase', type=int, default=1, help='Test case identifier')
    parser.add_argument('--initial-refinement', type=int, default=0, 
                       help='Initial refinement level (0=base mesh, >0 refines all elements)')
    
    # Output options
    parser.add_argument('--verbose', action='store_true', help='Print detailed logs')
    
    args = parser.parse_args()
    
    # Run batch evaluation
    csv_path, json_dir, metadata = run_batch_evaluation(
        sweep_name=args.sweep_name,
        time_final=args.time_final,
        element_budget=args.element_budget,
        max_level=args.max_level,
        nop=args.nop,
        courant_max=args.courant_max,
        icase=args.icase,
        initial_refinement=args.initial_refinement,
        verbose=args.verbose
    )

if __name__ == "__main__":
    main()