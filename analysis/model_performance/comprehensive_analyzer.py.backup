"""
Comprehensive Model Performance Analyzer

This script provides comprehensive analysis of batch model evaluation results including:
- Parameter family visualization
- Pareto front analysis  
- Distance-to-ideal performance zones
- Ideal point visualization
- Flexible output formats

Usage:
    python comprehensive_analyzer.py session3_100k_uniform --plot-mode pdf --pareto --include-ideal --include-zones
    python comprehensive_analyzer.py session3_100k_uniform --plot-mode png --no-pareto --no-ideal --no-zones
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
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

class ComprehensiveAnalyzer:
    """
    Comprehensive analyzer for AMR parameter sweep results with distance-to-ideal zones.
    """
    
    def __init__(self, sweep_name, verbose=False):
        """
        Initialize the comprehensive analyzer.
        
        Args:
            sweep_name (str): Name of the sweep (e.g., 'session3_100k_uniform')
            verbose (bool): Whether to print detailed logs
        """
        self.sweep_name = sweep_name
        self.verbose = verbose
        
        # Set up paths
        self.results_dir = os.path.join(PROJECT_ROOT, 'analysis', 'data', 'model_performance', sweep_name)
        self.csv_path = os.path.join(self.results_dir, 'batch_results_all_models.csv')
        self.output_dir = os.path.join(self.results_dir, 'comprehensive_analysis')
        
        # Create output directory
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Load and validate data
        self.df = self._load_and_validate_data()
        
        # Calculate ideal point and distances
        self.ideal_point = self._calculate_ideal_point()
        self.df['distance_to_ideal'] = self._calculate_distances_to_ideal()
        
        # Calculate zone boundaries
        self.zone_boundaries = self._calculate_zone_boundaries()
        self.df['performance_zone'] = self._assign_performance_zones()
        
        # Define parameter families (current 4-parameter setup)
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
            print(f"Ideal point: Cost={self.ideal_point['cost']:.0f}, Error={self.ideal_point['error']:.2e}")
            print(f"Distance range: {self.df['distance_to_ideal'].min():.3f} to {self.df['distance_to_ideal'].max():.3f}")
    
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
    
    def _calculate_ideal_point(self):
        """Calculate the ideal point (minimum cost, minimum error intersection)."""
        ideal_cost = self.df['total_cost'].min()
        ideal_error = self.df['final_l2_error'].min()
        
        return {
            'cost': ideal_cost,
            'error': ideal_error
        }
    
    def _calculate_distances_to_ideal(self):
        """Calculate normalized Euclidean distances to the ideal point."""
        # Normalize cost (linear scale)
        cost_min, cost_max = self.df['total_cost'].min(), self.df['total_cost'].max()
        cost_norm = (self.df['total_cost'] - cost_min) / (cost_max - cost_min)
        
        # Normalize error (log scale)
        log_error = np.log(self.df['final_l2_error'])
        error_min, error_max = log_error.min(), log_error.max()
        error_norm = (log_error - error_min) / (error_max - error_min)
        
        # Calculate Euclidean distance (equal weighting)
        distances = np.sqrt(cost_norm**2 + error_norm**2)
        
        return distances
    
    def _calculate_zone_boundaries(self):
        """Calculate zone boundaries using percentile approach."""
        distances = self.df['distance_to_ideal']
        boundaries = np.percentile(distances, [25, 50, 75])
        
        return {
            'elite_upper': boundaries[0],
            'good_upper': boundaries[1], 
            'fair_upper': boundaries[2],
            'poor_upper': distances.max()
        }
    
    def _assign_performance_zones(self):
        """Assign performance zones based on distance to ideal."""
        distances = self.df['distance_to_ideal']
        zones = []
        
        for dist in distances:
            if dist <= self.zone_boundaries['elite_upper']:
                zones.append('Elite')
            elif dist <= self.zone_boundaries['good_upper']:
                zones.append('Good')
            elif dist <= self.zone_boundaries['fair_upper']:
                zones.append('Fair')
            else:
                zones.append('Poor')
        
        return zones
    
    def identify_pareto_optimal_models(self):
        """Identify Pareto-optimal models (non-dominated solutions)."""
        df = self.df.copy()
        pareto_models = []
        
        if self.verbose:
            print("Identifying Pareto-optimal models...")
        
        for idx, row in df.iterrows():
            # Check if this model is dominated by any other model
            is_dominated = False
            
            for _, other_row in df.iterrows():
                # Other model dominates if it's both more accurate AND more efficient
                if (other_row['final_l2_error'] <= row['final_l2_error'] and 
                    other_row['total_cost'] <= row['total_cost'] and
                    (other_row['final_l2_error'] < row['final_l2_error'] or 
                     other_row['total_cost'] < row['total_cost'])):
                    is_dominated = True
                    break
            
            if not is_dominated:
                pareto_models.append(row.to_dict())
        
        # Sort Pareto models by cost
        pareto_models.sort(key=lambda x: x['total_cost'])
        
        return pareto_models
    
    def _add_ideal_point_overlay(self, ax):
        """Add ideal point and intersection lines to the plot."""
        ideal_cost = self.ideal_point['cost']
        ideal_error = self.ideal_point['error']
        
        # Add intersection lines
        ax.axhline(y=ideal_error, color='blue', linestyle='--', alpha=0.7, 
                  label='Ideal Error', linewidth=2)
        ax.axvline(x=ideal_cost, color='blue', linestyle='--', alpha=0.7, 
                  label='Ideal Cost', linewidth=2)
        
        # Add ideal point
        ax.scatter(ideal_cost, ideal_error, c='blue', s=200, marker='*', 
                  label='Ideal Point', edgecolors='darkblue', linewidths=2, zorder=10)
        
        # Add arrows pointing to ideal point
        arrow_props = dict(arrowstyle='->', color='blue', lw=2, alpha=0.7)
        ax.annotate('', xy=(ideal_cost, ideal_error), 
                   xytext=(ideal_cost + 2000, ideal_error * 1.5),
                   arrowprops=arrow_props)
        ax.annotate('', xy=(ideal_cost, ideal_error), 
                   xytext=(ideal_cost * 1.05, ideal_error * 0.7),
                   arrowprops=arrow_props)
    
    def _add_performance_zones(self, ax):
        """Add performance zone visualization with contour-style boundaries."""
        # Get the data ranges to set appropriate plot limits
        cost_min, cost_max = self.df['total_cost'].min(), self.df['total_cost'].max()
        error_min, error_max = self.df['final_l2_error'].min(), self.df['final_l2_error'].max()
        
        # Add some padding to the limits
        cost_padding = (cost_max - cost_min) * 0.05
        error_padding_factor = (error_max / error_min) ** 0.05
        
        # Set the plot limits to match original data range
        ax.set_xlim(cost_min - cost_padding, cost_max + cost_padding)
        ax.set_ylim(error_min / error_padding_factor, error_max * error_padding_factor)
        
        # Zone visualization using contour-style approach
        zone_colors = ['lightgray', 'darkgray', 'gray', 'dimgray']
        zone_alphas = [0.3, 0.3, 0.3, 0.3]
        zone_labels = ['Elite (0-25%)', 'Good (25-50%)', 'Fair (50-75%)', 'Poor (75-100%)']
        
        # Create a grid of points for zone calculation
        cost_range = np.linspace(cost_min, cost_max, 100)
        error_range = np.logspace(np.log10(error_min), np.log10(error_max), 100)
        Cost_grid, Error_grid = np.meshgrid(cost_range, error_range)
        
        # Calculate distances for the grid
        ideal_cost = self.ideal_point['cost']
        ideal_error = self.ideal_point['error']
        
        # Normalized distance calculation for grid
        cost_norm_grid = (Cost_grid - cost_min) / (cost_max - cost_min)
        error_norm_grid = (np.log(Error_grid) - np.log(error_min)) / (np.log(error_max) - np.log(error_min))
        distance_grid = np.sqrt(cost_norm_grid**2 + error_norm_grid**2)
        
        # Draw zone boundaries as contour lines
        boundaries = [
            self.zone_boundaries['elite_upper'],
            self.zone_boundaries['good_upper'], 
            self.zone_boundaries['fair_upper']
        ]
        
        # Draw contour lines for zone boundaries (no labels)
        for i, boundary in enumerate(boundaries):
            ax.contour(Cost_grid, Error_grid, distance_grid, 
                      levels=[boundary], colors=[zone_colors[i+1]], 
                      alpha=0.6, linewidths=1.5, linestyles='--')
        
        # Add zone shading using filled contours
        zone_contours = ax.contourf(Cost_grid, Error_grid, distance_grid,
                                   levels=[0] + boundaries + [distance_grid.max()],
                                   colors=zone_colors, alpha=0.35, zorder=0)
        
        # Add zone labels INSIDE each zone area (better positioning)
        ideal_cost = self.ideal_point['cost']
        ideal_error = self.ideal_point['error']
        
        # Calculate label positions within each zone's distance range
        cost_range_for_labels = (cost_max - ideal_cost) * 0.3  # Stay closer to ideal
        
        zone_positions = [
            (ideal_cost + cost_range_for_labels * 0.3, ideal_error * 2.5),    # Elite
            (ideal_cost + cost_range_for_labels * 0.25, ideal_error * 4.35),    # Good  
            (ideal_cost + cost_range_for_labels * 0.3, ideal_error * 5.5),   # Fair
            (ideal_cost + cost_range_for_labels * 0.7, ideal_error * 10.0)    # Poor
        ]
        
        for i, (pos_x, pos_y, label) in enumerate(zip([p[0] for p in zone_positions], 
                                                     [p[1] for p in zone_positions], 
                                                     zone_labels)):
            # Only add label if position is within plot bounds
            if pos_x < cost_max and pos_y < error_max:
                ax.text(pos_x, pos_y, label, fontsize=9, alpha=0.7, fontweight='bold',
                       bbox=dict(boxstyle="round,pad=0.2", facecolor="white", alpha=0.8),
                       ha='center', va='center')
        
        # Add zone legend in upper right corner of plot area
        from matplotlib.patches import Rectangle
        legend_elements = []
        for i, (color, alpha, label) in enumerate(zip(zone_colors, [0.15]*4, zone_labels)):
            legend_elements.append(Rectangle((0,0),1,1, facecolor=color, alpha=alpha, label=label))
        
        # Position legend inside plot area, upper right
        zone_legend = ax.legend(handles=legend_elements, loc='center right', 
                              framealpha=0.9, fontsize=8, title='Performance Zones')
        ax.add_artist(zone_legend)  # Keep this legend separate from main legend
    
    def create_comprehensive_plots(self, include_pareto=True, include_ideal=True, 
                                 include_zones=True, output_format='pdf'):
        """
        Create comprehensive parameter family plots with all options.
        
        Args:
            include_pareto (bool): Include Pareto front overlay
            include_ideal (bool): Include ideal point and intersection lines
            include_zones (bool): Include performance zones
            output_format (str): 'pdf', 'png', or 'both'
        """
        # Get Pareto data if needed
        pareto_models = None
        if include_pareto:
            pareto_models = self.identify_pareto_optimal_models()
            pareto_df = pd.DataFrame(pareto_models)
        
        # Create combined family plot
        self._create_combined_family_plot(pareto_models, include_ideal, include_zones, output_format)
        
        # Create individual family plots
        for family_name in self.parameter_families.keys():
            self._create_single_family_plot(family_name, pareto_models, include_ideal, 
                                          include_zones, output_format)
        
        # Create Pareto-only plots if Pareto analysis is enabled
        if include_pareto:
            self._create_pareto_only_plots(pareto_df, include_ideal, include_zones, output_format)
        
        if self.verbose:
            plot_count = len(self.parameter_families) + 1  # Individual + combined
            if include_pareto:
                plot_count += len(self.parameter_families) + 1  # Pareto-only plots
            print(f"Created {plot_count} comprehensive plots")
    
    def _create_combined_family_plot(self, pareto_models, include_ideal, include_zones, output_format):
        """Create combined plot showing all parameter families."""
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        axes = axes.flatten()
        
        for idx, family_name in enumerate(self.parameter_families.keys()):
            family = self.parameter_families[family_name]
            ax = axes[idx]
            
            # Add zones first (if enabled) so they appear behind data
            if include_zones:
                self._add_performance_zones(ax)
            
            # Add ideal point overlay (if enabled)
            if include_ideal:
                self._add_ideal_point_overlay(ax)
            
            # Plot parameter family data
            for i, param_value in enumerate(family['values']):
                mask = self.df[family['vary_param']] == param_value
                subset = self.df[mask]
                
                ax.scatter(subset['total_cost'], subset['final_l2_error'],
                          c=family['colors'][i], s=40, alpha=0.7,
                          label=f"{param_value}",
                          edgecolors='black', linewidths=0.3)
            
            # Add Pareto front if enabled
            if pareto_models is not None:
                pareto_df = pd.DataFrame(pareto_models)
                ax.scatter(pareto_df['total_cost'], pareto_df['final_l2_error'],
                          c='red', s=60, alpha=0.9, marker='*',
                          label='Pareto', edgecolors='darkred', linewidths=1, zorder=5)
                
                # Connect Pareto points
                pareto_sorted = pareto_df.sort_values('total_cost')
                ax.plot(pareto_sorted['total_cost'], pareto_sorted['final_l2_error'],
                       'r--', alpha=0.7, linewidth=1.5, zorder=4)
            
            # Formatting
            ax.set_xlabel('Total Cost', fontsize=10)
            ax.set_ylabel('L2 Error', fontsize=10)
            ax.set_yscale('log')
            ax.grid(True, alpha=0.3)
            ax.legend(fontsize=8, title=family['vary_param'], title_fontsize=9)
            ax.set_title(family['title'], fontsize=11, fontweight='bold')
        
        # Create title
        title_parts = [f'Comprehensive Analysis: {self.sweep_name}']
        if include_zones:
            title_parts.append('Performance Zones')
        if include_ideal:
            title_parts.append('Ideal Point')
        if pareto_models:
            title_parts.append(f'Pareto Front ({len(pareto_models)} models)')
        
        fig.suptitle(' + '.join(title_parts), fontsize=14, fontweight='bold')
        plt.tight_layout()
        
        # Save plot
        filename_base = "comprehensive_combined_families"
        self._save_plot(fig, filename_base, output_format)
        plt.close()
    
    def _create_single_family_plot(self, family_name, pareto_models, include_ideal, 
                                 include_zones, output_format):
        """Create individual family plot with comprehensive features."""
        family = self.parameter_families[family_name]
        
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Add zones first (if enabled)
        if include_zones:
            self._add_performance_zones(ax)
        
        # Add ideal point overlay (if enabled)
        if include_ideal:
            self._add_ideal_point_overlay(ax)
        
        # Plot parameter family data
        for i, param_value in enumerate(family['values']):
            mask = self.df[family['vary_param']] == param_value
            subset = self.df[mask]
            
            ax.scatter(subset['total_cost'], subset['final_l2_error'],
                      c=family['colors'][i], s=60, alpha=0.7,
                      label=f"{family['vary_param']}={param_value}",
                      edgecolors='black', linewidths=0.5)
        
        # Add Pareto front if enabled
        if pareto_models is not None:
            pareto_df = pd.DataFrame(pareto_models)
            ax.scatter(pareto_df['total_cost'], pareto_df['final_l2_error'],
                      c='red', s=100, alpha=0.9, marker='*',
                      label=f"Pareto Optimal (N={len(pareto_df)})",
                      edgecolors='darkred', linewidths=1.5, zorder=5)
            
            # Connect Pareto points
            pareto_sorted = pareto_df.sort_values('total_cost')
            ax.plot(pareto_sorted['total_cost'], pareto_sorted['final_l2_error'],
                   'r--', alpha=0.7, linewidth=2, zorder=4)
        
        # Formatting
        ax.set_xlabel('Total Computational Cost', fontsize=12, fontweight='bold')
        ax.set_ylabel('Final L2 Error', fontsize=12, fontweight='bold')
        ax.set_yscale('log')
        ax.grid(True, alpha=0.3)
        ax.legend(fontsize=10, framealpha=0.9)
        
        # Create title
        title_parts = [family['title']]
        if include_zones:
            title_parts.append('with Performance Zones')
        
        ax.set_title(' '.join(title_parts), fontsize=14, fontweight='bold', pad=20)
        
        plt.tight_layout()
        
        # Save plot
        filename_base = f"comprehensive_{family_name}_family"
        self._save_plot(fig, filename_base, output_format)
        plt.close()
    
    def _create_pareto_only_plots(self, pareto_df, include_ideal, include_zones, output_format):
        """Create plots showing only Pareto-optimal models."""
        # Combined Pareto plot
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        axes = axes.flatten()
        
        for i, (param, family) in enumerate(self.parameter_families.items()):
            ax = axes[i]
            
            # Add zones first (if enabled)
            if include_zones:
                self._add_performance_zones(ax)
            
            # Add ideal point overlay (if enabled)  
            if include_ideal:
                self._add_ideal_point_overlay(ax)
            
            # Group Pareto models by parameter value
            for j, value in enumerate(sorted(pareto_df[param].unique())):
                subset = pareto_df[pareto_df[param] == value]
                ax.scatter(subset['total_cost'], subset['final_l2_error'], 
                          s=100, alpha=0.8, label=f'{param}={value}',
                          c=family['colors'][j % len(family['colors'])])
            
            # Connect Pareto front
            df_sorted = pareto_df.sort_values('total_cost')
            ax.plot(df_sorted['total_cost'], df_sorted['final_l2_error'], 
                   'r--', alpha=0.5, linewidth=2, zorder=1)
            
            ax.set_xlabel('Total Cost')
            ax.set_ylabel('L2 Error')
            ax.set_yscale('log')
            ax.grid(True, alpha=0.3)
            ax.legend(fontsize=8)
            ax.set_title(f'{family["title"]} on Pareto Front', fontweight='bold')
        
        plt.suptitle(f'Pareto Front Analysis: {self.sweep_name}', fontsize=14, fontweight='bold')
        plt.tight_layout()
        
        # Save combined Pareto plot
        filename_base = "comprehensive_pareto_front_analysis"
        self._save_plot(fig, filename_base, output_format)
        plt.close()
    
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
    
    def export_analysis_results(self):
        """Export comprehensive analysis results to JSON."""
        # Zone analysis
        zone_analysis = {}
        for zone in ['Elite', 'Good', 'Fair', 'Poor']:
            zone_models = self.df[self.df['performance_zone'] == zone]
            zone_analysis[zone] = {
                'count': len(zone_models),
                'percentage': len(zone_models) / len(self.df) * 100,
                'distance_range': {
                    'min': float(zone_models['distance_to_ideal'].min()) if len(zone_models) > 0 else None,
                    'max': float(zone_models['distance_to_ideal'].max()) if len(zone_models) > 0 else None
                }
            }
        
        # Parameter distribution by zone
        param_by_zone = {}
        for param in self.parameter_families.keys():
            param_by_zone[param] = {}
            for zone in ['Elite', 'Good', 'Fair', 'Poor']:
                zone_data = self.df[self.df['performance_zone'] == zone]
                if len(zone_data) > 0:
                    param_by_zone[param][zone] = zone_data[param].value_counts().to_dict()
                else:
                    param_by_zone[param][zone] = {}
        
        results = {
            'analysis_type': 'comprehensive_distance_to_ideal',
            'sweep_name': self.sweep_name,
            'total_models': len(self.df),
            'ideal_point': self.ideal_point,
            'zone_boundaries': self.zone_boundaries,
            'zone_analysis': zone_analysis,
            'parameter_distribution_by_zone': param_by_zone,
            'analysis_timestamp': datetime.now().isoformat()
        }
        
        # Save results
        results_path = os.path.join(self.output_dir, 'comprehensive_analysis_results.json')
        with open(results_path, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        
        if self.verbose:
            print(f"Analysis results exported to: {results_path}")
        
        return results

def main():
    """Main function with comprehensive argument parsing."""
    parser = argparse.ArgumentParser(description='Comprehensive analysis of AMR parameter sweep results')
    
    # Required arguments
    parser.add_argument('sweep_name', help='Name of the sweep (e.g., session3_100k_uniform)')
    
    # Plot options
    parser.add_argument('--plot-mode', choices=['pdf', 'png', 'both'], default='pdf',
                       help='Output format for plots')
    
    # Feature toggles
    parser.add_argument('--pareto', action='store_true', default=True,
                       help='Include Pareto front analysis (default: True)')
    parser.add_argument('--no-pareto', dest='pareto', action='store_false',
                       help='Disable Pareto front analysis')
    
    parser.add_argument('--include-ideal', action='store_true', default=True,
                       help='Include ideal point and intersection lines (default: True)')
    parser.add_argument('--no-ideal', dest='include_ideal', action='store_false',
                       help='Disable ideal point visualization')
    
    parser.add_argument('--include-zones', action='store_true', default=True,
                       help='Include performance zones (default: True)')
    parser.add_argument('--no-zones', dest='include_zones', action='store_false',
                       help='Disable performance zone visualization')
    
    # Output options
    parser.add_argument('--verbose', action='store_true', help='Print detailed logs')
    parser.add_argument('--export-results', action='store_true', default=True,
                       help='Export analysis results to JSON (default: True)')
    
    args = parser.parse_args()
    
    # Create analyzer
    analyzer = ComprehensiveAnalyzer(args.sweep_name, verbose=args.verbose)
    
    # Generate comprehensive plots
    analyzer.create_comprehensive_plots(
        include_pareto=args.pareto,
        include_ideal=args.include_ideal,
        include_zones=args.include_zones,
        output_format=args.plot_mode
    )
    
    # Export analysis results
    if args.export_results:
        results = analyzer.export_analysis_results()
    
    print(f"\n=== COMPREHENSIVE ANALYSIS COMPLETE ===")
    print(f"Sweep: {args.sweep_name}")
    print(f"Features: Pareto={args.pareto}, Ideal={args.include_ideal}, Zones={args.include_zones}")
    print(f"Output format: {args.plot_mode}")
    print(f"Results directory: {analyzer.output_dir}")

if __name__ == "__main__":
    main()



# """
# Comprehensive Model Performance Analyzer

# This script provides comprehensive analysis of batch model evaluation results including:
# - Parameter family visualization
# - Pareto front analysis  
# - Distance-to-ideal performance zones
# - Ideal point visualization
# - Flexible output formats

# Usage:
#     python comprehensive_analyzer.py session3_100k_uniform --plot-mode pdf --pareto --include-ideal --include-zones
#     python comprehensive_analyzer.py session3_100k_uniform --plot-mode png --no-pareto --no-ideal --no-zones
# """

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.patches as patches
# import seaborn as sns
# import os
# import sys
# import argparse
# import json
# from pathlib import Path
# from datetime import datetime

# # Get absolute path to project root
# PROJECT_ROOT = os.path.abspath(os.path.join(
#     os.path.dirname(__file__), 
#     '..',
#     '..'
# ))
# sys.path.append(PROJECT_ROOT)

# class ComprehensiveAnalyzer:
#     """
#     Comprehensive analyzer for AMR parameter sweep results with distance-to-ideal zones.
#     """
    
#     def __init__(self, sweep_name, verbose=False):
#         """
#         Initialize the comprehensive analyzer.
        
#         Args:
#             sweep_name (str): Name of the sweep (e.g., 'session3_100k_uniform')
#             verbose (bool): Whether to print detailed logs
#         """
#         self.sweep_name = sweep_name
#         self.verbose = verbose
        
#         # Set up paths
#         self.results_dir = os.path.join(PROJECT_ROOT, 'analysis', 'data', 'model_performance', sweep_name)
#         self.csv_path = os.path.join(self.results_dir, 'batch_results_all_models.csv')
#         self.output_dir = os.path.join(self.results_dir, 'comprehensive_analysis')
        
#         # Create output directory
#         os.makedirs(self.output_dir, exist_ok=True)
        
#         # Load and validate data
#         self.df = self._load_and_validate_data()
        
#         # Calculate ideal point and distances
#         self.ideal_point = self._calculate_ideal_point()
#         self.df['distance_to_ideal'] = self._calculate_distances_to_ideal()
        
#         # Calculate zone boundaries
#         self.zone_boundaries = self._calculate_zone_boundaries()
#         self.df['performance_zone'] = self._assign_performance_zones()
        
#         # Define parameter families (current 4-parameter setup)
#         self.parameter_families = {
#             'gamma_c': {
#                 'vary_param': 'gamma_c',
#                 'fixed_params': ['step_domain_fraction', 'rl_iterations_per_timestep', 'element_budget'],
#                 'values': sorted(self.df['gamma_c'].unique()),
#                 'title': 'Gamma_c Family (Reward Scaling)',
#                 'colors': ['#1f77b4', '#ff7f0e', '#2ca02c']  # Blue, Orange, Green
#             },
#             'step_domain_fraction': {
#                 'vary_param': 'step_domain_fraction', 
#                 'fixed_params': ['gamma_c', 'rl_iterations_per_timestep', 'element_budget'],
#                 'values': sorted(self.df['step_domain_fraction'].unique()),
#                 'title': 'Step Domain Fraction Family (Wave Propagation)',
#                 'colors': ['#d62728', '#9467bd', '#8c564b']  # Red, Purple, Brown
#             },
#             'rl_iterations_per_timestep': {
#                 'vary_param': 'rl_iterations_per_timestep',
#                 'fixed_params': ['gamma_c', 'step_domain_fraction', 'element_budget'], 
#                 'values': sorted(self.df['rl_iterations_per_timestep'].unique()),
#                 'title': 'RL Iterations Family (Adaptation Frequency)',
#                 'colors': ['#e377c2', '#7f7f7f', '#bcbd22']  # Pink, Gray, Olive
#             },
#             'element_budget': {
#                 'vary_param': 'element_budget',
#                 'fixed_params': ['gamma_c', 'step_domain_fraction', 'rl_iterations_per_timestep'],
#                 'values': sorted(self.df['element_budget'].unique()),
#                 'title': 'Element Budget Family (Resource Constraint)', 
#                 'colors': ['#17becf', '#ff7f0e', '#2ca02c']  # Cyan, Orange, Green
#             }
#         }
        
#         if self.verbose:
#             print(f"Loaded {len(self.df)} model results")
#             print(f"Ideal point: Cost={self.ideal_point['cost']:.0f}, Error={self.ideal_point['error']:.2e}")
#             print(f"Distance range: {self.df['distance_to_ideal'].min():.3f} to {self.df['distance_to_ideal'].max():.3f}")
    
#     def _load_and_validate_data(self):
#         """Load and validate the CSV data."""
#         if not os.path.exists(self.csv_path):
#             raise FileNotFoundError(f"Batch results CSV not found: {self.csv_path}")
        
#         df = pd.read_csv(self.csv_path)
        
#         # Validate required columns
#         required_cols = ['gamma_c', 'step_domain_fraction', 'rl_iterations_per_timestep', 
#                         'element_budget', 'final_l2_error', 'total_cost']
#         missing_cols = [col for col in required_cols if col not in df.columns]
#         if missing_cols:
#             raise ValueError(f"Missing required columns: {missing_cols}")
        
#         # Validate data ranges
#         if df['final_l2_error'].min() <= 0:
#             raise ValueError("L2 errors must be positive for log scaling")
        
#         if self.verbose:
#             print(f"Data validation successful")
#             print(f"L2 error range: {df['final_l2_error'].min():.2e} to {df['final_l2_error'].max():.2e}")
#             print(f"Total cost range: {df['total_cost'].min():,} to {df['total_cost'].max():,}")
        
#         return df
    
#     def _calculate_ideal_point(self):
#         """Calculate the ideal point (minimum cost, minimum error intersection)."""
#         ideal_cost = self.df['total_cost'].min()
#         ideal_error = self.df['final_l2_error'].min()
        
#         return {
#             'cost': ideal_cost,
#             'error': ideal_error
#         }
    
#     def _calculate_distances_to_ideal(self):
#         """Calculate normalized Euclidean distances to the ideal point."""
#         # Normalize cost (linear scale)
#         cost_min, cost_max = self.df['total_cost'].min(), self.df['total_cost'].max()
#         cost_norm = (self.df['total_cost'] - cost_min) / (cost_max - cost_min)
        
#         # Normalize error (log scale)
#         log_error = np.log(self.df['final_l2_error'])
#         error_min, error_max = log_error.min(), log_error.max()
#         error_norm = (log_error - error_min) / (error_max - error_min)
        
#         # Calculate Euclidean distance (equal weighting)
#         distances = np.sqrt(cost_norm**2 + error_norm**2)
        
#         return distances
    
#     def _calculate_zone_boundaries(self):
#         """Calculate zone boundaries using percentile approach."""
#         distances = self.df['distance_to_ideal']
#         boundaries = np.percentile(distances, [25, 50, 75])
        
#         return {
#             'elite_upper': boundaries[0],
#             'good_upper': boundaries[1], 
#             'fair_upper': boundaries[2],
#             'poor_upper': distances.max()
#         }
    
#     def _assign_performance_zones(self):
#         """Assign performance zones based on distance to ideal."""
#         distances = self.df['distance_to_ideal']
#         zones = []
        
#         for dist in distances:
#             if dist <= self.zone_boundaries['elite_upper']:
#                 zones.append('Elite')
#             elif dist <= self.zone_boundaries['good_upper']:
#                 zones.append('Good')
#             elif dist <= self.zone_boundaries['fair_upper']:
#                 zones.append('Fair')
#             else:
#                 zones.append('Poor')
        
#         return zones
    
#     def identify_pareto_optimal_models(self):
#         """Identify Pareto-optimal models (non-dominated solutions)."""
#         df = self.df.copy()
#         pareto_models = []
        
#         if self.verbose:
#             print("Identifying Pareto-optimal models...")
        
#         for idx, row in df.iterrows():
#             # Check if this model is dominated by any other model
#             is_dominated = False
            
#             for _, other_row in df.iterrows():
#                 # Other model dominates if it's both more accurate AND more efficient
#                 if (other_row['final_l2_error'] <= row['final_l2_error'] and 
#                     other_row['total_cost'] <= row['total_cost'] and
#                     (other_row['final_l2_error'] < row['final_l2_error'] or 
#                      other_row['total_cost'] < row['total_cost'])):
#                     is_dominated = True
#                     break
            
#             if not is_dominated:
#                 pareto_models.append(row.to_dict())
        
#         # Sort Pareto models by cost
#         pareto_models.sort(key=lambda x: x['total_cost'])
        
#         return pareto_models
    
#     def _add_ideal_point_overlay(self, ax):
#         """Add ideal point and intersection lines to the plot."""
#         ideal_cost = self.ideal_point['cost']
#         ideal_error = self.ideal_point['error']
        
#         # Add intersection lines
#         ax.axhline(y=ideal_error, color='blue', linestyle='--', alpha=0.7, 
#                   label='Ideal Error', linewidth=2)
#         ax.axvline(x=ideal_cost, color='blue', linestyle='--', alpha=0.7, 
#                   label='Ideal Cost', linewidth=2)
        
#         # Add ideal point
#         ax.scatter(ideal_cost, ideal_error, c='blue', s=200, marker='*', 
#                   label='Ideal Point', edgecolors='darkblue', linewidths=2, zorder=10)
        
#         # Add arrows pointing to ideal point
#         arrow_props = dict(arrowstyle='->', color='blue', lw=2, alpha=0.7)
#         ax.annotate('', xy=(ideal_cost, ideal_error), 
#                    xytext=(ideal_cost + 2000, ideal_error * 1.5),
#                    arrowprops=arrow_props)
#         ax.annotate('', xy=(ideal_cost, ideal_error), 
#                    xytext=(ideal_cost * 1.05, ideal_error * 0.7),
#                    arrowprops=arrow_props)
    
#     def _add_performance_zones(self, ax):
#         """Add performance zone visualization with contour-style boundaries."""
#         # Get the data ranges to set appropriate plot limits
#         cost_min, cost_max = self.df['total_cost'].min(), self.df['total_cost'].max()
#         error_min, error_max = self.df['final_l2_error'].min(), self.df['final_l2_error'].max()
        
#         # Add some padding to the limits
#         cost_padding = (cost_max - cost_min) * 0.05
#         error_padding_factor = (error_max / error_min) ** 0.05
        
#         # Set the plot limits to match original data range
#         ax.set_xlim(cost_min - cost_padding, cost_max + cost_padding)
#         ax.set_ylim(error_min / error_padding_factor, error_max * error_padding_factor)
        
#         # Zone visualization using contour-style approach
#         zone_colors = ['lightgray', 'gray', 'darkgray', 'dimgray']
#         zone_alphas = [0.2, 0.3, 0.4, 0.5]
#         zone_labels = ['Elite (0-25%)', 'Good (25-50%)', 'Fair (50-75%)', 'Poor (75-100%)']
        
#         # Create a grid of points for zone calculation
#         cost_range = np.linspace(cost_min, cost_max, 100)
#         error_range = np.logspace(np.log10(error_min), np.log10(error_max), 100)
#         Cost_grid, Error_grid = np.meshgrid(cost_range, error_range)
        
#         # Calculate distances for the grid
#         ideal_cost = self.ideal_point['cost']
#         ideal_error = self.ideal_point['error']
        
#         # Normalized distance calculation for grid
#         cost_norm_grid = (Cost_grid - cost_min) / (cost_max - cost_min)
#         error_norm_grid = (np.log(Error_grid) - np.log(error_min)) / (np.log(error_max) - np.log(error_min))
#         distance_grid = np.sqrt(cost_norm_grid**2 + error_norm_grid**2)
        
#         # Draw zone boundaries as contour lines
#         boundaries = [
#             self.zone_boundaries['elite_upper'],
#             self.zone_boundaries['good_upper'], 
#             self.zone_boundaries['fair_upper']
#         ]
        
#         # Draw contour lines for zone boundaries
#         for i, boundary in enumerate(boundaries):
#             contour = ax.contour(Cost_grid, Error_grid, distance_grid, 
#                                levels=[boundary], colors=[zone_colors[i+1]], 
#                                alpha=0.8, linewidths=2, linestyles='--')
            
#             # Add zone labels on the contour lines
#             if i == 0:  # Elite boundary
#                 ax.clabel(contour, inline=True, fontsize=9, fmt='Elite Zone')
#             elif i == 2:  # Fair boundary  
#                 ax.clabel(contour, inline=True, fontsize=9, fmt='Poor Zone')
        
#         # Alternative: Add zone shading using filled contours
#         # This creates background shading between zone boundaries
#         zone_contours = ax.contourf(Cost_grid, Error_grid, distance_grid,
#                                    levels=[0] + boundaries + [distance_grid.max()],
#                                    colors=zone_colors, alpha=0.1, zorder=0)
        
#         # Add a subtle zone legend
#         from matplotlib.patches import Rectangle
#         legend_elements = []
#         for i, (color, alpha, label) in enumerate(zip(zone_colors, [0.1]*4, zone_labels)):
#             legend_elements.append(Rectangle((0,0),1,1, facecolor=color, alpha=alpha, label=label))
        
#         # Add zone legend in upper right
#         zone_legend = ax.legend(handles=legend_elements, loc='upper right', 
#                               framealpha=0.9, fontsize=8, title='Performance Zones')
#         ax.add_artist(zone_legend)  # Keep this legend separate from main legend
    
#     def create_comprehensive_plots(self, include_pareto=True, include_ideal=True, 
#                                  include_zones=True, output_format='pdf'):
#         """
#         Create comprehensive parameter family plots with all options.
        
#         Args:
#             include_pareto (bool): Include Pareto front overlay
#             include_ideal (bool): Include ideal point and intersection lines
#             include_zones (bool): Include performance zones
#             output_format (str): 'pdf', 'png', or 'both'
#         """
#         # Get Pareto data if needed
#         pareto_models = None
#         if include_pareto:
#             pareto_models = self.identify_pareto_optimal_models()
#             pareto_df = pd.DataFrame(pareto_models)
        
#         # Create combined family plot
#         self._create_combined_family_plot(pareto_models, include_ideal, include_zones, output_format)
        
#         # Create individual family plots
#         for family_name in self.parameter_families.keys():
#             self._create_single_family_plot(family_name, pareto_models, include_ideal, 
#                                           include_zones, output_format)
        
#         # Create Pareto-only plots if Pareto analysis is enabled
#         if include_pareto:
#             self._create_pareto_only_plots(pareto_df, include_ideal, include_zones, output_format)
        
#         if self.verbose:
#             plot_count = len(self.parameter_families) + 1  # Individual + combined
#             if include_pareto:
#                 plot_count += len(self.parameter_families) + 1  # Pareto-only plots
#             print(f"Created {plot_count} comprehensive plots")
    
#     def _create_combined_family_plot(self, pareto_models, include_ideal, include_zones, output_format):
#         """Create combined plot showing all parameter families."""
#         fig, axes = plt.subplots(2, 2, figsize=(16, 12))
#         axes = axes.flatten()
        
#         for idx, family_name in enumerate(self.parameter_families.keys()):
#             family = self.parameter_families[family_name]
#             ax = axes[idx]
            
#             # Add zones first (if enabled) so they appear behind data
#             if include_zones:
#                 self._add_performance_zones(ax)
            
#             # Add ideal point overlay (if enabled)
#             if include_ideal:
#                 self._add_ideal_point_overlay(ax)
            
#             # Plot parameter family data
#             for i, param_value in enumerate(family['values']):
#                 mask = self.df[family['vary_param']] == param_value
#                 subset = self.df[mask]
                
#                 ax.scatter(subset['total_cost'], subset['final_l2_error'],
#                           c=family['colors'][i], s=40, alpha=0.7,
#                           label=f"{param_value}",
#                           edgecolors='black', linewidths=0.3)
            
#             # Add Pareto front if enabled
#             if pareto_models is not None:
#                 pareto_df = pd.DataFrame(pareto_models)
#                 ax.scatter(pareto_df['total_cost'], pareto_df['final_l2_error'],
#                           c='red', s=60, alpha=0.9, marker='*',
#                           label='Pareto', edgecolors='darkred', linewidths=1, zorder=5)
                
#                 # Connect Pareto points
#                 pareto_sorted = pareto_df.sort_values('total_cost')
#                 ax.plot(pareto_sorted['total_cost'], pareto_sorted['final_l2_error'],
#                        'r--', alpha=0.7, linewidth=1.5, zorder=4)
            
#             # Formatting
#             ax.set_xlabel('Total Cost', fontsize=10)
#             ax.set_ylabel('L2 Error', fontsize=10)
#             ax.set_yscale('log')
#             ax.grid(True, alpha=0.3)
#             ax.legend(fontsize=8, title=family['vary_param'], title_fontsize=9)
#             ax.set_title(family['title'], fontsize=11, fontweight='bold')
        
#         # Create title
#         title_parts = [f'Comprehensive Analysis: {self.sweep_name}']
#         if include_zones:
#             title_parts.append('Performance Zones')
#         if include_ideal:
#             title_parts.append('Ideal Point')
#         if pareto_models:
#             title_parts.append(f'Pareto Front ({len(pareto_models)} models)')
        
#         fig.suptitle(' + '.join(title_parts), fontsize=14, fontweight='bold')
#         plt.tight_layout()
        
#         # Save plot
#         filename_base = "comprehensive_combined_families"
#         self._save_plot(fig, filename_base, output_format)
#         plt.close()
    
#     def _create_single_family_plot(self, family_name, pareto_models, include_ideal, 
#                                  include_zones, output_format):
#         """Create individual family plot with comprehensive features."""
#         family = self.parameter_families[family_name]
        
#         fig, ax = plt.subplots(figsize=(10, 8))
        
#         # Add zones first (if enabled)
#         if include_zones:
#             self._add_performance_zones(ax)
        
#         # Add ideal point overlay (if enabled)
#         if include_ideal:
#             self._add_ideal_point_overlay(ax)
        
#         # Plot parameter family data
#         for i, param_value in enumerate(family['values']):
#             mask = self.df[family['vary_param']] == param_value
#             subset = self.df[mask]
            
#             ax.scatter(subset['total_cost'], subset['final_l2_error'],
#                       c=family['colors'][i], s=60, alpha=0.7,
#                       label=f"{family['vary_param']}={param_value}",
#                       edgecolors='black', linewidths=0.5)
        
#         # Add Pareto front if enabled
#         if pareto_models is not None:
#             pareto_df = pd.DataFrame(pareto_models)
#             ax.scatter(pareto_df['total_cost'], pareto_df['final_l2_error'],
#                       c='red', s=100, alpha=0.9, marker='*',
#                       label=f"Pareto Optimal (N={len(pareto_df)})",
#                       edgecolors='darkred', linewidths=1.5, zorder=5)
            
#             # Connect Pareto points
#             pareto_sorted = pareto_df.sort_values('total_cost')
#             ax.plot(pareto_sorted['total_cost'], pareto_sorted['final_l2_error'],
#                    'r--', alpha=0.7, linewidth=2, zorder=4)
        
#         # Formatting
#         ax.set_xlabel('Total Computational Cost', fontsize=12, fontweight='bold')
#         ax.set_ylabel('Final L2 Error', fontsize=12, fontweight='bold')
#         ax.set_yscale('log')
#         ax.grid(True, alpha=0.3)
#         ax.legend(fontsize=10, framealpha=0.9)
        
#         # Create title
#         title_parts = [family['title']]
#         if include_zones:
#             title_parts.append('with Performance Zones')
        
#         ax.set_title(' '.join(title_parts), fontsize=14, fontweight='bold', pad=20)
        
#         plt.tight_layout()
        
#         # Save plot
#         filename_base = f"comprehensive_{family_name}_family"
#         self._save_plot(fig, filename_base, output_format)
#         plt.close()
    
#     def _create_pareto_only_plots(self, pareto_df, include_ideal, include_zones, output_format):
#         """Create plots showing only Pareto-optimal models."""
#         # Combined Pareto plot
#         fig, axes = plt.subplots(2, 2, figsize=(14, 10))
#         axes = axes.flatten()
        
#         for i, (param, family) in enumerate(self.parameter_families.items()):
#             ax = axes[i]
            
#             # Add zones first (if enabled)
#             if include_zones:
#                 self._add_performance_zones(ax)
            
#             # Add ideal point overlay (if enabled)  
#             if include_ideal:
#                 self._add_ideal_point_overlay(ax)
            
#             # Group Pareto models by parameter value
#             for j, value in enumerate(sorted(pareto_df[param].unique())):
#                 subset = pareto_df[pareto_df[param] == value]
#                 ax.scatter(subset['total_cost'], subset['final_l2_error'], 
#                           s=100, alpha=0.8, label=f'{param}={value}',
#                           c=family['colors'][j % len(family['colors'])])
            
#             # Connect Pareto front
#             df_sorted = pareto_df.sort_values('total_cost')
#             ax.plot(df_sorted['total_cost'], df_sorted['final_l2_error'], 
#                    'r--', alpha=0.5, linewidth=2, zorder=1)
            
#             ax.set_xlabel('Total Cost')
#             ax.set_ylabel('L2 Error')
#             ax.set_yscale('log')
#             ax.grid(True, alpha=0.3)
#             ax.legend(fontsize=8)
#             ax.set_title(f'{family["title"]} on Pareto Front', fontweight='bold')
        
#         plt.suptitle(f'Pareto Front Analysis: {self.sweep_name}', fontsize=14, fontweight='bold')
#         plt.tight_layout()
        
#         # Save combined Pareto plot
#         filename_base = "comprehensive_pareto_front_analysis"
#         self._save_plot(fig, filename_base, output_format)
#         plt.close()
    
#     def _save_plot(self, fig, filename_base, output_format):
#         """Save plot in specified format(s)."""
#         if output_format in ['pdf', 'both']:
#             pdf_path = os.path.join(self.output_dir, f"{filename_base}.pdf")
#             fig.savefig(pdf_path, format='pdf', dpi=300, bbox_inches='tight')
#             if self.verbose:
#                 print(f"Saved: {pdf_path}")
        
#         if output_format in ['png', 'both']:
#             png_path = os.path.join(self.output_dir, f"{filename_base}.png")
#             fig.savefig(png_path, format='png', dpi=300, bbox_inches='tight')
#             if self.verbose:
#                 print(f"Saved: {png_path}")
    
#     def export_analysis_results(self):
#         """Export comprehensive analysis results to JSON."""
#         # Zone analysis
#         zone_analysis = {}
#         for zone in ['Elite', 'Good', 'Fair', 'Poor']:
#             zone_models = self.df[self.df['performance_zone'] == zone]
#             zone_analysis[zone] = {
#                 'count': len(zone_models),
#                 'percentage': len(zone_models) / len(self.df) * 100,
#                 'distance_range': {
#                     'min': float(zone_models['distance_to_ideal'].min()) if len(zone_models) > 0 else None,
#                     'max': float(zone_models['distance_to_ideal'].max()) if len(zone_models) > 0 else None
#                 }
#             }
        
#         # Parameter distribution by zone
#         param_by_zone = {}
#         for param in self.parameter_families.keys():
#             param_by_zone[param] = {}
#             for zone in ['Elite', 'Good', 'Fair', 'Poor']:
#                 zone_data = self.df[self.df['performance_zone'] == zone]
#                 if len(zone_data) > 0:
#                     param_by_zone[param][zone] = zone_data[param].value_counts().to_dict()
#                 else:
#                     param_by_zone[param][zone] = {}
        
#         results = {
#             'analysis_type': 'comprehensive_distance_to_ideal',
#             'sweep_name': self.sweep_name,
#             'total_models': len(self.df),
#             'ideal_point': self.ideal_point,
#             'zone_boundaries': self.zone_boundaries,
#             'zone_analysis': zone_analysis,
#             'parameter_distribution_by_zone': param_by_zone,
#             'analysis_timestamp': datetime.now().isoformat()
#         }
        
#         # Save results
#         results_path = os.path.join(self.output_dir, 'comprehensive_analysis_results.json')
#         with open(results_path, 'w') as f:
#             json.dump(results, f, indent=2, default=str)
        
#         if self.verbose:
#             print(f"Analysis results exported to: {results_path}")
        
#         return results

# def main():
#     """Main function with comprehensive argument parsing."""
#     parser = argparse.ArgumentParser(description='Comprehensive analysis of AMR parameter sweep results')
    
#     # Required arguments
#     parser.add_argument('sweep_name', help='Name of the sweep (e.g., session3_100k_uniform)')
    
#     # Plot options
#     parser.add_argument('--plot-mode', choices=['pdf', 'png', 'both'], default='pdf',
#                        help='Output format for plots')
    
#     # Feature toggles
#     parser.add_argument('--pareto', action='store_true', default=True,
#                        help='Include Pareto front analysis (default: True)')
#     parser.add_argument('--no-pareto', dest='pareto', action='store_false',
#                        help='Disable Pareto front analysis')
    
#     parser.add_argument('--include-ideal', action='store_true', default=True,
#                        help='Include ideal point and intersection lines (default: True)')
#     parser.add_argument('--no-ideal', dest='include_ideal', action='store_false',
#                        help='Disable ideal point visualization')
    
#     parser.add_argument('--include-zones', action='store_true', default=True,
#                        help='Include performance zones (default: True)')
#     parser.add_argument('--no-zones', dest='include_zones', action='store_false',
#                        help='Disable performance zone visualization')
    
#     # Output options
#     parser.add_argument('--verbose', action='store_true', help='Print detailed logs')
#     parser.add_argument('--export-results', action='store_true', default=True,
#                        help='Export analysis results to JSON (default: True)')
    
#     args = parser.parse_args()
    
#     # Create analyzer
#     analyzer = ComprehensiveAnalyzer(args.sweep_name, verbose=args.verbose)
    
#     # Generate comprehensive plots
#     analyzer.create_comprehensive_plots(
#         include_pareto=args.pareto,
#         include_ideal=args.include_ideal,
#         include_zones=args.include_zones,
#         output_format=args.plot_mode
#     )
    
#     # Export analysis results
#     if args.export_results:
#         results = analyzer.export_analysis_results()
    
#     print(f"\n=== COMPREHENSIVE ANALYSIS COMPLETE ===")
#     print(f"Sweep: {args.sweep_name}")
#     print(f"Features: Pareto={args.pareto}, Ideal={args.include_ideal}, Zones={args.include_zones}")
#     print(f"Output format: {args.plot_mode}")
#     print(f"Results directory: {analyzer.output_dir}")

# if __name__ == "__main__":
#     main()




