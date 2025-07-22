#!/bin/bash
#SBATCH --job-name=baseline_ref_4_budget_80_max_4
#SBATCH --output=slurm-baseline-ref_4_budget_80_max_4-%j.out
#SBATCH --error=slurm-baseline-ref_4_budget_80_max_4-%j.err
#SBATCH --time=01:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4GB

echo "=================================================="
echo "SLURM Job ID: $SLURM_JOB_ID"
echo "Job Name: $SLURM_JOB_NAME"
echo "Node: $SLURMD_NODENAME"
echo "Start Time: $(date)"
echo "=================================================="

# Change to your project directory
cd /bsuhome/antonechacartegu/projects/drl-amr/1D-Wave-AMR

echo "Working directory: $(pwd)"
echo "Configuration: ref_4_budget_80_max_4"
echo "Thresholds: 0.3,0.2,0.1,0.01,0.001,0.0001"
echo

echo "Starting baseline evaluation..."
echo "Time: $(date)"

# Run baseline evaluation (you're already in rl-amr environment)
python analysis/model_performance/baseline_evaluator.py session3_100k_uniform \
    --mode conventional-amr \
    --initial-refinement 4 \
    --element-budget 80 \
    --max-level 4 \
    --threshold-list "0.3,0.2,0.1,0.01,0.001,0.0001" \
    --verbose

BASELINE_EXIT_CODE=$?

echo
echo "Baseline evaluation completed with exit code: $BASELINE_EXIT_CODE"
echo "End Time: $(date)"

# Check if output file was created
EXPECTED_OUTPUT="/bsuhome/antonechacartegu/projects/drl-amr/1D-Wave-AMR/analysis/data/model_performance/session3_100k_uniform/baseline_results_conventional-amr_ref4_budget80_max4.csv"

if [ -f "$EXPECTED_OUTPUT" ]; then
    echo "✓ Baseline file created: $EXPECTED_OUTPUT"
    LINES=$(wc -l < "$EXPECTED_OUTPUT")
    echo "  File contains $LINES lines (expected: 7 = header + 6 thresholds)"
else
    echo "✗ Expected output file not found: $EXPECTED_OUTPUT"
fi

echo "=================================================="
echo "Job completed at $(date)"
echo "=================================================="

exit $BASELINE_EXIT_CODE