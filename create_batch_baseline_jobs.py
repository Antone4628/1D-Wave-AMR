#!/usr/bin/env python3
"""
Generate SLURM batch baseline evaluation jobs for different initial refinement levels and element budgets.
Each job runs conventional-amr with multiple thresholds: 0.3, 0.2, 0.1, 0.01, 0.001, 0.0001
"""

import os
import sys

def create_slurm_baseline_job(refinement_level, element_budget):
    """Create a SLURM job file for baseline evaluation with specific refinement level and element budget."""
    
    # Read template
    template_file = 'slurm_scripts/batch_baseline_evaluation_template.slurm'
    
    # Create template if it doesn't exist
    if not os.path.exists(template_file):
        create_baseline_template()
    
    with open(template_file, 'r') as f:
        template = f.read()
    
    # Replace placeholders
    job_content = template.replace('REFINEMENT_LEVEL', str(refinement_level))
    job_content = job_content.replace('ELEMENT_BUDGET', str(element_budget))
    
    # Write job file
    job_file = f'slurm_scripts/batch_baseline_evaluation_ref_{refinement_level}_budget_{element_budget}.slurm'
    with open(job_file, 'w') as f:
        f.write(job_content)
    
    print(f"Created {job_file}")
    return job_file

def create_baseline_template():
    """Create the baseline template file if it doesn't exist."""
    template_content = '''#!/bin/bash
#SBATCH --job-name=baseline_ref_REFINEMENT_LEVEL_budget_ELEMENT_BUDGET
#SBATCH --output=slurm-baseline-ref_REFINEMENT_LEVEL_budget_ELEMENT_BUDGET-%j.out
#SBATCH --error=slurm-baseline-ref_REFINEMENT_LEVEL_budget_ELEMENT_BUDGET-%j.err
#SBATCH --time=01:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4GB
#SBATCH --partition=normal

# Baseline evaluation job for configuration: ref_REFINEMENT_LEVEL_budget_ELEMENT_BUDGET
# This job runs conventional-AMR with 6 thresholds: 0.3, 0.2, 0.1, 0.01, 0.001, 0.0001

echo "=================================================="
echo "SLURM Job ID: $SLURM_JOB_ID"
echo "Job Name: $SLURM_JOB_NAME"
echo "Node: $SLURMD_NODENAME"
echo "Start Time: $(date)"
echo "=================================================="

# Configuration parameters
REFINEMENT_LEVEL=REFINEMENT_LEVEL
ELEMENT_BUDGET=ELEMENT_BUDGET
SWEEP_NAME="session3_100k_uniform"
THRESHOLD_LIST="0.3,0.2,0.1,0.01,0.001,0.0001"

echo "Configuration:"
echo "  Initial Refinement: $REFINEMENT_LEVEL"
echo "  Element Budget: $ELEMENT_BUDGET"
echo "  Thresholds: $THRESHOLD_LIST"
echo

# Change to project directory
cd $SLURM_SUBMIT_DIR

# Set up environment
module load python/3.9
source venv/bin/activate

echo "Starting baseline evaluation..."
echo "Time: $(date)"

# Run baseline evaluation with all thresholds
python analysis/model_performance/baseline_evaluator.py $SWEEP_NAME \\
    --mode conventional-amr \\
    --initial-refinement $REFINEMENT_LEVEL \\
    --element-budget $ELEMENT_BUDGET \\
    --threshold-list "$THRESHOLD_LIST" \\
    --verbose

BASELINE_EXIT_CODE=$?

echo
echo "Baseline evaluation completed with exit code: $BASELINE_EXIT_CODE"
echo "End Time: $(date)"

# Check if output file was created
EXPECTED_OUTPUT="analysis/data/model_performance/$SWEEP_NAME/baseline_results_conventional-amr_ref${REFINEMENT_LEVEL}_budget${ELEMENT_BUDGET}.csv"

if [ -f "$EXPECTED_OUTPUT" ]; then
    echo "✓ Baseline file created: $EXPECTED_OUTPUT"
    LINES=$(wc -l < "$EXPECTED_OUTPUT")
    echo "  File contains $LINES lines (expected: 7 = header + 6 thresholds)"
    
    if [ $LINES -eq 7 ]; then
        echo "✓ File appears complete"
    else
        echo "⚠ Unexpected line count"
    fi
else
    echo "✗ Expected output file not found: $EXPECTED_OUTPUT"
fi

echo "=================================================="
echo "Job completed at $(date)"
echo "Total job time: $SECONDS seconds"
echo "=================================================="

exit $BASELINE_EXIT_CODE'''
    
    # Ensure directory exists
    os.makedirs('slurm_scripts', exist_ok=True)
    
    template_file = 'slurm_scripts/batch_baseline_evaluation_template.slurm'
    with open(template_file, 'w') as f:
        f.write(template_content)
    
    print(f"Created template: {template_file}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python create_batch_baseline_jobs.py <config1> [config2] ...")
        print("Where each config is: refinement_level,element_budget")
        print("Example: python create_batch_baseline_jobs.py 3,50 4,80 5,150")
        print()
        print("To create all 25 configurations:")
        print("python create_batch_baseline_jobs.py 3,50 3,80 3,100 3,150 3,200 \\")
        print("  4,50 4,80 4,100 4,150 4,200 \\")
        print("  5,50 5,80 5,100 5,150 5,200 \\")
        print("  6,50 6,80 6,100 6,150 6,200 \\")
        print("  7,50 7,80 7,100 7,150 7,200")
        sys.exit(1)
    
    configs = []
    for arg in sys.argv[1:]:
        try:
            refinement_level, element_budget = map(int, arg.split(','))
            configs.append((refinement_level, element_budget))
        except ValueError:
            print(f"Error: Invalid config '{arg}'. Use format: refinement_level,element_budget")
            sys.exit(1)
    
    # Calculate expected initial elements for each config
    print("Baseline Configuration Analysis:")
    for refinement_level, element_budget in configs:
        base_elements = 4
        expected_initial = base_elements * (2 ** refinement_level)
        
        # Baseline jobs run faster than model evaluations
        estimated_time = "5-15 minutes"
        
        print(f"  ref_{refinement_level}, budget_{element_budget}: {expected_initial} initial elements, est. time: {estimated_time}")
    print()
    
    job_files = []
    for refinement_level, element_budget in configs:
        job_file = create_slurm_baseline_job(refinement_level, element_budget)
        job_files.append((job_file, refinement_level, element_budget))
    
    print(f"\\nCreated {len(job_files)} baseline job files.")
    print("\\nTo submit all jobs:")
    for job_file, ref, budget in job_files:
        print(f"sbatch {job_file}")
    
    print(f"\\nExpected output files (each with 6 threshold results):")
    for _, ref, budget in job_files:
        print(f"  baseline_results_conventional-amr_ref{ref}_budget{budget}.csv")
    
    print(f"\\nEach job will run conventional-AMR with thresholds: 0.3, 0.2, 0.1, 0.01, 0.001, 0.0001")
    print(f"Total expected runtime: {len(job_files)} jobs × 5-15 minutes = ~2-6 hours")

if __name__ == "__main__":
    main()