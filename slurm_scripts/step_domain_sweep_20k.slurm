#!/bin/bash
#SBATCH --job-name=step_domain_sweep_20k
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G
#SBATCH --time=03:00:00
#SBATCH --array=0-2
#SBATCH --output=logs/parameter_sweeps/step_domain_fraction/job_array_20k_%A_%a.out
#SBATCH --error=logs/parameter_sweeps/step_domain_fraction/job_array_20k_%A_%a.err

# Create timestamp for this run
TIMESTAMP=$(date +%Y-%m-%d_%H%M%S)

# Map array task IDs to step_domain_fraction values (removed 0.20)
declare -a STEP_FRACTIONS=(0.05 0.10 0.15)
STEP_FRACTION=${STEP_FRACTIONS[$SLURM_ARRAY_TASK_ID]}

# Set up directory structure
RESULTS_BASE="results/parameter_sweeps/step_domain_fraction"
RUN_DIR="${RESULTS_BASE}/run_${TIMESTAMP}"
JOB_RESULTS_DIR="${RUN_DIR}/step_domain_${STEP_FRACTION}"
LOGS_BASE="logs/parameter_sweeps/step_domain_fraction"
LOGS_RUN_DIR="${LOGS_BASE}/run_${TIMESTAMP}"

# Create directories (including logs directory for SLURM output)
mkdir -p "$JOB_RESULTS_DIR"
mkdir -p "$LOGS_RUN_DIR"
mkdir -p "logs/parameter_sweeps/step_domain_fraction"

# Load environment
source ~/.bashrc
conda activate rl-amr

# Create temporary config file for this job
TEMP_CONFIG="temp_config_20k_${SLURM_ARRAY_TASK_ID}.yaml"
cp experiments/configs/production/gamma_c_100.0_random_step_domain_sweep.yaml "$TEMP_CONFIG"

# Modify step_domain_fraction and total_timesteps in the temporary config
sed -i "s/step_domain_fraction: 0.10/step_domain_fraction: ${STEP_FRACTION}/" "$TEMP_CONFIG"
sed -i "s/total_timesteps: 100000/total_timesteps: 20000/" "$TEMP_CONFIG"

# Print job information
echo "============================================"
echo "SLURM Array Job Information"
echo "============================================"
echo "Job ID: $SLURM_JOB_ID"
echo "Array Task ID: $SLURM_ARRAY_TASK_ID"
echo "Step Domain Fraction: $STEP_FRACTION"
echo "Total Timesteps: 20,000"
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

echo "============================================"
echo "Job completed for step_domain_fraction: $STEP_FRACTION"
echo "Results saved to: $JOB_RESULTS_DIR"
echo "============================================"
