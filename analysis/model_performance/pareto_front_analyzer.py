"""
Pareto Front Parameter Analysis

This script provides detailed analysis of which parameter combinations
dominate the Pareto front and quantifies parameter effects.

Usage:
    python pareto_front_analyzer.py session3_100k_uniform
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import os
import sys
from collections import Counter
import argparse

# Add project root to path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(PROJECT_ROOT)

def analyze_pareto_front(sweep_name, input_file=None):
    """Detailed analysis of Pareto front parameter distributions."""
    

    # Load data
    results_dir = os.path.join(PROJECT_ROOT, 'analysis', 'data', 'model_performance', sweep_name)

    # Determine CSV file path with auto-detection
    if input_file:
        csv_path = os.path.join(results_dir, input_file)
    else:
        # Auto-detect: look for model_results_*.csv first
        import glob
        model_results_files = glob.glob(os.path.join(results_dir, "model_results_*.csv"))
        if model_results_files:
            csv_path = model_results_files[0]  # Use first match
        else:
            # Fallback to old naming convention
            csv_path = os.path.join(results_dir, "batch_results_all_models.csv")
    pareto_path = os.path.join(results_dir, 'parameter_family_analysis', 'pareto_optimal_models.json')
    
    df_all = pd.read_csv(csv_path)
    
    with open(pareto_path, 'r') as f:
        pareto_data = json.load(f)
    
    df_pareto = pd.DataFrame(pareto_data['pareto_models'])
    
    print(f"=== PARETO FRONT ANALYSIS ===")
    print(f"Total models: {len(df_all)}")
    print(f"Pareto optimal: {len(df_pareto)} ({len(df_pareto)/len(df_all)*100:.1f}%)")
    print()
    
    # Parameter distributions on Pareto front
    print("=== PARAMETER DISTRIBUTIONS ON PARETO FRONT ===")
    
    params = ['gamma_c', 'step_domain_fraction', 'rl_iterations_per_timestep', 'element_budget']
    
    for param in params:
        print(f"\n{param}:")
        
        # Overall distribution
        overall_dist = df_all[param].value_counts().sort_index()
        pareto_dist = df_pareto[param].value_counts().sort_index()
        
        print("  Value | Overall | Pareto | Pareto%")
        print("  ------|---------|--------|--------")
        
        for value in sorted(df_all[param].unique()):
            overall_count = overall_dist.get(value, 0)
            pareto_count = pareto_dist.get(value, 0)
            pareto_pct = (pareto_count / pareto_dist.sum() * 100) if pareto_dist.sum() > 0 else 0
            overall_pct = (overall_count / overall_dist.sum() * 100)
            
            print(f"  {value:5} | {overall_count:7} | {pareto_count:6} | {pareto_pct:6.1f}%")
    
    # Performance ranges
    print(f"\n=== PERFORMANCE RANGES ===")
    print(f"All models:")
    print(f"  L2 Error: {df_all['final_l2_error'].min():.2e} to {df_all['final_l2_error'].max():.2e}")
    print(f"  Cost:     {df_all['total_cost'].min():,} to {df_all['total_cost'].max():,}")
    
    print(f"\nPareto front:")
    print(f"  L2 Error: {df_pareto['final_l2_error'].min():.2e} to {df_pareto['final_l2_error'].max():.2e}")
    print(f"  Cost:     {df_pareto['total_cost'].min():,} to {df_pareto['total_cost'].max():,}")
    
    # Pareto front segments
    print(f"\n=== PARETO FRONT SEGMENTS ===")
    df_pareto_sorted = df_pareto.sort_values('total_cost')
    
    print("Rank | Cost   | L2 Error | γ_c | step | rl | budget")
    print("-----|--------|----------|-----|------|----|---------")
    for i, (_, row) in enumerate(df_pareto_sorted.iterrows()):
        print(f"{i+1:4} | {row['total_cost']:6.0f} | {row['final_l2_error']:.2e} | "
              f"{row['gamma_c']:3.0f} | {row['step_domain_fraction']:4.3f} | "
              f"{row['rl_iterations_per_timestep']:2.0f} | {row['element_budget']:2.0f}")
    
    # Key insights
    print(f"\n=== KEY INSIGHTS ===")
    
    # Gamma_c dominance
    gamma_dist = df_pareto['gamma_c'].value_counts()
    dominant_gamma = gamma_dist.index[0]
    print(f"1. γ_c = {dominant_gamma} dominates Pareto front ({gamma_dist.iloc[0]}/{len(df_pareto)} models)")
    
    # Cost-accuracy regions
    low_cost = df_pareto_sorted.iloc[:5]  # 5 lowest cost
    high_acc = df_pareto_sorted.iloc[-5:]  # 5 highest accuracy (lowest error)
    
    print(f"\n2. Low-cost region (5 cheapest Pareto models):")
    print(f"   Avg cost: {low_cost['total_cost'].mean():,.0f}")
    print(f"   Avg error: {low_cost['final_l2_error'].mean():.2e}")
    print(f"   Common γ_c: {low_cost['gamma_c'].mode().iloc[0]}")
    
    print(f"\n3. High-accuracy region (5 most accurate Pareto models):")
    print(f"   Avg cost: {high_acc['total_cost'].mean():,.0f}")
    print(f"   Avg error: {high_acc['final_l2_error'].mean():.2e}")
    print(f"   Common γ_c: {high_acc['gamma_c'].mode().iloc[0]}")
    
    return df_all, df_pareto

def create_focused_plots(sweep_name, df_all, df_pareto):
    """Create more focused parameter analysis plots."""
    
    results_dir = os.path.join(PROJECT_ROOT, 'analysis', 'data', 'model_performance', sweep_name)
    output_dir = os.path.join(results_dir, 'parameter_family_analysis')
    
    # 1. Pareto-only parameter analysis
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes = axes.flatten()
    
    params = ['gamma_c', 'step_domain_fraction', 'rl_iterations_per_timestep', 'element_budget']
    param_names = ['Gamma_c (Reward Scaling)', 'Step Domain Fraction', 'RL Iterations/Timestep', 'Element Budget']
    
    for i, (param, name) in enumerate(zip(params, param_names)):
        ax = axes[i]
        
        # Group Pareto models by parameter value
        for value in sorted(df_pareto[param].unique()):
            subset = df_pareto[df_pareto[param] == value]
            ax.scatter(subset['total_cost'], subset['final_l2_error'], 
                      s=100, alpha=0.8, label=f'{param}={value}')
        
        # Connect Pareto front
        df_sorted = df_pareto.sort_values('total_cost')
        ax.plot(df_sorted['total_cost'], df_sorted['final_l2_error'], 
               'r--', alpha=0.5, linewidth=2, zorder=1)
        
        ax.set_xlabel('Total Cost')
        ax.set_ylabel('L2 Error')
        ax.set_yscale('log')
        ax.grid(True, alpha=0.3)
        ax.legend(fontsize=8)
        ax.set_title(f'{name} on Pareto Front', fontweight='bold')
    
    plt.suptitle(f'Pareto Front Parameter Analysis: {sweep_name}', fontsize=14, fontweight='bold')
    plt.tight_layout()
    
    # Save
    pareto_plot_path = os.path.join(output_dir, 'pareto_front_parameter_analysis.pdf')
    plt.savefig(pareto_plot_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    # 2. Parameter value histograms
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    axes = axes.flatten()
    
    for i, (param, name) in enumerate(zip(params, param_names)):
        ax = axes[i]
        
        # Overall distribution
        overall_counts = df_all[param].value_counts().sort_index()
        pareto_counts = df_pareto[param].value_counts().sort_index()
        
        x_pos = np.arange(len(overall_counts))
        width = 0.35
        
        ax.bar(x_pos - width/2, overall_counts.values, width, 
               label='All Models', alpha=0.7, color='lightblue')
        ax.bar(x_pos + width/2, [pareto_counts.get(val, 0) for val in overall_counts.index], 
               width, label='Pareto Optimal', alpha=0.9, color='red')
        
        ax.set_xlabel(param)
        ax.set_ylabel('Count')
        ax.set_title(f'{name} Distribution', fontweight='bold')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(overall_counts.index)
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
    
    plt.suptitle(f'Parameter Distribution: All vs Pareto Optimal', fontsize=14, fontweight='bold')
    plt.tight_layout()
    
    # Save
    hist_plot_path = os.path.join(output_dir, 'parameter_distribution_comparison.pdf')
    plt.savefig(hist_plot_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\nFocused plots saved:")
    print(f"  {pareto_plot_path}")
    print(f"  {hist_plot_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Analyze Pareto front parameter distributions')
    parser.add_argument('sweep_name', help='Name of the parameter sweep to analyze')
    parser.add_argument('--input-file', help='Specify input CSV file (e.g., model_results_ref0_budget50.csv). If not provided, auto-detects model_results_*.csv or falls back to batch_results_all_models.csv')
    
    args = parser.parse_args()
    
    df_all, df_pareto = analyze_pareto_front(args.sweep_name, input_file=args.input_file)
    create_focused_plots(args.sweep_name, df_all, df_pareto)