#!/bin/bash
#SBATCH --job-name=amr_100k_restart    # Job name
#SBATCH --output=logs/amr_restart_%j.out
#SBATCH --error=logs/amr_restart_%j.err
#SBATCH --time=08:00:00                # 8 hours (was 4, now doubled)
#SBATCH --partition=bsudfq
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G

echo "Restarting 100K AMR Training (8-hour limit)"
echo "Job ID: $SLURM_JOB_ID"
echo "Previous job 1879743 reached 76.5K steps in 4 hours"
echo "Expected completion: ~5.2 hours"
echo "Started at: $(date)"

cd /bsuhome/antonechacartegu/projects/drl-amr/1D-Wave-AMR
source /bsuhome/antonechacartegu/anaconda3/etc/profile.d/conda.sh
conda activate rl-amr

echo "Using config: experiments/configs/production/gamma_c_100.0_full_run.yaml"
python experiments/run_experiments_mixed.py --config experiments/configs/production/gamma_c_100.0_full_run.yaml

echo "Job completed at: $(date)"
echo "Duration: $((SECONDS/3600)) hours"
