#!/bin/bash
#SBATCH --job-name=batch_anim_final
#SBATCH --array=1-48
#SBATCH --time=01:00:00
#SBATCH --mem=4G
#SBATCH --cpus-per-task=1
#SBATCH --output=/bsuhome/antonechacartegu/projects/drl-amr/1D-Wave-AMR/analysis/data/model_performance/session3_100k_uniform/batch_analysis/animation_jobs/slurm_logs/batch_anim_final_%A_%a.out
#SBATCH --error=/bsuhome/antonechacartegu/projects/drl-amr/1D-Wave-AMR/analysis/data/model_performance/session3_100k_uniform/batch_analysis/animation_jobs/slurm_logs/batch_anim_final_%A_%a.err

# Load environment
source ~/anaconda3/etc/profile.d/conda.sh
conda activate rl-amr

# Navigate to project root
cd /bsuhome/antonechacartegu/projects/drl-amr/1D-Wave-AMR

# Create logs directory if it doesn't exist
mkdir -p /bsuhome/antonechacartegu/projects/drl-amr/1D-Wave-AMR/analysis/data/model_performance/session3_100k_uniform/batch_analysis/animation_jobs/slurm_logs

# Run single animation based on array task ID
python analysis/model_performance/run_single_animation.py $SLURM_ARRAY_TASK_ID final session3_100k_uniform

echo "Animation job $SLURM_ARRAY_TASK_ID (final mode) completed at $(date)"
