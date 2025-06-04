#!/bin/bash
#SBATCH --job-name=step_domain_sweep_50k
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G
#SBATCH --time=03:00:00
#SBATCH --array=0-2
#SBATCH --output=logs/step_domain_sweep_%A_%a.out
#SBATCH --error=logs/step_domain_sweep_%A_%a.err

# Create SHARED timestamp for the entire sweep (all array jobs use same timestamp)
TIMESTAMP_FILE="/tmp/sweep_timestamp_${SLURM_ARRAY_JOB_ID}"
if [ ! -f "$TIMESTAMP_FILE" ]; then
    date +%Y-%m-%d_%H%M%S > "$TIMESTAMP_FILE"
fi
TIMESTAMP=$(cat "$TIMESTAMP_FILE")

# Parameter mapping
declare -a STEP_FRACTIONS=(0.05 0.10 0.15)
STEP_FRACTION=${STEP_FRACTIONS[$SLURM_ARRAY_TASK_ID]}

# NEW: Streamlined directory structure (much flatter!)
SWEEP_DIR="results/step_domain_sweep_${TIMESTAMP}"
JOB_RESULTS_DIR="${SWEEP_DIR}/step_domain_${STEP_FRACTION}"

# Create directories
mkdir -p "$JOB_RESULTS_DIR"
mkdir -p "logs"

# Load environment
source ~/.bashrc
conda activate rl-amr

# Create temporary config file (keeping current approach)
TEMP_CONFIG="temp_config_50k_${SLURM_ARRAY_TASK_ID}.yaml"
cp experiments/configs/production/gamma_c_100.0_random_step_domain_sweep.yaml "$TEMP_CONFIG"

# Modify parameters in temp config
sed -i "s/step_domain_fraction: 0.10/step_domain_fraction: ${STEP_FRACTION}/" "$TEMP_CONFIG"
sed -i "s/total_timesteps: 100000/total_timesteps: 50000/" "$TEMP_CONFIG"

# Print job information
echo "============================================"
echo "SLURM Array Job Information"
echo "============================================"
echo "Job ID: $SLURM_JOB_ID"
echo "Array Task ID: $SLURM_ARRAY_TASK_ID"
echo "Step Domain Fraction: $STEP_FRACTION"
echo "Total Timesteps: 50,000"
echo "Sweep Directory: $SWEEP_DIR"
echo "Results Directory: $JOB_RESULTS_DIR"
echo "Temporary Config: $TEMP_CONFIG"
echo "Timestamp: $TIMESTAMP"
echo "============================================"

# Verify GPU availability
nvidia-smi
echo "============================================"

# Run the training with GPU acceleration
python experiments/run_experiments_mixed_gpu.py \
    --config "$TEMP_CONFIG" \
    --results-dir "$JOB_RESULTS_DIR"

# Clean up temporary config
rm "$TEMP_CONFIG"

# NEW: Create metadata file for tracking
cat > "$JOB_RESULTS_DIR/run_info.yaml" << EOL
sweep_type: step_domain_fraction
parameter_value: $STEP_FRACTION
timestamp: $TIMESTAMP
slurm_job_id: $SLURM_JOB_ID
slurm_array_task_id: $SLURM_ARRAY_TASK_ID
total_timesteps: 50000
config_file: gamma_c_100.0_random_step_domain_sweep.yaml
min_rl_iterations: 10
max_rl_iterations: 25
EOL

echo "============================================"
echo "Job completed for step_domain_fraction: $STEP_FRACTION"
echo "Results saved to: $JOB_RESULTS_DIR"
echo "============================================"
