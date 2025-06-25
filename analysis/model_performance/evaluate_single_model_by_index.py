#!/usr/bin/env python3
"""
Evaluate a single model by index for parallel batch processing.
Usage: python evaluate_single_model_by_index.py <index> <sweep_name> <initial_refinement> <element_budget>
"""

import sys
import os
import glob
import json
import csv
from pathlib import Path

# Add project root to path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(PROJECT_ROOT)

from single_model_runner import run_single_model, extract_training_parameters

def main():
    if len(sys.argv) != 5:
        print("Usage: python evaluate_single_model_by_index.py <index> <sweep_name> <initial_refinement> <element_budget>")
        sys.exit(1)
    
    index = int(sys.argv[1]) - 1  # Convert to 0-based indexing
    sweep_name = sys.argv[2]
    initial_refinement = int(sys.argv[3])
    element_budget = int(sys.argv[4])
    
    # Calculate expected initial elements
    base_elements = 4  # From xelem = [-1, -0.4, 0, 0.4, 1]
    expected_initial_elements = base_elements * (2 ** initial_refinement)
    
    print(f"Configuration: initial_refinement={initial_refinement}, element_budget={element_budget}")
    print(f"Expected initial elements: {expected_initial_elements}")
    
    if expected_initial_elements >= element_budget:
        print(f"WARNING: Starting with {expected_initial_elements} elements but budget is {element_budget}")
        print("Model will start over budget and can only coarsen or do nothing!")
    
    # Find all model paths
    models_dir = os.path.join(PROJECT_ROOT, 'analysis', 'data', 'models', sweep_name)
    model_dirs = sorted([d for d in os.listdir(models_dir) if d.startswith('gamma_')])
    
    if index >= len(model_dirs):
        print(f"Error: Index {index+1} out of range (1-{len(model_dirs)})")
        sys.exit(1)
    
    # Get the specific model
    model_dir = model_dirs[index]
    model_path = os.path.join(models_dir, model_dir, 'final_model.zip')
    
    print(f"Evaluating model {index+1}/{len(model_dirs)}: {model_dir}")
    
    # Run evaluation
    results = run_single_model(
        model_path=model_path,
        time_final=1.0,
        element_budget=element_budget,  # Use configurable budget
        max_level=5,
        nop=4,
        courant_max=0.1,
        icase=1,
        plot_mode=None,  # No plots for batch processing
        include_exact=False,
        verbose=False,
        output_dir=None,
        initial_refinement=initial_refinement
    )
    
    # Save individual results
    output_dir = os.path.join(PROJECT_ROOT, 'analysis', 'data', 'model_performance', sweep_name)
    os.makedirs(output_dir, exist_ok=True)
    
    # Save detailed JSON with both parameters in filename
    json_file = os.path.join(output_dir, f'{model_dir}_ref_{initial_refinement}_budget_{element_budget}_results.json')
    with open(json_file, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    
    # Append to CSV (separate file for each configuration)
    csv_file = os.path.join(output_dir, f'model_results_ref{initial_refinement}_budget{element_budget}.csv')
    training_params = results['training_parameters']
    
    # Create CSV row
    csv_row = [
        training_params['gamma_c'],
        training_params['step_domain_fraction'], 
        training_params['rl_iterations_per_timestep'],
        training_params['element_budget'],  # Original training budget
        initial_refinement,
        element_budget,  # Evaluation budget
        results['final_l2_error'],
        results['total_cost'],
        results['final_elements'],
        results['total_adaptations'],
        results['simulation_metrics']['final_time'],
        results['simulation_metrics']['initial_elements'],
        model_path
    ]
    
    # Thread-safe CSV writing
    import fcntl
    csv_headers = [
        'gamma_c', 'step_domain_fraction', 'rl_iterations_per_timestep', 'element_budget',
        'initial_refinement', 'evaluation_element_budget', 'final_l2_error', 'total_cost', 
        'final_elements', 'total_adaptations', 'final_time', 'initial_elements', 'model_path'
    ]
    
    with open(csv_file, 'a') as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        writer = csv.writer(f)
        # Write header if file is empty
        if f.tell() == 0:
            writer.writerow(csv_headers)
        writer.writerow(csv_row)
    
    print(f"Completed model {index+1}: L2 error = {results['final_l2_error']:.2e}")
    print(f"Actual initial elements = {results['simulation_metrics']['initial_elements']}")

if __name__ == "__main__":
    main()
