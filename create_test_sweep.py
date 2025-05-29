#!/usr/bin/env python3
"""
Test Parameter Sweep - Mini Version
Creates a small test with 2 parameter combinations for validation.

Usage: python3 create_test_sweep.py
"""

import yaml
import os
import itertools
from datetime import datetime

def create_test_combinations():
    """Create 2 test parameter combinations."""
    # Just test 2 combinations instead of 81
    combinations = [
        (25.0, 0.05, 10, 25),   # gamma_c, step_domain, rl_iterations, element_budget
        (50.0, 0.1, 25, 30)     # A different combination
    ]
    
    print(f"✓ Generated {len(combinations)} test combinations")
    return combinations

def create_test_manifest(combinations, timestamp):
    """Generate test manifest."""
    manifest = {
        'sweep_info': {
            'timestamp': timestamp,
            'total_combinations': len(combinations),
            'total_groups': 1,  # All in one group for testing
            'total_timesteps': 2000,  # Much shorter for testing
            'test_mode': True,
            'parameters': {
                'gamma_c': [25.0, 50.0],
                'step_domain_fraction': [0.05, 0.1],
                'rl_iterations_per_timestep': [10, 25],
                'element_budget': [25, 30]
            }
        },
        'directory_structure': {
            'base_path': f"results/test_param_sweep_{timestamp}",
            'naming_convention': "gamma_{gamma_c}_step_{step_domain}_rl_{rl_iterations}_budget_{budget}",
            'collection_naming': "gamma_{gamma_c}_step_{step_domain}_rl_{rl_iterations}_budget_{budget}_2k"
        },
        'groups': [{
            'group_id': 1,
            'group_name': 'test_group',
            'slurm_script': 'test_group.slurm',
            'job_id': None,
            'status': 'not_submitted',
            'combinations_count': len(combinations)
        }],
        'combinations': []
    }
    
    # Add combination details
    for i, combo in enumerate(combinations):
        gamma_c, step_domain, rl_iterations, element_budget = combo
        
        combo_info = {
            'combo_id': i + 1,
            'group_id': 1,
            'array_index': i,
            'parameters': {
                'gamma_c': gamma_c,
                'step_domain_fraction': step_domain,
                'rl_iterations_per_timestep': rl_iterations,
                'element_budget': element_budget
            },
            'paths': {
                'directory': f"gamma_{gamma_c}_step_{step_domain}_rl_{rl_iterations}_budget_{element_budget}",
                'expected_files': [
                    'final_model.zip',
                    'training_report.pdf',
                    'monitor.csv',
                    'config.yaml'
                ]
            },
            'collection': {
                'final_model_name': f"gamma_{gamma_c}_step_{step_domain}_rl_{rl_iterations}_budget_{element_budget}_2k_final_model.zip",
                'report_name': f"gamma_{gamma_c}_step_{step_domain}_rl_{rl_iterations}_budget_{element_budget}_2k_training_report.pdf"
            },
            'status': {
                'submitted': False,
                'running': False,
                'completed': False,
                'collected': False,
                'job_id': None,
                'completion_time': None
            }
        }
        manifest['combinations'].append(combo_info)
    
    return manifest

def create_test_base_config():
    """Create test base config with fewer timesteps."""
    base_config = {
        'environment': {
            'max_episode_steps': 200,
            'element_budget': '{{ELEMENT_BUDGET}}',
            'gamma_c': '{{GAMMA_C}}',
            'rl_iterations_per_timestep': '{{RL_ITERATIONS}}',
            'min_rl_iterations': '{{MIN_RL_ITERATIONS}}',
            'max_rl_iterations': '{{MAX_RL_ITERATIONS}}',
            'max_consecutive_no_action': 30,
            'step_domain_fraction': '{{STEP_DOMAIN_FRACTION}}',
            'initial_refinement': {
                'mode': 'random',
                'fixed_level': 2,
                'max_initial_level': 4,
                'probability': 0.7
            }
        },
        'training': {
            'total_timesteps': 2000,  # Much shorter for testing!
            'algorithm': 'A2C',
            'learning_rate': 0.0003,
            'n_steps': 5,
            'ent_coef': 0.01,
            'callback': 'enhanced'
        },
        'solver': {
            'nop': 4,
            'max_level': 8,
            'courant_max': 0.1,
            'icase': 1,
            'initial_elements': [-1, -0.4, 0, 0.4, 1],
            'verbose': False,
            'balance': False
        }
    }
    
    return base_config

def create_test_slurm_script(combinations, timestamp):
    """Create test SLURM script."""
    
    # Generate parameter cases
    parameter_cases = []
    for i, combo in enumerate(combinations):
        gamma_c, step_domain, rl_iterations, element_budget = combo
        case_block = f'''    {i})
        GAMMA_C={gamma_c}
        STEP_DOMAIN_FRACTION={step_domain}
        RL_ITERATIONS={rl_iterations}
        ELEMENT_BUDGET={element_budget}
        ;;'''
        parameter_cases.append(case_block)
    
    cases_str = '\n'.join(parameter_cases)
    
    script_content = f'''#!/bin/bash
#SBATCH --job-name=test_param_sweep
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G
#SBATCH --time=30:00
#SBATCH --array=0-{len(combinations)-1}
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
{cases_str}
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
SWEEP_TIMESTAMP="{timestamp}"
BASE_RESULTS_DIR="results/test_param_sweep_$SWEEP_TIMESTAMP"
CURRENT_RESULTS_DIR="$BASE_RESULTS_DIR/gamma_${{GAMMA_C}}_step_${{STEP_DOMAIN_FRACTION}}_rl_${{RL_ITERATIONS}}_budget_${{ELEMENT_BUDGET}}"

echo "Creating test results directory: $CURRENT_RESULTS_DIR"
mkdir -p "$CURRENT_RESULTS_DIR"

# Copy and modify config
BASE_CONFIG_TEMPLATE="experiments/configs/test_base_template.yaml"
CURRENT_CONFIG="$CURRENT_RESULTS_DIR/config.yaml"

cp "$BASE_CONFIG_TEMPLATE" "$CURRENT_CONFIG"
sed -i "s/{{{{GAMMA_C}}}}/$GAMMA_C/g" "$CURRENT_CONFIG"
sed -i "s/{{{{STEP_DOMAIN_FRACTION}}}}/$STEP_DOMAIN_FRACTION/g" "$CURRENT_CONFIG"
sed -i "s/{{{{RL_ITERATIONS}}}}/$RL_ITERATIONS/g" "$CURRENT_CONFIG"
sed -i "s/{{{{MIN_RL_ITERATIONS}}}}/$RL_ITERATIONS/g" "$CURRENT_CONFIG"
sed -i "s/{{{{MAX_RL_ITERATIONS}}}}/$RL_ITERATIONS/g" "$CURRENT_CONFIG"
sed -i "s/{{{{ELEMENT_BUDGET}}}}/$ELEMENT_BUDGET/g" "$CURRENT_CONFIG"

echo "✓ Test configuration prepared"

# Change to project directory and run training
cd /bsuhome/ahegedus/1D-Wave-AMR

echo "Starting TEST training (2000 timesteps)..."
python3 run_experiments_mixed_gpu.py \\
    --config "$CURRENT_CONFIG" \\
    --results-dir "$CURRENT_RESULTS_DIR" \\
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
'''
    
    return script_content

def main():
    """Main test setup function."""
    print("Creating TEST Parameter Sweep (2 combinations, 2k timesteps)")
    print("=" * 70)
    
    # Create directories
    os.makedirs('experiments/configs', exist_ok=True)
    os.makedirs('experiments/manifests', exist_ok=True)
    os.makedirs('slurm_scripts', exist_ok=True)
    os.makedirs('logs', exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    
    # Create test combinations
    combinations = create_test_combinations()
    
    # Create test manifest
    manifest = create_test_manifest(combinations, timestamp)
    
    # Save test manifest
    test_manifest_path = f"experiments/manifests/test_manifest_{timestamp}.yaml"
    with open(test_manifest_path, 'w') as f:
        yaml.dump(manifest, f, default_flow_style=False, indent=2)
    
    with open("experiments/manifests/latest_test_manifest.yaml", 'w') as f:
        yaml.dump(manifest, f, default_flow_style=False, indent=2)
    
    print(f"✓ Test manifest: {test_manifest_path}")
    
    # Create test base config
    test_config = create_test_base_config()
    test_config_path = "experiments/configs/test_base_template.yaml"
    with open(test_config_path, 'w') as f:
        yaml.dump(test_config, f, default_flow_style=False, indent=2)
    
    print(f"✓ Test config template: {test_config_path}")
    
    # Create test SLURM script
    test_script_content = create_test_slurm_script(combinations, timestamp)
    test_script_path = "slurm_scripts/test_param_sweep.slurm"
    with open(test_script_path, 'w') as f:
        f.write(test_script_content)
    
    os.chmod(test_script_path, 0o755)
    print(f"✓ Test SLURM script: {test_script_path}")
    
    # Create test submission script
    submit_script = f'''#!/bin/bash
echo "Submitting TEST parameter sweep..."
echo "2 combinations, 2000 timesteps each (~10 minutes total)"
echo ""

JOB_ID=$(sbatch {test_script_path} | cut -d' ' -f4)
echo "Test job submitted with ID: $JOB_ID"
echo ""
echo "Monitor with:"
echo "  squeue -u $USER"
echo "  watch -n 10 'squeue -u $USER'"
echo ""
echo "Check results in: results/test_param_sweep_{timestamp}/"
'''
    
    submit_test_path = "submit_test_sweep.sh"
    with open(submit_test_path, 'w') as f:
        f.write(submit_script)
    
    os.chmod(submit_test_path, 0o755)
    print(f"✓ Test submission script: {submit_test_path}")
    
    print(f"\n" + "="*70)
    print("TEST SWEEP READY!")
    print("="*70)
    print(f"• 2 parameter combinations")
    print(f"• 2,000 timesteps each (~10 minutes)")
    print(f"• Enhanced callback with do-nothing tracking")
    print(f"• Tests full pipeline end-to-end")
    print(f"")
    print(f"To run test:")
    print(f"  bash {submit_test_path}")
    print(f"")
    print(f"If test passes, run full sweep with:")
    print(f"  python3 create_manifest_system.py")
    print(f"  python3 create_base_config.py")
    print(f"  python3 create_slurm_scripts.py")
    print(f"  bash submit_param_sweep.sh")

if __name__ == "__main__":
    main()
    