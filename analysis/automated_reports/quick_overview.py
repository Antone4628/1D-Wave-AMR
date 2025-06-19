#!/usr/bin/env python3
"""
Quick Overview and Validation Script
Provides immediate insights into transferred parameter sweep data.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os

# Add modules to path
# sys.path.append(str(Path(__file__).parent.parent / "data_management"))
# sys.path.append(str(Path(__file__).parent.parent / "utilities"))

PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 
    '..',  # Go up to analysis/
    '..'   # Go up to main project root (1D_wave_AMR/)
))
sys.path.append(PROJECT_ROOT)


from analysis.data_management.data_loader import ParameterSweepLoader, quick_load_sweep
from analysis.utilities.config import CURRENT_SWEEP, PARAMETER_SPACE

def quick_overview(sweep_name=CURRENT_SWEEP):
    """Generate quick overview of parameter sweep data"""
    
    print("🔍 AMR Parameter Sweep - Quick Overview")
    print("=" * 60)
    
    try:
        # Load data
        df = quick_load_sweep(sweep_name)
        print(f"✅ Successfully loaded {len(df)} parameter combinations")
        
        # Basic info
        print(f"\\n📊 Dataset Overview:")
        print(f"Shape: {df.shape[0]} combinations × {df.shape[1]} total columns")
        
        # Parameter space coverage
        print(f"\\n🎯 Parameter Space Coverage:")
        for param, expected_values in PARAMETER_SPACE.items():
            actual_values = sorted(df[param].unique())
            coverage = len(actual_values) / len(expected_values) * 100
            print(f"  {param}: {actual_values} ({coverage:.0f}% coverage)")
        
        # Key metrics overview
        key_metrics = [
            'final_episode_reward_mean', 'convergence_score', 'episodes_completed',
            'training_duration_hours', 'budget_exceeded_percentage'
        ]
        
        available_metrics = [m for m in key_metrics if m in df.columns]
        
        if available_metrics:
            print(f"\\n📈 Key Metrics Summary:")
            for metric in available_metrics:
                values = df[metric].dropna()
                if len(values) > 0:
                    print(f"  {metric}:")
                    print(f"    Mean: {values.mean():.3f} ± {values.std():.3f}")
                    print(f"    Range: [{values.min():.3f}, {values.max():.3f}]")
                    print(f"    Missing: {df[metric].isna().sum()}/{len(df)}")
        
        # Quick convergence analysis
        analyze_convergence_patterns(df)
        
        # Data quality check
        check_data_quality(df)
        
        return df
        
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        print(f"\\nTroubleshooting:")
        print(f"1. Ensure data has been transferred: python data_management/transfer_json_data.py")
        print(f"2. Check data path exists: data/raw/{sweep_name}")
        return None

def analyze_convergence_patterns(df):
    """Quick analysis of convergence patterns by gamma_c"""
    
    print(f"\\n🎯 Convergence Analysis by gamma_c:")
    
    if 'convergence_score' in df.columns:
        convergence_by_gamma = df.groupby('gamma_c')['convergence_score'].agg([
            'count', 'mean', 'std', 'min', 'max'
        ]).round(3)
        print(convergence_by_gamma)
        
        # Classification
        print(f"\\n📊 Convergence Classification:")
        for gamma in sorted(df['gamma_c'].unique()):
            gamma_data = df[df['gamma_c'] == gamma]['convergence_score'].dropna()
            if len(gamma_data) > 0:
                well_converged = (gamma_data >= 0.8).sum()
                moderate = ((gamma_data >= 0.5) & (gamma_data < 0.8)).sum()
                poor = (gamma_data < 0.5).sum()
                
                print(f"  gamma_c={gamma}: {well_converged} well-converged, {moderate} moderate, {poor} poor")
    else:
        print("  convergence_score not available")

def check_data_quality(df):
    """Check data quality and completeness"""
    
    print(f"\\n🔍 Data Quality Check:")
    
    # Missing data analysis
    missing_data = df.isnull().sum()
    missing_cols = missing_data[missing_data > 0]
    
    if len(missing_cols) > 0:
        print(f"  Columns with missing data:")
        for col, missing_count in missing_cols.items():
            pct_missing = missing_count / len(df) * 100
            print(f"    {col}: {missing_count}/{len(df)} ({pct_missing:.1f}%)")
    else:
        print(f"  ✅ No missing data detected")
    
    # Parameter combination completeness
    expected_combinations = 1
    for param_values in PARAMETER_SPACE.values():
        expected_combinations *= len(param_values)
    
    actual_combinations = len(df)
    completeness = actual_combinations / expected_combinations * 100
    
    print(f"\\n📋 Parameter Space Completeness:")
    print(f"  Expected combinations: {expected_combinations}")
    print(f"  Actual combinations: {actual_combinations}")
    print(f"  Completeness: {completeness:.1f}%")
    
    if completeness < 100:
        missing_combinations = expected_combinations - actual_combinations
        print(f"  ⚠️ Missing {missing_combinations} combinations")

def generate_quick_plots(df, output_dir="outputs/figures"):
    """Generate quick visualization plots"""
    
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    print(f"\\n📊 Generating quick plots...")
    
    # Set style
    plt.style.use('default')
    sns.set_palette("husl")
    
    # 1. Convergence by gamma_c
    if 'convergence_score' in df.columns:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(data=df, x='gamma_c', y='convergence_score', ax=ax)
        ax.set_title('Convergence Score by gamma_c')
        ax.set_ylabel('Convergence Score')
        plt.tight_layout()
        plt.savefig(output_path / 'convergence_by_gamma.png', dpi=150)
        plt.close()
        print(f"  ✓ Saved: convergence_by_gamma.png")
    
    # 2. Training duration analysis
    if 'training_duration_hours' in df.columns:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(data=df, x='gamma_c', y='training_duration_hours', 
                       hue='element_budget', size='rl_iterations_per_timestep', ax=ax)
        ax.set_title('Training Duration by Parameters')
        ax.set_ylabel('Training Duration (hours)')
        plt.tight_layout()
        plt.savefig(output_path / 'training_duration.png', dpi=150)
        plt.close()
        print(f"  ✓ Saved: training_duration.png")
    
    # 3. Parameter correlation heatmap
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    param_cols = ['gamma_c', 'step_domain_fraction', 'rl_iterations_per_timestep', 'element_budget']
    available_params = [col for col in param_cols if col in numeric_cols]
    
    if len(available_params) >= 2:
        # Add a few key metrics if available
        key_metrics = ['final_episode_reward_mean', 'convergence_score', 'episodes_completed']
        available_metrics = [col for col in key_metrics if col in numeric_cols]
        
        heatmap_cols = available_params + available_metrics[:3]  # Limit to keep readable
        
        if len(heatmap_cols) >= 3:
            fig, ax = plt.subplots(figsize=(10, 8))
            correlation_matrix = df[heatmap_cols].corr()
            sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, ax=ax)
            ax.set_title('Parameter and Metrics Correlation')
            plt.tight_layout()
            plt.savefig(output_path / 'correlation_heatmap.png', dpi=150)
            plt.close()
            print(f"  ✓ Saved: correlation_heatmap.png")

if __name__ == "__main__":
    # Run quick overview
    df = quick_overview()
    
    if df is not None:
        # Generate plots
        generate_quick_plots(df)
        
        print(f"\\n🎉 Quick overview complete!")
        print(f"\\n📁 Files generated:")
        print(f"  - Processed data: data/processed/{CURRENT_SWEEP}/")
        print(f"  - Quick plots: outputs/figures/")
        
        print(f"\\n🚀 Next steps:")
        print(f"  1. Review the plots and data quality results")
        print(f"  2. Begin interactive analysis in Jupyter notebooks")
        print(f"  3. Run statistical analysis (ANOVA/regression)")
        
        print(f"\\n💡 Ready for Session 2: Statistical Analysis!")
    else:
        print(f"\\n❌ Data loading failed. Please ensure data transfer completed successfully.")