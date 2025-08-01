#!/usr/bin/env python3
"""
Key Models Analyzer for DRL-AMR Aggregate Results

Analyzes the three key model types (lowest_cost, lowest_l2, optimal_neutral) across 
simulation configurations to identify patterns, trade-offs, and flagship models.

Core Visualizations:
1. Performance Heatmaps (4x4): Shows L2 error, cost, and training params across simulation configs
2. Parameter Distributions: Box plots of training parameter patterns across model types  
3. Performance Trade-offs: 2D scatters showing cost vs accuracy relationships
4. Efficiency Analysis: Cost ratio distributions and trade-off analysis
5. Flagship Models: Identify and visualize the 3 most impactful models using distance-to-ideal

Usage:
    python key_models_analyzer.py session3_100k_uniform --visualizations all --output-format png --verbose
    python key_models_analyzer.py session3_100k_uniform --visualizations flagship --output-format pdf
"""
import matplotlib
matplotlib.use('Agg') 

import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
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
        self.datasets = {}
        filenames = {
            'lowest_cost': 'lowest_cost_models.csv',
            'lowest_l2': 'lowest_l2_models.csv', 
            'optimal_neutral': 'optimal_neutral_models.csv'
        }
        
        for model_type, filename in filenames.items():
            filepath = os.path.join(self.aggregate_dir, filename)
            if os.path.exists(filepath):
                df = pd.read_csv(filepath)
                
                # Parse config_id for additional information
                df = self.parse_config_info(df)
                
                self.datasets[model_type] = df
                
                if self.verbose:
                    print(f"   Loaded {model_type}: {len(df)} configurations")
            else:
                raise FileNotFoundError(f"Required file not found: {filepath}")
    
    def parse_config_info(self, df):
        """Parse configuration information from config_id."""
        df = df.copy()
        
        # Extract simulation configuration parameters from config_id
        df['initial_refinement'] = df['config_id'].str.extract(r'ref(\d+)').astype(int)
        # df['element_budget'] = df['config_id'].str.extract(r'budget(\d+)').astype(int)
        df['evaluation_element_budget'] = df['config_id'].str.extract(r'budget(\d+)').astype(int)
        df['max_level'] = df['config_id'].str.extract(r'max(\d+)').astype(int)
        
        # Calculate derived metrics
        df['initial_elements'] = 4 * (4**(df['initial_refinement'] - 1))
        df['resource_usage_ratio'] = df['initial_elements'] / df['element_budget']
        
        return df
    
    def setup_plotting_style(self):
        """Set up consistent plotting style."""
        plt.style.use('default')
        plt.rcParams.update({
            'font.size': 12,
            'axes.titlesize': 14,
            'axes.labelsize': 12,
            'xtick.labelsize': 10,
            'ytick.labelsize': 10,
            'legend.fontsize': 10,
            'figure.titlesize': 16,
            'lines.linewidth': 2,
            'axes.grid': True,
            'grid.alpha': 0.3
        })
    
    def create_performance_heatmaps(self):
        """Create performance heatmaps for each metric across configurations."""
        if self.verbose:
            print("🔥 Creating performance heatmaps...")
        
        metrics = {
            'final_l2_error': {'title': 'Final L2 Error', 'cmap': 'Reds_r', 'format': '.2e'},
            'cost_ratio': {'title': 'Cost Ratio vs No-AMR', 'cmap': 'Blues_r', 'format': '.3f'},
            'gamma_c': {'title': 'Reward Scaling (γc)', 'cmap': 'viridis', 'format': '.1f'},
            'rl_iterations_per_timestep': {'title': 'RL Iterations/Timestep', 'cmap': 'plasma', 'format': '.0f'}
        }
        
        for metric, config in metrics.items():
            fig, axes = plt.subplots(1, 3, figsize=(18, 5))
            
            for i, (model_type, df) in enumerate(self.datasets.items()):
                ax = axes[i]
                
                # Create pivot table for heatmap
                pivot_data = df.pivot_table(
                    values=metric,
                    index='initial_refinement',
                    columns='element_budget',
                    aggfunc='mean'
                )
                
                # Create heatmap
                sns.heatmap(pivot_data, annot=True, fmt=config['format'], 
                           cmap=config['cmap'], ax=ax, cbar_kws={'shrink': .8})
                
                ax.set_title(f"{model_type.replace('_', ' ').title()}")
                ax.set_xlabel('Element Budget')
                ax.set_ylabel('Initial Refinement Level')
            
            fig.suptitle(f'{config["title"]} Across Simulation Configurations', 
                        fontsize=16, fontweight='bold', y=1.02)
            plt.tight_layout()
            
            # Save plot
            filename = f'heatmap_{metric}.{self.output_format}'
            filepath = os.path.join(self.output_dir, filename)
            plt.savefig(filepath, dpi=300, bbox_inches='tight')
            
            if self.verbose:
                print(f"   Saved: {filename}")
            
            plt.close()
    
    def analyze_parameter_distributions(self):
        """Analyze parameter distributions across model types."""
        if self.verbose:
            print("📊 Analyzing parameter distributions...")
        
        # Combine all datasets
        combined_data = []
        for model_type, df in self.datasets.items():
            df_copy = df.copy()
            df_copy['model_type'] = model_type
            combined_data.append(df_copy)
        
        combined_df = pd.concat(combined_data, ignore_index=True)
        
        # Parameters to analyze
        params = ['gamma_c', 'step_domain_fraction', 'rl_iterations_per_timestep']
        param_labels = ['Reward Scaling (γc)', 'Step Domain Fraction', 'RL Iterations/Timestep']
        
        fig, axes = plt.subplots(1, 3, figsize=(18, 6))
        
        model_type_order = ['lowest_cost', 'optimal_neutral', 'lowest_l2']
        model_labels = ['Best Cost', 'Optimal Balance', 'Best Accuracy']
        
        for i, (param, label) in enumerate(zip(params, param_labels)):
            ax = axes[i]
            
            # Box plot
            sns.boxplot(data=combined_df, x='model_type', y=param, 
                       order=model_type_order, ax=ax)
            ax.set_xticklabels(model_labels, rotation=45)
            ax.set_xlabel('Model Selection Strategy')
            ax.set_ylabel(label)
            ax.set_title(f'{label} Distribution')
            ax.grid(True, alpha=0.3)
        
        plt.suptitle('Training Parameter Distributions by Model Type', 
                    fontsize=16, fontweight='bold', y=1.02)
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
    
    def identify_flagship_models(self):
        """
        Identify the 3 flagship models using distance-to-ideal methodology.
        
        Returns:
            dict: Dictionary with flagship models and analysis data
        """
        if self.verbose:
            print("🎯 Identifying flagship models using distance-to-ideal methodology...")
        
        # Combine all 27 models
        combined_data = []
        for model_type, df in self.datasets.items():
            df_copy = df.copy()
            df_copy['category'] = model_type
            combined_data.append(df_copy)
        
        all_models_df = pd.concat(combined_data, ignore_index=True)
        
        # Calculate global ideal point (across all 27 models)
        global_ideal = {
            'cost_ratio': all_models_df['cost_ratio'].min(),
            'final_l2_error': all_models_df['final_l2_error'].min()
        }
        
        if self.verbose:
            print(f"   Global ideal point: Cost={global_ideal['cost_ratio']:.4f}, "
                  f"Error={global_ideal['final_l2_error']:.2e}")
        
        # Calculate flagship models for each category
        flagship_models = {}
        
        for category in ['lowest_cost', 'lowest_l2', 'optimal_neutral']:
            category_df = all_models_df[all_models_df['category'] == category].copy()
            
            # Normalize within category for distance calculation
            cost_min = category_df['cost_ratio'].min()
            cost_max = category_df['cost_ratio'].max()
            cost_range = cost_max - cost_min if cost_max > cost_min else 1.0
            
            log_error = np.log(category_df['final_l2_error'])
            error_min = log_error.min()
            error_max = log_error.max()
            error_range = error_max - error_min if error_max > error_min else 1.0
            
            # Calculate normalized distances to global ideal point
            cost_norm = (category_df['cost_ratio'] - global_ideal['cost_ratio']) / cost_range
            error_norm = (np.log(category_df['final_l2_error']) - np.log(global_ideal['final_l2_error'])) / error_range
            
            distances = np.sqrt(cost_norm**2 + error_norm**2)
            
            # Find flagship model (minimum distance)
            flagship_idx = distances.idxmin()
            flagship_model = category_df.loc[flagship_idx].copy()
            flagship_model['distance_to_ideal'] = distances.loc[flagship_idx]
            
            flagship_models[category] = flagship_model
            
            if self.verbose:
                print(f"   {category} flagship: Cost={flagship_model['cost_ratio']:.4f}, "
                      f"Error={flagship_model['final_l2_error']:.2e}, Distance={flagship_model['distance_to_ideal']:.4f}")
        
        return {
            'flagship_models': flagship_models,
            'all_models': all_models_df,
            'global_ideal': global_ideal
        }
    
    def calculate_pareto_front(self, models_df):
        """Calculate Pareto front for a set of models."""
        pareto_models = []
        
        for idx, row in models_df.iterrows():
            # Check if this model is dominated by any other model
            is_dominated = False
            
            for _, other_row in models_df.iterrows():
                # Other model dominates if it's both more accurate AND more efficient
                if (other_row['final_l2_error'] <= row['final_l2_error'] and 
                    other_row['cost_ratio'] <= row['cost_ratio'] and
                    (other_row['final_l2_error'] < row['final_l2_error'] or 
                     other_row['cost_ratio'] < row['cost_ratio'])):
                    is_dominated = True
                    break
            
            if not is_dominated:
                pareto_models.append(row)
        
        return pd.DataFrame(pareto_models)
    
    def create_flagship_category_plots(self):
        """Create the 3 category-focused flagship analysis plots."""
        if self.verbose:
            print("🏴‍☠️ Creating flagship category analysis plots...")
        
        # Get flagship analysis data
        flagship_data = self.identify_flagship_models()
        flagship_models = flagship_data['flagship_models']
        all_models_df = flagship_data['all_models']
        global_ideal = flagship_data['global_ideal']
        
        # Color scheme
        colors = {'lowest_cost': 'blue', 'optimal_neutral': 'green', 'lowest_l2': 'red'}
        gray_colors = {'lowest_cost': '#CCCCCC', 'optimal_neutral': '#999999', 'lowest_l2': '#666666'}
        
        categories = ['lowest_cost', 'lowest_l2', 'optimal_neutral']
        category_labels = ['Best Cost Focus', 'Best Accuracy Focus', 'Optimal Balance Focus']
        
        for focus_category, focus_label in zip(categories, category_labels):
            fig, ax = plt.subplots(figsize=(12, 8))
            
            # Plot all 27 models with category-specific coloring
            for category in categories:
                subset = all_models_df[all_models_df['category'] == category]
                
                if category == focus_category:
                    # Focus category in full color
                    ax.scatter(subset['cost_ratio'], subset['final_l2_error'],
                             c=colors[category], s=80, alpha=0.8, 
                             edgecolors='black', linewidth=0.5,
                             label=f'{category.replace("_", " ").title()} (N={len(subset)})')
                else:
                    # Other categories in gray
                    ax.scatter(subset['cost_ratio'], subset['final_l2_error'],
                             c=gray_colors[category], s=50, alpha=0.5,
                             edgecolors='gray', linewidth=0.3)
            
            # Calculate and plot Pareto front for focus category only
            focus_subset = all_models_df[all_models_df['category'] == focus_category]
            pareto_front = self.calculate_pareto_front(focus_subset)
            
            if len(pareto_front) > 1:
                pareto_sorted = pareto_front.sort_values('cost_ratio')
                ax.plot(pareto_sorted['cost_ratio'], pareto_sorted['final_l2_error'],
                       '--', color=colors[focus_category], alpha=0.7, linewidth=2,
                       label=f'Pareto Front (N={len(pareto_front)})')
            
            # Highlight flagship model with black circle
            flagship = flagship_models[focus_category]
            ax.scatter(flagship['cost_ratio'], flagship['final_l2_error'],
                      facecolors='none', s=300, marker='o', 
                      edgecolors='black', linewidths=2, alpha=0.9,
                      label='Flagship Model', zorder=10)
            
            # Mark global ideal point
            ax.scatter(global_ideal['cost_ratio'], global_ideal['final_l2_error'],
                      marker='*', s=200, c='gold', edgecolors='black', linewidth=1,
                      label='Global Ideal Point', zorder=10)
            
            # Add ideal point reference lines
            ax.axvline(global_ideal['cost_ratio'], color='orange', linestyle=':', alpha=0.7)
            ax.axhline(global_ideal['final_l2_error'], color='orange', linestyle=':', alpha=0.7)
            
            # Formatting
            ax.set_xlabel('Cost Ratio vs No-AMR', fontsize=12, fontweight='bold')
            ax.set_ylabel('Final L2 Error', fontsize=12, fontweight='bold')
            ax.set_yscale('log')
            ax.grid(True, alpha=0.3)
            ax.legend(fontsize=10, framealpha=0.9)
            ax.set_title(f'Flagship Analysis: {focus_label}\n'
                        f'Distance to Ideal: {flagship["distance_to_ideal"]:.4f}', 
                        fontsize=14, fontweight='bold', pad=20)
            
            plt.tight_layout()
            
            # Save plot
            filename = f'flagship_analysis_{focus_category}.{self.output_format}'
            filepath = os.path.join(self.output_dir, filename)
            plt.savefig(filepath, dpi=300, bbox_inches='tight')
            
            if self.verbose:
                print(f"   Saved: {filename}")
            
            plt.close()
    
    def create_flagship_summary_plot(self):
        """Create the final flagship summary plot with detailed annotations."""
        if self.verbose:
            print("👑 Creating flagship summary plot...")
        
        # Get flagship analysis data
        flagship_data = self.identify_flagship_models()
        flagship_models = flagship_data['flagship_models']
        global_ideal = flagship_data['global_ideal']
        
        fig, ax = plt.subplots(figsize=(14, 10))
        
        # Color scheme and labels
        colors = {'lowest_cost': 'blue', 'optimal_neutral': 'green', 'lowest_l2': 'red'}
        labels = {'lowest_cost': 'Best Cost', 'optimal_neutral': 'Optimal Balance', 'lowest_l2': 'Best Accuracy'}
        
        # Plot the 3 flagship models
        for category, flagship in flagship_models.items():
            ax.scatter(flagship['cost_ratio'], flagship['final_l2_error'],
                      c=colors[category], s=200, alpha=0.8,
                      edgecolors='black', linewidth=2,
                      label=labels[category], zorder=5)
        
        # Mark global ideal point
        ax.scatter(global_ideal['cost_ratio'], global_ideal['final_l2_error'],
                  marker='*', s=300, c='gold', edgecolors='black', linewidth=2,
                  label='Global Ideal Point', zorder=10)

        # Set axis limits to match other plots (broader view)
        ax.set_xlim(0.0, 1.0)  # Full cost ratio range
        ax.set_ylim(1e-5, 1e-1)  # Full L2 error range
        
        # Create detailed annotation boxes for each flagship model
        for i, (category, flagship) in enumerate(flagship_models.items()):
            # Calculate cost savings percentage
            cost_savings = (1 - flagship['cost_ratio']) * 100
            
            # Create annotation text with LaTeX formatting
            annotation_text = (
                f"{labels[category]} Flagship Model\n"
                f"Training Parameters:\n"
                f"  Reward scaling $\\gamma_c$: {flagship['gamma_c']:.1f}\n"
                f"  Element budget $N_{{\\text{{max}}}}$: {flagship['element_budget']}\n"
                f"  Step domain fraction $\\Delta_{{\\text{{dom}}}}$: {flagship['step_domain_fraction']:.2f}\n"
                f"  RL-iterations per timestep $N_{{\\text{{rl}}}}$: {flagship['rl_iterations_per_timestep']}\n\n"
                f"Simulation Configuration:\n"
                f"  Initial refinement level: {flagship['initial_refinement']}\n"
                f"  Initial number of elements: {flagship['initial_elements']}\n"
                f"  Element budget: {flagship['evaluation_element_budget']}\n"
                f"  Initial resource usage ratio: {flagship['resource_usage_ratio']:.3f}\n"
                f"  Max refinement level: {flagship['max_level']}\n\n"
                f"Performance Metrics:\n"
                f"  L2 Error: {flagship['final_l2_error']:.2e}\n"
                f"  Cost Ratio: {flagship['cost_ratio']:.4f}\n"
                f"  Cost Savings: {cost_savings:.1f}%\n"
                f"  Performance Category: {category}"
            )
            
            # Position annotation boxes to avoid overlap
            x_pos = flagship['cost_ratio']
            y_pos = flagship['final_l2_error']
            
            # Smart positioning based on model location
            if category == 'lowest_cost':
                xytext = (-160, 220)  # Directly to the left of blue flagship
            elif category == 'lowest_l2':
                xytext = (20, 200)    # Directly to the right of red flagship
            else:  # optimal_neutral
                xytext = (20, 280)   # Above and to the right of green flagship
            
            # Create annotation with box
            bbox_props = dict(boxstyle="round,pad=0.5", facecolor=colors[category], 
                             alpha=0.1, edgecolor=colors[category], linewidth=1)
            
            ax.annotate(annotation_text, xy=(x_pos, y_pos), xytext=xytext,
                       textcoords='offset points', fontsize=9,
                       bbox=bbox_props, ha='left', va='top',
                       arrowprops=dict(arrowstyle='->', color=colors[category], 
                                     connectionstyle="arc3,rad=0.1"))
        
        # Formatting
        ax.set_xlabel('Cost Ratio vs No-AMR', fontsize=14, fontweight='bold')
        ax.set_ylabel('Final L2 Error', fontsize=14, fontweight='bold')
        ax.set_yscale('log')
        ax.grid(True, alpha=0.3)
        ax.legend(fontsize=12, framealpha=0.9, loc='upper right')
        ax.set_title('DRL-AMR Flagship Models: Optimal Representatives\n'
                    'Three Most Impactful Models from 729 Candidates', 
                    fontsize=16, fontweight='bold', pad=20)
        
        plt.tight_layout()
        
        # Save plot
        filename = f'flagship_summary.{self.output_format}'
        filepath = os.path.join(self.output_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        
        if self.verbose:
            print(f"   Saved: {filename}")
        
        plt.close()
    
    def generate_flagship_summary_report(self):
        """Generate a text summary report of the flagship models."""
        if self.verbose:
            print("📄 Generating flagship models summary report...")
        
        # Get flagship analysis data
        flagship_data = self.identify_flagship_models()
        flagship_models = flagship_data['flagship_models']
        global_ideal = flagship_data['global_ideal']
        
        # Create summary report
        report_lines = [
            "DRL-AMR FLAGSHIP MODELS SUMMARY REPORT",
            "=" * 50,
            f"Generated: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"Analysis: {self.sweep_name}",
            "",
            "METHODOLOGY:",
            "- Combined 27 key models from 3 performance categories (9 models each)",
            "- Calculated global ideal point across all 27 models",
            "- Used within-category normalization for distance calculations", 
            "- Selected flagship model with minimum distance-to-ideal per category",
            "",
            f"GLOBAL IDEAL POINT:",
            f"  Cost Ratio: {global_ideal['cost_ratio']:.6f}",
            f"  L2 Error: {global_ideal['final_l2_error']:.2e}",
            "",
            "=" * 50,
            "FLAGSHIP MODELS (3 OF 729 TOTAL CANDIDATES)",
            "=" * 50,
        ]
        
        # Add details for each flagship model
        category_labels = {
            'lowest_cost': 'MOST COMPUTATIONALLY EFFICIENT',
            'lowest_l2': 'MOST ACCURATE', 
            'optimal_neutral': 'BEST BALANCED PERFORMANCE'
        }
        
        for category, flagship in flagship_models.items():
            cost_savings = (1 - flagship['cost_ratio']) * 100
            
            report_lines.extend([
                "",
                f"{category_labels[category]} FLAGSHIP MODEL:",
                "-" * 40,
                f"Configuration ID: {flagship['config_id']}",
                "",
                "Training Parameters:",
                f"  Reward scaling (γc): {flagship['gamma_c']:.1f}",
                f"  Element budget (N_max): {flagship['element_budget']}",
                f"  Step domain fraction (Δ_dom): {flagship['step_domain_fraction']:.3f}",
                f"  RL iterations per timestep (N_rl): {flagship['rl_iterations_per_timestep']}",
                "",
                "Simulation Configuration:",
                f"  Initial refinement level: {flagship['initial_refinement']}",
                f"  Initial number of elements: {flagship['initial_elements']}",
                f"  Element budget: {flagship['evaluation_element_budget']}",
                f"  Initial resource usage ratio: {flagship['resource_usage_ratio']:.3f}",
                f"  Max refinement level: {flagship['max_level']}",
                "",
                "Performance Metrics:",
                f"  Final L2 Error: {flagship['final_l2_error']:.6e}",
                f"  Grid-normalized L2 Error: {flagship['grid_normalized_l2_error']:.6e}",
                f"  Cost Ratio vs No-AMR: {flagship['cost_ratio']:.6f}",
                f"  Computational Cost Savings: {cost_savings:.1f}%",
                f"  Distance to Ideal: {flagship['distance_to_ideal']:.6f}",
                f"  Performance Category: {category}",
            ])
        
        report_lines.extend([
            "",
            "=" * 50,
            "IMPACT SUMMARY:",
            "=" * 50,
            "These 3 flagship models represent the optimal computational efficiency,",
            "accuracy, and balanced performance achievable through DRL-AMR across",
            "the entire 729-model parameter space explored.",
            "",
            "Key Findings:",
            f"- Computational efficiency range: {flagship_models['lowest_cost']['cost_ratio']:.1%} to {flagship_models['lowest_l2']['cost_ratio']:.1%} of no-AMR cost",
            f"- Accuracy range: {flagship_models['lowest_l2']['final_l2_error']:.2e} to {flagship_models['lowest_cost']['final_l2_error']:.2e} L2 error",
            f"- Optimal balance achieves {(1-flagship_models['optimal_neutral']['cost_ratio'])*100:.1f}% cost savings",
            f"  with {flagship_models['optimal_neutral']['final_l2_error']:.2e} L2 error",
            "",
            "These models will be featured in thesis results, conference presentations,",
            "and animation generation as definitive DRL-AMR capabilities demonstration.",
        ])
        
        # Save report
        report_text = "\n".join(report_lines)
        filename = f'flagship_models_summary.txt'
        filepath = os.path.join(self.output_dir, filename)
        
        with open(filepath, 'w') as f:
            f.write(report_text)
        
        if self.verbose:
            print(f"   Saved: {filename}")
        
        return report_text
    
    def run_flagship_analysis(self):
        """Run the complete flagship models analysis."""
        if self.verbose:
            print(f"\n🎯 Running Flagship Models Analysis")
            print(f"   Data Pipeline: 729 models → 27 key models → 3 flagship models")
        
        # Create the 4 flagship visualizations
        self.create_flagship_category_plots()  # 3 plots
        self.create_flagship_summary_plot()    # 1 plot
        
        # Generate summary report
        self.generate_flagship_summary_report()
        
        if self.verbose:
            print(f"\n✅ Flagship analysis complete! 3 flagship models identified.")
            print(f"   Check output directory: {self.output_dir}")
    
    def run_analysis(self, visualizations=['all']):
        """
        Run the complete key models analysis.
        
        Args:
            visualizations (list): List of visualizations to create
                Options: 'all', 'heatmaps', 'distributions', 'tradeoffs', 'efficiency', 'flagship'
        """
        if 'all' in visualizations:
            visualizations = ['heatmaps', 'distributions', 'tradeoffs', 'efficiency', 'flagship']
        
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
        
        if 'flagship' in visualizations:
            self.run_flagship_analysis()
        
        if self.verbose:
            print(f"\n✅ Analysis complete! Check: {self.output_dir}")

def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(description='Analyze key models across simulation configurations')
    parser.add_argument('sweep_name', help='Parameter sweep name (e.g., session3_100k_uniform)')
    parser.add_argument('--visualizations', default='all', 
                       help='Comma-separated list of visualizations: all, heatmaps, distributions, tradeoffs, efficiency, flagship')
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

# #!/usr/bin/env python3
# """
# Key Models Analyzer for DRL-AMR Aggregate Results

# Analyzes the three key model types (lowest_cost, lowest_l2, optimal_neutral) across 
# 16 simulation configurations to identify patterns, trade-offs, and parameter relationships.

# Core Visualizations:
# 1. Performance Heatmaps (4x4): Shows L2 error, cost, and training params across simulation configs
# 2. Parameter Distributions: Box plots of training parameter patterns across model types  
# 3. Performance Trade-offs: 2D scatters showing cost vs accuracy relationships

# Usage:
#     python key_models_analyzer.py session3_100k_uniform --visualizations all --output-format png --verbose
#     python key_models_analyzer.py session3_100k_uniform --visualizations heatmaps,distributions --output-format pdf
# """

# import os
# import sys
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import argparse
# from pathlib import Path

# # Get absolute path to project root
# PROJECT_ROOT = os.path.abspath(os.path.join(
#     os.path.dirname(__file__), 
#     '..',
#     '..'
# ))
# sys.path.append(PROJECT_ROOT)

# class KeyModelsAnalyzer:
#     """Analyzer for key models across simulation configurations."""
    
#     def __init__(self, sweep_name, output_subdir="uniform_initial_max", output_format='png', verbose=True):
#         """
#         Initialize analyzer.
        
#         Args:
#             sweep_name (str): Parameter sweep name (e.g., 'session3_100k_uniform')
#             output_subdir (str): Subdirectory name for analysis type
#             output_format (str): Output format ('png' or 'pdf')
#             verbose (bool): Whether to print detailed progress
#         """
#         self.sweep_name = sweep_name
#         self.output_subdir = output_subdir
#         self.output_format = output_format
#         self.verbose = verbose
        
#         # Set up paths
#         self.data_dir = os.path.join(PROJECT_ROOT, 'analysis', 'data', 'model_performance', sweep_name)
#         self.aggregate_dir = os.path.join(self.data_dir, 'aggregate_results')
#         self.output_dir = os.path.join(self.aggregate_dir, 'aggregate_analysis', output_subdir)
        
#         # Create output directory
#         os.makedirs(self.output_dir, exist_ok=True)
        
#         # Load data
#         self.load_data()
        
#         # Set up plotting style
#         self.setup_plotting_style()
        
#         if self.verbose:
#             print(f"🔍 Key Models Analyzer initialized")
#             print(f"   Sweep: {sweep_name}")
#             print(f"   Output: {self.output_dir}")
#             print(f"   Data shapes: {[len(df) for df in self.datasets.values()]} configs each")
    
#     def load_data(self):
#         """Load the three aggregate CSV files."""
#         csv_files = {
#             'lowest_cost': 'lowest_cost_models.csv',
#             'lowest_l2': 'lowest_l2_models.csv', 
#             'optimal_neutral': 'optimal_neutral_models.csv'
#         }
        
#         self.datasets = {}
#         for model_type, filename in csv_files.items():
#             filepath = os.path.join(self.aggregate_dir, filename)
#             if not os.path.exists(filepath):
#                 raise FileNotFoundError(f"Required file not found: {filepath}")
            
#             df = pd.read_csv(filepath)
            
#             # Validate expected structure - should be 9 configs now, not 16
#             if len(df) not in [9, 16]:
#                 print(f"⚠️ Warning: Expected 9 or 16 configs, found {len(df)} in {filename}")
            
#             self.datasets[model_type] = df
            
#         if self.verbose:
#             print(f"✅ Loaded {len(self.datasets)} datasets successfully")
    
#     def setup_plotting_style(self):
#         """Set up consistent plotting style."""
#         plt.style.use('default')
#         sns.set_palette("husl")
        
#         # Configure matplotlib for consistent output
#         plt.rcParams.update({
#             'figure.figsize': (12, 8),
#             'font.size': 10,
#             'axes.titlesize': 12,
#             'axes.labelsize': 10,
#             'xtick.labelsize': 9,
#             'ytick.labelsize': 9,
#             'legend.fontsize': 9,
#             'figure.titlesize': 14
#         })
    
#     def extract_simulation_config(self, config_id):
#         """
#         Extract initial_refinement and element_budget from config_id.
        
#         Args:
#             config_id (str): e.g., 'ref4_budget50_max4'
            
#         Returns:
#             tuple: (initial_refinement, element_budget)
#         """
#         import re
#         match = re.match(r'ref(\d+)_budget(\d+)_max\d+', config_id)
#         if match:
#             return int(match.group(1)), int(match.group(2))
#         else:
#             raise ValueError(f"Cannot parse config_id: {config_id}")
    
#     def create_performance_heatmaps(self):
#         """Create 3x3 heatmaps showing performance across simulation configurations."""
#         if self.verbose:
#             print("📊 Creating performance heatmaps...")
        
#         # Define unique refinement levels and budgets based on actual data
#         all_configs = []
#         for df in self.datasets.values():
#             for config_id in df['config_id']:
#                 ref_level, budget = self.extract_simulation_config(config_id)
#                 all_configs.append((ref_level, budget))
        
#         # Get unique sorted values from actual data
#         refinement_levels = sorted(list(set([config[0] for config in all_configs])))
#         element_budgets = sorted(list(set([config[1] for config in all_configs])))
        
#         if self.verbose:
#             print(f"   Refinement levels: {refinement_levels}")
#             print(f"   Element budgets: {element_budgets}")
        
#         # Color schemes for each model type
#         color_schemes = {
#             'lowest_cost': 'Blues',
#             'lowest_l2': 'Reds', 
#             'optimal_neutral': 'Greens'
#         }
        
#         for model_type, df in self.datasets.items():
#             fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
#             axes = [ax1, ax2, ax3, ax4]
#             metrics = ['final_l2_error', 'cost_ratio', 'gamma_c', 'step_domain_fraction']
#             titles = ['L2 Error', 'Cost Ratio', 'Gamma C', 'Step Domain Fraction']
            
#             for idx, (metric, title, ax) in enumerate(zip(metrics, titles, axes)):
#                 # Create matrix for heatmap (NaN for missing combinations)
#                 heatmap_data = np.full((len(refinement_levels), len(element_budgets)), np.nan)
#                 annotations = np.full((len(refinement_levels), len(element_budgets)), '', dtype=object)
                
#                 # Collect all values for this metric to determine range
#                 all_values = []
                
#                 for _, row in df.iterrows():
#                     ref_level, budget = self.extract_simulation_config(row['config_id'])
                    
#                     # Find position in matrix
#                     try:
#                         ref_idx = refinement_levels.index(ref_level)
#                         budget_idx = element_budgets.index(budget)
                        
#                         # Set value and annotation
#                         value = row[metric]
#                         heatmap_data[ref_idx, budget_idx] = value
#                         all_values.append(value)  # Collect for range calculation
                        
#                         # Format annotation based on metric
#                         if metric == 'final_l2_error':
#                             annotations[ref_idx, budget_idx] = f'{value:.1e}'
#                         elif metric == 'cost_ratio':
#                             annotations[ref_idx, budget_idx] = f'{value:.3f}'
#                         else:
#                             annotations[ref_idx, budget_idx] = f'{value:.3f}'
                            
#                     except ValueError as e:
#                         if self.verbose:
#                             print(f"   Warning: Could not place {row['config_id']} in heatmap: {e}")
#                         continue
                
#                 # ROBUST FIX: Use all_values for vmin/vmax instead of heatmap_data
#                 if len(all_values) > 0:
#                     vmin = min(all_values)
#                     vmax = max(all_values)
                    
#                     # DEBUG: Print the range for verification
#                     if self.verbose:
#                         print(f"   {model_type} {metric}: range [{vmin:.3e}, {vmax:.3e}]")
#                 else:
#                     vmin, vmax = None, None
#                     if self.verbose:
#                         print(f"   {model_type} {metric}: No valid data found!")
                
#                 # Create heatmap with explicit colorbar range
#                 im = ax.imshow(heatmap_data, 
#                             cmap=color_schemes[model_type],
#                             vmin=vmin, 
#                             vmax=vmax,
#                             aspect='auto')
                
#                 # Add colorbar with explicit range
#                 cbar = plt.colorbar(im, ax=ax)
#                 cbar.set_label(title)
                
#                 # Add annotations manually
#                 for i in range(len(refinement_levels)):
#                     for j in range(len(element_budgets)):
#                         if not np.isnan(heatmap_data[i, j]):
#                             text = annotations[i, j]
#                             ax.text(j, i, text, ha='center', va='center', 
#                                 color='white' if heatmap_data[i, j] > (vmin + vmax) / 2 else 'black',
#                                 fontweight='bold')
                
#                 # Set labels and ticks
#                 ax.set_xticks(range(len(element_budgets)))
#                 ax.set_xticklabels([f'Budget {b}' for b in element_budgets])
#                 ax.set_yticks(range(len(refinement_levels)))
#                 ax.set_yticklabels([f'Ref {r}' for r in refinement_levels])
                
#                 ax.set_title(f'{title}', fontweight='bold')
#                 ax.set_xlabel('Element Budget')
#                 ax.set_ylabel('Initial Refinement Level')
            
#             plt.suptitle(f'Performance Heatmaps: {model_type.replace("_", " ").title()} Models', 
#                         fontsize=16, fontweight='bold')
#             plt.tight_layout()
            
#             # Save plot
#             filename = f'performance_heatmaps_{model_type}.{self.output_format}'
#             filepath = os.path.join(self.output_dir, filename)
#             plt.savefig(filepath, dpi=300, bbox_inches='tight')
            
#             if self.verbose:
#                 print(f"   Saved: {filename}")
            
#             plt.close()
    
#     def analyze_parameter_distributions(self):
#         """Analyze training parameter distributions across model types."""
#         if self.verbose:
#             print("📈 Creating parameter distribution analysis...")
        
#         # Combine all datasets with model type labels
#         combined_data = []
#         for model_type, df in self.datasets.items():
#             df_copy = df.copy()
#             df_copy['model_type'] = model_type.replace('_', ' ').title()
#             combined_data.append(df_copy)
        
#         combined_df = pd.concat(combined_data, ignore_index=True)
        
#         # Parameters to analyze
#         parameters = ['gamma_c', 'step_domain_fraction', 'rl_iterations_per_timestep']
#         parameter_labels = ['Gamma C', 'Step Domain Fraction', 'RL Iterations per Timestep']
        
#         # Create subplot grid
#         fig, axes = plt.subplots(2, 2, figsize=(15, 12))
#         axes = axes.flatten()
        
#         # Box plots for each parameter
#         for i, (param, label) in enumerate(zip(parameters, parameter_labels)):
#             if i < len(axes):
#                 sns.boxplot(data=combined_df, x='model_type', y=param, ax=axes[i])
#                 axes[i].set_title(f'{label} Distribution by Model Type', fontweight='bold')
#                 axes[i].set_xlabel('Model Type')
#                 axes[i].set_ylabel(label)
#                 axes[i].tick_params(axis='x', rotation=45)
        
#         # Performance summary in last subplot
#         if len(parameters) < len(axes):
#             ax = axes[len(parameters)]
            
#             # Create performance summary scatter
#             for model_type, df in self.datasets.items():
#                 ax.scatter(df['cost_ratio'], df['final_l2_error'], 
#                           label=model_type.replace('_', ' ').title(), 
#                           alpha=0.7, s=100)
            
#             ax.set_xlabel('Cost Ratio vs No-AMR', fontweight='bold')
#             ax.set_ylabel('Final L2 Error', fontweight='bold')
#             ax.set_yscale('log')
#             ax.set_title('Performance Summary: All Model Types', fontweight='bold')
#             ax.legend()
#             ax.grid(True, alpha=0.3)
        
#         # Hide any unused subplots
#         for i in range(len(parameters) + 1, len(axes)):
#             axes[i].set_visible(False)
        
#         plt.suptitle('Training Parameter Analysis Across Model Types', 
#                     fontsize=16, fontweight='bold')
#         plt.tight_layout()
        
#         # Save plot
#         filename = f'parameter_distributions.{self.output_format}'
#         filepath = os.path.join(self.output_dir, filename)
#         plt.savefig(filepath, dpi=300, bbox_inches='tight')
        
#         if self.verbose:
#             print(f"   Saved: {filename}")
        
#         plt.close()
    
#     def plot_performance_tradeoffs(self):
#         """Create performance trade-off scatter plots for each model type."""
#         if self.verbose:
#             print("⚖️ Creating performance trade-off plots...")
        
#         colors = {'lowest_cost': 'blue', 'lowest_l2': 'red', 'optimal_neutral': 'green'}
        
#         for model_type, df in self.datasets.items():
#             fig, ax = plt.subplots(figsize=(12, 8))
            
#             # Scatter plot: cost_ratio vs L2 error
#             scatter = ax.scatter(df['cost_ratio'], df['final_l2_error'], 
#                                c=colors[model_type], alpha=0.7, s=100, 
#                                edgecolors='black', linewidth=0.5)
            
#             # Add config labels to points
#             for _, row in df.iterrows():
#                 ax.annotate(row['config_id'].replace('_budget', '\nb').replace('_max', '_m'), 
#                            (row['cost_ratio'], row['final_l2_error']),
#                            xytext=(5, 5), textcoords='offset points',
#                            fontsize=8, alpha=0.8)
            
#             ax.set_xlabel('Cost Ratio vs No-AMR', fontweight='bold')
#             ax.set_ylabel('Final L2 Error', fontweight='bold')
#             ax.set_yscale('log')  # Log scale for L2 error
#             ax.grid(True, alpha=0.3)
            
#             # Add trend line
#             if len(df) > 1:  # Need at least 2 points for trend
#                 z = np.polyfit(df['cost_ratio'], np.log10(df['final_l2_error']), 1)
#                 p = np.poly1d(z)
#                 x_trend = np.linspace(df['cost_ratio'].min(), df['cost_ratio'].max(), 100)
#                 y_trend = 10**p(x_trend)
#                 ax.plot(x_trend, y_trend, '--', color='gray', alpha=0.8, 
#                        label=f'Trend (slope: {z[0]:.2e})')
#                 ax.legend()
            
#             ax.set_title(f'Performance Trade-offs: {model_type.replace("_", " ").title()} Models\n'
#                         f'Cost vs Accuracy Across {len(df)} Simulation Configurations', 
#                         fontweight='bold', fontsize=14)
            
#             plt.tight_layout()
            
#             # Save plot
#             filename = f'performance_tradeoffs_{model_type}.{self.output_format}'
#             filepath = os.path.join(self.output_dir, filename)
#             plt.savefig(filepath, dpi=300, bbox_inches='tight')
            
#             if self.verbose:
#                 print(f"   Saved: {filename}")
            
#             plt.close()
    
#     def create_efficiency_comparison(self):
#         """Create comparison plots showing efficiency gains across model types."""
#         if self.verbose:
#             print("🚀 Creating efficiency comparison analysis...")
        
#         # Combine all datasets for comparison
#         combined_data = []
#         for model_type, df in self.datasets.items():
#             df_copy = df.copy()
#             df_copy['model_type'] = model_type
#             combined_data.append(df_copy)
        
#         combined_df = pd.concat(combined_data, ignore_index=True)
        
#         fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
        
#         # Plot 1: Cost Ratio Distribution by Model Type
#         model_type_order = ['lowest_cost', 'optimal_neutral', 'lowest_l2']
#         model_labels = ['Best Cost', 'Optimal Balance', 'Best Accuracy']
        
#         # Box plot of cost ratios
#         sns.boxplot(data=combined_df, x='model_type', y='cost_ratio', 
#                    order=model_type_order, ax=ax1)
#         ax1.set_xticklabels(model_labels)
#         ax1.set_xlabel('Model Selection Strategy', fontweight='bold')
#         ax1.set_ylabel('Cost Ratio vs No-AMR', fontweight='bold')
#         ax1.set_title('Computational Efficiency by Model Type', fontweight='bold')
#         ax1.grid(True, alpha=0.3)
        
#         # Add efficiency percentages as text
#         for i, model_type in enumerate(model_type_order):
#             subset = combined_df[combined_df['model_type'] == model_type]
#             mean_ratio = subset['cost_ratio'].mean()
#             efficiency_pct = (1 - mean_ratio) * 100
#             ax1.text(i, mean_ratio + 0.02, f'{efficiency_pct:.1f}% savings', 
#                     ha='center', fontweight='bold', fontsize=10)
        
#         # Plot 2: Accuracy vs Efficiency Scatter
#         colors = {'lowest_cost': 'blue', 'optimal_neutral': 'green', 'lowest_l2': 'red'}
#         for model_type in model_type_order:
#             subset = combined_df[combined_df['model_type'] == model_type]
#             ax2.scatter(subset['cost_ratio'], subset['final_l2_error'],
#                        c=colors[model_type], label=model_labels[model_type_order.index(model_type)],
#                        alpha=0.7, s=80, edgecolors='black', linewidth=0.5)
        
#         ax2.set_xlabel('Cost Ratio vs No-AMR', fontweight='bold')
#         ax2.set_ylabel('Final L2 Error', fontweight='bold')
#         ax2.set_yscale('log')
#         ax2.set_title('Accuracy vs Efficiency Trade-off', fontweight='bold')
#         ax2.legend()
#         ax2.grid(True, alpha=0.3)
        
#         plt.tight_layout()
        
#         # Save plot
#         filename = f'efficiency_comparison.{self.output_format}'
#         filepath = os.path.join(self.output_dir, filename)
#         plt.savefig(filepath, dpi=300, bbox_inches='tight')
        
#         if self.verbose:
#             print(f"   Saved: {filename}")
        
#         plt.close()
    
#     def run_analysis(self, visualizations=['all']):
#         """
#         Run the complete key models analysis.
        
#         Args:
#             visualizations (list): List of visualizations to create
#                 Options: 'all', 'heatmaps', 'distributions', 'tradeoffs', 'efficiency'
#         """
#         if 'all' in visualizations:
#             visualizations = ['heatmaps', 'distributions', 'tradeoffs', 'efficiency']
        
#         if self.verbose:
#             print(f"\n🎯 Running Key Models Analysis")
#             print(f"   Visualizations: {', '.join(visualizations)}")
        
#         # Run requested visualizations
#         if 'heatmaps' in visualizations:
#             self.create_performance_heatmaps()
        
#         if 'distributions' in visualizations:
#             self.analyze_parameter_distributions()
        
#         if 'tradeoffs' in visualizations:
#             self.plot_performance_tradeoffs()
        
#         if 'efficiency' in visualizations:
#             self.create_efficiency_comparison()
        
#         if self.verbose:
#             print(f"\n✅ Analysis complete! Check: {self.output_dir}")

# def main():
#     """Main execution function."""
#     parser = argparse.ArgumentParser(description='Analyze key models across simulation configurations')
#     parser.add_argument('sweep_name', help='Parameter sweep name (e.g., session3_100k_uniform)')
#     parser.add_argument('--visualizations', default='all', 
#                        help='Comma-separated list of visualizations: all, heatmaps, distributions, tradeoffs, efficiency')
#     parser.add_argument('--output-subdir', default='uniform_initial_max',
#                        help='Output subdirectory name')
#     parser.add_argument('--output-format', choices=['png', 'pdf'], default='png',
#                        help='Output format for plots')
#     parser.add_argument('--verbose', action='store_true', default=True,
#                        help='Enable verbose output')
    
#     args = parser.parse_args()
    
#     # Parse visualizations list
#     if args.visualizations == 'all':
#         visualizations = ['all']
#     else:
#         visualizations = [v.strip() for v in args.visualizations.split(',')]
    
#     # Create analyzer and run analysis
#     analyzer = KeyModelsAnalyzer(
#         sweep_name=args.sweep_name,
#         output_subdir=args.output_subdir,
#         output_format=args.output_format,
#         verbose=args.verbose
#     )
    
#     analyzer.run_analysis(visualizations=visualizations)

# if __name__ == "__main__":
#     main()


# #     main()