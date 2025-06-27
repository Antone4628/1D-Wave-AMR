#!/usr/bin/env python3
"""
CSV Structure Inspector
Examine the structure of model and baseline CSV files to understand column differences
"""

import pandas as pd
import os
import glob

def inspect_csv_structure(csv_path, file_type):
    """Inspect and display CSV structure"""
    print(f"\n{'='*60}")
    print(f"INSPECTING {file_type.upper()}: {os.path.basename(csv_path)}")
    print(f"{'='*60}")
    
    if not os.path.exists(csv_path):
        print(f"❌ File not found: {csv_path}")
        return
    
    try:
        df = pd.read_csv(csv_path)
        
        print(f"📊 Shape: {df.shape[0]} rows, {df.shape[1]} columns")
        print(f"📋 Columns: {list(df.columns)}")
        
        # Show first few rows
        print(f"\n🔍 First 3 rows:")
        print(df.head(3).to_string())
        
        # Check for key columns
        key_columns = ['final_l2_error', 'grid_normalized_l2_error', 'total_cost', 'threshold_value']
        print(f"\n🔑 Key columns present:")
        for col in key_columns:
            present = col in df.columns
            print(f"  {col}: {'✅' if present else '❌'}")
        
        # Show data ranges for error columns
        print(f"\n📈 Data ranges:")
        if 'final_l2_error' in df.columns:
            final_l2_range = (df['final_l2_error'].min(), df['final_l2_error'].max())
            print(f"  final_l2_error: {final_l2_range[0]:.2e} to {final_l2_range[1]:.2e}")
        
        if 'grid_normalized_l2_error' in df.columns:
            grid_l2_range = (df['grid_normalized_l2_error'].min(), df['grid_normalized_l2_error'].max())
            print(f"  grid_normalized_l2_error: {grid_l2_range[0]:.2e} to {grid_l2_range[1]:.2e}")
        
        if 'total_cost' in df.columns:
            cost_range = (df['total_cost'].min(), df['total_cost'].max())
            print(f"  total_cost: {cost_range[0]:,} to {cost_range[1]:,}")
        
        if 'threshold_value' in df.columns:
            thresholds = sorted(df['threshold_value'].unique())
            print(f"  threshold_values: {thresholds}")
            
    except Exception as e:
        print(f"❌ Error reading file: {e}")

def main():
    """Main inspection function"""
    # Define base directory
    base_dir = "analysis/data/model_performance/session3_100k_uniform"
    
    print("🔍 CSV STRUCTURE INSPECTION")
    print("=" * 60)
    
    # Look for model results files
    model_pattern = os.path.join(base_dir, "model_results_*.csv")
    model_files = sorted(glob.glob(model_pattern))
    
    if model_files:
        print(f"\n📁 Found {len(model_files)} model result files")
        # Inspect ALL model files to check for inconsistencies
        for model_file in model_files:
            file_name = os.path.basename(model_file)
            inspect_csv_structure(model_file, f"MODEL FILE: {file_name}")
    else:
        print(f"\n❌ No model files found matching: {model_pattern}")
    
    # Look for baseline files
    baseline_patterns = [
        "baseline_results_no-amr_*.csv",
        "baseline_results_conventional-amr_*.csv"
    ]
    
    for pattern in baseline_patterns:
        baseline_pattern = os.path.join(base_dir, pattern)
        baseline_files = glob.glob(baseline_pattern)
        
        if baseline_files:
            print(f"\n📁 Found {len(baseline_files)} files matching {pattern}")
            # Inspect first file of each type
            inspect_csv_structure(baseline_files[0], f"BASELINE FILE ({pattern.split('_')[2]})")

if __name__ == "__main__":
    main()