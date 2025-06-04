#!/usr/bin/env python3
import os
import shutil
import glob

def collect_reports():
    base_dir = "results/full_param_sweep_2025-05-29_105232"
    output_dir = "collected_reports"
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Find all result directories
    pattern = f"{base_dir}/gamma_*"
    directories = glob.glob(pattern)
    
    collected = 0
    for dir_path in directories:
        # Extract parameters from directory name
        dirname = os.path.basename(dir_path)
        
        # Check if training_report.pdf exists
        report_path = os.path.join(dir_path, "training_report.pdf")
        if os.path.exists(report_path):
            # Create new filename
            new_name = f"{dirname}_50k_training_report.pdf"
            new_path = os.path.join(output_dir, new_name)
            
            # Copy with new name
            shutil.copy2(report_path, new_path)
            print(f"Collected: {new_name}")
            collected += 1
        else:
            print(f"Missing report: {dirname}")
    
    print(f"\nCollected {collected} training reports to {output_dir}/")

if __name__ == "__main__":
    collect_reports()
