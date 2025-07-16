#!/usr/bin/env python3
"""
Pingouin-Based ANOVA Analysis for AMR Parameter Optimization
Designed to run directly on HPC using raw training data files.
FIXED VERSION with proper data cleaning.
"""

import pandas as pd
import numpy as np
import os
import sys
import json
import glob
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

# Statistical analysis with Pingouin
import pingouin as pg
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

class HPC_ANOVAAnalyzer:
    """
    HPC-ready ANOVA analysis using Pingouin library.
    Reads training data directly from HPC results directory.
    FIXED VERSION with robust data cleaning.
    """
    
    def __init__(self, sweep_name: str, results_base_dir: str = "./results"):
        self.sweep_name = sweep_name
        self.results_dir = os.path.join(results_base_dir, sweep_name)
        self.df = None
        self.anova_results = {}
        
        # Analysis configuration
        self.factors = ['gamma_c', 'step_domain_fraction', 'rl_iterations_per_timestep', 'element_budget']
        self.response_variables = [
            'final_episode_reward_mean',
            'convergence_score', 
            'episodes_completed',
            'training_duration_hours',
            'budget_exceeded_percentage',
            'mean_resource_usage'
        ]
        
        # Create output directory
        self.output_dir = f"anova_results_{sweep_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        os.makedirs(self.output_dir, exist_ok=True)
        
        print(f"🎯 HPC ANOVA Analyzer initialized (FIXED VERSION)")
        print(f"📁 Results directory: {self.results_dir}")
        print(f"📊 Output directory: {self.output_dir}")
    
    def load_hpc_data(self) -> pd.DataFrame:
        """Load training data directly from HPC results directory."""
        
        print(f"🔍 Loading data from {self.results_dir}")
        
        # Verify results directory exists
        if not os.path.exists(self.results_dir):
            raise FileNotFoundError(f"Results directory not found: {self.results_dir}")
        
        # Find all parameter combination directories
        param_dirs = [d for d in os.listdir(self.results_dir) 
                     if os.path.isdir(os.path.join(self.results_dir, d)) 
                     and d.startswith('gamma_')]
        
        if len(param_dirs) == 0:
            raise ValueError(f"No parameter directories found in {self.results_dir}")
        
        print(f"📂 Found {len(param_dirs)} parameter combinations")
        
        # Load data from each parameter combination
        data_rows = []
        failed_loads = []
        
        for param_dir in param_dirs:
            dir_path = os.path.join(self.results_dir, param_dir)
            
            # Parse parameters from directory name
            params = self._parse_parameter_dir_name(param_dir)
            if params is None:
                print(f"⚠️ Skipping invalid directory name: {param_dir}")
                continue
            
            # Find training metrics files
            json_files = glob.glob(os.path.join(dir_path, "*_training_metrics.json"))
            csv_files = glob.glob(os.path.join(dir_path, "*_training_summary.csv"))
            
            if len(json_files) == 0 and len(csv_files) == 0:
                print(f"⚠️ No training data files found in {param_dir}")
                continue
            
            # Load metrics from JSON (preferred) or CSV
            metrics = None
            if json_files:
                metrics = self._load_json_metrics(json_files[0])
            elif csv_files:
                metrics = self._load_csv_metrics(csv_files[0])
            
            if metrics is None:
                failed_loads.append(param_dir)
                continue
            
            # Combine parameters and metrics
            row_data = {**params, **metrics}
            data_rows.append(row_data)
        
        # Report loading results
        print(f"✅ Successfully loaded: {len(data_rows)}/{len(param_dirs)} parameter combinations")
        if failed_loads:
            print(f"⚠️ Failed to load: {len(failed_loads)} combinations")
        
        # Create DataFrame
        if len(data_rows) == 0:
            raise ValueError("No valid training data found")
        
        self.df = pd.DataFrame(data_rows)
        
        # Clean the data
        self.df = self._clean_data(self.df)
        
        # Validate required columns
        missing_factors = [f for f in self.factors if f not in self.df.columns]
        missing_responses = [r for r in self.response_variables if r not in self.df.columns]
        
        if missing_factors:
            raise ValueError(f"Missing parameter columns: {missing_factors}")
        
        if missing_responses:
            print(f"⚠️ Missing response variables: {missing_responses}")
            self.response_variables = [r for r in self.response_variables if r in self.df.columns]
        
        # Final data quality check
        self._check_data_quality()
        
        print(f"✅ Data loaded successfully: {len(self.df)} observations")
        print(f"📊 Parameters: {self.factors}")
        print(f"📈 Response variables: {self.response_variables}")
        
        return self.df
    
    def _parse_parameter_dir_name(self, dir_name: str) -> Optional[Dict]:
        """Parse parameter values from directory name."""
        # Expected format: gamma_25.0_step_0.025_rl_10_budget_25
        try:
            parts = dir_name.split('_')
            if len(parts) != 8:  # gamma, 25.0, step, 0.025, rl, 10, budget, 25
                return None
            
            return {
                'gamma_c': float(parts[1]),
                'step_domain_fraction': float(parts[3]),
                'rl_iterations_per_timestep': int(parts[5]),
                'element_budget': int(parts[7])
            }
        except (ValueError, IndexError):
            return None
    
    def _load_json_metrics(self, json_path: str) -> Optional[Dict]:
        """Load training metrics from JSON file with robust cleaning."""
        try:
            with open(json_path, 'r') as f:
                data = json.load(f)
            
            # Direct mapping from your JSON structure
            metric_mappings = {
                'final_episode_reward_mean': 'final_episode_reward_mean',
                'convergence_score': 'convergence_score',
                'episodes_completed': 'episodes_completed',
                'training_duration_hours': 'training_duration_hours',
                'budget_exceeded_percentage': 'budget_exceeded_percentage',
                'mean_resource_usage': 'mean_resource_usage'
            }
            
            metrics = {}
            
            for target_name, json_key in metric_mappings.items():
                if json_key in data:
                    value = data[json_key]
                    # Clean the data - handle NaN, inf, None, and string values
                    cleaned_value = self._clean_numeric_value(value, json_key, json_path)
                    if cleaned_value is not None:
                        metrics[target_name] = cleaned_value
            
            return metrics if metrics else None
            
        except (json.JSONDecodeError, FileNotFoundError, KeyError) as e:
            print(f"Error loading JSON {json_path}: {e}")
            return None
    
    def _clean_numeric_value(self, value, field_name: str, source_path: str) -> Optional[float]:
        """Clean and validate a numeric value."""
        if value is None:
            return None
        
        try:
            # Convert to float
            numeric_value = float(value)
            
            # Check for NaN or infinite values
            if not np.isfinite(numeric_value):
                return None
            
            return numeric_value
            
        except (ValueError, TypeError):
            # Handle string values or other non-numeric types
            return None
    
    def _load_csv_metrics(self, csv_path: str) -> Optional[Dict]:
        """Load training metrics from CSV file (fallback)."""
        try:
            df = pd.read_csv(csv_path)
            if len(df) == 0:
                return None
            
            # Take the last row (final metrics)
            row = df.iloc[-1]
            
            metrics = {}
            for response_var in self.response_variables:
                if response_var in row.index:
                    cleaned_value = self._clean_numeric_value(row[response_var], response_var, csv_path)
                    if cleaned_value is not None:
                        metrics[response_var] = cleaned_value
            
            return metrics if metrics else None
            
        except (pd.errors.EmptyDataError, FileNotFoundError, KeyError) as e:
            print(f"Error loading CSV {csv_path}: {e}")
            return None
    
    def _clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Clean data by handling NaN, infinite, and problematic values."""
        
        print(f"🧹 Cleaning data...")
        original_rows = len(df)
        
        # Remove rows with NaN in parameter columns
        df = df.dropna(subset=self.factors)
        rows_after_param_clean = len(df)
        
        # For response variables, handle NaN and infinite values
        for response in self.response_variables:
            if response in df.columns:
                # Replace infinite values with NaN
                df[response] = pd.to_numeric(df[response], errors='coerce')
                df[response] = df[response].replace([np.inf, -np.inf], np.nan)
                
                # Count problematic values
                nan_count = df[response].isna().sum()
                if nan_count > 0:
                    print(f"   ⚠️ {response}: {nan_count}/{len(df)} NaN/invalid values")
        
        # Remove response variables with too many NaN values (>50%)
        valid_responses = []
        for response in self.response_variables:
            if response in df.columns:
                valid_count = df[response].notna().sum()
                valid_ratio = valid_count / len(df)
                if valid_ratio < 0.5:
                    print(f"   ❌ Removing {response}: only {valid_ratio:.1%} valid values")
                else:
                    valid_responses.append(response)
                    print(f"   ✅ Keeping {response}: {valid_ratio:.1%} valid values")
        
        self.response_variables = valid_responses
        
        param_removed = original_rows - rows_after_param_clean
        if param_removed > 0:
            print(f"   📊 Removed {param_removed} rows with missing parameters")
        
        print(f"   📊 Final cleaned data: {len(df)} rows")
        return df
    
    def _check_data_quality(self):
        """Check data quality and report issues."""
        
        print(f"🔍 Data Quality Check:")
        
        for response in self.response_variables:
            if response in self.df.columns:
                data = self.df[response].dropna()
                
                if len(data) == 0:
                    print(f"   ❌ {response}: No valid data")
                    continue
                
                # Check for zero variance
                if len(data.unique()) == 1:
                    print(f"   ⚠️ {response}: Zero variance (all values = {data.iloc[0]:.6f})")
                    continue
                
                # Check data range and basic stats
                variance = data.var()
                print(f"   ✅ {response}: n={len(data)}, range=[{data.min():.6f}, {data.max():.6f}], var={variance:.6f}")
    
    def run_pingouin_anova(self) -> Dict:
        """Run factorial ANOVA using Pingouin for all response variables."""
        
        print(f"\n🎯 Running Pingouin ANOVA Analysis")
        print("=" * 60)
        
        if self.df is None:
            self.load_hpc_data()
        
        anova_results = {}
        
        for response in self.response_variables:
            print(f"\n📊 Analyzing: {response}")
            
            # Create a clean dataset for this response variable
            analysis_df = self.df[[response] + self.factors].dropna()
            
            # Check if we have enough valid data
            if len(analysis_df) < 10:
                print(f"   ❌ Insufficient data: only {len(analysis_df)} complete observations")
                anova_results[response] = {'error': 'Insufficient complete data'}
                continue
            
            # Check for zero variance
            if analysis_df[response].var() == 0:
                print(f"   ❌ Zero variance: all values are {analysis_df[response].iloc[0]}")
                anova_results[response] = {'error': 'Zero variance in response variable'}
                continue
            
            # Check for sufficient variability in factors
            factor_issues = []
            for factor in self.factors:
                unique_vals = analysis_df[factor].nunique()
                if unique_vals < 2:
                    factor_issues.append(f"{factor} has only {unique_vals} unique value(s)")
            
            if factor_issues:
                print(f"   ❌ Factor issues: {'; '.join(factor_issues)}")
                anova_results[response] = {'error': f"Factor variability issues: {'; '.join(factor_issues)}"}
                continue
            
            try:
                # Run factorial ANOVA with Pingouin
                print(f"   Running ANOVA with {len(analysis_df)} observations...")
                
                aov = pg.anova(data=analysis_df, 
                              dv=response, 
                              between=self.factors,
                              detailed=True)
                
                # Store results
                anova_results[response] = {
                    'anova_table': aov,
                    'significant_factors': self._identify_significant_factors(aov),
                    'effect_sizes': self._extract_effect_sizes(aov),
                    'interpretation': self._interpret_anova_results(response, aov),
                    'n_observations': len(analysis_df)
                }
                
                # Print summary
                print(f"✅ ANOVA completed for {response} (n={len(analysis_df)})")
                sig_factors = anova_results[response]['significant_factors']
                if sig_factors:
                    print(f"   Significant factors (p<0.05): {', '.join(sig_factors)}")
                else:
                    print(f"   No significant factors at α = 0.05")
                
            except Exception as e:
                print(f"❌ Error in ANOVA for {response}: {e}")
                anova_results[response] = {'error': str(e)}
        
        self.anova_results = anova_results
        return anova_results
    
    def _identify_significant_factors(self, anova_table: pd.DataFrame) -> List[str]:
        """Identify statistically significant factors."""
        if 'p-unc' not in anova_table.columns:
            return []
        
        significant = anova_table[anova_table['p-unc'] < 0.05]
        # Filter out interaction terms and residual
        main_effects = [idx for idx in significant.index 
                       if ':' not in str(idx) and 'Residual' not in str(idx)]
        return main_effects
    
    def _extract_effect_sizes(self, anova_table: pd.DataFrame) -> Dict:
        """Extract effect sizes from ANOVA table."""
        effect_sizes = {}
        
        # Calculate partial eta-squared
        if 'SS' in anova_table.columns:
            total_ss = anova_table['SS'].sum()
            
            for idx, row in anova_table.iterrows():
                if 'Residual' not in str(idx):
                    effect_size = row['SS'] / total_ss
                    
                    # Classify effect size magnitude
                    if effect_size < 0.01:
                        magnitude = "Negligible"
                    elif effect_size < 0.06:
                        magnitude = "Small"
                    elif effect_size < 0.14:
                        magnitude = "Medium"
                    else:
                        magnitude = "Large"
                    
                    effect_sizes[str(idx)] = {
                        'eta_squared': effect_size,
                        'percentage_variance': effect_size * 100,
                        'magnitude': magnitude
                    }
        
        return effect_sizes
    
    def _interpret_anova_results(self, response: str, anova_table: pd.DataFrame) -> str:
        """Generate interpretation of ANOVA results."""
        significant_factors = self._identify_significant_factors(anova_table)
        
        if significant_factors:
            interpretation = f"Significant factors affecting {response}: {', '.join(significant_factors)}"
        else:
            interpretation = f"No factors significantly affect {response} at α = 0.05"
        
        return interpretation
    
    def generate_visualizations(self):
        """Generate thesis-quality visualizations."""
        
        print(f"\n🎨 Generating visualizations...")
        
        if not self.anova_results:
            print("⚠️ No ANOVA results to visualize. Run analysis first.")
            return
        
        # Create comprehensive PDF report
        pdf_path = os.path.join(self.output_dir, f"pingouin_anova_results_{self.sweep_name}.pdf")
        
        with PdfPages(pdf_path) as pdf:
            # 1. Overview page
            self._create_overview_page(pdf)
            
            # 2. Main effects plots for each successful response variable
            successful_responses = [r for r, res in self.anova_results.items() 
                                  if 'anova_table' in res]
            
            for response in successful_responses:
                self._create_main_effects_plot(response, pdf)
            
            # 3. Effect sizes summary (only if we have successful analyses)
            if successful_responses:
                self._create_effect_sizes_summary(pdf)
        
        print(f"📊 Visualizations saved: {pdf_path}")
    
    def _create_overview_page(self, pdf):
        """Create analysis overview page."""
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
        
        # 1. Parameter space visualization
        param_counts = [3, 3, 3, 3]  # All factors have 3 levels
        ax1.bar(range(len(self.factors)), param_counts, color='skyblue')
        ax1.set_xlabel('Factors')
        ax1.set_ylabel('Number of Levels')
        ax1.set_title('Experimental Design: Factor Levels')
        ax1.set_xticks(range(len(self.factors)))
        ax1.set_xticklabels([f.replace('_', '\n') for f in self.factors], rotation=0)
        
        # 2. Analysis success summary
        ax2.axis('off')
        
        # Count successful vs failed analyses
        successful = len([r for r, res in self.anova_results.items() if 'anova_table' in res])
        failed = len([r for r, res in self.anova_results.items() if 'error' in res])
        total_attempted = len(self.response_variables)
        
        summary_text = f"""
        Pingouin ANOVA Analysis Summary
        
        Study Design:
        • {len(self.df)} total observations
        • {len(self.factors)} factors (parameters)
        • Complete factorial design (3^4 = 81)
        
        Analysis Results:
        • Variables attempted: {total_attempted}
        • Successful analyses: {successful}
        • Failed analyses: {failed}
        
        Factors:
        • gamma_c: {{25.0, 50.0, 100.0}}
        • step_domain_fraction: {{0.025, 0.05, 0.1}}
        • rl_iterations_per_timestep: {{10, 25, 40}}
        • element_budget: {{25, 30, 40}}
        """
        
        ax2.text(0.1, 0.9, summary_text, transform=ax2.transAxes, fontsize=11,
                verticalalignment='top', fontfamily='monospace',
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.1))
        
        # 3. Significant effects count
        sig_factor_counts = {}
        for factor in self.factors:
            count = sum(1 for response, results in self.anova_results.items() 
                       if 'significant_factors' in results and factor in results['significant_factors'])
            sig_factor_counts[factor] = count
        
        if any(sig_factor_counts.values()):
            ax3.bar(range(len(sig_factor_counts)), list(sig_factor_counts.values()), 
                    color='lightcoral')
            ax3.set_xlabel('Factors')
            ax3.set_ylabel('Number of Significant Effects')
            ax3.set_title('Parameter Significance Across Metrics')
            ax3.set_xticks(range(len(sig_factor_counts)))
            ax3.set_xticklabels([f.replace('_', '\n') for f in sig_factor_counts.keys()], rotation=0)
        else:
            ax3.text(0.5, 0.5, 'No significant effects\nfound at α = 0.05', 
                    ha='center', va='center', transform=ax3.transAxes, fontsize=12)
            ax3.set_title('Parameter Significance Across Metrics')
        
        # 4. Sample data distributions (for successful variables only)
        successful_vars = [r for r in self.response_variables 
                          if r in self.df.columns and r in self.anova_results 
                          and 'anova_table' in self.anova_results[r]]
        
        if successful_vars:
            colors = plt.cm.Set3(np.linspace(0, 1, len(successful_vars)))
            for i, response in enumerate(successful_vars[:4]):  # Show max 4
                data = self.df[response].dropna()
                ax4.hist(data, alpha=0.6, bins=15, 
                        label=response.replace('_', ' ')[:15], color=colors[i])
            ax4.set_xlabel('Value')
            ax4.set_ylabel('Frequency')
            ax4.set_title('Response Variable Distributions')
            ax4.legend(fontsize=8)
        else:
            ax4.text(0.5, 0.5, 'No valid response\nvariables for display', 
                    ha='center', va='center', transform=ax4.transAxes, fontsize=12)
            ax4.set_title('Response Variable Distributions')
        
        plt.suptitle(f'Pingouin ANOVA Analysis Overview - {self.sweep_name}', 
                    fontsize=16, fontweight='bold')
        plt.tight_layout()
        pdf.savefig(bbox_inches='tight', dpi=300)
        plt.close()
    
    def _create_main_effects_plot(self, response: str, pdf):
        """Create main effects plot for a response variable."""
        
        # Use clean data for this response
        plot_df = self.df[[response] + self.factors].dropna()
        
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        axes = axes.flatten()
        
        for i, factor in enumerate(self.factors):
            ax = axes[i]
            
            # Calculate means and standard errors for each factor level
            factor_stats = plot_df.groupby(factor)[response].agg(['mean', 'sem']).reset_index()
            
            # Plot main effects
            ax.errorbar(factor_stats[factor], factor_stats['mean'], 
                       yerr=factor_stats['sem'], marker='o', linewidth=2, markersize=8,
                       capsize=5, capthick=2)
            
            ax.set_xlabel(factor.replace('_', ' ').title())
            ax.set_ylabel(response.replace('_', ' ').title())
            ax.grid(True, alpha=0.3)
            
            # Check if factor is significant
            is_significant = (response in self.anova_results and 
                            'significant_factors' in self.anova_results[response] and
                            factor in self.anova_results[response]['significant_factors'])
            
            title = f"{factor.replace('_', ' ').title()}"
            if is_significant:
                title += " *"
                ax.tick_params(axis='both', colors='red', labelsize=10)
                ax.spines['top'].set_color('red')
                ax.spines['right'].set_color('red')
                ax.spines['bottom'].set_color('red')
                ax.spines['left'].set_color('red')
            
            ax.set_title(title, fontweight='bold' if is_significant else 'normal')
        
        plt.suptitle(f'Main Effects: {response.replace("_", " ").title()}\n(* indicates p < 0.05)', 
                    fontsize=14, fontweight='bold')
        plt.tight_layout()
        pdf.savefig(bbox_inches='tight', dpi=300)
        plt.close()
    
    def _create_effect_sizes_summary(self, pdf):
        """Create effect sizes summary visualization."""
        
        # Collect all effect sizes from successful analyses
        all_effect_sizes = []
        for response, results in self.anova_results.items():
            if 'effect_sizes' in results and results['effect_sizes']:
                for factor, es_data in results['effect_sizes'].items():
                    all_effect_sizes.append({
                        'Response': response.replace('_', ' ').title(),
                        'Factor': factor,
                        'Eta_Squared': es_data['eta_squared'],
                        'Magnitude': es_data['magnitude']
                    })
        
        if not all_effect_sizes:
            # Create placeholder page
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.text(0.5, 0.5, 'No effect sizes available\nfrom successful analyses', 
                   ha='center', va='center', fontsize=16, transform=ax.transAxes)
            ax.set_title('Effect Sizes Summary')
            ax.axis('off')
            pdf.savefig(bbox_inches='tight', dpi=300)
            plt.close()
            return
        
        effect_df = pd.DataFrame(all_effect_sizes)
        
        # Create visualization
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Heatmap of effect sizes
        pivot_df = effect_df.pivot(index='Factor', columns='Response', values='Eta_Squared')
        
        if not pivot_df.empty:
            sns.heatmap(pivot_df, annot=True, fmt='.3f', cmap='Reds', ax=ax1, cbar_kws={'label': 'η²'})
            ax1.set_title('Effect Sizes (η²) Heatmap')
            ax1.set_xlabel('Response Variables')
            ax1.set_ylabel('Factors')
        else:
            ax1.text(0.5, 0.5, 'No data for heatmap', ha='center', va='center', transform=ax1.transAxes)
            ax1.set_title('Effect Sizes (η²) Heatmap')
        
        # Effect size magnitude distribution
        magnitude_counts = effect_df['Magnitude'].value_counts()
        colors = {'Negligible': 'yellow', 'Small': 'orange', 'Medium': 'gray', 'Large': 'red'}
        
        bars = ax2.bar(magnitude_counts.index, magnitude_counts.values,
                      color=[colors.get(mag, 'blue') for mag in magnitude_counts.index])
        
        # Add count labels on bars
        for bar, count in zip(bars, magnitude_counts.values):
            ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                    str(count), ha='center', va='bottom')
        
        ax2.set_xlabel('Effect Magnitude')
        ax2.set_ylabel('Count')
        ax2.set_title('Distribution of Effect Magnitudes')
        
        plt.suptitle('ANOVA Effect Sizes Summary', fontsize=14, fontweight='bold')
        plt.tight_layout()
        pdf.savefig(bbox_inches='tight', dpi=300)
        plt.close()
    
    def export_results(self):
        """Export ANOVA results to CSV and JSON files."""
        
        print(f"\n💾 Exporting results...")
        
        # Export summary CSV
        summary_data = []
        for response, results in self.anova_results.items():
            if 'anova_table' in results:
                anova_table = results['anova_table']
                for idx, row in anova_table.iterrows():
                    if 'Residual' not in str(idx):
                        summary_data.append({
                            'response_variable': response,
                            'factor': str(idx),
                            'F_statistic': row.get('F', np.nan),
                            'p_value': row.get('p-unc', np.nan),
                            'eta_squared': results['effect_sizes'].get(str(idx), {}).get('eta_squared', np.nan),
                            'effect_magnitude': results['effect_sizes'].get(str(idx), {}).get('magnitude', 'Unknown'),
                            'significant': row.get('p-unc', 1.0) < 0.05,
                            'n_observations': results.get('n_observations', 0)
                        })
            else:
                # Record failed analyses
                summary_data.append({
                    'response_variable': response,
                    'factor': 'ANALYSIS_FAILED',
                    'F_statistic': np.nan,
                    'p_value': np.nan,
                    'eta_squared': np.nan,
                    'effect_magnitude': 'N/A',
                    'significant': False,
                    'n_observations': 0,
                    'error': results.get('error', 'Unknown error')
                })
        
        if summary_data:
            summary_df = pd.DataFrame(summary_data)
            summary_path = os.path.join(self.output_dir, f"anova_summary_{self.sweep_name}.csv")
            summary_df.to_csv(summary_path, index=False)
            print(f"📄 Summary exported: {summary_path}")
        
        # Export detailed JSON
        json_path = os.path.join(self.output_dir, f"anova_detailed_{self.sweep_name}.json")
        
        # Convert DataFrames to dictionaries for JSON serialization
        json_results = {}
        for response, results in self.anova_results.items():
            json_results[response] = {}
            for key, value in results.items():
                if isinstance(value, pd.DataFrame):
                    json_results[response][key] = value.to_dict()
                else:
                    json_results[response][key] = value
        
        with open(json_path, 'w') as f:
            json.dump(json_results, f, indent=2, default=str)
        
        print(f"📄 Detailed results exported: {json_path}")
        
        # Export cleaned data for reference
        data_path = os.path.join(self.output_dir, f"cleaned_data_{self.sweep_name}.csv")
        self.df.to_csv(data_path, index=False)
        print(f"📄 Cleaned data exported: {data_path}")

def main():
    """Main function with command line interface."""
    
    parser = argparse.ArgumentParser(description='Run Pingouin ANOVA analysis on HPC training data')
    parser.add_argument('sweep_name', help='Name of the parameter sweep (e.g., session3_100k_uniform)')
    parser.add_argument('--results-dir', default='./results', 
                       help='Base directory containing results (default: ./results)')
    parser.add_argument('--no-viz', action='store_true', 
                       help='Skip visualization generation')
    parser.add_argument('--responses', nargs='+', 
                       help='Specific response variables to analyze (default: all)')
    
    args = parser.parse_args()
    
    # Initialize analyzer
    analyzer = HPC_ANOVAAnalyzer(args.sweep_name, args.results_dir)
    
    # Optionally filter response variables
    if args.responses:
        analyzer.response_variables = [r for r in args.responses 
                                     if r in analyzer.response_variables]
        print(f"📊 Analyzing subset: {analyzer.response_variables}")
    
    # Run analysis
    try:
        # Load data
        analyzer.load_hpc_data()
        
        # Run ANOVA
        results = analyzer.run_pingouin_anova()
        
        # Generate visualizations
        if not args.no_viz:
            analyzer.generate_visualizations()
        
        # Export results
        analyzer.export_results()
        
        print(f"\n🎉 Analysis complete!")
        print(f"📁 Results saved to: {analyzer.output_dir}")
        
        # Print summary
        total_responses = len(analyzer.response_variables)
        successful_analyses = len([r for r in results.values() if 'error' not in r])
        
        print(f"\n📊 Summary:")
        print(f"   • Responses analyzed: {successful_analyses}/{total_responses}")
        print(f"   • Data points: {len(analyzer.df)}")
        print(f"   • Parameters: {len(analyzer.factors)}")
        
        # Report which analyses succeeded/failed
        if successful_analyses > 0:
            success_vars = [var for var, res in results.items() if 'error' not in res]
            print(f"   • Successful: {', '.join(success_vars)}")
        
        failed_analyses = total_responses - successful_analyses
        if failed_analyses > 0:
            failed_vars = [var for var, res in results.items() if 'error' in res]
            print(f"   • Failed: {', '.join(failed_vars)}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()