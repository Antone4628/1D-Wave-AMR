#!/usr/bin/env python3
"""
Batch Analysis Runner for DRL-AMR Parameter Sweep

Automatically processes all available configurations with organized output structure:

batch_analysis/
├── ref3_budget50_max3/
│   ├── comprehensive_no_baselines/
│   │   ├── gamma_c_family_comprehensive_ref3_budget50_max3.png
│   │   ├── step_domain_fraction_family_comprehensive_ref3_budget50_max3.png
│   │   ├── rl_iterations_per_timestep_family_comprehensive_ref3_budget50_max3.png
│   │   ├── element_budget_family_comprehensive_ref3_budget50_max3.png
│   │   └── combined_families_comprehensive_ref3_budget50_max3.png
│   ├── comprehensive_with_baselines/
│   │   └── [same 5 plots with baselines]
│   └── pareto_analysis/
│       └── annotated_pareto_gamma_c_family_ref3_budget50_max3.png
├── [... all configurations]
└── aggregate_results/
    ├── lowest_cost_models.csv
    ├── lowest_l2_models.csv
    └── optimal_neutral_models.csv

Usage:
    python batch_analysis_runner.py session3_100k_uniform [--resume] [--dry-run]
"""

import os
import sys
import glob
import subprocess
import argparse
import json
from datetime import datetime
from pathlib import Path
import re

# Get absolute path to project root
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.append(PROJECT_ROOT)

class BatchAnalysisRunner:
    """Automated batch analysis runner with organized output structure."""
    
    def __init__(self, sweep_name, resume=False, dry_run=False, verbose=True):
        """
        Initialize the batch runner.
        
        Args:
            sweep_name (str): Name of the sweep (e.g., 'session3_100k_uniform')
            resume (bool): Whether to resume from previous run
            dry_run (bool): Whether to only show what would be done
            verbose (bool): Whether to print detailed progress
        """
        self.sweep_name = sweep_name
        self.resume = resume
        self.dry_run = dry_run
        self.verbose = verbose
        
        # Set up paths
        self.data_dir = os.path.join(PROJECT_ROOT, 'analysis', 'data', 'model_performance', sweep_name)
        self.batch_output_dir = os.path.join(self.data_dir, 'batch_analysis')
        self.aggregate_dir = os.path.join(self.batch_output_dir, 'aggregate_results')
        
        # Progress tracking
        self.progress_file = os.path.join(self.batch_output_dir, 'batch_progress.json')
        self.completed_operations = set()
        
        # Analysis scripts
        self.comprehensive_script = os.path.join(PROJECT_ROOT, 'analysis', 'model_performance', 'comprehensive_analyzer.py')
        self.pareto_script = os.path.join(PROJECT_ROOT, 'analysis', 'model_performance', 'pareto_key_models_analyzer.py')

        
        # Validate setup
        self._validate_setup()
        
    def _validate_setup(self):
        """Validate that required directories and scripts exist."""
        if not os.path.exists(self.data_dir):
            raise ValueError(f"Data directory not found: {self.data_dir}")
            
        if not os.path.exists(self.comprehensive_script):
            raise ValueError(f"Comprehensive analyzer script not found: {self.comprehensive_script}")
            
        if not os.path.exists(self.pareto_script):
            raise ValueError(f"Pareto analyzer script not found: {self.pareto_script}")
            
        # Create batch output directory
        os.makedirs(self.batch_output_dir, exist_ok=True)
        os.makedirs(self.aggregate_dir, exist_ok=True)
        
    def discover_configurations(self):
        """
        Discover all available model configuration files.
        
        Returns:
            list: List of configuration info dictionaries
        """
        model_files = glob.glob(os.path.join(self.data_dir, "model_results_*.csv"))
        configurations = []
        
        for model_file in model_files:
            config_info = self._extract_config_from_filename(model_file)
            if config_info['config_id'] != 'unknown':
                config_info['model_file'] = os.path.basename(model_file)
                config_info['model_path'] = model_file
                configurations.append(config_info)
                
        # Sort by initial_refinement, then element_budget
        configurations.sort(key=lambda x: (x['initial_refinement'], x['element_budget']))
        
        return configurations
        
    def _extract_config_from_filename(self, filepath):
        """Extract configuration info from model filename."""
        filename = os.path.basename(filepath)
        config_info = {
            'initial_refinement': None,
            'element_budget': None,
            'max_level': None,
            'config_id': 'unknown'
        }
        
        if 'model_results_ref' in filename:
            try:
                config_part = filename.replace('model_results_ref', '').replace('.csv', '')
                
                if '_max' in config_part:
                    # New format: ref5_budget150_max5
                    parts = config_part.split('_')
                    initial_refinement = int(parts[0])
                    element_budget = int(parts[1].replace('budget', ''))
                    max_level = int(parts[2].replace('max', ''))
                    
                    config_info.update({
                        'initial_refinement': initial_refinement,
                        'element_budget': element_budget,
                        'max_level': max_level,
                        'config_id': f"ref{initial_refinement}_budget{element_budget}_max{max_level}"
                    })
                else:
                    # Old format: ref5_budget150
                    parts = config_part.split('_budget')
                    if len(parts) == 2:
                        initial_refinement = int(parts[0])
                        element_budget = int(parts[1])
                        max_level = initial_refinement
                        
                        config_info.update({
                            'initial_refinement': initial_refinement,
                            'element_budget': element_budget,
                            'max_level': max_level,
                            'config_id': f"ref{initial_refinement}_budget{element_budget}_max{max_level}"
                        })
                        
            except (ValueError, IndexError) as e:
                if self.verbose:
                    print(f"Warning: Could not parse configuration from {filename}: {e}")
        
        return config_info
        
    def _load_progress(self):
        """Load previous progress if resuming."""
        if self.resume and os.path.exists(self.progress_file):
            try:
                with open(self.progress_file, 'r') as f:
                    progress_data = json.load(f)
                    self.completed_operations = set(progress_data.get('completed_operations', []))
                    if self.verbose:
                        print(f"Resuming: {len(self.completed_operations)} operations already completed")
            except Exception as e:
                print(f"Warning: Could not load progress file: {e}")
                self.completed_operations = set()
        else:
            self.completed_operations = set()
            
    def _save_progress(self):
        """Save current progress."""
        progress_data = {
            'timestamp': datetime.now().isoformat(),
            'sweep_name': self.sweep_name,
            'completed_operations': list(self.completed_operations)
        }
        
        try:
            with open(self.progress_file, 'w') as f:
                json.dump(progress_data, f, indent=2)
        except Exception as e:
            print(f"Warning: Could not save progress: {e}")
            
    def _create_config_directories(self, config_info):
        """Create organized directory structure for a configuration."""
        config_dir = os.path.join(self.batch_output_dir, config_info['config_id'])
        
        subdirs = [
            'comprehensive_no_baselines',
            'comprehensive_with_baselines', 
            'pareto_analysis'
        ]
        
        for subdir in subdirs:
            os.makedirs(os.path.join(config_dir, subdir), exist_ok=True)
            
        return config_dir
        
    def _run_comprehensive_analysis(self, config_info, output_subdir, include_baselines=False):
        """Run comprehensive analysis for a configuration."""
        config_dir = self._create_config_directories(config_info)
        output_dir = os.path.join(config_dir, output_subdir)
        
        operation_id = f"{config_info['config_id']}_comprehensive_{'with' if include_baselines else 'no'}_baselines"
        
        if operation_id in self.completed_operations:
            if self.verbose:
                print(f"  Skipping {operation_id} (already completed)")
            return True
            
        cmd = [
            'python', self.comprehensive_script, self.sweep_name,
            '--input-file', config_info['model_file'],
            '--output-format', 'png',
            '--output-dir', output_dir,  # New parameter we need to add
            '--verbose'
        ]
        
        if include_baselines:
            cmd.append('--include-baselines')
            
        if self.dry_run:
            print(f"  Would run: {' '.join(cmd)}")
            return True
            
        try:
            if self.verbose:
                baseline_str = "with baselines" if include_baselines else "no baselines"
                print(f"    Running comprehensive analysis ({baseline_str})...")
                
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=PROJECT_ROOT)
            
            if result.returncode == 0:
                self.completed_operations.add(operation_id)
                self._save_progress()
                return True
            else:
                print(f"    Error in comprehensive analysis: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"    Exception running comprehensive analysis: {e}")
            return False
            
    def _run_pareto_analysis(self, config_info):
        """Run pareto key models analysis for a configuration."""
        config_dir = self._create_config_directories(config_info)
        output_dir = os.path.join(config_dir, 'pareto_analysis')
        
        operation_id = f"{config_info['config_id']}_pareto_analysis"
        
        if operation_id in self.completed_operations:
            if self.verbose:
                print(f"  Skipping {operation_id} (already completed)")
            return True
            
        cmd = [
            'python', self.pareto_script, self.sweep_name,
            '--pareto-family', 'gamma_c',
            '--identify-key-models',
            '--annotate-models',  # Always include annotation
            '--export-key-models',
            '--baseline-mode', 'minimal',
            '--output-format', 'png',
            '--output-dir', output_dir,  # New parameter we need to add
            '--input-file', config_info['model_file'],
            '--verbose'
        ]
        
        if self.dry_run:
            print(f"  Would run: {' '.join(cmd)}")
            return True
            
        try:
            if self.verbose:
                print(f"    Running pareto analysis (with annotation)...")
                
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=PROJECT_ROOT)
            
            if result.returncode == 0:
                self.completed_operations.add(operation_id)
                self._save_progress()
                return True
            else:
                print(f"    Error in pareto analysis: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"    Exception running pareto analysis: {e}")
            return False
            
    def run_batch_analysis(self):
        """Run complete batch analysis on all configurations."""
        print(f"🚀 Starting Batch Analysis for {self.sweep_name}")
        print(f"{'='*60}")
        
        # Load previous progress if resuming
        self._load_progress()
        
        # Discover configurations
        configurations = self.discover_configurations()
        
        if not configurations:
            print("❌ No model configuration files found!")
            return False
            
        print(f"📊 Found {len(configurations)} configurations to process")
        
        # Calculate total operations
        total_operations = len(configurations) * 3  # 3 analysis types per config
        completed_count = len(self.completed_operations)
        
        if self.dry_run:
            print(f"🔍 DRY RUN - Showing what would be processed:")
            
        print(f"📈 Progress: {completed_count}/{total_operations} operations completed ({completed_count/total_operations*100:.1f}%)")
        print()
        
        # Process each configuration
        failed_configs = []
        
        for i, config_info in enumerate(configurations, 1):
            config_id = config_info['config_id']
            print(f"🔄 Processing configuration {i}/{len(configurations)}: {config_id}")
            
            # Run 3 analysis types
            analyses = [
                ("comprehensive_no_baselines", False),
                ("comprehensive_with_baselines", True),
                ("pareto_analysis", None)
            ]
            
            config_success = True
            
            for analysis_name, include_baselines in analyses:
                if analysis_name == "pareto_analysis":
                    success = self._run_pareto_analysis(config_info)
                else:
                    success = self._run_comprehensive_analysis(config_info, analysis_name, include_baselines)
                
                if not success:
                    config_success = False
                    print(f"    ❌ Failed: {analysis_name}")
                else:
                    print(f"    ✅ Completed: {analysis_name}")
                    
            if config_success:
                print(f"✅ Configuration {config_id} completed successfully")
            else:
                print(f"❌ Configuration {config_id} had failures")
                failed_configs.append(config_id)
                
            print()
            
        # Final summary
        print(f"{'='*60}")
        print(f"🎉 Batch Analysis Complete!")
        print(f"✅ Successful configurations: {len(configurations) - len(failed_configs)}/{len(configurations)}")
        
        if failed_configs:
            print(f"❌ Failed configurations: {len(failed_configs)}")
            for config_id in failed_configs:
                print(f"   - {config_id}")
                
        print(f"📁 Results saved to: {self.batch_output_dir}")
        print(f"📊 Aggregate CSVs in: {self.aggregate_dir}")
        
        # Show expected output summary
        total_plots = (len(configurations) - len(failed_configs)) * 11  # 5+5+1 plots per config
        print(f"📈 Expected output: ~{total_plots} plots + 3 aggregate CSV files")
        
        return len(failed_configs) == 0


def main():
    """Main function with command line interface."""
    parser = argparse.ArgumentParser(description='Automated batch analysis for AMR parameter sweep')
    
    # Required arguments
    parser.add_argument('sweep_name', help='Name of the sweep (e.g., session3_100k_uniform)')
    
    # Optional arguments
    parser.add_argument('--resume', action='store_true', help='Resume from previous incomplete run')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done without executing')
    parser.add_argument('--quiet', action='store_true', help='Reduce console output')
    
    args = parser.parse_args()
    
    try:
        runner = BatchAnalysisRunner(
            sweep_name=args.sweep_name,
            resume=args.resume,
            dry_run=args.dry_run,
            verbose=not args.quiet
        )
        
        success = runner.run_batch_analysis()
        sys.exit(0 if success else 1)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()