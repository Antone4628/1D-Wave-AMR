#!/bin/bash
#SBATCH --job-name=batch_ref_7_budget_50
#SBATCH --account=antonechacartegu
#SBATCH --partition=bsudfq
#SBATCH --time=03:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --array=1-81
#SBATCH --output=logs/batch_ref_7_budget_50_%A_%a.out
#SBATCH --error=logs/batch_ref_7_budget_50_%A_%a.err

# Load conda environment
source ~/anaconda3/etc/profile.d/conda.sh
conda activate rl-amr

# Navigate to project directory
cd /bsuhome/antonechacartegu/projects/drl-amr/1D-Wave-AMR

# Run single model evaluation
python analysis/model_performance/evaluate_single_model_by_index.py $SLURM_ARRAY_TASK_ID session3_100k_uniform 7 50

echo "Completed array task $SLURM_ARRAY_TASK_ID (ref_7, budget_50)"
