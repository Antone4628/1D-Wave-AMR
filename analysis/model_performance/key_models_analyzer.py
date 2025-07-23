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
        """Load the three aggregate CSV files."""
        csv_files = {
            'lowest_cost': 'lowest_cost_models.csv',
            'lowest_l2': 'lowest_l2_models.csv', 
            'optimal_neutral': 'optimal_neutral_models.csv'
        }
        
        self.datasets = {}
        for model_type, filename in csv_files.items():
            filepath = os.path.join(self.aggregate_dir, filename)
            if not os.path.exists(filepath):
                raise FileNotFoundError(f"Required file not found: {filepath}")
            
            df = pd.read_csv(filepath)
            
            # Validate expected structure - should be 9 configs now, not 16
            if len(df) not in [9, 16]:
                print(f"⚠️ Warning: Expected 9 or 16 configs, found {len(df)} in {filename}")
            
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
        """Create 3x3 heatmaps showing performance across simulation configurations."""
        if self.verbose:
            print("📊 Creating performance heatmaps...")
        
        # Define unique refinement levels and budgets based on actual data
        all_configs = []
        for df in self.datasets.values():
            for config_id in df['config_id']:
                ref_level, budget = self.extract_simulation_config(config_id)
                all_configs.append((ref_level, budget))
        
        # Get unique sorted values from actual data
        refinement_levels = sorted(list(set([config[0] for config in all_configs])))
        element_budgets = sorted(list(set([config[1] for config in all_configs])))
        
        if self.verbose:
            print(f"   Refinement levels: {refinement_levels}")
            print(f"   Element budgets: {element_budgets}")
        
        # Color schemes for each model type
        color_schemes = {
            'lowest_cost': 'Blues',
            'lowest_l2': 'Reds', 
            'optimal_neutral': 'Greens'
        }
        
        for model_type, df in self.datasets.items():
            fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
            axes = [ax1, ax2, ax3, ax4]
            metrics = ['final_l2_error', 'cost_ratio', 'gamma_c', 'step_domain_fraction']
            titles = ['L2 Error', 'Cost Ratio', 'Gamma C', 'Step Domain Fraction']
            
            for idx, (metric, title, ax) in enumerate(zip(metrics, titles, axes)):
                # Create matrix for heatmap (NaN for missing combinations)
                heatmap_data = np.full((len(refinement_levels), len(element_budgets)), np.nan)
                annotations = np.full((len(refinement_levels), len(element_budgets)), '', dtype=object)
                
                # Collect all values for this metric to determine range
                all_values = []
                
                for _, row in df.iterrows():
                    ref_level, budget = self.extract_simulation_config(row['config_id'])
                    
                    # Find position in matrix
                    try:
                        ref_idx = refinement_levels.index(ref_level)
                        budget_idx = element_budgets.index(budget)
                        
                        # Set value and annotation
                        value = row[metric]
                        heatmap_data[ref_idx, budget_idx] = value
                        all_values.append(value)  # Collect for range calculation
                        
                        # Format annotation based on metric
                        if metric == 'final_l2_error':
                            annotations[ref_idx, budget_idx] = f'{value:.1e}'
                        elif metric == 'cost_ratio':
                            annotations[ref_idx, budget_idx] = f'{value:.3f}'
                        else:
                            annotations[ref_idx, budget_idx] = f'{value:.3f}'
                            
                    except ValueError as e:
                        if self.verbose:
                            print(f"   Warning: Could not place {row['config_id']} in heatmap: {e}")
                        continue
                
                # ROBUST FIX: Use all_values for vmin/vmax instead of heatmap_data
                if len(all_values) > 0:
                    vmin = min(all_values)
                    vmax = max(all_values)
                    
                    # DEBUG: Print the range for verification
                    if self.verbose:
                        print(f"   {model_type} {metric}: range [{vmin:.3e}, {vmax:.3e}]")
                else:
                    vmin, vmax = None, None
                    if self.verbose:
                        print(f"   {model_type} {metric}: No valid data found!")
                
                # Create heatmap with explicit colorbar range
                im = ax.imshow(heatmap_data, 
                            cmap=color_schemes[model_type],
                            vmin=vmin, 
                            vmax=vmax,
                            aspect='auto')
                
                # Add colorbar with explicit range
                cbar = plt.colorbar(im, ax=ax)
                cbar.set_label(title)
                
                # Add annotations manually
                for i in range(len(refinement_levels)):
                    for j in range(len(element_budgets)):
                        if not np.isnan(heatmap_data[i, j]):
                            text = annotations[i, j]
                            ax.text(j, i, text, ha='center', va='center', 
                                color='white' if heatmap_data[i, j] > (vmin + vmax) / 2 else 'black',
                                fontweight='bold')
                
                # Set labels and ticks
                ax.set_xticks(range(len(element_budgets)))
                ax.set_xticklabels([f'Budget {b}' for b in element_budgets])
                ax.set_yticks(range(len(refinement_levels)))
                ax.set_yticklabels([f'Ref {r}' for r in refinement_levels])
                
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
            print("📈 Creating parameter distribution analysis...")
        
        # Combine all datasets with model type labels
        combined_data = []
        for model_type, df in self.datasets.items():
            df_copy = df.copy()
            df_copy['model_type'] = model_type.replace('_', ' ').title()
            combined_data.append(df_copy)
        
        combined_df = pd.concat(combined_data, ignore_index=True)
        
        # Parameters to analyze
        parameters = ['gamma_c', 'step_domain_fraction', 'rl_iterations_per_timestep']
        parameter_labels = ['Gamma C', 'Step Domain Fraction', 'RL Iterations per Timestep']
        
        # Create subplot grid
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        axes = axes.flatten()
        
        # Box plots for each parameter
        for i, (param, label) in enumerate(zip(parameters, parameter_labels)):
            if i < len(axes):
                sns.boxplot(data=combined_df, x='model_type', y=param, ax=axes[i])
                axes[i].set_title(f'{label} Distribution by Model Type', fontweight='bold')
                axes[i].set_xlabel('Model Type')
                axes[i].set_ylabel(label)
                axes[i].tick_params(axis='x', rotation=45)
        
        # Performance summary in last subplot
        if len(parameters) < len(axes):
            ax = axes[len(parameters)]
            
            # Create performance summary scatter
            for model_type, df in self.datasets.items():
                ax.scatter(df['cost_ratio'], df['final_l2_error'], 
                          label=model_type.replace('_', ' ').title(), 
                          alpha=0.7, s=100)
            
            ax.set_xlabel('Cost Ratio vs No-AMR', fontweight='bold')
            ax.set_ylabel('Final L2 Error', fontweight='bold')
            ax.set_yscale('log')
            ax.set_title('Performance Summary: All Model Types', fontweight='bold')
            ax.legend()
            ax.grid(True, alpha=0.3)
        
        # Hide any unused subplots
        for i in range(len(parameters) + 1, len(axes)):
            axes[i].set_visible(False)
        
        plt.suptitle('Training Parameter Analysis Across Model Types', 
                    fontsize=16, fontweight='bold')
        plt.tight_layout()
        
        # Save plot
        filename = f'parameter_distributions.{self.output_format}'
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
            
            # Scatter plot: cost_ratio vs L2 error
            scatter = ax.scatter(df['cost_ratio'], df['final_l2_error'], 
                               c=colors[model_type], alpha=0.7, s=100, 
                               edgecolors='black', linewidth=0.5)
            
            # Add config labels to points
            for _, row in df.iterrows():
                ax.annotate(row['config_id'].replace('_budget', '\nb').replace('_max', '_m'), 
                           (row['cost_ratio'], row['final_l2_error']),
                           xytext=(5, 5), textcoords='offset points',
                           fontsize=8, alpha=0.8)
            
            ax.set_xlabel('Cost Ratio vs No-AMR', fontweight='bold')
            ax.set_ylabel('Final L2 Error', fontweight='bold')
            ax.set_yscale('log')  # Log scale for L2 error
            ax.grid(True, alpha=0.3)
            
            # Add trend line
            if len(df) > 1:  # Need at least 2 points for trend
                z = np.polyfit(df['cost_ratio'], np.log10(df['final_l2_error']), 1)
                p = np.poly1d(z)
                x_trend = np.linspace(df['cost_ratio'].min(), df['cost_ratio'].max(), 100)
                y_trend = 10**p(x_trend)
                ax.plot(x_trend, y_trend, '--', color='gray', alpha=0.8, 
                       label=f'Trend (slope: {z[0]:.2e})')
                ax.legend()
            
            ax.set_title(f'Performance Trade-offs: {model_type.replace("_", " ").title()} Models\n'
                        f'Cost vs Accuracy Across {len(df)} Simulation Configurations', 
                        fontweight='bold', fontsize=14)
            
            plt.tight_layout()
            
            # Save plot
            filename = f'performance_tradeoffs_{model_type}.{self.output_format}'
            filepath = os.path.join(self.output_dir, filename)
            plt.savefig(filepath, dpi=300, bbox_inches='tight')
            
            if self.verbose:
                print(f"   Saved: {filename}")
            
            plt.close()
    
    def create_efficiency_comparison(self):
        """Create comparison plots showing efficiency gains across model types."""
        if self.verbose:
            print("🚀 Creating efficiency comparison analysis...")
        
        # Combine all datasets for comparison
        combined_data = []
        for model_type, df in self.datasets.items():
            df_copy = df.copy()
            df_copy['model_type'] = model_type
            combined_data.append(df_copy)
        
        combined_df = pd.concat(combined_data, ignore_index=True)
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
        
        # Plot 1: Cost Ratio Distribution by Model Type
        model_type_order = ['lowest_cost', 'optimal_neutral', 'lowest_l2']
        model_labels = ['Best Cost', 'Optimal Balance', 'Best Accuracy']
        
        # Box plot of cost ratios
        sns.boxplot(data=combined_df, x='model_type', y='cost_ratio', 
                   order=model_type_order, ax=ax1)
        ax1.set_xticklabels(model_labels)
        ax1.set_xlabel('Model Selection Strategy', fontweight='bold')
        ax1.set_ylabel('Cost Ratio vs No-AMR', fontweight='bold')
        ax1.set_title('Computational Efficiency by Model Type', fontweight='bold')
        ax1.grid(True, alpha=0.3)
        
        # Add efficiency percentages as text
        for i, model_type in enumerate(model_type_order):
            subset = combined_df[combined_df['model_type'] == model_type]
            mean_ratio = subset['cost_ratio'].mean()
            efficiency_pct = (1 - mean_ratio) * 100
            ax1.text(i, mean_ratio + 0.02, f'{efficiency_pct:.1f}% savings', 
                    ha='center', fontweight='bold', fontsize=10)
        
        # Plot 2: Accuracy vs Efficiency Scatter
        colors = {'lowest_cost': 'blue', 'optimal_neutral': 'green', 'lowest_l2': 'red'}
        for model_type in model_type_order:
            subset = combined_df[combined_df['model_type'] == model_type]
            ax2.scatter(subset['cost_ratio'], subset['final_l2_error'],
                       c=colors[model_type], label=model_labels[model_type_order.index(model_type)],
                       alpha=0.7, s=80, edgecolors='black', linewidth=0.5)
        
        ax2.set_xlabel('Cost Ratio vs No-AMR', fontweight='bold')
        ax2.set_ylabel('Final L2 Error', fontweight='bold')
        ax2.set_yscale('log')
        ax2.set_title('Accuracy vs Efficiency Trade-off', fontweight='bold')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        # Save plot
        filename = f'efficiency_comparison.{self.output_format}'
        filepath = os.path.join(self.output_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        
        if self.verbose:
            print(f"   Saved: {filename}")
        
        plt.close()
    
    def run_analysis(self, visualizations=['all']):
        """
        Run the complete key models analysis.
        
        Args:
            visualizations (list): List of visualizations to create
                Options: 'all', 'heatmaps', 'distributions', 'tradeoffs', 'efficiency'
        """
        if 'all' in visualizations:
            visualizations = ['heatmaps', 'distributions', 'tradeoffs', 'efficiency']
        
        if self.verbose:
            print(f"\n🎯 Running Key Models Analysis")
            print(f"   Visualizations: {', '.join(visualizations)}")
        
        # Run requested visualizations
        if 'heatmaps' in visualizations:
            self.create_performance_heatmaps()
        
        if 'distributions' in visualizations:
            self.analyze_parameter_distributions()
        
        if 'tradeoffs' in visualizations:
            self.plot_performance_tradeoffs()
        
        if 'efficiency' in visualizations:
            self.create_efficiency_comparison()
        
        if self.verbose:
            print(f"\n✅ Analysis complete! Check: {self.output_dir}")

def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(description='Analyze key models across simulation configurations')
    parser.add_argument('sweep_name', help='Parameter sweep name (e.g., session3_100k_uniform)')
    parser.add_argument('--visualizations', default='all', 
                       help='Comma-separated list of visualizations: all, heatmaps, distributions, tradeoffs, efficiency')
    parser.add_argument('--output-subdir', default='uniform_initial_max',
                       help='Output subdirectory name')
    parser.add_argument('--output-format', choices=['png', 'pdf'], default='png',
                       help='Output format for plots')
    parser.add_argument('--verbose', action='store_true', default=True,
                       help='Enable verbose output')
    
    args = parser.parse_args()
    
    # Parse visualizations list
    if args.visualizations == 'all':
        visualizations = ['all']
    else:
        visualizations = [v.strip() for v in args.visualizations.split(',')]
    
    # Create analyzer and run analysis
    analyzer = KeyModelsAnalyzer(
        sweep_name=args.sweep_name,
        output_subdir=args.output_subdir,
        output_format=args.output_format,
        verbose=args.verbose
    )
    
    analyzer.run_analysis(visualizations=visualizations)

if __name__ == "__main__":
    main()


#     main()