#!/usr/bin/env python3
"""
Data Transfer Script for AMR Parameter Analysis
Transfers JSON training metrics from Borah HPC to local analysis environment.
"""

import subprocess
import os
from pathlib import Path
import json
import sys

# Add utilities to path
# sys.path.append(str(Path(__file__).parent.parent / "utilities"))
# from config import HPC_HOST, HPC_BASE_PATH, CURRENT_SWEEP, RAW_DATA_DIR

PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 
    '..',  # Go up to analysis/
    '..'   # Go up to main project root (1D_wave_AMR/)
))
sys.path.append(PROJECT_ROOT)
from analysis.utilities.config import HPC_HOST, HPC_BASE_PATH, CURRENT_SWEEP, RAW_DATA_DIR


def transfer_json_data(sweep_name=CURRENT_SWEEP, dry_run=False):
    """Transfer JSON training metrics from HPC"""
    
    # Define paths
    remote_path = f"{HPC_HOST}:{HPC_BASE_PATH}/results/{sweep_name}/"
    local_path = Path(RAW_DATA_DIR) / sweep_name
    
    print(f"Transferring data from HPC...")
    print(f"Remote: {remote_path}")
    print(f"Local: {local_path}")
    
    # Create local directory
    local_path.mkdir(parents=True, exist_ok=True)
    
    # Build rsync command to transfer only JSON files
    rsync_cmd = [
        "rsync", "-av", "--progress",
        "--include=*/",  # Include directories
        "--include=*_training_metrics.json",  # Include JSON files
        "--include=*_training_summary.csv",   # Include CSV files too
        "--exclude=*",   # Exclude everything else
        remote_path,
        str(local_path) + "/"
    ]
    
    if dry_run:
        rsync_cmd.insert(1, "--dry-run")
        print("DRY RUN - Command that would be executed:")
        print(" ".join(rsync_cmd))
        return
    
    print("Executing transfer...")
    print("Command:", " ".join(rsync_cmd))
    
    try:
        result = subprocess.run(rsync_cmd, check=True, capture_output=True, text=True)
        print("✅ Transfer completed successfully!")
        print(result.stdout)
        
        # Validate transferred data
        validate_transfer(local_path)
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Transfer failed: {e}")
        print(f"Error output: {e.stderr}")
        return False
    
    return True

def validate_transfer(data_path):
    """Validate that JSON files were transferred correctly"""
    
    json_files = list(data_path.rglob("*_training_metrics.json"))
    csv_files = list(data_path.rglob("*_training_summary.csv"))
    
    print(f"\n📊 Transfer validation:")
    print(f"JSON files found: {len(json_files)}")
    print(f"CSV files found: {len(csv_files)}")
    
    # Check a sample JSON file
    if json_files:
        sample_file = json_files[0]
        try:
            with open(sample_file, 'r') as f:
                data = json.load(f)
            print(f"✓ Sample JSON file valid: {len(data)} metrics")
            print(f"  Sample keys: {list(data.keys())[:5]}")
        except Exception as e:
            print(f"⚠️ Issue with sample JSON: {e}")
    
    return len(json_files), len(csv_files)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Transfer AMR training data from HPC")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be transferred")
    parser.add_argument("--sweep", default=CURRENT_SWEEP, help="Sweep name to transfer")
    
    args = parser.parse_args()
    
    success = transfer_json_data(args.sweep, args.dry_run)
    if success and not args.dry_run:
        print("\n🎉 Data transfer complete! Ready for analysis.")
