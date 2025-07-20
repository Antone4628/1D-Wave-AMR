#!/usr/bin/env python3
"""
Single Animation Job Executor

Executes individual animation jobs based on SLURM array task ID.
Called by SLURM array jobs to run specific model animations.

Usage:
    python run_single_animation.py <task_id> <mode> <sweep_name>
    
Examples:
    python run_single_animation.py 1 snapshot session3_100k_uniform
    python run_single_animation.py 5 final session3_100k_uniform
"""

import os
import sys
import json
import subprocess
import argparse
from pathlib import Path

# Get absolute path to project root
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 
    '..',
    '..'
))
sys.path.append(PROJECT_ROOT)

class SingleAnimationRunner:
    """Execute individual animation based on job definition."""
    
    def __init__(self, task_id, mode, sweep_name, verbose=True):
        """
        Initialize single animation runner.
        
        Args:
            task_id (int): SLURM array task ID (1-indexed)
            mode (str): Animation mode ('snapshot' or 'final')
            sweep_name (str): Parameter sweep name
            verbose (bool): Whether to print detailed output
        """
        self.task_id = task_id
        self.mode = mode
        self.sweep_name = sweep_name
        self.verbose = verbose
        
        # Set up paths
        self.data_dir = os.path.join(PROJECT_ROOT, 'analysis', 'data', 'model_performance', sweep_name)
        self.batch_output_dir = os.path.join(self.data_dir, 'batch_analysis')
        self.jobs_dir = os.path.join(self.batch_output_dir, 'animation_jobs')
        
        # Job definition file
        self.jobs_file = os.path.join(self.jobs_dir, f'animation_jobs_{mode}.json')
        
        # Single model runner script
        self.runner_script = os.path.join(PROJECT_ROOT, 'analysis', 'model_performance', 'single_model_runner_batch.py')
        
    def load_job_definition(self):
        """
        Load job definition from JSON file.
        
        Returns:
            dict: Job definition for this task
        """
        if not os.path.exists(self.jobs_file):
            raise FileNotFoundError(f"Jobs file not found: {self.jobs_file}")
            
        with open(self.jobs_file, 'r') as f:
            jobs = json.load(f)
            
        # Convert to 0-indexed
        job_index = self.task_id - 1
        
        if job_index < 0 or job_index >= len(jobs):
            raise IndexError(f"Task ID {self.task_id} out of range (1-{len(jobs)})")
            
        job = jobs[job_index]
        
        if self.verbose:
            print(f"📋 Loaded job definition:")
            print(f"   Job ID: {job['job_id']}")
            print(f"   Model Type: {job['model_type']}")
            print(f"   Config ID: {job['config_id']}")
            print(f"   Animation Mode: {job['animation_mode']}")
            
        return job
    
    def execute_animation(self, job):
        """
        Execute animation using single_model_runner_batch.py.
        
        Args:
            job (dict): Job definition with all parameters
        """
        if self.verbose:
            print(f"\n🎬 Executing animation...")
            print(f"   Model: {os.path.basename(job['model_path'])}")
            print(f"   Config: {job['config_id']}")
            print(f"   Mode: {job['animation_mode']}")
            
        # Build command arguments
        cmd = [
            'python', self.runner_script,
            '--model-path', job['model_path'],
            '--plot-mode', job['animation_mode'],
            '--batch-analysis-output',
            '--eval-refinement', str(job['eval_refinement']),
            '--eval-budget', str(job['eval_budget']),
            '--eval-max-level', str(job['eval_max_level']),
            '--initial-refinement', str(job['initial_refinement']),
            '--element-budget', str(job['element_budget']),
            '--max-level', str(job['max_level'])
        ]
        
        if self.verbose:
            print(f"   Command: {' '.join(cmd)}")
            
        try:
            # Execute the animation
            result = subprocess.run(
                cmd,
                cwd=PROJECT_ROOT,
                capture_output=True,
                text=True,
                timeout=3600  # 1 hour timeout
            )
            
            if result.returncode == 0:
                if self.verbose:
                    print(f"✅ Animation completed successfully")
                    if result.stdout.strip():
                        print(f"   Output: {result.stdout.strip()}")
            else:
                print(f"❌ Animation failed with return code {result.returncode}")
                if result.stderr.strip():
                    print(f"   Error: {result.stderr.strip()}")
                if result.stdout.strip():
                    print(f"   Output: {result.stdout.strip()}")
                sys.exit(1)
                
        except subprocess.TimeoutExpired:
            print(f"❌ Animation timed out after 1 hour")
            sys.exit(1)
        except Exception as e:
            print(f"❌ Animation failed with exception: {e}")
            sys.exit(1)
    
    def verify_output(self, job):
        """
        Verify that animation output was created.
        
        Args:
            job (dict): Job definition
        """
        # Expected output path
        config_dir = os.path.join(self.batch_output_dir, job['config_id'])
        expected_filename = f"{job['animation_mode']}_{job['model_type']}_{job['config_id']}.png"
        expected_path = os.path.join(config_dir, expected_filename)
        
        if os.path.exists(expected_path):
            file_size = os.path.getsize(expected_path)
            if self.verbose:
                print(f"✅ Output verified: {expected_filename} ({file_size:,} bytes)")
        else:
            print(f"⚠️  Expected output not found: {expected_path}")
    
    def run(self):
        """Execute the complete single animation job."""
        if self.verbose:
            print(f"🎯 Single Animation Runner")
            print(f"   Task ID: {self.task_id}")
            print(f"   Mode: {self.mode}")
            print(f"   Sweep: {self.sweep_name}")
            print(f"   Jobs file: {os.path.basename(self.jobs_file)}")
            
        # Load job definition
        job = self.load_job_definition()
        
        # Execute animation
        self.execute_animation(job)
        
        # Verify output
        self.verify_output(job)
        
        if self.verbose:
            print(f"\n🎉 Animation job {self.task_id} completed successfully!")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='Execute single animation job')
    parser.add_argument('task_id', type=int, help='SLURM array task ID (1-indexed)')
    parser.add_argument('mode', choices=['snapshot', 'final'], help='Animation mode')
    parser.add_argument('sweep_name', help='Parameter sweep name')
    parser.add_argument('--verbose', action='store_true', default=True, help='Print detailed output')
    parser.add_argument('--quiet', dest='verbose', action='store_false', help='Minimal output')
    
    args = parser.parse_args()
    
    try:
        runner = SingleAnimationRunner(
            task_id=args.task_id,
            mode=args.mode,
            sweep_name=args.sweep_name,
            verbose=args.verbose
        )
        runner.run()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()