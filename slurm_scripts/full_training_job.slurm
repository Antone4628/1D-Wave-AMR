#!/bin/bash
#SBATCH --job-name=amr_100k_train      # Job name
#SBATCH --output=logs/amr_100k_%j.out  # Standard output log
#SBATCH --error=logs/amr_100k_%j.err   # Standard error log
#SBATCH --time=04:00:00                # 4 hours for 100K timesteps
#SBATCH --partition=bsudfq             # Borah's default partition
#SBATCH --nodes=1                      # Number of nodes
#SBATCH --ntasks=1                     # Number of tasks
#SBATCH --cpus-per-task=8              # More cores for full run
#SBATCH --mem=16G                      # More memory for full run

# Print job information
echo "Starting AMR 100K Timestep Training Job"
echo "Job ID: $SLURM_JOB_ID"
echo "Node: $SLURM_NODELIST"
echo "Working Directory: $(pwd)"
echo "Started at: $(date)"

# Navigate to project directory
cd /bsuhome/antonechacartegu/projects/drl-amr/1D-Wave-AMR

# Activate conda environment
source /bsuhome/antonechacartegu/anaconda3/etc/profile.d/conda.sh
conda activate rl-amr

# Verify environment is active
echo "Active conda environment: $CONDA_DEFAULT_ENV"
echo "Python path: $(which python)"

# Show configuration being used
echo "=== Training Configuration ==="
cat experiments/configs/production/gamma_c_100.0_full_run.yaml
echo "=========================="

# Run the full 100K timestep training
echo "Starting 100K timestep AMR training..."
echo "Expected duration: 2-4 hours"
python experiments/run_experiments_mixed.py --config experiments/configs/production/gamma_c_100.0_full_run.yaml

# Print completion info
echo "Job completed at: $(date)"
echo "Job duration: $((SECONDS/60)) minutes"
echo "Hours: $((SECONDS/3600)) hours"
