#!/bin/bash
#SBATCH --job-name=batch_ref_5_budget_80
#SBATCH --account=antonechacartegu
#SBATCH --partition=bsudfq
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --array=1-81
#SBATCH --output=logs/batch_ref_5_budget_80_%A_%a.out
#SBATCH --error=logs/batch_ref_5_budget_80_%A_%a.err

# Load conda environment
source ~/anaconda3/etc/profile.d/conda.sh
conda activate rl-amr

# Navigate to project directory
cd /bsuhome/antonechacartegu/projects/drl-amr/1D-Wave-AMR

# Run single model evaluation
# python analysis/model_performance/evaluate_single_model_by_index.py $SLURM_ARRAY_TASK_ID session3_100k_uniform 5 80
python analysis/model_performance/evaluate_single_model_by_index.py $SLURM_ARRAY_TASK_ID session3_100k_uniform 5 80 5

echo "Completed array task $SLURM_ARRAY_TASK_ID (ref_5, budget_80)"
