#!/usr/bin/env python3
"""
Quick Data Sample Script
Shows DataFrame structure and sample data for ANOVA development.
"""

import sys
from pathlib import Path

# Add modules to path
sys.path.append(str(Path(__file__) / "data_management"))
sys.path.append(str(Path(__file__) / "utilities"))

from data_management.data_loader import quick_load_sweep
from utilities.config import CURRENT_SWEEP

def show_data_structure():
    """Display comprehensive data structure information"""
    
    print("🔍 AMR Parameter Sweep - Data Structure Analysis")
    print("=" * 70)
    
    try:
        # Load the data
        print(f"Loading sweep: {CURRENT_SWEEP}")
        df = quick_load_sweep(CURRENT_SWEEP)
        
        print(f"\n📊 BASIC DATA INFO")
        print(f"DataFrame shape: {df.shape}")
        print(f"Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
        
        print(f"\n📋 ALL COLUMNS ({len(df.columns)} total):")
        for i, col in enumerate(df.columns, 1):
            dtype = df[col].dtype
            non_null = df[col].notna().sum()
            print(f"  {i:2d}. {col:<35} ({dtype}, {non_null}/{len(df)} non-null)")
        
        print(f"\n🎯 PARAMETER COLUMNS:")
        param_cols = ['gamma_c', 'step_domain_fraction', 'rl_iterations_per_timestep', 'element_budget']
        param_summary = df[param_cols].describe()
        print(param_summary)
        
        print(f"\n📈 KEY METRICS SAMPLE:")
        key_metrics = ['final_episode_reward_mean', 'convergence_score', 'episodes_completed', 
                      'training_duration_hours', 'budget_exceeded_percentage']
        available_metrics = [m for m in key_metrics if m in df.columns]
        
        if available_metrics:
            metrics_summary = df[available_metrics].describe()
            print(metrics_summary)
        else:
            print("Key metrics not found. Available numeric columns:")
            numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
            print(f"  {numeric_cols}")
        
        print(f"\n🔬 SAMPLE ROWS:")
        print("First 3 parameter combinations:")
        display_cols = param_cols + available_metrics[:3]  # Show params + first 3 metrics
        display_cols = [col for col in display_cols if col in df.columns]
        print(df[display_cols].head(3).to_string(index=False))
        
        print(f"\n📊 PARAMETER SPACE COVERAGE:")
        for param in param_cols:
            if param in df.columns:
                unique_vals = sorted(df[param].unique())
                print(f"  {param}: {unique_vals} (n={len(unique_vals)})")
        
        print(f"\n✅ FACTORIAL DESIGN CHECK:")
        param_counts = {}
        for param in param_cols:
            if param in df.columns:
                param_counts[param] = df[param].nunique()
        
        total_combinations = 1
        for count in param_counts.values():
            total_combinations *= count
        
        print(f"  Expected combinations: {total_combinations}")
        print(f"  Actual combinations: {len(df)}")
        print(f"  Complete factorial: {'✅ Yes' if len(df) == total_combinations else '❌ No'}")
        
        print(f"\n🎉 DATA STRUCTURE ANALYSIS COMPLETE!")
        print(f"\nThis data is ready for ANOVA analysis with:")
        print(f"  - {len(param_cols)} factors (parameters)")
        print(f"  - {len(df)} observations")
        print(f"  - {len(available_metrics)} response variables (metrics)")
        
        return df
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    df = show_data_structure()