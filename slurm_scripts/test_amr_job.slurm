#!/bin/bash
#SBATCH --job-name=amr_test          # Job name
#SBATCH --output=logs/amr_test_%j.out # Standard output log (%j = job ID)
#SBATCH --error=logs/amr_test_%j.err  # Standard error log
#SBATCH --time=01:00:00              # Time limit (1 hour for test)
#SBATCH --partition=bsudfq           # Borah's default partition
#SBATCH --nodes=1                    # Number of nodes
#SBATCH --ntasks=1                   # Number of tasks
#SBATCH --cpus-per-task=4            # Number of CPU cores per task
#SBATCH --mem=8G                     # Memory per node

# Print job information
echo "Starting AMR RL Training Job"
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

# Test the ACTUAL imports used in training
echo "Testing training pipeline imports..."
python -c "
import stable_baselines3
import gymnasium
from numerical.solvers.dg_wave_solver_mixed_clean import DGWaveSolverMixed
from numerical.environments.dg_amr_env_mixed import DGAMREnv
from numerical.callbacks.enhanced_callback_mixed import EnhancedMonitorCallback
print('✅ All training imports successful')
print('stable-baselines3:', stable_baselines3.__version__)
print('gymnasium:', gymnasium.__version__)
print('✅ DGWaveSolverMixed loaded')
print('✅ DGAMREnv loaded') 
print('✅ EnhancedMonitorCallback loaded')
"

# Run the training with the organized test config
echo "Starting training..."
python experiments/run_experiments_mixed.py --config experiments/configs/tests/test_quick.yaml

# Print completion info
echo "Job completed at: $(date)"
echo "Job duration: $((SECONDS/60)) minutes"
