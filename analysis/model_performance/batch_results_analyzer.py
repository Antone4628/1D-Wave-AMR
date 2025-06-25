"""
Batch Results Analyzer for AMR Parameter Family Visualization

This script processes batch evaluation results to create parameter family plots
showing accuracy vs cost tradeoffs across the 4-dimensional parameter space.

Usage:
    python batch_results_analyzer.py session3_100k_uniform --plot-families all --output-format pdf --verbose
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys
import argparse
import json
from pathlib import Path
from datetime import datetime

# Get absolute path to project root
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 
    '..',
    '..'
))
sys.path.append(PROJECT_ROOT)

class BatchResultsAnalyzer:
    """
    Analyzer for creating parameter family visualizations from batch model evaluation results.
    """
    
    def __init__(self, sweep_name, input_file=None, verbose=False):
        """
        Initialize the analyzer with batch results data.
        
        Args:
            sweep_name (str): Name of the sweep (e.g., 'session3_100k_uniform')
            verbose (bool): Whether to print detailed logs
        """
        self.sweep_name = sweep_name
        self.verbose = verbose
        
        # Set up paths
        self.results_dir = os.path.join(PROJECT_ROOT, 'analysis', 'data', 'model_performance', sweep_name)

        # Determine CSV file path with auto-detection
        if input_file:
            self.csv_path = os.path.join(self.results_dir, input_file)
        else:
            # Auto-detect: look for model_results_*.csv first
            import glob
            model_results_files = glob.glob(os.path.join(self.results_dir, "model_results_*.csv"))
            if model_results_files:
                self.csv_path = model_results_files[0]  # Use first match
            else:
                # Fallback to old naming convention
                self.csv_path = os.path.join(self.results_dir, "batch_results_all_models.csv")
        
        self.json_dir = os.path.join(self.results_dir, 'individual_results')
        self.output_dir = os.path.join(self.results_dir, 'parameter_family_analysis')
        
        # Create output directory
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Load data
        self.df = self._load_and_validate_data()
        
        # Define parameter families
        self.parameter_families = {
            'gamma_c': {
                'vary_param': 'gamma_c',
                'fixed_params': ['step_domain_fraction', 'rl_iterations_per_timestep', 'element_budget'],
                'values': sorted(self.df['gamma_c'].unique()),
                'title': 'Gamma_c Family (Reward Scaling)',
                'colors': ['#1f77b4', '#ff7f0e', '#2ca02c']  # Blue, Orange, Green
            },
            'step_domain_fraction': {
                'vary_param': 'step_domain_fraction', 
                'fixed_params': ['gamma_c', 'rl_iterations_per_timestep', 'element_budget'],
                'values': sorted(self.df['step_domain_fraction'].unique()),
                'title': 'Step Domain Fraction Family (Wave Propagation)',
                'colors': ['#d62728', '#9467bd', '#8c564b']  # Red, Purple, Brown
            },
            'rl_iterations_per_timestep': {
                'vary_param': 'rl_iterations_per_timestep',
                'fixed_params': ['gamma_c', 'step_domain_fraction', 'element_budget'], 
                'values': sorted(self.df['rl_iterations_per_timestep'].unique()),
                'title': 'RL Iterations Family (Adaptation Frequency)',
                'colors': ['#e377c2', '#7f7f7f', '#bcbd22']  # Pink, Gray, Olive
            },
            'element_budget': {
                'vary_param': 'element_budget',
                'fixed_params': ['gamma_c', 'step_domain_fraction', 'rl_iterations_per_timestep'],
                'values': sorted(self.df['element_budget'].unique()),
                'title': 'Element Budget Family (Resource Constraint)', 
                'colors': ['#17becf', '#ff7f0e', '#2ca02c']  # Cyan, Orange, Green
            }
        }
        
        if self.verbose:
            print(f"Loaded {len(self.df)} model results")
            print(f"Parameter ranges:")
            for param, family in self.parameter_families.items():
                print(f"  {param}: {family['values']}")
    
    def _load_and_validate_data(self):
        """Load and validate the CSV data."""
        if not os.path.exists(self.csv_path):
            raise FileNotFoundError(f"Batch results CSV not found: {self.csv_path}")
        
        df = pd.read_csv(self.csv_path)
        
        # Validate required columns
        required_cols = ['gamma_c', 'step_domain_fraction', 'rl_iterations_per_timestep', 
                        'element_budget', 'final_l2_error', 'total_cost']
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
        
        # Validate data ranges
        if df['final_l2_error'].min() <= 0:
            raise ValueError("L2 errors must be positive for log scaling")
        
        if self.verbose:
            print(f"Data validation successful")
            print(f"L2 error range: {df['final_l2_error'].min():.2e} to {df['final_l2_error'].max():.2e}")
            print(f"Total cost range: {df['total_cost'].min():,} to {df['total_cost'].max():,}")
        
        return df
    
    def create_parameter_family_plots(self, families='all', output_format='pdf', include_pareto=True):
        """
        Create parameter family scatter plots.
        
        Args:
            families (str or list): 'all' or list of family names to plot
            output_format (str): Output format ('pdf', 'png', or 'both')
            include_pareto (bool): Whether to include Pareto front analysis
        """
        if families == 'all':
            families_to_plot = list(self.parameter_families.keys())
        else:
            families_to_plot = families if isinstance(families, list) else [families]
        
        # Perform Pareto analysis if requested
        pareto_results = None
        if include_pareto:
            pareto_results = self.identify_pareto_optimal_models()
        
        # Create individual family plots
        for family_name in families_to_plot:
            self._create_single_family_plot(family_name, output_format, pareto_results)
        
        # Create combined plot
        self._create_combined_family_plot(families_to_plot, output_format, pareto_results)
        
        if self.verbose:
            print(f"Created {len(families_to_plot)} individual plots + 1 combined plot")
            if include_pareto:
                print(f"Pareto front analysis included in all plots")
    
    def _create_single_family_plot(self, family_name, output_format, pareto_results=None):
        """Create a scatter plot for a single parameter family."""
        family = self.parameter_families[family_name]
        
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Plot each parameter value with different color/symbol
        for i, param_value in enumerate(family['values']):
            # Filter data for this parameter value
            mask = self.df[family['vary_param']] == param_value
            subset = self.df[mask]
            
            ax.scatter(subset['total_cost'], subset['final_l2_error'],
                      c=family['colors'][i], s=60, alpha=0.7,
                      label=f"{family['vary_param']}={param_value}",
                      edgecolors='black', linewidths=0.5)
        
        # Overlay Pareto front if available
        if pareto_results is not None:
            pareto_df = pd.DataFrame(pareto_results['pareto_models'])
            ax.scatter(pareto_df['total_cost'], pareto_df['final_l2_error'],
                      c='red', s=100, alpha=0.9, marker='*',
                      label=f"Pareto Optimal (N={len(pareto_df)})",
                      edgecolors='darkred', linewidths=1.5, zorder=5)
            
            # Connect Pareto points with lines
            pareto_sorted = pareto_df.sort_values('total_cost')
            ax.plot(pareto_sorted['total_cost'], pareto_sorted['final_l2_error'],
                   'r--', alpha=0.7, linewidth=2, zorder=4)
        
        # Formatting
        ax.set_xlabel('Total Computational Cost', fontsize=12, fontweight='bold')
        ax.set_ylabel('Final L2 Error', fontsize=12, fontweight='bold')
        ax.set_yscale('log')
        ax.grid(True, alpha=0.3)
        ax.legend(fontsize=10, framealpha=0.9)
        
        # Title with data statistics
        n_models = len(self.df[self.df[family['vary_param']].isin(family['values'])])
        title = f"{family['title']}\n"
        title += f"N={n_models} models, {len(family['values'])} parameter values"
        if pareto_results:
            title += f", {pareto_results['pareto_optimal_count']} Pareto-optimal"
        ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
        
        # Tight layout
        plt.tight_layout()
        
        # Save plot
        filename_base = f"{family_name}_family_accuracy_vs_cost"
        self._save_plot(fig, filename_base, output_format)
        plt.close()
    
    def _create_combined_family_plot(self, families_to_plot, output_format, pareto_results=None):
        """Create a combined plot showing all parameter families."""
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        axes = axes.flatten()
        
        for idx, family_name in enumerate(families_to_plot[:4]):  # Limit to 4 families
            family = self.parameter_families[family_name]
            ax = axes[idx]
            
            # Plot each parameter value
            for i, param_value in enumerate(family['values']):
                mask = self.df[family['vary_param']] == param_value
                subset = self.df[mask]
                
                ax.scatter(subset['total_cost'], subset['final_l2_error'],
                          c=family['colors'][i], s=40, alpha=0.7,
                          label=f"{param_value}",
                          edgecolors='black', linewidths=0.3)
            
            # Add Pareto front if available
            if pareto_results is not None:
                pareto_df = pd.DataFrame(pareto_results['pareto_models'])
                ax.scatter(pareto_df['total_cost'], pareto_df['final_l2_error'],
                          c='red', s=60, alpha=0.9, marker='*',
                          label='Pareto', edgecolors='darkred', linewidths=1, zorder=5)
                
                # Connect Pareto points
                pareto_sorted = pareto_df.sort_values('total_cost')
                ax.plot(pareto_sorted['total_cost'], pareto_sorted['final_l2_error'],
                       'r--', alpha=0.7, linewidth=1.5, zorder=4)
            
            # Formatting for subplot
            ax.set_xlabel('Total Cost', fontsize=10)
            ax.set_ylabel('L2 Error', fontsize=10)
            ax.set_yscale('log')
            ax.grid(True, alpha=0.3)
            ax.legend(fontsize=8, title=family['vary_param'], title_fontsize=9)
            ax.set_title(family['title'], fontsize=11, fontweight='bold')
        
        # Overall title
        title = f'Parameter Family Analysis: {self.sweep_name}\n'
        title += f'Accuracy vs Cost Across 4-D Parameter Space'
        if pareto_results:
            title += f' (Pareto Front: {pareto_results["pareto_optimal_count"]} models)'
        fig.suptitle(title, fontsize=16, fontweight='bold')
        
        plt.tight_layout()
        
        # Save combined plot
        filename_base = "combined_families_accuracy_vs_cost"
        self._save_plot(fig, filename_base, output_format)
        plt.close()
    
    def identify_best_models(self, criteria='balanced', top_n=10):
        """
        Identify best performing models based on different criteria.
        
        Args:
            criteria (str): 'accuracy', 'efficiency', or 'balanced'
            top_n (int): Number of top models to return
            
        Returns:
            dict: Analysis results with best models
        """
        df = self.df.copy()
        
        if criteria == 'accuracy':
            # Best accuracy (lowest L2 error)
            df = df.nsmallest(top_n, 'final_l2_error')
            ranking_metric = 'final_l2_error'
        elif criteria == 'efficiency':
            # Best efficiency (lowest cost)
            df = df.nsmallest(top_n, 'total_cost')
            ranking_metric = 'total_cost'
        elif criteria == 'balanced':
            # Balanced: normalize both metrics and find best combined score
            df['norm_error'] = (df['final_l2_error'] - df['final_l2_error'].min()) / (df['final_l2_error'].max() - df['final_l2_error'].min())
            df['norm_cost'] = (df['total_cost'] - df['total_cost'].min()) / (df['total_cost'].max() - df['total_cost'].min())
            df['combined_score'] = df['norm_error'] + df['norm_cost']  # Lower is better
            df = df.nsmallest(top_n, 'combined_score')
            ranking_metric = 'combined_score'
        
        results = {
            'criteria': criteria,
            'ranking_metric': ranking_metric,
            'top_models': []
        }
        
        for idx, row in df.iterrows():
            model_info = {
                'rank': len(results['top_models']) + 1,
                'gamma_c': row['gamma_c'],
                'step_domain_fraction': row['step_domain_fraction'],
                'rl_iterations_per_timestep': row['rl_iterations_per_timestep'],
                'element_budget': row['element_budget'],
                'final_l2_error': row['final_l2_error'],
                'total_cost': row['total_cost'],
                'model_path': row['model_path']
            }
            
            if criteria == 'balanced':
                model_info['combined_score'] = row['combined_score']
            
            results['top_models'].append(model_info)
        
        # Save results
        results_path = os.path.join(self.output_dir, f'best_models_{criteria}.json')
        with open(results_path, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        
        if self.verbose:
            print(f"\nTop {top_n} models by {criteria}:")
            for model in results['top_models'][:5]:  # Show top 5
                print(f"  Rank {model['rank']}: γ={model['gamma_c']}, step={model['step_domain_fraction']}, "
                     f"rl={model['rl_iterations_per_timestep']}, budget={model['element_budget']} "
                     f"→ L2={model['final_l2_error']:.2e}, Cost={model['total_cost']:,}")
        
        return results
    
    def identify_pareto_optimal_models(self):
        """
        Identify Pareto-optimal models (non-dominated solutions).
        
        A model is Pareto-optimal if no other model is both more accurate 
        (lower L2 error) AND more efficient (lower cost).
        
        Returns:
            dict: Analysis results with Pareto-optimal models
        """
        df = self.df.copy()
        pareto_models = []
        
        if self.verbose:
            print("Identifying Pareto-optimal models...")
        
        for idx, row in df.iterrows():
            # Check if this model is dominated by any other model
            is_dominated = False
            
            for _, other_row in df.iterrows():
                # Other model dominates if it's both more accurate AND more efficient
                # (allowing for ties in one dimension)
                if (other_row['final_l2_error'] <= row['final_l2_error'] and 
                    other_row['total_cost'] <= row['total_cost'] and
                    (other_row['final_l2_error'] < row['final_l2_error'] or 
                     other_row['total_cost'] < row['total_cost'])):
                    is_dominated = True
                    break
            
            if not is_dominated:
                pareto_models.append({
                    'gamma_c': row['gamma_c'],
                    'step_domain_fraction': row['step_domain_fraction'],
                    'rl_iterations_per_timestep': row['rl_iterations_per_timestep'],
                    'element_budget': row['element_budget'],
                    'final_l2_error': row['final_l2_error'],
                    'total_cost': row['total_cost'],
                    'final_elements': row['final_elements'],
                    'total_adaptations': row['total_adaptations'],
                    'model_path': row['model_path']
                })
        
        # Sort Pareto models by cost (for better visualization)
        pareto_models.sort(key=lambda x: x['total_cost'])
        
        results = {
            'analysis_type': 'pareto_optimal',
            'total_models_evaluated': len(df),
            'pareto_optimal_count': len(pareto_models),
            'pareto_percentage': (len(pareto_models) / len(df)) * 100,
            'pareto_models': pareto_models,
            'analysis_timestamp': datetime.now().isoformat()
        }
        
        # Save results
        results_path = os.path.join(self.output_dir, 'pareto_optimal_models.json')
        with open(results_path, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        
        if self.verbose:
            print(f"Found {len(pareto_models)} Pareto-optimal models ({len(pareto_models)/len(df)*100:.1f}% of total)")
            print("Pareto front (sorted by cost):")
            for i, model in enumerate(pareto_models[:10]):  # Show first 10
                print(f"  {i+1}: γ={model['gamma_c']}, step={model['step_domain_fraction']}, "
                     f"rl={model['rl_iterations_per_timestep']}, budget={model['element_budget']} "
                     f"→ L2={model['final_l2_error']:.2e}, Cost={model['total_cost']:,}")
            if len(pareto_models) > 10:
                print(f"  ... and {len(pareto_models)-10} more")
        
        return results
    
    def _save_plot(self, fig, filename_base, output_format):
        """Save plot in specified format(s)."""
        if output_format in ['pdf', 'both']:
            pdf_path = os.path.join(self.output_dir, f"{filename_base}.pdf")
            fig.savefig(pdf_path, format='pdf', dpi=300, bbox_inches='tight')
            if self.verbose:
                print(f"Saved: {pdf_path}")
        
        if output_format in ['png', 'both']:
            png_path = os.path.join(self.output_dir, f"{filename_base}.png")
            fig.savefig(png_path, format='png', dpi=300, bbox_inches='tight')
            if self.verbose:
                print(f"Saved: {png_path}")
    
    def generate_summary_report(self):
        """Generate a comprehensive summary report."""
        # Calculate summary statistics
        stats = {
            'total_models': len(self.df),
            'parameter_ranges': {},
            'performance_stats': {
                'l2_error': {
                    'min': float(self.df['final_l2_error'].min()),
                    'max': float(self.df['final_l2_error'].max()),
                    'mean': float(self.df['final_l2_error'].mean()),
                    'std': float(self.df['final_l2_error'].std())
                },
                'total_cost': {
                    'min': int(self.df['total_cost'].min()),
                    'max': int(self.df['total_cost'].max()),
                    'mean': float(self.df['total_cost'].mean()),
                    'std': float(self.df['total_cost'].std())
                }
            },
            'analysis_timestamp': datetime.now().isoformat()
        }
        
        # Parameter ranges
        for param in ['gamma_c', 'step_domain_fraction', 'rl_iterations_per_timestep', 'element_budget']:
            stats['parameter_ranges'][param] = sorted(self.df[param].unique().tolist())
        
        # Save summary
        summary_path = os.path.join(self.output_dir, 'analysis_summary.json')
        with open(summary_path, 'w') as f:
            json.dump(stats, f, indent=2)
        
        if self.verbose:
            print(f"Generated summary report: {summary_path}")
        
        return stats

def main():
    """Main function with argument parsing for command line usage"""
    parser = argparse.ArgumentParser(description='Analyze batch model evaluation results for parameter families')
    
    # Required arguments
    parser.add_argument('sweep_name', help='Name of the sweep (e.g., session3_100k_uniform)')
    parser.add_argument('--input-file', help='Specify input CSV file (e.g., model_results_ref0_budget50.csv). If not provided, auto-detects model_results_*.csv or falls back to batch_results_all_models.csv')
    
    # Plot options
    parser.add_argument('--plot-families', default='all', 
                       help='Families to plot: all, or comma-separated list (gamma_c,step_domain_fraction,rl_iterations_per_timestep,element_budget)')
    parser.add_argument('--output-format', choices=['pdf', 'png', 'both'], default='pdf',
                       help='Output format for plots')
    
    # Analysis options
    parser.add_argument('--best-models', type=int, default=10,
                       help='Number of best models to identify')
    parser.add_argument('--criteria', choices=['accuracy', 'efficiency', 'balanced'], default='balanced',
                       help='Criteria for best model identification')
    parser.add_argument('--include-pareto', action='store_true', default=True,
                       help='Include Pareto front analysis (default: True)')
    parser.add_argument('--no-pareto', action='store_true',
                       help='Disable Pareto front analysis')
    parser.add_argument('--statistical-integration', action='store_true',
                       help='Integrate with existing ANOVA results (if available)')
    
    # Output options
    parser.add_argument('--verbose', action='store_true', help='Print detailed logs')
    
    args = parser.parse_args()
    
    # Parse families argument
    if args.plot_families != 'all':
        families = [f.strip() for f in args.plot_families.split(',')]
    else:
        families = 'all'
    
    # Determine Pareto analysis setting
    include_pareto = args.include_pareto and not args.no_pareto
    
    # Create analyzer
    analyzer = BatchResultsAnalyzer(args.sweep_name, input_file=args.input_file, verbose=args.verbose)
    
    
    # Generate plots (with or without Pareto)
    analyzer.create_parameter_family_plots(families=families, 
                                         output_format=args.output_format,
                                         include_pareto=include_pareto)
    
    # Identify best models using traditional criteria
    analyzer.identify_best_models(criteria=args.criteria, top_n=args.best_models)
    
    # Generate summary report
    analyzer.generate_summary_report()
    
    print(f"\n=== PARAMETER FAMILY ANALYSIS COMPLETE ===")
    print(f"Results saved to: {analyzer.output_dir}")
    if include_pareto:
        print(f"Pareto front analysis included")

if __name__ == "__main__":
    main()