#!/usr/bin/env python3
"""
Batch Animation Runner for DRL-AMR Key Models

Orchestrates animation generation for all 48 key models (16 configs × 3 model types)
in both snapshot and final modes, using SLURM array jobs for parallel processing.

Directory Structure Created:
analysis/data/model_performance/session3_100k_uniform/batch_analysis/
├── ref4_budget50_max4/
│   ├── snapshot_lowest_cost_ref4_budget50_max4.png
│   ├── snapshot_lowest_l2_ref4_budget50_max4.png  
│   ├── snapshot_optimal_neutral_ref4_budget50_max4.png
│   ├── final_lowest_cost_ref4_budget50_max4.png
│   ├── final_lowest_l2_ref4_budget50_max4.png
│   └── final_optimal_neutral_ref4_budget50_max4.png
├── [... 15 more config directories]
└── animation_jobs/
    ├── animation_jobs_snapshot.json
    ├── animation_jobs_final.json
    ├── slurm_animation_snapshot.slurm
    └── slurm_animation_final.slurm

Usage:
    python batch_animation_runner.py session3_100k_uniform [--dry-run] [--test-count N]
"""

import os
import sys
import json
import argparse
from datetime import datetime
from pathlib import Path
import csv

# Get absolute path to project root
# PROJECT_ROOT = os.path.abspath(os.path.join(
#     os.path.dirname(__file__), 
#     '..',
#     '..'
# ))
# sys.path.append(PROJECT_ROOT)

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

class BatchAnimationRunner:
    """Automated batch animation runner for key models."""
    
    def __init__(self, sweep_name, dry_run=False, test_count=None, verbose=True):
        """
        Initialize the batch animation runner.
        
        Args:
            sweep_name (str): Name of the sweep (e.g., 'session3_100k_uniform')
            dry_run (bool): Whether to only show what would be done
            test_count (int): Limit to N jobs for testing (None = all jobs)
            verbose (bool): Whether to print detailed progress
        """
        self.sweep_name = sweep_name
        self.dry_run = dry_run
        self.test_count = test_count
        self.verbose = verbose
        
        # Set up paths
        self.data_dir = os.path.join(PROJECT_ROOT, 'analysis', 'data', 'model_performance', sweep_name)
        self.batch_output_dir = os.path.join(self.data_dir, 'batch_analysis')
        self.aggregate_dir = os.path.join(self.data_dir, 'aggregate_results')
        self.jobs_dir = os.path.join(self.batch_output_dir, 'animation_jobs')
        
        # SLURM scripts go in project root slurm_scripts directory (consistent with other batch scripts)
        self.slurm_dir = os.path.join(PROJECT_ROOT, 'slurm_scripts')
        
        # CSV files with cleaned key models
        self.csv_files = {
            'lowest_cost': os.path.join(self.aggregate_dir, 'lowest_cost_models_cleaned.csv'),
            'lowest_l2': os.path.join(self.aggregate_dir, 'lowest_l2_models_cleaned.csv'),
            'optimal_neutral': os.path.join(self.aggregate_dir, 'optimal_neutral_models_cleaned.csv')
        }
        
        # Animation modes to generate
        self.animation_modes = ['snapshot', 'final']
        
        # Validate setup
        self._validate_setup()
        
    def _validate_setup(self):
        """Validate that required directories and files exist."""
        if not os.path.exists(self.data_dir):
            raise FileNotFoundError(f"Data directory not found: {self.data_dir}")
            
        if not os.path.exists(self.aggregate_dir):
            raise FileNotFoundError(f"Aggregate results directory not found: {self.aggregate_dir}")
            
        # Check for cleaned CSV files
        for model_type, csv_path in self.csv_files.items():
            if not os.path.exists(csv_path):
                raise FileNotFoundError(f"Cleaned CSV file not found: {csv_path}")
                
        # Create directories
        os.makedirs(self.jobs_dir, exist_ok=True)
        os.makedirs(self.slurm_dir, exist_ok=True)
        
        if self.verbose:
            print(f"✅ Validation complete - all required files found")
            print(f"📁 Jobs directory: {self.jobs_dir}")
            print(f"📁 SLURM directory: {self.slurm_dir}")
    
    def load_animation_targets(self):
        """
        Load all models from cleaned CSV files.
        
        Returns:
            dict: Animation jobs organized by mode
        """
        jobs_by_mode = {mode: [] for mode in self.animation_modes}
        
        if self.verbose:
            print(f"\n📖 Loading animation targets from CSV files...")
            
        for model_type, csv_path in self.csv_files.items():
            if self.verbose:
                print(f"   Reading {model_type} models from {os.path.basename(csv_path)}")
                
            with open(csv_path, 'r') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
                
                for row in rows:
                    # Create animation job for each mode
                    for mode in self.animation_modes:
                        job = self._create_animation_job(row, model_type, mode)
                        jobs_by_mode[mode].append(job)
                        
        # Apply test count limit if specified
        if self.test_count is not None:
            for mode in self.animation_modes:
                jobs_by_mode[mode] = jobs_by_mode[mode][:self.test_count]
                
        if self.verbose:
            for mode in self.animation_modes:
                print(f"   📊 {mode} mode: {len(jobs_by_mode[mode])} animation jobs")
            print(f"   📊 Total animations: {sum(len(jobs) for jobs in jobs_by_mode.values())}")
                
        return jobs_by_mode
    
    def _create_animation_job(self, csv_row, model_type, animation_mode):
        """
        Create animation job definition from CSV row.
        
        Args:
            csv_row (dict): Row from cleaned CSV file
            model_type (str): Model type ('lowest_cost', 'lowest_l2', 'optimal_neutral')
            animation_mode (str): Animation mode ('snapshot', 'final')
            
        Returns:
            dict: Complete job definition
        """
        config_id = csv_row['config_id']
        
        # Extract evaluation parameters from CSV (CRITICAL for consistency)
        initial_refinement = int(csv_row['initial_refinement'])
        element_budget = int(csv_row['evaluation_element_budget'])
        max_level = int(csv_row['max_level'])
        
        # Create job definition
        job = {
            'job_id': f"{animation_mode}_{model_type}_{config_id}",
            'model_type': model_type,
            'animation_mode': animation_mode,
            'config_id': config_id,
            'model_path': csv_row['model_path'],
            
            # Evaluation parameters (from CSV - ensures consistency)
            'initial_refinement': initial_refinement,
            'element_budget': element_budget,
            'max_level': max_level,
            
            # Directory naming parameters (must match evaluation params)
            'eval_refinement': initial_refinement,
            'eval_budget': element_budget,
            'eval_max_level': max_level,
            
            # Additional metadata for tracking
            'final_l2_error': float(csv_row['final_l2_error']),
            'total_cost': int(csv_row['total_cost']),
            'created_at': datetime.now().isoformat()
        }
        
        return job
    
    def generate_animation_jobs(self):
        """
        Generate all animation job definitions.
        
        Returns:
            dict: Jobs organized by animation mode
        """
        if self.verbose:
            print(f"\n🔧 Generating animation jobs...")
            
        jobs_by_mode = self.load_animation_targets()
        
        # Save job definitions to JSON files
        for mode, jobs in jobs_by_mode.items():
            jobs_file = os.path.join(self.jobs_dir, f'animation_jobs_{mode}.json')
            
            if not self.dry_run:
                with open(jobs_file, 'w') as f:
                    json.dump(jobs, f, indent=2)
                    
            if self.verbose:
                print(f"   💾 Saved {len(jobs)} {mode} jobs to {os.path.basename(jobs_file)}")
                
        return jobs_by_mode
    
    def create_slurm_scripts(self, jobs_by_mode):
        """
        Generate SLURM job scripts for parallel animation processing.
        
        Args:
            jobs_by_mode (dict): Animation jobs organized by mode
        """
        if self.verbose:
            print(f"\n📝 Creating SLURM job scripts...")
            
        for mode, jobs in jobs_by_mode.items():
            if len(jobs) == 0:
                continue
                
            script_content = self._create_slurm_script_content(mode, len(jobs))
            script_file = os.path.join(self.slurm_dir, f'batch_animation_{mode}.slurm')
            
            if not self.dry_run:
                with open(script_file, 'w') as f:
                    f.write(script_content)
                    
            if self.verbose:
                print(f"   📜 Created {mode} SLURM script: {os.path.basename(script_file)}")
                print(f"      Array size: 1-{len(jobs)} (one job per model/mode combination)")
                
    def _create_slurm_script_content(self, mode, job_count):
        """
        Create SLURM script content for animation jobs.
        
        Args:
            mode (str): Animation mode
            job_count (int): Number of jobs in array
            
        Returns:
            str: SLURM script content
        """
        script_content = f'''#!/bin/bash
#SBATCH --job-name=batch_anim_{mode}
#SBATCH --array=1-{job_count}
#SBATCH --time=01:00:00
#SBATCH --mem=4G
#SBATCH --cpus-per-task=1
#SBATCH --output={self.jobs_dir}/slurm_logs/batch_anim_{mode}_%A_%a.out
#SBATCH --error={self.jobs_dir}/slurm_logs/batch_anim_{mode}_%A_%a.err

# Load environment
source ~/anaconda3/etc/profile.d/conda.sh
conda activate rl-amr

# Navigate to project root
cd {PROJECT_ROOT}

# Create logs directory if it doesn't exist
mkdir -p {self.jobs_dir}/slurm_logs

# Run single animation based on array task ID
python analysis/model_performance/run_single_animation.py $SLURM_ARRAY_TASK_ID {mode} {self.sweep_name}

echo "Animation job $SLURM_ARRAY_TASK_ID ({mode} mode) completed at $(date)"
'''
        return script_content
    
    def create_job_summary(self, jobs_by_mode):
        """
        Create summary report of animation jobs.
        
        Args:
            jobs_by_mode (dict): Animation jobs organized by mode
        """
        if self.verbose:
            print(f"\n📊 Animation Jobs Summary")
            print(f"=" * 50)
            
        total_jobs = 0
        for mode, jobs in jobs_by_mode.items():
            print(f"{mode.upper()} MODE: {len(jobs)} animations")
            total_jobs += len(jobs)
            
            # Count by model type
            model_type_counts = {}
            for job in jobs:
                model_type = job['model_type']
                model_type_counts[model_type] = model_type_counts.get(model_type, 0) + 1
                
            for model_type, count in sorted(model_type_counts.items()):
                print(f"  {model_type}: {count} configs")
                
        print(f"\nTOTAL ANIMATIONS: {total_jobs}")
        print(f"Expected output files: {total_jobs} PNG files")
        
        if self.test_count is not None:
            print(f"\n⚠️  TEST MODE: Limited to {self.test_count} jobs per mode")
            
    def run(self):
        """Execute the complete batch animation setup."""
        if self.verbose:
            print(f"🚀 DRL-AMR Batch Animation Runner")
            print(f"Sweep: {self.sweep_name}")
            print(f"Mode: {'DRY RUN' if self.dry_run else 'PRODUCTION'}")
            if self.test_count:
                print(f"Test limit: {self.test_count} jobs per mode")
            print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
        # Generate all animation jobs
        jobs_by_mode = self.generate_animation_jobs()
        
        # Create SLURM scripts
        self.create_slurm_scripts(jobs_by_mode)
        
        # Create summary
        self.create_job_summary(jobs_by_mode)
        
        if self.verbose:
            print(f"\n✅ Batch animation setup complete!")
            print(f"📁 Job files location: {self.jobs_dir}")
            print(f"📁 SLURM scripts location: {self.slurm_dir}")
            print(f"\n🔥 Ready to submit SLURM jobs:")
            for mode in self.animation_modes:
                if len(jobs_by_mode[mode]) > 0:
                    script_file = f"batch_animation_{mode}.slurm"
                    print(f"   sbatch slurm_scripts/{script_file}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='Batch Animation Runner for DRL-AMR Key Models')
    parser.add_argument('sweep_name', help='Name of the parameter sweep (e.g., session3_100k_uniform)')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done without creating files')
    parser.add_argument('--test-count', type=int, help='Limit to N jobs per mode for testing')
    parser.add_argument('--verbose', action='store_true', default=True, help='Print detailed progress')
    parser.add_argument('--quiet', dest='verbose', action='store_false', help='Minimal output')
    
    args = parser.parse_args()
    
    try:
        runner = BatchAnimationRunner(
            sweep_name=args.sweep_name,
            dry_run=args.dry_run,
            test_count=args.test_count,
            verbose=args.verbose
        )
        runner.run()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()