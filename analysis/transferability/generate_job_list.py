#!/usr/bin/env python3
"""
Generate job list file for SLURM array submission.

Creates a text file with one command per line. SLURM array task N runs line N.

Usage:
    python generate_job_list.py                     # Creates job_list.txt
    python generate_job_list.py --output my_jobs.txt
"""

import argparse
from pathlib import Path

# Import configuration
from transferability_config import MODELS, TEST_ICASES, SIMULATION_PARAMS

def generate_job_list(output_path, plot_mode='snapshot'):
    """Generate job list file."""
    
    # Ensure results directory exists
    results_dir = Path('analysis/transferability/results')
    results_dir.mkdir(parents=True, exist_ok=True)
    
    jobs = []
    for model in MODELS:
        for icase in TEST_ICASES:
            # JSON output file for this job
            json_output = f"analysis/transferability/results/{model['name']}_icase{icase}.json"
            
            cmd = (
                f"python analysis/transferability/transferability_runner.py "
                f"--model-path {model['path']} "
                f"--icase {icase} "
                f"--initial-refinement {model['eval_config']['initial_refinement']} "
                f"--element-budget {model['eval_config']['element_budget']} "
                f"--max-level {model['eval_config']['max_level']} "
                f"--time-final {SIMULATION_PARAMS['time_final']} "
                f"--nop {SIMULATION_PARAMS['nop']} "
                f"--courant-max {SIMULATION_PARAMS['courant_max']} "
                f"--plot-mode {plot_mode} "
                f"--output-file {json_output}"
            )
            jobs.append(cmd)
    
    # Write to file
    with open(output_path, 'w') as f:
        for job in jobs:
            f.write(job + '\n')
    
    print(f"Generated {len(jobs)} jobs in {output_path}")
    print(f"\nTo submit as SLURM array:")
    print(f"  sbatch --array=1-{len(jobs)} transferability_array.slurm")
    
    return jobs


def main():
    parser = argparse.ArgumentParser(description='Generate job list for SLURM array')
    parser.add_argument('--output', type=str, default='job_list.txt',
                        help='Output file path')
    parser.add_argument('--plot-mode', choices=['snapshot', 'animate', 'final'],
                        default='snapshot', help='Plotting mode')
    args = parser.parse_args()
    
    generate_job_list(args.output, args.plot_mode)


if __name__ == '__main__':
    main()