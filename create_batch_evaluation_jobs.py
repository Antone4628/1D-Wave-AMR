#!/usr/bin/env python3
"""
Generate SLURM batch evaluation jobs for different initial refinement levels and element budgets.
"""

import os
import sys

def create_slurm_job(refinement_level, element_budget, max_level):
    """Create a SLURM job file for specific refinement level and element budget."""
    
    # Read template
    template_file = 'slurm_scripts/batch_model_evaluation_template.slurm'
    with open(template_file, 'r') as f:
        template = f.read()
    
    # Replace placeholders
    job_content = template.replace('REFINEMENT_LEVEL', str(refinement_level))
    job_content = job_content.replace('ELEMENT_BUDGET', str(element_budget))
    job_content = job_content.replace('MAX_LEVEL', str(max_level))
    
    # Write job file
    job_file = f'slurm_scripts/batch_model_evaluation_ref_{refinement_level}_budget_{element_budget}.slurm'
    with open(job_file, 'w') as f:
        f.write(job_content)
    
    print(f"Created {job_file}")
    return job_file

def main():
    if len(sys.argv) < 2:
        print("Usage: python create_batch_evaluation_jobs.py <config1> [config2] ...")
        print("Where each config is: refinement_level,element_budget,max_level")
        print("Example: python create_batch_evaluation_jobs.py 0,50 1,60 2,70 4,80")
        sys.exit(1)
    
    configs = []
    for arg in sys.argv[1:]:
        try:
            refinement_level, element_budget, max_level = map(int, arg.split(','))
            # configs.append((refinement_level, element_budget))
            configs.append((refinement_level, element_budget, max_level)) 
        except ValueError:
            print(f"Error: Invalid config '{arg}'. Use format: refinement_level,element_budget")
            sys.exit(1)
    
    # Calculate expected initial elements for each config
    print("Configuration analysis:")
    for refinement_level, element_budget, max_level in configs:
        base_elements = 4
        expected_initial = base_elements * (2 ** refinement_level)
        status = "✓ OK" if expected_initial < element_budget else "⚠ OVER BUDGET"
        print(f"  ref_{refinement_level}, budget_{element_budget}, maxlvl_{max_level}: {expected_initial} initial elements {status}")
    print()
    
    job_files = []
    for refinement_level, element_budget, max_level in configs: 
        job_file = create_slurm_job(refinement_level, element_budget, max_level)
        job_files.append((job_file, refinement_level, element_budget))
    
    print(f"\nCreated {len(job_files)} job files.")
    print("\nTo submit jobs:")
    for job_file, ref, budget in job_files:
        print(f"sbatch {job_file}")
    
    print(f"\nResults will be saved as:")
    for _, ref, budget in job_files:
        print(f"  model_results_ref{ref}_budget{budget}.csv")

if __name__ == "__main__":
    main()
