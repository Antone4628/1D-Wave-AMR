#!/usr/bin/env python3
"""
Key Models Analyzer for DRL-AMR Aggregate Results

Analyzes the three key model types (lowest_cost, lowest_l2, optimal_neutral) across 
16 simulation configurations to identify patterns, trade-offs, and parameter relationships.

Core Visualizations:
1. Performance Heatmaps (4x4): Shows L2 error, cost, and training params across simulation configs
2. Parameter Distributions: Box plots of training parameter patterns across model types  
3. Performance Trade-offs: 2D scatters showing cost vs accuracy relationships

Usage:
    python key_models_analyzer.py session3_100k_uniform --visualizations all --output-format png --verbose
    python key_models_analyzer.py session3_100k_uniform --visualizations heatmaps,distributions --output-format pdf
"""

import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
from pathlib import Path

# Get absolute path to project root
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 
    '..',
    '..'
))
sys.path.append(PROJECT_ROOT)

class KeyModelsAnalyzer:
    """Analyzer for key models across simulation configurations."""
    
    def __init__(self, sweep_name, output_subdir="uniform_initial_max", output_format='png', verbose=True):
        """
        Initialize analyzer.
        
        Args:
            sweep_name (str): Parameter sweep name (e.g., 'session3_100k_uniform')
            output_subdir (str): Subdirectory name for analysis type
            output_format (str): Output format ('png' or 'pdf')
            verbose (bool): Whether to print detailed progress
        """
        self.sweep_name = sweep_name
        self.output_subdir = output_subdir
        self.output_format = output_format
        self.verbose = verbose
        
        # Set up paths
        self.data_dir = os.path.join(PROJECT_ROOT, 'analysis', 'data', 'model_performance', sweep_name)
        self.aggregate_dir = os.path.join(self.data_dir, 'aggregate_results')
        self.output_dir = os.path.join(self.aggregate_dir, 'aggregate_analysis', output_subdir)
        
        # Create output directory
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Load data
        self.load_data()
        
        # Set up plotting style
        self.setup_plotting_style()
        
        if self.verbose:
            print(f"🔍 Key Models Analyzer initialized")
            print(f"   Sweep: {sweep_name}")
            print(f"   Output: {self.output_dir}")
            print(f"   Data shapes: {[len(df) for df in self.datasets.values()]} configs each")
    
    def load_data(self):
        """Load the three cleaned CSV files."""
        csv_files = {
            'lowest_cost': 'lowest_cost_models_cleaned.csv',
            'lowest_l2': 'lowest_l2_models_cleaned.csv', 
            'optimal_neutral': 'optimal_neutral_models_cleaned.csv'
        }
        
        self.datasets = {}
        for model_type, filename in csv_files.items():
            filepath = os.path.join(self.aggregate_dir, filename)
            if not os.path.exists(filepath):
                raise FileNotFoundError(f"Required file not found: {filepath}")
            
            df = pd.read_csv(filepath)
            
            # Validate expected structure (16 configs)
            if len(df) != 16:
                print(f"⚠️ Warning: Expected 16 configs, found {len(df)} in {filename}")
            
            self.datasets[model_type] = df
            
        if self.verbose:
            print(f"✅ Loaded {len(self.datasets)} datasets successfully")
    
    def setup_plotting_style(self):
        """Set up consistent plotting style."""
        plt.style.use('default')
        sns.set_palette("husl")
        
        # Configure matplotlib for consistent output
        plt.rcParams.update({
            'figure.figsize': (12, 8),
            'font.size': 10,
            'axes.titlesize': 12,
            'axes.labelsize': 10,
            'xtick.labelsize': 9,
            'ytick.labelsize': 9,
            'legend.fontsize': 9,
            'figure.titlesize': 14
        })
    
    def extract_simulation_config(self, config_id):
        """
        Extract initial_refinement and element_budget from config_id.
        
        Args:
            config_id (str): e.g., 'ref4_budget50_max4'
            
        Returns:
            tuple: (initial_refinement, element_budget)
        """
        import re
        match = re.match(r'ref(\d+)_budget(\d+)_max\d+', config_id)
        if match:
            return int(match.group(1)), int(match.group(2))
        else:
            raise ValueError(f"Cannot parse config_id: {config_id}")
    
    def create_performance_heatmaps(self):
        """Create 4x4 heatmaps showing performance across simulation configurations."""
        if self.verbose:
            print("📊 Creating performance heatmaps...")
        
        # Define unique refinement levels and budgets
        refinement_levels = sorted([4, 5, 6, 7])
        element_budgets = sorted([50, 80, 100, 150])
        
        # Color schemes for each model type
        color_schemes = {
            'lowest_cost': 'Blues',
            'lowest_l2': 'Reds', 
            'optimal_neutral': 'Greens'
        }
        
        for model_type, df in self.datasets.items():
            fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
            axes = [ax1, ax2, ax3, ax4]
            metrics = ['final_l2_error', 'total_cost', 'gamma_c', 'step_domain_fraction']
            titles = ['L2 Error', 'Total Cost', 'Gamma C', 'Step Domain Fraction']
            
            for idx, (metric, title, ax) in enumerate(zip(metrics, titles, axes)):
                # Create 4x4 matrix for heatmap
                heatmap_data = np.full((len(refinement_levels), len(element_budgets)), np.nan)
                annotations = np.full((len(refinement_levels), len(element_budgets)), '', dtype=object)
                
                for _, row in df.iterrows():
                    ref_level, budget = self.extract_simulation_config(row['config_id'])
                    
                    # Find position in matrix
                    ref_idx = refinement_levels.index(ref_level)
                    budget_idx = element_budgets.index(budget)
                    
                    # Set value and annotation
                    value = row[metric]
                    heatmap_data[ref_idx, budget_idx] = value
                    
                    # Format annotation based on metric
                    if metric == 'final_l2_error':
                        annotations[ref_idx, budget_idx] = f'{value:.1e}'
                    elif metric == 'total_cost':
                        annotations[ref_idx, budget_idx] = f'{int(value):,}'
                    else:
                        annotations[ref_idx, budget_idx] = f'{value:.3f}'
                
                # Create heatmap
                sns.heatmap(heatmap_data, 
                           annot=annotations, 
                           fmt='s',
                           cmap=color_schemes[model_type], 
                           xticklabels=[f'Budget {b}' for b in element_budgets],
                           yticklabels=[f'Ref {r}' for r in refinement_levels],
                           ax=ax,
                           cbar_kws={'label': title})
                
                ax.set_title(f'{title}', fontweight='bold')
                ax.set_xlabel('Element Budget')
                ax.set_ylabel('Initial Refinement Level')
            
            plt.suptitle(f'Performance Heatmaps: {model_type.replace("_", " ").title()} Models', 
                        fontsize=16, fontweight='bold')
            plt.tight_layout()
            
            # Save plot
            filename = f'performance_heatmaps_{model_type}.{self.output_format}'
            filepath = os.path.join(self.output_dir, filename)
            plt.savefig(filepath, dpi=300, bbox_inches='tight')
            
            if self.verbose:
                print(f"   Saved: {filename}")
            
            plt.close()
    
    def analyze_parameter_distributions(self):
        """Analyze training parameter distributions across model types."""
        if self.verbose:
            print("📈 Analyzing parameter distributions...")
        
        # Combine all datasets with model type labels
        combined_data = []
        for model_type, df in self.datasets.items():
            df_copy = df.copy()
            df_copy['model_type'] = model_type.replace('_', ' ').title()
            combined_data.append(df_copy)
        
        combined_df = pd.concat(combined_data, ignore_index=True)
        
        # Training parameters to analyze
        training_params = ['gamma_c', 'step_domain_fraction', 'rl_iterations_per_timestep', 'element_budget']
        param_labels = ['Gamma C', 'Step Domain Fraction', 'RL Iterations per Timestep', 'Training Element Budget']
        
        # Create subplot for each parameter
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        axes = axes.flatten()
        
        for idx, (param, label) in enumerate(zip(training_params, param_labels)):
            ax = axes[idx]
            
            # Box plot showing distribution across model types
            sns.boxplot(data=combined_df, x='model_type', y=param, ax=ax)
            
            # Add individual points
            sns.stripplot(data=combined_df, x='model_type', y=param, 
                         size=4, alpha=0.7, ax=ax)
            
            ax.set_title(f'{label} Distribution', fontweight='bold')
            ax.set_xlabel('Model Optimization Type')
            ax.set_ylabel(label)
            ax.tick_params(axis='x', rotation=45)
        
        plt.suptitle('Training Parameter Distributions Across Model Types', 
                    fontsize=16, fontweight='bold')
        plt.tight_layout()
        
        # Save plot
        filename = f'parameter_distributions_all_models.{self.output_format}'
        filepath = os.path.join(self.output_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        
        if self.verbose:
            print(f"   Saved: {filename}")
        
        plt.close()
    
    def plot_performance_tradeoffs(self):
        """Create performance trade-off scatter plots for each model type."""
        if self.verbose:
            print("⚖️ Creating performance trade-off plots...")
        
        colors = {'lowest_cost': 'blue', 'lowest_l2': 'red', 'optimal_neutral': 'green'}
        
        for model_type, df in self.datasets.items():
            fig, ax = plt.subplots(figsize=(12, 8))
            
            # Scatter plot: total cost vs L2 error
            scatter = ax.scatter(df['total_cost'], df['final_l2_error'], 
                               c=colors[model_type], alpha=0.7, s=100, 
                               edgecolors='black', linewidth=0.5)
            
            # Add config labels to points
            for _, row in df.iterrows():
                ax.annotate(row['config_id'].replace('_budget', '\nb').replace('_max', '_m'), 
                           (row['total_cost'], row['final_l2_error']),
                           xytext=(5, 5), textcoords='offset points',
                           fontsize=8, alpha=0.8)
            
            ax.set_xlabel('Total Computational Cost', fontweight='bold')
            ax.set_ylabel('Final L2 Error', fontweight='bold')
            ax.set_yscale('log')  # Log scale for L2 error
            ax.grid(True, alpha=0.3)
            
            # Add trend line
            z = np.polyfit(df['total_cost'], np.log10(df['final_l2_error']), 1)
            p = np.poly1d(z)
            x_trend = np.linspace(df['total_cost'].min(), df['total_cost'].max(), 100)
            y_trend = 10**p(x_trend)
            ax.plot(x_trend, y_trend, '--', color='gray', alpha=0.8, 
                   label=f'Trend (slope: {z[0]:.2e})')
            
            ax.legend()
            ax.set_title(f'Performance Trade-offs: {model_type.replace("_", " ").title()} Models\n'
                        f'Cost vs Accuracy Across 16 Simulation Configurations', 
                        fontweight='bold', fontsize=14)
            
            plt.tight_layout()
            
            # Save plot
            filename = f'performance_tradeoffs_{model_type}.{self.output_format}'
            filepath = os.path.join(self.output_dir, filename)
            plt.savefig(filepath, dpi=300, bbox_inches='tight')
            
            if self.verbose:
                print(f"   Saved: {filename}")
            
            plt.close()
    
    def run_analysis(self, visualizations=['all']):
        """
        Run the complete key models analysis.
        
        Args:
            visualizations (list): List of visualization types to create
        """
        if self.verbose:
            print(f"\n🚀 Starting Key Models Analysis")
            print(f"   Requested visualizations: {', '.join(visualizations)}")
        
        # Map visualization names to methods
        viz_methods = {
            'heatmaps': self.create_performance_heatmaps,
            'distributions': self.analyze_parameter_distributions,
            'tradeoffs': self.plot_performance_tradeoffs
        }
        
        # Determine which visualizations to run
        if 'all' in visualizations:
            methods_to_run = list(viz_methods.values())
        else:
            methods_to_run = [viz_methods[viz] for viz in visualizations if viz in viz_methods]
        
        # Execute visualizations
        for method in methods_to_run:
            try:
                method()
            except Exception as e:
                print(f"❌ Error in {method.__name__}: {e}")
                if self.verbose:
                    import traceback
                    traceback.print_exc()
        
        if self.verbose:
            print(f"\n✅ Key Models Analysis completed")
            print(f"   Output directory: {self.output_dir}")
            
            # List created files
            created_files = list(Path(self.output_dir).glob(f'*.{self.output_format}'))
            print(f"   Created {len(created_files)} visualization files:")
            for file in sorted(created_files):
                print(f"     - {file.name}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='Key Models Analysis for DRL-AMR')
    parser.add_argument('sweep_name', help='Parameter sweep name (e.g., session3_100k_uniform)')
    parser.add_argument('--visualizations', 
                       default='all',
                       help='Comma-separated list: heatmaps,distributions,tradeoffs,all (default: all)')
    parser.add_argument('--output-subdir', 
                       default='uniform_initial_max',
                       help='Output subdirectory name (default: uniform_initial_max)')
    parser.add_argument('--output-format', 
                       choices=['png', 'pdf'], 
                       default='png',
                       help='Output format (default: png)')
    parser.add_argument('--verbose', 
                       action='store_true', 
                       default=True,
                       help='Print detailed progress (default: True)')
    parser.add_argument('--quiet', 
                       dest='verbose', 
                       action='store_false',
                       help='Minimal output')
    
    args = parser.parse_args()
    
    # Parse visualization list
    if args.visualizations.lower() == 'all':
        visualizations = ['all']
    else:
        visualizations = [v.strip() for v in args.visualizations.split(',')]
    
    try:
        # Create analyzer
        analyzer = KeyModelsAnalyzer(
            sweep_name=args.sweep_name,
            output_subdir=args.output_subdir,
            output_format=args.output_format,
            verbose=args.verbose
        )
        
        # Run analysis
        analyzer.run_analysis(visualizations)
        
    except Exception as e:
        print(f"❌ Analysis failed: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()