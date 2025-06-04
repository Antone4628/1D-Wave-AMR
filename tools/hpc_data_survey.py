#!/usr/bin/env python3
"""
HPC Data Survey Script
Survey the JSON data structure on Borah HPC for the full parameter sweep.
Run this ON the HPC to understand what data we have available.
"""

import os
import glob
import json
from pathlib import Path
import pandas as pd

def survey_sweep_data(base_path="/bsuhome/antonechacartegu/projects/drl-amr/1D-Wave-AMR"):
    """Survey the parameter sweep data structure on HPC"""
    
    # Define the sweep directory
    sweep_dir = Path(base_path) / "results" / "full_param_sweep_data_20250601_105453"
    
    print(f"Surveying data in: {sweep_dir}")
    print("=" * 80)
    
    if not sweep_dir.exists():
        print(f"ERROR: Sweep directory not found: {sweep_dir}")
        return
    
    # Find all parameter combination directories
    param_dirs = list(sweep_dir.glob("gamma_*_step_*_rl_*_budget_*"))
    print(f"Found {len(param_dirs)} parameter combination directories")
    
    # Analyze the data structure
    json_files = []
    missing_json = []
    
    for param_dir in sorted(param_dirs):
        # Look for JSON files
        json_pattern = param_dir / "*_training_metrics.json"
        found_json = list(param_dir.glob("*_training_metrics.json"))
        
        if found_json:
            json_files.extend(found_json)
            print(f"✓ {param_dir.name}: {len(found_json)} JSON file(s)")
        else:
            missing_json.append(param_dir)
            print(f"✗ {param_dir.name}: No JSON files found")
    
    print("\n" + "=" * 80)
    print(f"SUMMARY:")
    print(f"Total parameter directories: {len(param_dirs)}")
    print(f"Directories with JSON files: {len(param_dirs) - len(missing_json)}")
    print(f"Total JSON files found: {len(json_files)}")
    print(f"Missing JSON files: {len(missing_json)}")
    
    if missing_json:
        print(f"\nDirectories missing JSON files:")
        for missing in missing_json:
            print(f"  - {missing.name}")
    
    # Sample a few JSON files to understand structure
    if json_files:
        print(f"\nSampling JSON file structure (first 3 files):")
        for i, json_file in enumerate(json_files[:3]):
            print(f"\n--- Sample {i+1}: {json_file.name} ---")
            try:
                with open(json_file, 'r') as f:
                    data = json.load(f)
                print(f"Keys in JSON: {list(data.keys())}")
                print(f"Total metrics: {len(data)}")
                
                # Show a few sample metrics
                sample_keys = list(data.keys())[:5]
                for key in sample_keys:
                    print(f"  {key}: {data[key]}")
                    
            except Exception as e:
                print(f"ERROR reading {json_file}: {e}")
    
    # Generate transfer commands
    print(f"\n" + "=" * 80)
    print("TRANSFER COMMANDS:")
    print("To transfer JSON files to local machine, use:")
    print(f"rsync -av --include='*/' --include='*_training_metrics.json' --exclude='*' \\")
    print(f"antonechacartegu@borah-login.boisestate.edu:{sweep_dir}/ \\")
    print(f"./local_analysis_data/full_param_sweep_data_20250601_105453/")
    
    return {
        'total_dirs': len(param_dirs),
        'json_files': len(json_files),
        'missing_json': len(missing_json),
        'sweep_dir': str(sweep_dir)
    }

if __name__ == "__main__":
    results = survey_sweep_data()
    print(f"\nSurvey complete. Results: {results}")