#!/usr/bin/env python3
"""
Simple Transfer Tool for ANOVA Analysis Files

This script transfers only the JSON and CSV files needed for your existing
ANOVA analysis pipeline, placing them in the exact expected location and format.

Usage:
    python simple_transfer_for_anova.py session3_100k_uniform \
        --hpc-path antonechacartegu@borah-login:/path/to/1D-Wave-AMR/results/session3_100k_uniform

Expected HPC file pattern:
    results/session3_100k_uniform/gamma_X_step_Y_rl_Z_budget_W/
    ├── gamma_X_step_Y_rl_Z_budget_W_100k_training_metrics.json
    └── gamma_X_step_Y_rl_Z_budget_W_100k_training_summary.csv

Creates local structure for ANOVA analysis:
    analysis/data/raw/session3_100k_uniform/raw_metrics/
    ├── gamma_X_step_Y_rl_Z_budget_W_100k_training_metrics.json
    └── gamma_X_step_Y_rl_Z_budget_W_100k_training_summary.csv
"""

import os
import subprocess
import json
from pathlib import Path
from datetime import datetime
import argparse

class SimpleANOVATransfer:
    """Simple transfer tool focused on ANOVA analysis requirements."""
    
    def __init__(self, sweep_name: str):
        self.sweep_name = sweep_name
        
        # Local paths (matching your established convention)
        self.local_base = Path("analysis/data")
        self.local_raw = self.local_base / "raw" / sweep_name
        self.local_metrics = self.local_raw / "raw_metrics"
        
        # Expected 81 parameter combinations
        self.expected_combinations = self._generate_parameter_combinations()
    
    def _generate_parameter_combinations(self):
        """Generate the 81 expected parameter combination names."""
        gamma_values = [25.0, 50.0, 100.0]
        step_values = [0.025, 0.05, 0.1]
        rl_values = [10, 25, 40] 
        budget_values = [25, 30, 40]
        
        combinations = []
        for gamma in gamma_values:
            for step in step_values:
                for rl in rl_values:
                    for budget in budget_values:
                        combo = f"gamma_{gamma}_step_{step}_rl_{rl}_budget_{budget}"
                        combinations.append(combo)
        return combinations
    
    def setup_local_directories(self):
        """Create the expected local directory structure."""
        print(f"📁 Creating local directory structure...")
        
        directories = [
            self.local_raw,
            self.local_metrics,
            self.local_base / "processed" / self.sweep_name
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
            print(f"   Created: {directory}")
        
        return True
    
    def transfer_analysis_files(self, hpc_path: str, dry_run: bool = False):
        """Transfer JSON and CSV files using rsync."""
        print(f"🚀 Starting transfer from HPC...")
        print(f"   Source: {hpc_path}")
        print(f"   Destination: {self.local_metrics}")
        
        if dry_run:
            print("   [DRY RUN MODE - No files will be transferred]")
        
        # Transfer JSON files
        json_pattern = f"{hpc_path}/*/*_training_metrics.json"
        
        # Transfer CSV files  
        csv_pattern = f"{hpc_path}/*/*_training_summary.csv"
        
        if dry_run:
            print("Would run:")
            print(f"  rsync -avz --progress '{json_pattern}' '{self.local_metrics}/'")
            print(f"  rsync -avz --progress '{csv_pattern}' '{self.local_metrics}/'")
            return {"json_transferred": 0, "csv_transferred": 0, "dry_run": True}
        
        try:
            # Execute JSON transfer
            print("📥 Transferring JSON metrics files...")
            json_cmd_str = f"rsync -avz --progress '{json_pattern}' '{self.local_metrics}/'"
            result_json = subprocess.run(json_cmd_str, shell=True, capture_output=True, text=True)
            if result_json.returncode != 0:
                print(f"❌ JSON transfer failed: {result_json.stderr}")
                return {"error": f"JSON transfer failed: {result_json.stderr}"}
            
            # Execute CSV transfer
            print("📥 Transferring CSV summary files...")
            csv_cmd_str = f"rsync -avz --progress '{csv_pattern}' '{self.local_metrics}/'"
            result_csv = subprocess.run(csv_cmd_str, shell=True, capture_output=True, text=True)
            if result_csv.returncode != 0:
                print(f"❌ CSV transfer failed: {result_csv.stderr}")
                return {"error": f"CSV transfer failed: {result_csv.stderr}"}
            
            print("✅ Transfer completed!")
            
        except Exception as e:
            print(f"❌ Transfer error: {e}")
            return {"error": str(e)}
        
        # Count transferred files
        json_files = list(self.local_metrics.glob("*_training_metrics.json"))
        csv_files = list(self.local_metrics.glob("*_training_summary.csv"))
        
        return {
            "json_transferred": len(json_files),
            "csv_transferred": len(csv_files),
            "json_files": [f.name for f in json_files],
            "csv_files": [f.name for f in csv_files]
        }
    
    def validate_for_anova(self):
        """Validate that transferred files are ready for ANOVA analysis."""
        print(f"🔍 Validating files for ANOVA analysis...")
        
        # Check JSON files
        json_files = list(self.local_metrics.glob("*_training_metrics.json"))
        csv_files = list(self.local_metrics.glob("*_training_summary.csv"))
        
        print(f"   JSON files found: {len(json_files)}/81")
        print(f"   CSV files found: {len(csv_files)}/81")
        
        # Check if we have expected parameter combinations
        json_combos = set()
        csv_combos = set()
        
        for json_file in json_files:
            # Extract combination from filename
            combo = json_file.name.replace("_100k_training_metrics.json", "")
            json_combos.add(combo)
        
        for csv_file in csv_files:
            combo = csv_file.name.replace("_100k_training_summary.csv", "")  
            csv_combos.add(combo)
        
        # Find missing combinations
        expected_set = set(self.expected_combinations)
        missing_json = expected_set - json_combos
        missing_csv = expected_set - csv_combos
        
        validation_result = {
            "total_expected": 81,
            "json_found": len(json_files),
            "csv_found": len(csv_files),
            "missing_json": list(missing_json),
            "missing_csv": list(missing_csv),
            "ready_for_anova": len(json_files) >= 70 and len(csv_files) >= 70  # 86% threshold
        }
        
        if validation_result["ready_for_anova"]:
            print("✅ Ready for ANOVA analysis!")
            print(f"   Sufficient data: {len(json_files)} JSON, {len(csv_files)} CSV files")
            print(f"   Next step: python analysis/statistical_analysis/anova_analysis.py {self.sweep_name}")
        else:
            print("❌ Not ready for ANOVA analysis")
            if missing_json:
                print(f"   Missing JSON files for: {missing_json[:5]}...")
            if missing_csv:  
                print(f"   Missing CSV files for: {missing_csv[:5]}...")
        
        return validation_result
    
    def create_sweep_metadata(self):
        """Create basic sweep metadata file expected by analysis pipeline."""
        metadata = {
            "sweep_name": self.sweep_name,
            "transfer_timestamp": datetime.now().isoformat(),
            "total_combinations": 81,
            "parameter_space": {
                "gamma_c": [25.0, 50.0, 100.0],
                "step_domain_fraction": [0.025, 0.05, 0.1],
                "rl_iterations_per_timestep": [10, 25, 40],
                "element_budget": [25, 30, 40]
            },
            "timesteps": "100k",
            "transfer_type": "anova_analysis_files"
        }
        
        metadata_path = self.local_raw / "sweep_metadata.json"
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        print(f"📋 Created sweep metadata: {metadata_path}")
        return metadata_path


def main():
    parser = argparse.ArgumentParser(description='Transfer JSON/CSV files for ANOVA analysis')
    parser.add_argument('sweep_name', help='Name of the parameter sweep (e.g., session3_100k_uniform)')
    parser.add_argument('--hpc-path', required=True, 
                        help='HPC path with user@host:path format (e.g., user@host:/path/to/results/sweep_name)')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be transferred without doing it')
    
    args = parser.parse_args()
    
    print("="*60)
    print(f"SIMPLE ANOVA TRANSFER: {args.sweep_name}")
    print("="*60)
    
    # Initialize transfer tool
    transfer = SimpleANOVATransfer(args.sweep_name)
    
    # Setup local directories
    transfer.setup_local_directories()
    
    # Transfer files
    result = transfer.transfer_analysis_files(args.hpc_path, dry_run=args.dry_run)
    
    if "error" in result:
        print(f"💥 Transfer failed: {result['error']}")
        return 1
    
    if not args.dry_run:
        # Validate for ANOVA
        validation = transfer.validate_for_anova()
        
        # Create metadata
        transfer.create_sweep_metadata()
        
        print("\n" + "="*60)
        print("TRANSFER SUMMARY")
        print("="*60)
        print(f"JSON files: {result['json_transferred']}/81")
        print(f"CSV files: {result['csv_transferred']}/81") 
        print(f"ANOVA ready: {'✅ YES' if validation['ready_for_anova'] else '❌ NO'}")
        print(f"Data location: {transfer.local_metrics}")
        
        if validation['ready_for_anova']:
            print(f"\n🎉 Ready to run:")
            print(f"   python analysis/statistical_analysis/anova_analysis.py {args.sweep_name}")
    
    return 0


if __name__ == "__main__":
    exit(main())