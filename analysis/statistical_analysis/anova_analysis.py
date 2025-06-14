#!/usr/bin/env python3
"""
Multi-Factor ANOVA Analysis for AMR Parameter Optimization
Performs comprehensive statistical analysis of parameter sweep results.
"""

import pandas as pd
import numpy as np
import sys
import os
from typing import Dict, List, Tuple, Optional
import json
from datetime import datetime

# Get absolute path to project root using established pattern
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 
    '..',  # Go up to analysis/
    '..'   # Go up to main project root (1D_wave_AMR/)
))
sys.path.append(PROJECT_ROOT)

# Statistical analysis imports
from scipy import stats
import statsmodels.api as sm
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import itertools

# Visualization imports
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages


# Import modules using full path from PROJECT_ROOT
from analysis.data_management.data_loader import quick_load_sweep
from analysis.utilities.config import CURRENT_SWEEP, PARAMETER_SPACE, FIGURE_DPI, OUTPUTS_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR

# Debug: Check what paths are being used
print(f"🔍 RAW_DATA_DIR: {RAW_DATA_DIR}")
print(f"🔍 PROCESSED_DATA_DIR: {PROCESSED_DATA_DIR}")
print(f"🔍 Current working directory: {os.getcwd()}")
print(f"🔍 PROJECT_ROOT: {PROJECT_ROOT}")

class ANOVAAnalyzer:
    """
    Comprehensive ANOVA analysis for AMR parameter optimization.
    
    Performs multi-factor ANOVA, effect size calculations, post-hoc tests,
    and generates thesis-quality visualizations and statistical reports.
    """
    
    def __init__(self, sweep_name: str = CURRENT_SWEEP):
        self.sweep_name = sweep_name
        self.df = None
        self.anova_results = {}
        self.effect_sizes = {}
        self.posthoc_results = {}
        
        # Define analysis configuration
        self.factors = ['gamma_c', 'step_domain_fraction', 'rl_iterations_per_timestep', 'element_budget']
        self.response_variables = [
            'final_episode_reward_mean',
            'convergence_score', 
            'episodes_completed',
            'training_duration_hours',
            'budget_exceeded_percentage',
            'mean_resource_usage'
        ]
        
        # Output paths - use PROJECT_ROOT for consistency
        analysis_dir = os.path.join(PROJECT_ROOT, 'analysis')
        self.output_dir = os.path.join(analysis_dir, "outputs")
        self.figures_dir = os.path.join(self.output_dir, "figures")
        self.reports_dir = os.path.join(self.output_dir, "reports")
        self.exports_dir = os.path.join(analysis_dir, "data", "exports")
        
        # Create directories
        for dir_path in [self.figures_dir, self.reports_dir, self.exports_dir]:
            os.makedirs(dir_path, exist_ok=True)
    
    def load_data(self) -> pd.DataFrame:
        """Load and validate data for ANOVA analysis."""
        print(f"🔍 Loading data for ANOVA analysis...")
        
        self.df = quick_load_sweep(self.sweep_name)
        
        # Validate factors and response variables
        missing_factors = [f for f in self.factors if f not in self.df.columns]
        missing_responses = [r for r in self.response_variables if r not in self.df.columns]
        
        if missing_factors:
            raise ValueError(f"Missing factors in data: {missing_factors}")
        
        if missing_responses:
            print(f"⚠️ Missing response variables: {missing_responses}")
            self.response_variables = [r for r in self.response_variables if r in self.df.columns]
        
        print(f"✅ Data loaded: {len(self.df)} observations")
        print(f"📊 Factors: {len(self.factors)} ({self.factors})")
        print(f"📈 Response variables: {len(self.response_variables)} ({self.response_variables})")
        
        return self.df
    
    def run_complete_analysis(self) -> Dict:
        """Run complete ANOVA analysis pipeline."""
        print(f"\n🎯 Starting Complete ANOVA Analysis")
        print("=" * 60)
        
        # Load data
        if self.df is None:
            self.load_data()
        
        # Run ANOVA for each response variable
        for response in self.response_variables:
            print(f"\n📊 Analyzing: {response}")
            self._analyze_response_variable(response)
        
        # Generate comprehensive report
        # self._generate_statistical_report()
        
        # Generate thesis-quality visualizations
        self._generate_thesis_visualizations()
        
        # Export results for future use
        self._export_results()
        
        print(f"\n🎉 Complete ANOVA analysis finished!")
        print(f"📁 Results saved to: {self.output_dir}")
        
        return self.anova_results
    
    def _analyze_response_variable(self, response: str):
        """Perform complete ANOVA analysis for a single response variable."""
        
        # 1. Multi-factor ANOVA
        anova_result = self._perform_multifactor_anova(response)
        
        # 2. Effect size calculations
        effect_sizes = self._calculate_effect_sizes(response, anova_result)
        
        # 3. Post-hoc tests for significant factors
        posthoc_results = self._perform_posthoc_tests(response, anova_result)
        
        # Store results
        self.anova_results[response] = {
            'anova_table': anova_result,
            'effect_sizes': effect_sizes,
            'posthoc_tests': posthoc_results,
            'significant_factors': self._identify_significant_factors(anova_result),
            'interpretation': self._interpret_results(response, anova_result, effect_sizes)
        }
    
    def _perform_multifactor_anova(self, response: str) -> pd.DataFrame:
        """Perform multi-factor ANOVA with interactions."""
        
        # Create formula for full factorial design with 2-way interactions
        # For 4 factors, this includes all main effects + all 2-way interactions
        formula_parts = []
        
        # Main effects
        formula_parts.extend([f"C({factor})" for factor in self.factors])
        
        # 2-way interactions (6 total for 4 factors)
        for factor1, factor2 in itertools.combinations(self.factors, 2):
            formula_parts.append(f"C({factor1}):C({factor2})")
        
        formula = f"{response} ~ " + " + ".join(formula_parts)
        
        try:
            # Fit the model
            model = ols(formula, data=self.df).fit()
            
            # Generate ANOVA table
            anova_table = anova_lm(model, typ=2)  # Type II ANOVA
            
            # Add interpretation columns
            anova_table['Significant'] = anova_table['PR(>F)'] < 0.05
            anova_table['Effect_Strength'] = pd.cut(
                anova_table['PR(>F)'], 
                bins=[0, 0.001, 0.01, 0.05, 1.0],
                labels=['Very Strong (p<0.001)', 'Strong (p<0.01)', 'Moderate (p<0.05)', 'Not Significant'],
                include_lowest=True
            )
            
            return anova_table
            
        except Exception as e:
            print(f"❌ Error in ANOVA for {response}: {e}")
            return pd.DataFrame()
    
    def _calculate_effect_sizes(self, response: str, anova_table: pd.DataFrame) -> Dict:
        """Calculate effect sizes (eta-squared) for ANOVA results."""
        
        if anova_table.empty:
            return {}
        
        total_ss = anova_table['sum_sq'].sum()
        effect_sizes = {}
        
        for factor in anova_table.index:
            if factor != 'Residual':
                eta_squared = anova_table.loc[factor, 'sum_sq'] / total_ss
                
                # Classify effect size (Cohen's conventions, adapted for eta-squared)
                if eta_squared < 0.01:
                    magnitude = "Negligible"
                elif eta_squared < 0.06:
                    magnitude = "Small"
                elif eta_squared < 0.14:
                    magnitude = "Medium"
                else:
                    magnitude = "Large"
                
                effect_sizes[factor] = {
                    'eta_squared': eta_squared,
                    'percentage_variance': eta_squared * 100,
                    'magnitude': magnitude
                }
        
        return effect_sizes
    
    def _perform_posthoc_tests(self, response: str, anova_table: pd.DataFrame) -> Dict:
        """Perform Tukey HSD post-hoc tests for significant main effects."""
        
        posthoc_results = {}
        
        if anova_table.empty:
            return posthoc_results
        
        for factor in self.factors:
            factor_key = f"C({factor})"
            
            # Only run post-hoc if factor is significant and has >2 levels
            if (factor_key in anova_table.index and 
                anova_table.loc[factor_key, 'PR(>F)'] < 0.05 and
                self.df[factor].nunique() > 2):
                
                try:
                    # Perform Tukey HSD test
                    tukey_result = pairwise_tukeyhsd(
                        endog=self.df[response],
                        groups=self.df[factor],
                        alpha=0.05
                    )
                    
                    posthoc_results[factor] = {
                        'tukey_summary': str(tukey_result),
                        'significant_pairs': self._extract_significant_pairs(tukey_result),
                        'group_means': self.df.groupby(factor)[response].agg(['mean', 'std']).round(3)
                    }
                    
                except Exception as e:
                    print(f"⚠️ Post-hoc test failed for {factor}: {e}")
        
        return posthoc_results
    
    def _extract_significant_pairs(self, tukey_result) -> List[Dict]:
        """Extract significant pairwise comparisons from Tukey results."""
        
        significant_pairs = []
        
        # Parse the Tukey results
        for i, row in enumerate(tukey_result.summary().data[1:]):  # Skip header
            group1, group2, meandiff, p_adj, lower, upper, reject = row
            
            if reject:  # Significant difference
                significant_pairs.append({
                    'group1': group1,
                    'group2': group2,
                    'mean_difference': float(meandiff),
                    'p_adj': float(p_adj),
                    'confidence_interval': [float(lower), float(upper)]
                })
        
        return significant_pairs
    
    def _identify_significant_factors(self, anova_table: pd.DataFrame) -> List[str]:
        """Identify factors with significant effects."""
        
        if anova_table.empty:
            return []
        
        significant_factors = []
        
        for factor in self.factors:
            factor_key = f"C({factor})"
            if (factor_key in anova_table.index and 
                anova_table.loc[factor_key, 'PR(>F)'] < 0.05):
                significant_factors.append(factor)
        
        return significant_factors
    
    def _interpret_results(self, response: str, anova_table: pd.DataFrame, effect_sizes: Dict) -> str:
        """Generate interpretation of ANOVA results."""
        
        if anova_table.empty:
            return "Analysis failed - no results available."
        
        interpretation = []
        
        # Overall model significance
        significant_factors = self._identify_significant_factors(anova_table)
        
        if significant_factors:
            interpretation.append(f"Significant factors affecting {response}: {', '.join(significant_factors)}")
            
            # Effect sizes
            for factor in significant_factors:
                factor_key = f"C({factor})"
                if factor_key in effect_sizes:
                    es = effect_sizes[factor_key]
                    interpretation.append(
                        f"- {factor}: {es['magnitude']} effect (η² = {es['eta_squared']:.3f}, "
                        f"{es['percentage_variance']:.1f}% of variance)"
                    )
        else:
            interpretation.append(f"No factors significantly affect {response} at α = 0.05")
        
        # Check for interactions
        interaction_effects = [idx for idx in anova_table.index if ':' in idx and anova_table.loc[idx, 'PR(>F)'] < 0.05]
        if interaction_effects:
            interpretation.append(f"Significant interactions found: {', '.join(interaction_effects)}")
        
        return ". ".join(interpretation)
    
    def _generate_statistical_report(self):
        """Generate comprehensive statistical report."""
        
        report_path = os.path.join(self.reports_dir, f"anova_statistical_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html")
        
        html_content = self._build_html_report()
        
        with open(report_path, 'w') as f:
            f.write(html_content)
        
        print(f"📄 Statistical report saved: {os.path.basename(report_path)}")
    
    def _build_html_report(self) -> str:
        """Build comprehensive HTML statistical report."""
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>AMR Parameter ANOVA Analysis Report</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; }}
                .header {{ text-align: center; color: #2c3e50; }}
                .section {{ margin: 30px 0; }}
                .metric {{ margin: 20px 0; padding: 15px; background-color: #f8f9fa; border-left: 4px solid #007bff; }}
                table {{ border-collapse: collapse; width: 100%; margin: 10px 0; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                th {{ background-color: #f2f2f2; font-weight: bold; }}
                .significant {{ background-color: #d4edda; }}
                .not-significant {{ background-color: #f8d7da; }}
                .effect-large {{ color: #d63384; font-weight: bold; }}
                .effect-medium {{ color: #fd7e14; font-weight: bold; }}
                .effect-small {{ color: #20c997; }}
                .effect-negligible {{ color: #6c757d; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>Multi-Factor ANOVA Analysis Report</h1>
                <h2>AMR Parameter Optimization Study</h2>
                <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                <p>Dataset: {self.sweep_name} ({len(self.df)} observations)</p>
            </div>
        """
        
        # Executive Summary
        html += self._build_executive_summary()
        
        # Detailed results for each response variable
        for response in self.response_variables:
            if response in self.anova_results:
                html += self._build_response_analysis_section(response)
        
        html += """
            </body>
        </html>
        """
        
        return html
    
    def _build_executive_summary(self) -> str:
        """Build executive summary section of report."""
        
        summary_html = f"""
        <div class="section">
            <h2>Executive Summary</h2>
            <h3>Study Design</h3>
            <ul>
                <li><strong>Design:</strong> Complete 3×3×3×3 factorial (81 combinations)</li>
                <li><strong>Factors:</strong> {len(self.factors)} parameters with 3 levels each</li>
                <li><strong>Response Variables:</strong> {len(self.response_variables)} performance metrics</li>
                <li><strong>Analysis:</strong> Multi-factor ANOVA with 2-way interactions</li>
            </ul>
            
            <h3>Key Findings</h3>
        """
        
        # Summarize significant factors across all responses
        all_significant_factors = set()
        response_significance = {}
        
        for response, results in self.anova_results.items():
            sig_factors = results['significant_factors']
            all_significant_factors.update(sig_factors)
            response_significance[response] = len(sig_factors)
        
        summary_html += f"""
            <ul>
                <li><strong>Parameters with significant effects:</strong> {', '.join(sorted(all_significant_factors)) if all_significant_factors else 'None detected'}</li>
                <li><strong>Metrics with parameter sensitivity:</strong> {sum(1 for count in response_significance.values() if count > 0)} out of {len(self.response_variables)}</li>
                <li><strong>Most sensitive metric:</strong> {max(response_significance.items(), key=lambda x: x[1])[0] if response_significance else 'None'}</li>
            </ul>
        </div>
        """
        
        return summary_html
    
    def _build_response_analysis_section(self, response: str) -> str:
        """Build detailed analysis section for a response variable."""
        
        results = self.anova_results[response]
        anova_table = results['anova_table']
        
        section_html = f"""
        <div class="section metric">
            <h2>Analysis: {response.replace('_', ' ').title()}</h2>
            <p><strong>Interpretation:</strong> {results['interpretation']}</p>
        """
        
        # ANOVA Table
        if not anova_table.empty:
            section_html += f"""
            <h3>ANOVA Table</h3>
            <table>
                <tr>
                    <th>Factor</th>
                    <th>Sum of Squares</th>
                    <th>DF</th>
                    <th>Mean Square</th>
                    <th>F-statistic</th>
                    <th>p-value</th>
                    <th>Significance</th>
                </tr>
            """
            
            for factor, row in anova_table.iterrows():
                css_class = "significant" if row['PR(>F)'] < 0.05 else "not-significant"
                section_html += f"""
                <tr class="{css_class}">
                    <td>{factor}</td>
                    <td>{row['sum_sq']:.2f}</td>
                    <td>{row['df']:.0f}</td>
                    <td>{row['mean_sq']:.2f}</td>
                    <td>{row['F']:.2f}</td>
                    <td>{row['PR(>F)']:.4f}</td>
                    <td>{row['Effect_Strength']}</td>
                </tr>
                """
            
            section_html += "</table>"
        
        # Effect Sizes
        if results['effect_sizes']:
            section_html += f"""
            <h3>Effect Sizes (η²)</h3>
            <table>
                <tr>
                    <th>Factor</th>
                    <th>Eta Squared</th>
                    <th>% Variance Explained</th>
                    <th>Magnitude</th>
                </tr>
            """
            
            for factor, es in results['effect_sizes'].items():
                magnitude_class = f"effect-{es['magnitude'].lower()}"
                section_html += f"""
                <tr>
                    <td>{factor}</td>
                    <td>{es['eta_squared']:.3f}</td>
                    <td>{es['percentage_variance']:.1f}%</td>
                    <td class="{magnitude_class}">{es['magnitude']}</td>
                </tr>
                """
            
            section_html += "</table>"
        
        section_html += "</div>"
        
        return section_html
    
    def _generate_thesis_visualizations(self):
        """Generate thesis-quality visualizations."""
        
        print(f"🎨 Generating thesis-quality visualizations...")
        
        # Create comprehensive visualization PDF
        pdf_path = os.path.join(self.figures_dir, f"anova_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf")
        
        with PdfPages(pdf_path) as pdf:
            # 1. Overview page
            self._create_overview_page(pdf)
            
            # 2. Main effects plots for each response variable
            for response in self.response_variables:
                if response in self.anova_results:
                    self._create_main_effects_plot(response, pdf)
            
            # 3. Effect sizes summary
            self._create_effect_sizes_summary(pdf)
            
            # 4. Interaction effects (if significant)
            self._create_interaction_plots(pdf)
        
        print(f"📊 Thesis visualizations saved: {os.path.basename(pdf_path)}")
    
    def _create_overview_page(self, pdf):
        """Create analysis overview page."""
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
        
        # Parameter space visualization
        param_counts = [len(PARAMETER_SPACE[factor]) for factor in self.factors]
        ax1.bar(range(len(self.factors)), param_counts, color='skyblue')
        ax1.set_xlabel('Factors')
        ax1.set_ylabel('Number of Levels')
        ax1.set_title('Experimental Design: Factor Levels')
        ax1.set_xticks(range(len(self.factors)))
        ax1.set_xticklabels([f.replace('_', '\n') for f in self.factors], rotation=0)
        
        # Response variable distributions
        response_subset = self.response_variables[:4]  # Show first 4
        for i, response in enumerate(response_subset):
            ax2.hist(self.df[response], alpha=0.6, bins=15, label=response.replace('_', ' ')[:15])
        ax2.set_xlabel('Value')
        ax2.set_ylabel('Frequency')
        ax2.set_title('Response Variable Distributions')
        ax2.legend(fontsize=8)
        
        # Significant factors count
        sig_factor_counts = {}
        for factor in self.factors:
            count = sum(1 for results in self.anova_results.values() 
                       if factor in results['significant_factors'])
            sig_factor_counts[factor] = count
        
        ax3.bar(range(len(sig_factor_counts)), list(sig_factor_counts.values()), 
                color='lightcoral')
        ax3.set_xlabel('Factors')
        ax3.set_ylabel('Number of Significant Effects')
        ax3.set_title('Parameter Significance Across Metrics')
        ax3.set_xticks(range(len(sig_factor_counts)))
        ax3.set_xticklabels([f.replace('_', '\n') for f in sig_factor_counts.keys()], rotation=0)
        
        # Summary statistics
        ax4.axis('off')
        summary_text = f"""
        ANOVA Analysis Summary
        
        Study Design:
        • {len(self.df)} total observations
        • {len(self.factors)} factors (parameters)
        • {len(self.response_variables)} response variables
        • Complete factorial design
        
        Key Results:
        • Factors tested: {', '.join(self.factors)}
        • Most significant factor: {max(sig_factor_counts.items(), key=lambda x: x[1])[0] if any(sig_factor_counts.values()) else 'None'}
        • Response variables analyzed: {len(self.response_variables)}
        """
        
        ax4.text(0.1, 0.9, summary_text, transform=ax4.transAxes, fontsize=11,
                verticalalignment='top', fontfamily='monospace',
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.1))
        
        plt.suptitle('AMR Parameter ANOVA Analysis Overview', fontsize=16, fontweight='bold')
        plt.tight_layout()
        pdf.savefig(bbox_inches='tight', dpi=FIGURE_DPI)
        plt.close()
    
    def _create_main_effects_plot(self, response: str, pdf):
        """Create main effects plot for a response variable."""
        
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        axes = axes.flatten()
        
        results = self.anova_results[response]
        significant_factors = results['significant_factors']
        
        for i, factor in enumerate(self.factors):
            ax = axes[i]
            
            # Calculate means and standard errors
            group_stats = self.df.groupby(factor)[response].agg(['mean', 'std', 'count'])
            group_stats['se'] = group_stats['std'] / np.sqrt(group_stats['count'])
            
            x_pos = range(len(group_stats))
            
            # Color significant factors differently
            color = 'red' if factor in significant_factors else 'blue'
            
            # Plot means with error bars
            ax.errorbar(x_pos, group_stats['mean'], yerr=group_stats['se'], 
                       marker='o', capsize=5, capthick=2, linewidth=2, color=color)
            
            ax.set_xlabel(factor.replace('_', ' ').title())
            ax.set_ylabel(response.replace('_', ' ').title())
            ax.set_title(f"{factor.replace('_', ' ').title()}" + 
                        (" *" if factor in significant_factors else ""))
            ax.set_xticks(x_pos)
            ax.set_xticklabels(group_stats.index)
            ax.grid(True, alpha=0.3)
        
        plt.suptitle(f'Main Effects: {response.replace("_", " ").title()}\n(* indicates p < 0.05)', 
                    fontsize=14, fontweight='bold')
        plt.tight_layout()
        pdf.savefig(bbox_inches='tight', dpi=FIGURE_DPI)
        plt.close()
    
    def _create_effect_sizes_summary(self, pdf):
        """Create effect sizes summary visualization."""
        
        # Collect all effect sizes
        all_effects = []
        
        for response, results in self.anova_results.items():
            for factor, es in results['effect_sizes'].items():
                all_effects.append({
                    'Response': response.replace('_', ' ').title(),
                    'Factor': factor.replace('C(', '').replace(')', '').replace('_', ' ').title(),
                    'Eta_Squared': es['eta_squared'],
                    'Magnitude': es['magnitude']
                })
        
        if not all_effects:
            return
        
        effects_df = pd.DataFrame(all_effects)
        
        # Create heatmap
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 8))
        
        # Pivot for heatmap
        heatmap_data = effects_df.pivot(index='Factor', columns='Response', values='Eta_Squared')
        
        # Effect sizes heatmap
        sns.heatmap(heatmap_data, annot=True, fmt='.3f', cmap='Reds', ax=ax1)
        ax1.set_title('Effect Sizes (η²) Heatmap')
        ax1.set_xlabel('Response Variables')
        ax1.set_ylabel('Factors')
        
        # Effect magnitude distribution
        magnitude_counts = effects_df['Magnitude'].value_counts()
        colors = {'Large': 'red', 'Medium': 'orange', 'Small': 'yellow', 'Negligible': 'gray'}
        bar_colors = [colors.get(mag, 'blue') for mag in magnitude_counts.index]
        
        ax2.bar(range(len(magnitude_counts)), magnitude_counts.values, color=bar_colors)
        ax2.set_xlabel('Effect Magnitude')
        ax2.set_ylabel('Count')
        ax2.set_title('Distribution of Effect Magnitudes')
        ax2.set_xticks(range(len(magnitude_counts)))
        ax2.set_xticklabels(magnitude_counts.index, rotation=45)
        
        plt.suptitle('ANOVA Effect Sizes Summary', fontsize=16, fontweight='bold')
        plt.tight_layout()
        pdf.savefig(bbox_inches='tight', dpi=FIGURE_DPI)
        plt.close()
    
    def _create_interaction_plots(self, pdf):
        """Create interaction plots for significant interactions."""
        
        # Find significant interactions across all response variables
        significant_interactions = []
        
        for response, results in self.anova_results.items():
            anova_table = results['anova_table']
            for factor in anova_table.index:
                if ':' in factor and anova_table.loc[factor, 'PR(>F)'] < 0.05:
                    factor1, factor2 = factor.replace('C(', '').replace(')', '').split(':')
                    significant_interactions.append((response, factor1, factor2))
        
        if not significant_interactions:
            # Create a placeholder page
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.text(0.5, 0.5, 'No significant interactions detected\nat α = 0.05 level', 
                   ha='center', va='center', fontsize=16, transform=ax.transAxes)
            ax.set_title('Interaction Effects Analysis')
            ax.axis('off')
            pdf.savefig(bbox_inches='tight', dpi=FIGURE_DPI)
            plt.close()
            return
        
        # Plot significant interactions (up to 4 per page)
        n_interactions = len(significant_interactions)
        n_rows = (n_interactions + 1) // 2
        
        fig, axes = plt.subplots(n_rows, 2, figsize=(15, 4*n_rows))
        if n_rows == 1:
            axes = [axes]
        axes = axes.flatten()
        
        for i, (response, factor1, factor2) in enumerate(significant_interactions[:4]):
            ax = axes[i]
            
            # Create interaction plot
            for level in sorted(self.df[factor2].unique()):
                subset = self.df[self.df[factor2] == level]
                group_means = subset.groupby(factor1)[response].mean()
                
                ax.plot(group_means.index, group_means.values, 
                       marker='o', label=f'{factor2}={level}', linewidth=2)
            
            ax.set_xlabel(factor1.replace('_', ' ').title())
            ax.set_ylabel(response.replace('_', ' ').title())
            ax.set_title(f'Interaction: {factor1} × {factor2}')
            ax.legend()
            ax.grid(True, alpha=0.3)
        
        # Hide unused subplots
        for j in range(i+1, len(axes)):
            axes[j].axis('off')
        
        plt.suptitle('Significant Interaction Effects', fontsize=16, fontweight='bold')
        plt.tight_layout()
        pdf.savefig(bbox_inches='tight', dpi=FIGURE_DPI)
        plt.close()
    
    def _export_results(self):
        """Export results for future analysis and thesis integration."""
        
        export_data = {
            'analysis_metadata': {
                'sweep_name': self.sweep_name,
                'analysis_date': datetime.now().isoformat(),
                'n_observations': len(self.df),
                'factors': self.factors,
                'response_variables': self.response_variables
            },
            'anova_results': {},
            'summary_statistics': {}
        }
        
        # Export ANOVA results (convert to serializable format)
        for response, results in self.anova_results.items():
            export_data['anova_results'][response] = {
                'significant_factors': results['significant_factors'],
                'interpretation': results['interpretation'],
                'anova_table': results['anova_table'].to_dict() if not results['anova_table'].empty else {},
                'effect_sizes': results['effect_sizes']
            }
        
        # Summary statistics for each response variable
        for response in self.response_variables:
            export_data['summary_statistics'][response] = {
                'mean': float(self.df[response].mean()),
                'std': float(self.df[response].std()),
                'min': float(self.df[response].min()),
                'max': float(self.df[response].max()),
                'median': float(self.df[response].median())
            }
        
        # Save as JSON
        export_path = os.path.join(self.exports_dir, f"anova_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        
        with open(export_path, 'w') as f:
            json.dump(export_data, f, indent=2, default=str)
        
        print(f"📤 Results exported: {os.path.basename(export_path)}")

def main():
    """Run complete ANOVA analysis."""
    import sys
    
    # Use command line argument or default
    if len(sys.argv) > 1:
        sweep_name = sys.argv[1]
    else:
        sweep_name = CURRENT_SWEEP
    
    analyzer = ANOVAAnalyzer(sweep_name)
    results = analyzer.run_complete_analysis()
    
    return results

if __name__ == "__main__":
    main()