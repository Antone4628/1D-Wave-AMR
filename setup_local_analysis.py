#!/usr/bin/env python3
"""
Setup Local Analysis Environment
Creates the directory structure and data transfer system for AMR parameter analysis.
"""

import os
import subprocess
from pathlib import Path
import shutil

def setup_analysis_environment(base_dir="./analysis"):
    """Create the local analysis directory structure"""
    
    base_path = Path(base_dir)
    
    # Define directory structure
    directories = [
        "data_management",
        "statistical_analysis", 
        "interactive_analysis",
        "automated_reports",
        "utilities",
        "data/raw",
        "data/processed", 
        "data/exports",
        "outputs/reports",
        "outputs/figures",
        "outputs/thesis_assets"
    ]
    
    print("Setting up analysis environment...")
    print(f"Base directory: {base_path.absolute()}")
    
    # Create directories
    for dir_name in directories:
        dir_path = base_path / dir_name
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"✓ Created: {dir_path}")
    
    # Create __init__.py files for Python packages
    python_packages = ["data_management", "statistical_analysis", "utilities"]
    for pkg in python_packages:
        init_file = base_path / pkg / "__init__.py"
        init_file.touch()
        print(f"✓ Created: {init_file}")
    
    # Create basic configuration file
    config_content = '''"""
Configuration for AMR Parameter Analysis
"""

# HPC Connection Settings
HPC_HOST = "antonechacartegu@borah-login.boisestate.edu"
HPC_BASE_PATH = "/bsuhome/antonechacartegu/projects/drl-amr/1D-Wave-AMR"

# Analysis Settings
CURRENT_SWEEP = "full_param_sweep_data_20250601_105453"
PARAMETER_SPACE = {
    'gamma_c': [25.0, 50.0, 100.0],
    'step_domain_fraction': [0.025, 0.05, 0.1],
    'rl_iterations_per_timestep': [10, 25, 40],
    'element_budget': [25, 30, 40]
}

# Paths
DATA_DIR = "data"
RAW_DATA_DIR = "data/raw"
PROCESSED_DATA_DIR = "data/processed"
OUTPUTS_DIR = "outputs"

# Analysis Parameters
CONVERGENCE_THRESHOLDS = {
    'well_converged': 0.8,
    'moderate': 0.5,
    'under_trained': 0.2
}

# Visualization Settings
FIGURE_DPI = 300
FIGURE_FORMAT = 'png'
THESIS_FIGURE_FORMAT = 'pdf'
'''
    
    config_file = base_path / "utilities" / "config.py"
    with open(config_file, 'w') as f:
        f.write(config_content)
    print(f"✓ Created: {config_file}")
    
    print(f"\n✅ Analysis environment setup complete!")
    print(f"📁 Base directory: {base_path.absolute()}")
    return base_path

def create_data_transfer_script(analysis_dir="./analysis"):
    """Create script to transfer JSON data from HPC"""
    
    base_path = Path(analysis_dir)
    script_content = '''#!/usr/bin/env python3
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
sys.path.append(str(Path(__file__).parent.parent / "utilities"))
from config import HPC_HOST, HPC_BASE_PATH, CURRENT_SWEEP, RAW_DATA_DIR

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
    
    print(f"\\n📊 Transfer validation:")
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
        print("\\n🎉 Data transfer complete! Ready for analysis.")
'''
    
    script_path = base_path / "data_management" / "transfer_json_data.py"
    with open(script_path, 'w') as f:
        f.write(script_content)
    
    # Make executable
    os.chmod(script_path, 0o755)
    print(f"✓ Created: {script_path}")
    
    return script_path

if __name__ == "__main__":
    # Setup the environment
    analysis_path = setup_analysis_environment()
    
    # Create transfer script
    transfer_script = create_data_transfer_script(analysis_path)
    
    print(f"\\n🚀 Ready to begin!")
    print(f"\\nNext steps:")
    print(f"1. Run HPC survey: Upload hpc_data_survey.py to HPC and run")
    print(f"2. Transfer data: python {transfer_script} --dry-run")
    print(f"3. Transfer data: python {transfer_script}")
    print(f"4. Begin data analysis!")