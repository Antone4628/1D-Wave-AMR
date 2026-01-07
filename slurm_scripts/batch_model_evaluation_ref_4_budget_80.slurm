#!/bin/bash
#SBATCH --job-name=batch_ref_4_budget_80_max_4
#SBATCH --account=antonechacartegu
#SBATCH --partition=bsudfq
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --array=1-81
#SBATCH --output=logs/batch_ref_4_budget_80_max_4_%A_%a.out
#SBATCH --error=logs/batch_ref_4_budget_80_max_4_%A_%a.err

# Load conda environment
source ~/anaconda3/etc/profile.d/conda.sh
conda activate rl-amr

# Navigate to project directory
cd /bsuhome/antonechacartegu/projects/drl-amr/1D-Wave-AMR

# Run single model evaluation
# python analysis/model_performance/evaluate_single_model_by_index.py $SLURM_ARRAY_TASK_ID session3_100k_uniform 4 80
# python analysis/model_performance/evaluate_single_model_by_index.py $SLURM_ARRAY_TASK_ID session5_mexican_hat_200k 4 80 4
python analysis/model_performance/evaluate_single_model_by_index.py $SLURM_ARRAY_TASK_ID session5_mexican_hat_200k 4 80 4 16
# python analysis/model_performance/evaluate_single_model_by_index.py $SLURM_ARRAY_TASK_ID session3_100k_uniform 4 80 4

# echo "Completed array task $SLURM_ARRAY_TASK_ID (ref_4, budget_80, max_4)"
# echo "Completed array task $SLURM_ARRAY_TASK_ID for sweep session5_mexican_hat_200k (ref_4, budget_80, max_4)"
echo "Completed array task $SLURM_ARRAY_TASK_ID for sweep session5_mexican_hat_200k (ref_4, budget_80, max_4, icase_16)"