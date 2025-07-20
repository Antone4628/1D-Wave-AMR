#!/usr/bin/env python3
"""
Clean up aggregate CSV files to contain only the 4x4 target grid:
- Refinement levels: 4, 5, 6, 7
- Evaluation element budgets: 50, 80, 100, 150
- Total: 16 configurations × 3 model types = 48 models

Note: Filters on 'evaluation_element_budget' column, not 'element_budget'
"""

import pandas as pd
import os

# Define target parameters
TARGET_REFINEMENTS = [4, 5, 6, 7]
TARGET_EVAL_BUDGETS = [50, 80, 100, 150]

def clean_csv_file(input_filename, output_filename):
    """Clean a single CSV file to only include target configurations."""
    
    print(f"Processing {input_filename}...")
    
    # Read the CSV
    df = pd.read_csv(input_filename)
    print(f"  Original rows: {len(df)}")
    
    # Filter to target refinement levels and EVALUATION budgets
    # Also ensure config_id follows proper format: ref{X}_budget{Y}_max{X}
    def has_proper_config_format(row):
        config_id = row['config_id']
        ref_level = row['initial_refinement']
        if pd.isna(config_id) or pd.isna(ref_level):
            return False
        # Check if config_id ends with _max{ref_level}
        expected_suffix = f"_max{int(ref_level)}"
        return config_id.endswith(expected_suffix)
    
    filtered_df = df[
        (df['initial_refinement'].isin(TARGET_REFINEMENTS)) &
        (df['evaluation_element_budget'].isin(TARGET_EVAL_BUDGETS)) &
        (df['initial_refinement'].notna()) &
        (df['evaluation_element_budget'].notna()) &
        (df.apply(has_proper_config_format, axis=1))  # Proper config_id format
    ].copy()
    
    print(f"  After filtering: {len(filtered_df)}")
    
    # Verify we have exactly one model per configuration
    config_counts = filtered_df.groupby(['initial_refinement', 'evaluation_element_budget']).size()
    print(f"  Configuration counts:")
    for (ref, budget), count in config_counts.items():
        print(f"    ref{ref}_budget{budget}: {count} model(s)")
    
    # Check if we have the expected 16 configurations
    expected_configs = len(TARGET_REFINEMENTS) * len(TARGET_EVAL_BUDGETS)
    if len(config_counts) != expected_configs:
        print(f"  WARNING: Expected {expected_configs} configurations, got {len(config_counts)}")
        missing_configs = []
        for ref in TARGET_REFINEMENTS:
            for budget in TARGET_EVAL_BUDGETS:
                if (ref, budget) not in config_counts.index:
                    missing_configs.append(f"ref{ref}_budget{budget}")
        if missing_configs:
            print(f"  Missing configurations: {missing_configs}")
    
    # Save cleaned CSV
    filtered_df.to_csv(output_filename, index=False)
    print(f"  Saved to {output_filename}")
    print(f"  Final model count: {len(filtered_df)}")
    
    return len(filtered_df)

def main():
    """Main function to clean all three CSV files."""
    
    csv_files = [
        ('lowest_cost_models.csv', 'lowest_cost_models_cleaned.csv'),
        ('lowest_l2_models.csv', 'lowest_l2_models_cleaned.csv'),
        ('optimal_neutral_models.csv', 'optimal_neutral_models_cleaned.csv')
    ]
    
    total_models = 0
    
    print("=== CLEANING AGGREGATE CSV FILES ===")
    print(f"Target grid: {len(TARGET_REFINEMENTS)} refinement levels × {len(TARGET_EVAL_BUDGETS)} eval budgets = {len(TARGET_REFINEMENTS) * len(TARGET_EVAL_BUDGETS)} configurations")
    print(f"Expected total models: {len(TARGET_REFINEMENTS) * len(TARGET_EVAL_BUDGETS) * 3} models (16 configs × 3 types)")
    print()
    
    for input_file, output_file in csv_files:
        if os.path.exists(input_file):
            count = clean_csv_file(input_file, output_file)
            total_models += count
            print()
        else:
            print(f"WARNING: {input_file} not found!")
            print()
    
    print("=== SUMMARY ===")
    print(f"Total models after cleanup: {total_models}")
    print(f"Expected: {len(TARGET_REFINEMENTS) * len(TARGET_EVAL_BUDGETS) * 3}")
    
    if total_models == len(TARGET_REFINEMENTS) * len(TARGET_EVAL_BUDGETS) * 3:
        print("✅ SUCCESS: CSV cleanup completed successfully!")
    else:
        print("❌ WARNING: Model count doesn't match expected value")

if __name__ == "__main__":
    main()