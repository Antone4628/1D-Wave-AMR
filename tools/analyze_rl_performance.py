"""
RL Model Performance Analysis

This script analyzes the performance of RL-driven adaptive mesh refinement
compared to traditional methods across different model configurations and
simulation parameters.
"""

import os
import sys
import json
import numpy as np
import matplotlib.pyplot as plt
import argparse
from datetime import datetime
import glob

# Get absolute path to project root
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 
    '..'
))
sys.path.append(PROJECT_ROOT)

# Import the run functions
from tests.test_amr.model_class_test import compare_amr_approaches

def run_analysis(models_dir, output_dir, runs_per_model=3, time_final=0.2, max_level=4, 
                element_budget=40, verbose=False):
    """
    Analyze RL model performance across multiple models and runs.
    
    Args:
        models_dir: Directory containing model files (*.zip)
        output_dir: Directory to save analysis results
        runs_per_model: Number of runs per model
        time_final: Final simulation time
        max_level: Maximum refinement level
        element_budget: Maximum allowed elements
        verbose: Whether to print detailed logs
        
    Returns:
        dict: Analysis results
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Find all model files
    model_files = glob.glob(os.path.join(models_dir, "**", "*.zip"), recursive=True)
    if not model_files:
        print(f"No model files found in {models_dir}")
        return {}
    
    print(f"Found {len(model_files)} model files")
    
    # Initialize results dictionary
    results = {
        'models': {},
        'summary': {},
        'parameters': {
            'time_final': time_final,
            'max_level': max_level,
            'element_budget': element_budget,
            'runs_per_model': runs_per_model,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    }
    
    # Run comparisons for each model
    for model_path in model_files:
        model_name = os.path.basename(model_path).replace('.zip', '')
        model_dir = os.path.dirname(model_path)
        
        print(f"\n--- Analyzing model: {model_name} ---")
        print(f"Model path: {model_path}")
        
        model_results = []
        
        # Run multiple comparisons for statistical significance
        for run in range(runs_per_model):
            print(f"\nRun {run+1}/{runs_per_model}")
            
            try:
                # Run comparison
                comparison = compare_amr_approaches(
                    time_final=time_final,
                    max_level=max_level,
                    element_budget=element_budget,
                    model_path=model_path,
                    verbose=verbose
                )
                
                model_results.append(comparison)
                print(f"Run {run+1} completed successfully")
                
            except Exception as e:
                print(f"Error in run {run+1}: {e}")
                # Continue with next run
        
        if not model_results:
            print(f"No successful runs for model {model_name}, skipping")
            continue
        
        # Calculate average metrics
        avg_metrics = calculate_average_metrics(model_results)
        
        # Store results
        results['models'][model_name] = {
            'path': model_path,
            'runs': model_results,
            'average': avg_metrics
        }
    
    # Calculate overall summary
    if results['models']:
        summary = calculate_summary(results['models'])
        results['summary'] = summary
    
    # Save results to JSON
    results_path = os.path.join(output_dir, f"rl_performance_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    with open(results_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    # Generate plots
    generate_plots(results, output_dir)
    
    return results

def calculate_average_metrics(runs):
    """Calculate average metrics across multiple runs."""
    if not runs:
        return {}
    
    # Extract metrics
    trad_final_elements = [run['traditional']['final_elements'] for run in runs]
    trad_errors = [run['traditional']['error'] for run in runs]
    rl_final_elements = [run['rl_driven']['final_elements'] for run in runs]
    rl_errors = [run['rl_driven']['error'] for run in runs]
    efficiencies = [run['element_efficiency'] for run in runs]
    error_ratios = [run['error_ratio'] for run in runs]
    
    # Calculate averages
    avg_metrics = {
        'traditional': {
            'final_elements': {
                'avg': np.mean(trad_final_elements),
                'std': np.std(trad_final_elements),
                'min': np.min(trad_final_elements),
                'max': np.max(trad_final_elements)
            },
            'error': {
                'avg': np.mean(trad_errors),
                'std': np.std(trad_errors),
                'min': np.min(trad_errors),
                'max': np.max(trad_errors)
            }
        },
        'rl_driven': {
            'final_elements': {
                'avg': np.mean(rl_final_elements),
                'std': np.std(rl_final_elements),
                'min': np.min(rl_final_elements),
                'max': np.max(rl_final_elements)
            },
            'error': {
                'avg': np.mean(rl_errors),
                'std': np.std(rl_errors),
                'min': np.min(rl_errors),
                'max': np.max(rl_errors)
            }
        },
        'element_efficiency': {
            'avg': np.mean(efficiencies),
            'std': np.std(efficiencies),
            'min': np.min(efficiencies),
            'max': np.max(efficiencies)
        },
        'error_ratio': {
            'avg': np.mean(error_ratios),
            'std': np.std(error_ratios),
            'min': np.min(error_ratios),
            'max': np.max(error_ratios)
        }
    }
    
    return avg_metrics

def calculate_summary(models_results):
    """Calculate summary statistics across all models."""
    if not models_results:
        return {}
    
    # Extract metrics for all models
    element_efficiencies = []
    error_ratios = []
    
    for model_name, model_data in models_results.items():
        avg_metrics = model_data['average']
        element_efficiencies.append(avg_metrics['element_efficiency']['avg'])
        error_ratios.append(avg_metrics['error_ratio']['avg'])
    
    # Calculate summary statistics
    summary = {
        'element_efficiency': {
            'avg': np.mean(element_efficiencies),
            'std': np.std(element_efficiencies),
            'min': np.min(element_efficiencies),
            'max': np.max(element_efficiencies),
            'best_model': max(models_results.keys(), key=lambda k: models_results[k]['average']['element_efficiency']['avg'])
        },
        'error_ratio': {
            'avg': np.mean(error_ratios),
            'std': np.std(error_ratios),
            'min': np.min(error_ratios),
            'max': np.max(error_ratios),
            'best_model': max(models_results.keys(), key=lambda k: models_results[k]['average']['error_ratio']['avg'])
        }
    }
    
    return summary

def generate_plots(results, output_dir):
    """Generate comparison plots across models."""
    if not results['models']:
        print("No models to plot")
        return
    
    # Create plots directory
    plots_dir = os.path.join(output_dir, "plots")
    os.makedirs(plots_dir, exist_ok=True)
    
    # Extract model names and metrics
    model_names = list(results['models'].keys())
    element_efficiencies = [results['models'][model]['average']['element_efficiency']['avg'] for model in model_names]
    element_efficiencies_std = [results['models'][model]['average']['element_efficiency']['std'] for model in model_names]
    error_ratios = [results['models'][model]['average']['error_ratio']['avg'] for model in model_names]
    error_ratios_std = [results['models'][model]['average']['error_ratio']['std'] for model in model_names]
    
    # Sort by element efficiency
    sorted_indices = np.argsort(element_efficiencies)[::-1]  # descending
    sorted_model_names = [model_names[i] for i in sorted_indices]
    sorted_element_efficiencies = [element_efficiencies[i] for i in sorted_indices]
    sorted_element_efficiencies_std = [element_efficiencies_std[i] for i in sorted_indices]
    sorted_error_ratios = [error_ratios[i] for i in sorted_indices]
    sorted_error_ratios_std = [error_ratios_std[i] for i in sorted_indices]
    
    # Element efficiency plot
    plt.figure(figsize=(12, 8))
    bars = plt.bar(sorted_model_names, sorted_element_efficiencies, yerr=sorted_element_efficiencies_std,
            capsize=5, color='skyblue', alpha=0.8)
    plt.axhline(y=1.0, color='r', linestyle='--', label='Traditional AMR')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xlabel('Model')
    plt.ylabel('Element Efficiency (higher is better)')
    plt.title('RL Model Element Efficiency Comparison')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "element_efficiency_comparison.png"), dpi=300)
    plt.close()
    
    # Error ratio plot
    plt.figure(figsize=(12, 8))
    bars = plt.bar(sorted_model_names, sorted_error_ratios, yerr=sorted_error_ratios_std,
            capsize=5, color='lightgreen', alpha=0.8)
    plt.axhline(y=1.0, color='r', linestyle='--', label='Traditional AMR')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xlabel('Model')
    plt.ylabel('Error Ratio (Traditional/RL, higher is better)')
    plt.title('RL Model Error Ratio Comparison')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "error_ratio_comparison.png"), dpi=300)
    plt.close()
    
    # Element count vs. error plot (scatter)
    plt.figure(figsize=(10, 8))
    
    # Plot traditional AMR points
    trad_elements = [results['models'][model]['average']['traditional']['final_elements']['avg'] for model in model_names]
    trad_errors = [results['models'][model]['average']['traditional']['error']['avg'] for model in model_names]
    plt.scatter(trad_elements, trad_errors, color='blue', marker='o', label='Traditional AMR', alpha=0.7, s=100)
    
    # Plot RL-driven AMR points
    rl_elements = [results['models'][model]['average']['rl_driven']['final_elements']['avg'] for model in model_names]
    rl_errors = [results['models'][model]['average']['rl_driven']['error']['avg'] for model in model_names]
    
    # Create scatter plot with model names as annotations
    for i, model in enumerate(model_names):
        plt.scatter(rl_elements[i], rl_errors[i], color='red', marker='x', alpha=0.7, s=100)
        plt.annotate(model, (rl_elements[i], rl_errors[i]), fontsize=8, 
                    xytext=(5, 5), textcoords='offset points')
    
    # Connect traditional and RL points for each model with lines
    for i in range(len(model_names)):
        plt.plot([trad_elements[i], rl_elements[i]], [trad_errors[i], rl_errors[i]], 
                color='gray', linestyle='--', alpha=0.4)
    
    plt.grid(linestyle='--', alpha=0.7)
    plt.xlabel('Final Number of Elements')
    plt.ylabel('Solution Error')
    plt.title('Error vs. Element Count Comparison')
    plt.legend(['', 'Traditional AMR', 'RL-driven AMR'])
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "error_vs_elements.png"), dpi=300)
    plt.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Analyze RL model performance')
    parser.add_argument('--models_dir', type=str, required=True, 
                        help='Directory containing model files')
    parser.add_argument('--output_dir', type=str, default=os.path.join(PROJECT_ROOT, "rl_analysis"),
                        help='Directory to save analysis results')
    parser.add_argument('--runs_per_model', type=int, default=3,
                        help='Number of runs per model')
    parser.add_argument('--time_final', type=float, default=0.2,
                        help='Final simulation time')
    parser.add_argument('--max_level', type=int, default=4,
                        help='Maximum refinement level')
    parser.add_argument('--element_budget', type=int, default=40,
                        help='Maximum allowed elements')
    parser.add_argument('--verbose', action='store_true',
                        help='Print detailed logs')
    args = parser.parse_args()
    
    # Verify models directory exists
    if not os.path.exists(args.models_dir):
        print(f"Error: Models directory '{args.models_dir}' does not exist.")
        sys.exit(1)
    
    # Run analysis
    results = run_analysis(
        args.models_dir,
        args.output_dir,
        runs_per_model=args.runs_per_model,
        time_final=args.time_final,
        max_level=args.max_level,
        element_budget=args.element_budget,
        verbose=args.verbose
    )
    
    # Print summary
    if results and 'summary' in results:
        print("\n--- Analysis Summary ---")
        print(f"Best model for element efficiency: {results['summary']['element_efficiency']['best_model']}")
        print(f"Average element efficiency: {results['summary']['element_efficiency']['avg']:.2f}x")
        print(f"Best model for error ratio: {results['summary']['error_ratio']['best_model']}")
        print(f"Average error ratio: {results['summary']['error_ratio']['avg']:.2f}x")
    else:
        print("No analysis results to display")