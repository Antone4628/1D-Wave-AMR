#!/bin/bash
#SBATCH --job-name=test_param_sweep
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G
#SBATCH --time=30:00
#SBATCH --array=0-1
#SBATCH --output=logs/test_param_sweep_%A_%a.out
#SBATCH --error=logs/test_param_sweep_%A_%a.err

# TEST Parameter Sweep - 2 combinations, 2k timesteps each
echo "=================================================="
echo "TEST Parameter Sweep - Job $SLURM_ARRAY_JOB_ID Task $SLURM_ARRAY_TASK_ID"
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
        GAMMA_C=50.0
        STEP_DOMAIN_FRACTION=0.1
        RL_ITERATIONS=25
        ELEMENT_BUDGET=30
        ;;
    *)
        echo "❌ Invalid array index: $SLURM_ARRAY_TASK_ID"
        exit 1
        ;;
esac

echo "TEST PARAMETERS:"
echo "  GAMMA_C: $GAMMA_C"
echo "  STEP_DOMAIN_FRACTION: $STEP_DOMAIN_FRACTION"
echo "  RL_ITERATIONS: $RL_ITERATIONS"
echo "  ELEMENT_BUDGET: $ELEMENT_BUDGET"
echo "  TIMESTEPS: 2000 (TEST MODE)"
echo ""

# Create results directory
SWEEP_TIMESTAMP="2025-08-11_144339"
BASE_RESULTS_DIR="results/test_param_sweep_$SWEEP_TIMESTAMP"
CURRENT_RESULTS_DIR="$BASE_RESULTS_DIR/gamma_${GAMMA_C}_step_${STEP_DOMAIN_FRACTION}_rl_${RL_ITERATIONS}_budget_${ELEMENT_BUDGET}"

echo "Creating test results directory: $CURRENT_RESULTS_DIR"
mkdir -p "$CURRENT_RESULTS_DIR"

# Copy and modify config
BASE_CONFIG_TEMPLATE="experiments/configs/test_base_template.yaml"
CURRENT_CONFIG="$CURRENT_RESULTS_DIR/config.yaml"

cp "$BASE_CONFIG_TEMPLATE" "$CURRENT_CONFIG"
sed -i "s/{{GAMMA_C}}/$GAMMA_C/g" "$CURRENT_CONFIG"
sed -i "s/{{STEP_DOMAIN_FRACTION}}/$STEP_DOMAIN_FRACTION/g" "$CURRENT_CONFIG"
sed -i "s/{{RL_ITERATIONS}}/$RL_ITERATIONS/g" "$CURRENT_CONFIG"
sed -i "s/{{MIN_RL_ITERATIONS}}/$RL_ITERATIONS/g" "$CURRENT_CONFIG"
sed -i "s/{{MAX_RL_ITERATIONS}}/$RL_ITERATIONS/g" "$CURRENT_CONFIG"
sed -i "s/{{ELEMENT_BUDGET}}/$ELEMENT_BUDGET/g" "$CURRENT_CONFIG"

echo "✓ Test configuration prepared"


echo "Starting TEST training (2000 timesteps)..."
python3 experiments/run_experiments_mixed_gpu.py \
    --config "$CURRENT_CONFIG" \
    --results-dir "$CURRENT_RESULTS_DIR" \
    --no-timestamp

# Check results
if [ $? -eq 0 ]; then
    echo "✓ TEST training completed successfully"
    echo "completion_time: $(date -Iseconds)" > "$CURRENT_RESULTS_DIR/test_completed.yaml"
    
    # Verify files
    if [ -f "$CURRENT_RESULTS_DIR/final_model.zip" ] && [ -f "$CURRENT_RESULTS_DIR/training_report.pdf" ]; then
        echo "✓ All expected files present"
        echo "✅ TEST PASSED"
    else
        echo "⚠️  Missing files"
        ls -la "$CURRENT_RESULTS_DIR/"
    fi
else
    echo "❌ TEST training failed"
    echo "❌ TEST FAILED"
fi

echo "=================================================="
echo "Test completed at: $(date)"
echo "=================================================="
