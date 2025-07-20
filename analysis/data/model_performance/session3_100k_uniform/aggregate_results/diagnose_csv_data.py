#!/usr/bin/env python3
"""
Diagnose the actual data in the CSV files to understand the correct filtering criteria.
"""

import pandas as pd
import numpy as np

def diagnose_csv(filename):
    """Analyze a CSV file to understand its structure and values."""
    
    print(f"\n=== ANALYZING {filename} ===")
    
    try:
        df = pd.read_csv(filename)
        print(f"Total rows: {len(df)}")
        print(f"Columns: {list(df.columns)}")
        
        # Show the key columns we care about
        key_cols = ['config_id', 'initial_refinement', 'element_budget', 'max_level']
        available_cols = [col for col in key_cols if col in df.columns]
        
        print(f"\nKey configuration columns:")
        for col in available_cols:
            unique_vals = sorted(df[col].dropna().unique())
            print(f"  {col}: {unique_vals}")
        
        # Show some sample rows
        print(f"\nFirst 5 rows of key columns:")
        print(df[available_cols].head())
        
        # Check for evaluation_element_budget column
        if 'evaluation_element_budget' in df.columns:
            eval_budgets = sorted(df['evaluation_element_budget'].dropna().unique())
            print(f"\nEvaluation element budgets: {eval_budgets}")
        
        # Group by config_id to see patterns
        if 'config_id' in df.columns:
            config_counts = df['config_id'].value_counts()
            print(f"\nConfigurations (top 10):")
            for config, count in config_counts.head(10).items():
                print(f"  {config}: {count} model(s)")
        
        return df
        
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return None

def main():
    """Diagnose all CSV files."""
    
    files = ['lowest_cost_models.csv', 'lowest_l2_models.csv', 'optimal_neutral_models.csv']
    
    for filename in files:
        try:
            df = diagnose_csv(filename)
        except FileNotFoundError:
            print(f"File {filename} not found!")
    
    print("\n" + "="*60)
    print("DIAGNOSIS COMPLETE")
    print("Based on the output above, we can determine:")
    print("1. What the actual refinement levels are")
    print("2. What the actual element_budget values are") 
    print("3. How to properly filter for the 4x4 grid")

if __name__ == "__main__":
    main()