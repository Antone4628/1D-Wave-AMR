#!/bin/bash
#SBATCH --job-name=param_sweep_group_02
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G
#SBATCH --time=3:00:00
#SBATCH --array=0-8
#SBATCH --output=logs/param_sweep/group_02_%A_%a.out
#SBATCH --error=logs/param_sweep/group_02_%A_%a.err

# Parameter Sweep Group 2: gamma_25.0_step_0.05
# This script handles 9 parameter combinations using array indices 0-8

echo "=================================================="
echo "Parameter Sweep Group 2 - Job $SLURM_ARRAY_JOB_ID Task $SLURM_ARRAY_TASK_ID"
echo "Node: $SLURM_NODEID"
echo "Start time: $(date)"
echo "=================================================="

# Activate conda environment
source ~/.bashrc
conda activate rl-amr

# Set parameters based on array index
case $SLURM_ARRAY_TASK_ID in
    0)
        GAMMA_C=25.0
        STEP_DOMAIN_FRACTION=0.05
        RL_ITERATIONS=10
        ELEMENT_BUDGET=25
        ;;
    1)
        GAMMA_C=25.0
        STEP_DOMAIN_FRACTION=0.05
        RL_ITERATIONS=10
        ELEMENT_BUDGET=30
        ;;
    2)
        GAMMA_C=25.0
        STEP_DOMAIN_FRACTION=0.05
        RL_ITERATIONS=10
        ELEMENT_BUDGET=40
        ;;
    3)
        GAMMA_C=25.0
        STEP_DOMAIN_FRACTION=0.05
        RL_ITERATIONS=25
        ELEMENT_BUDGET=25
        ;;
    4)
        GAMMA_C=25.0
        STEP_DOMAIN_FRACTION=0.05
        RL_ITERATIONS=25
        ELEMENT_BUDGET=30
        ;;
    5)
        GAMMA_C=25.0
        STEP_DOMAIN_FRACTION=0.05
        RL_ITERATIONS=25
        ELEMENT_BUDGET=40
        ;;
    6)
        GAMMA_C=25.0
        STEP_DOMAIN_FRACTION=0.05
        RL_ITERATIONS=40
        ELEMENT_BUDGET=25
        ;;
    7)
        GAMMA_C=25.0
        STEP_DOMAIN_FRACTION=0.05
        RL_ITERATIONS=40
        ELEMENT_BUDGET=30
        ;;
    8)
        GAMMA_C=25.0
        STEP_DOMAIN_FRACTION=0.05
        RL_ITERATIONS=40
        ELEMENT_BUDGET=40
        ;;
    *)
        echo "❌ Invalid array index: $SLURM_ARRAY_TASK_ID"
        exit 1
        ;;
esac

# Print current parameter configuration
echo "Current parameters:"
echo "  GAMMA_C: $GAMMA_C"
echo "  STEP_DOMAIN_FRACTION: $STEP_DOMAIN_FRACTION"
echo "  RL_ITERATIONS: $RL_ITERATIONS"
echo "  ELEMENT_BUDGET: $ELEMENT_BUDGET"
echo ""

# Create unique timestamp for this sweep
SWEEP_TIMESTAMP="2025-05-29_105232"

# Create results directory structure
BASE_RESULTS_DIR="results/full_param_sweep_$SWEEP_TIMESTAMP"
CURRENT_RESULTS_DIR="$BASE_RESULTS_DIR/gamma_${GAMMA_C}_step_${STEP_DOMAIN_FRACTION}_rl_${RL_ITERATIONS}_budget_${ELEMENT_BUDGET}"

echo "Creating results directory: $CURRENT_RESULTS_DIR"
mkdir -p "$CURRENT_RESULTS_DIR"

# Copy and modify base configuration
BASE_CONFIG_TEMPLATE="experiments/configs/param_sweep/base_template.yaml"
CURRENT_CONFIG="/tmp/config_${SLURM_JOB_ID}_${SLURM_ARRAY_TASK_ID}.yaml"

echo "Creating configuration file: $CURRENT_CONFIG"
cp "$BASE_CONFIG_TEMPLATE" "$CURRENT_CONFIG"

# Substitute parameters in config file
sed -i "s/{{GAMMA_C}}/$GAMMA_C/g" "$CURRENT_CONFIG"
sed -i "s/{{STEP_DOMAIN_FRACTION}}/$STEP_DOMAIN_FRACTION/g" "$CURRENT_CONFIG"
sed -i "s/{{RL_ITERATIONS}}/$RL_ITERATIONS/g" "$CURRENT_CONFIG"
sed -i "s/{{MIN_RL_ITERATIONS}}/$RL_ITERATIONS/g" "$CURRENT_CONFIG"
sed -i "s/{{MAX_RL_ITERATIONS}}/$RL_ITERATIONS/g" "$CURRENT_CONFIG"
sed -i "s/{{ELEMENT_BUDGET}}/$ELEMENT_BUDGET/g" "$CURRENT_CONFIG"

echo "✓ Configuration file prepared"

# Change to project directory
cd /bsuhome/antonechacartegu/projects/drl-amr/1D-Wave-AMR

# Run training with no-timestamp flag for predictable directory structure
echo "Starting training..."
python3 experiments/run_experiments_mixed_gpu.py \
    --config "$CURRENT_CONFIG" \
    --results-dir "$CURRENT_RESULTS_DIR" \
    --no-timestamp

# Check if training completed successfully
if [ $? -eq 0 ]; then
    echo "✓ Training completed successfully"
    
    # Create completion marker
    echo "job_id: $SLURM_ARRAY_JOB_ID" > "$CURRENT_RESULTS_DIR/job_completed.yaml"
    echo "task_id: $SLURM_ARRAY_TASK_ID" >> "$CURRENT_RESULTS_DIR/job_completed.yaml"
    echo "completion_time: $(date -Iseconds)" >> "$CURRENT_RESULTS_DIR/job_completed.yaml"
    echo "parameters:" >> "$CURRENT_RESULTS_DIR/job_completed.yaml"
    echo "  gamma_c: $GAMMA_C" >> "$CURRENT_RESULTS_DIR/job_completed.yaml"
    echo "  step_domain_fraction: $STEP_DOMAIN_FRACTION" >> "$CURRENT_RESULTS_DIR/job_completed.yaml"
    echo "  rl_iterations: $RL_ITERATIONS" >> "$CURRENT_RESULTS_DIR/job_completed.yaml"
    echo "  element_budget: $ELEMENT_BUDGET" >> "$CURRENT_RESULTS_DIR/job_completed.yaml"
    
    # Verify expected files exist
    if [ -f "$CURRENT_RESULTS_DIR/final_model.zip" ] && [ -f "$CURRENT_RESULTS_DIR/training_report.pdf" ]; then
        echo "✓ All expected output files present"
    else
        echo "⚠️  Missing expected output files"
        ls -la "$CURRENT_RESULTS_DIR/"
    fi
else
    echo "❌ Training failed with exit code $?"
    echo "failure_time: $(date -Iseconds)" > "$CURRENT_RESULTS_DIR/job_failed.yaml"
    echo "exit_code: $?" >> "$CURRENT_RESULTS_DIR/job_failed.yaml"
fi

echo "=================================================="
echo "Job completed at: $(date)"
echo "Results directory: $CURRENT_RESULTS_DIR"
echo "=================================================="
