#!/usr/bin/env python3
"""
SLURM Scripts Generator for Parameter Sweep
Creates 9 SLURM array job scripts for parameter sweep groups.

Usage: python3 create_slurm_scripts.py
"""

import yaml
import os
from datetime import datetime

def load_manifest():
    """Load the latest manifest file."""
    manifest_path = "experiments/manifests/latest_manifest.yaml"
    
    if not os.path.exists(manifest_path):
        print(f"❌ Manifest not found: {manifest_path}")
        print(f"Please run: python3 create_manifest_system.py first")
        return None
    
    with open(manifest_path, 'r') as f:
        manifest = yaml.safe_load(f)
    
    print(f"✓ Loaded manifest with {len(manifest['combinations'])} combinations")
    return manifest

def create_slurm_script_template():
    """Create the base SLURM script template."""
    
    template = '''#!/bin/bash
#SBATCH --job-name=param_sweep_group_{group_id:02d}
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G
#SBATCH --time=3:00:00
#SBATCH --array=0-8
#SBATCH --output=logs/param_sweep/group_{group_id:02d}_%A_%a.out
#SBATCH --error=logs/param_sweep/group_{group_id:02d}_%A_%a.err

# Parameter Sweep Group {group_id}: {group_name}
# This script handles 9 parameter combinations using array indices 0-8

echo "=================================================="
echo "Parameter Sweep Group {group_id} - Job $SLURM_ARRAY_JOB_ID Task $SLURM_ARRAY_TASK_ID"
echo "Node: $SLURM_NODEID"
echo "Start time: $(date)"
echo "=================================================="

# Activate conda environment
source ~/.bashrc
conda activate rl-amr

# Set parameters based on array index
case $SLURM_ARRAY_TASK_ID in
{parameter_cases}
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
SWEEP_TIMESTAMP="{timestamp}"

# Create results directory structure
BASE_RESULTS_DIR="results/full_param_sweep_$SWEEP_TIMESTAMP"
CURRENT_RESULTS_DIR="$BASE_RESULTS_DIR/gamma_${{GAMMA_C}}_step_${{STEP_DOMAIN_FRACTION}}_rl_${{RL_ITERATIONS}}_budget_${{ELEMENT_BUDGET}}"

echo "Creating results directory: $CURRENT_RESULTS_DIR"
mkdir -p "$CURRENT_RESULTS_DIR"

# Copy and modify base configuration
BASE_CONFIG_TEMPLATE="experiments/configs/param_sweep/base_template.yaml"
CURRENT_CONFIG="$CURRENT_RESULTS_DIR/config.yaml"

echo "Creating configuration file: $CURRENT_CONFIG"
cp "$BASE_CONFIG_TEMPLATE" "$CURRENT_CONFIG"

# Substitute parameters in config file
sed -i "s/{{{{GAMMA_C}}}}/$GAMMA_C/g" "$CURRENT_CONFIG"
sed -i "s/{{{{STEP_DOMAIN_FRACTION}}}}/$STEP_DOMAIN_FRACTION/g" "$CURRENT_CONFIG"
sed -i "s/{{{{RL_ITERATIONS}}}}/$RL_ITERATIONS/g" "$CURRENT_CONFIG"
sed -i "s/{{{{MIN_RL_ITERATIONS}}}}/$RL_ITERATIONS/g" "$CURRENT_CONFIG"
sed -i "s/{{{{MAX_RL_ITERATIONS}}}}/$RL_ITERATIONS/g" "$CURRENT_CONFIG"
sed -i "s/{{{{ELEMENT_BUDGET}}}}/$ELEMENT_BUDGET/g" "$CURRENT_CONFIG"

echo "✓ Configuration file prepared"

# Change to project directory
cd /bsuhome/ahegedus/1D-Wave-AMR

# Run training with no-timestamp flag for predictable directory structure
echo "Starting training..."
python3 run_experiments_mixed_gpu.py \\
    --config "$CURRENT_CONFIG" \\
    --results-dir "$CURRENT_RESULTS_DIR" \\
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
'''
    
    return template

def generate_parameter_cases(group_combinations):
    """Generate the parameter case statements for the SLURM script."""
    cases = []
    
    for i, combo in enumerate(group_combinations):
        gamma_c, step_domain, rl_iterations, element_budget = combo
        
        case_block = f'''    {i})
        GAMMA_C={gamma_c}
        STEP_DOMAIN_FRACTION={step_domain}
        RL_ITERATIONS={rl_iterations}
        ELEMENT_BUDGET={element_budget}
        ;;'''
        cases.append(case_block)
    
    return '\n'.join(cases)

def create_group_slurm_script(group, timestamp):
    """Create SLURM script for a specific group."""
    
    # Generate parameter cases
    parameter_cases = generate_parameter_cases(group['combinations'])
    
    # Fill template
    template = create_slurm_script_template()
    script_content = template.format(
        group_id=group['group_id'],
        group_name=group['group_name'],
        parameter_cases=parameter_cases,
        timestamp=timestamp
    )
    
    return script_content

def save_slurm_scripts(manifest):
    """Save all SLURM scripts."""
    
    # Create directories
    slurm_dir = "slurm_scripts/param_sweep"
    logs_dir = "logs/param_sweep"
    os.makedirs(slurm_dir, exist_ok=True)
    os.makedirs(logs_dir, exist_ok=True)
    
    timestamp = manifest['sweep_info']['timestamp']
    script_paths = []
    
    print(f"Creating SLURM scripts for {len(manifest['groups'])} groups...")
    
    for group_info in manifest['groups']:
        # Find group combinations
        group_combinations = []
        for combo in manifest['combinations']:
            if combo['group_id'] == group_info['group_id']:
                params = combo['parameters']
                group_combinations.append((
                    params['gamma_c'],
                    params['step_domain_fraction'],
                    params['rl_iterations_per_timestep'],
                    params['element_budget']
                ))
        
        group_data = {
            'group_id': group_info['group_id'],
            'group_name': group_info['group_name'],
            'combinations': group_combinations
        }
        
        # Generate script content
        script_content = create_group_slurm_script(group_data, timestamp)
        
        # Save script
        script_filename = f"group_{group_info['group_id']:02d}.slurm"
        script_path = os.path.join(slurm_dir, script_filename)
        
        with open(script_path, 'w') as f:
            f.write(script_content)
        
        # Make executable
        os.chmod(script_path, 0o755)
        
        script_paths.append(script_path)
        print(f"✓ Created: {script_path}")
    
    return script_paths

def create_submission_script(manifest, script_paths):
    """Create master submission script."""
    
    submission_script = '''#!/bin/bash
# Master submission script for parameter sweep
# Submits all 9 group jobs and tracks job IDs

echo "Starting 81-Parameter Sweep Submission"
echo "========================================"

# Array to store job IDs
declare -a JOB_IDS

# Submit each group
'''
    
    for i, group in enumerate(manifest['groups']):
        script_name = f"group_{group['group_id']:02d}.slurm"
        submission_script += f'''
echo "Submitting Group {group['group_id']}: {group['group_name']}"
JOB_ID_{group['group_id']}=$(sbatch slurm_scripts/param_sweep/{script_name} | cut -d' ' -f4)
echo "  Job ID: $JOB_ID_{group['group_id']}"
JOB_IDS+=($JOB_ID_{group['group_id']})
sleep 2  # Brief pause between submissions
'''
    
    submission_script += f'''
echo ""
echo "All jobs submitted successfully!"
echo "Total jobs: {len(manifest['groups'])}"
echo "Total parameter combinations: {len(manifest['combinations'])}"
echo ""
echo "Job IDs:"
'''
    
    for group in manifest['groups']:
        submission_script += f'echo "  Group {group["group_id"]:2d}: $JOB_ID_{group["group_id"]}"' + '\n'
    
    submission_script += '''
echo ""
echo "Monitor jobs with:"
echo "  squeue -u $USER"
echo "  python3 monitor_param_sweep.py"
echo ""
echo "Next steps:"
echo "  1. Monitor job progress: python3 monitor_param_sweep.py"
echo "  2. Collect results when complete: python3 collect_results.py"
'''
    
    submission_path = "submit_param_sweep.sh"
    with open(submission_path, 'w') as f:
        f.write(submission_script)
    
    os.chmod(submission_path, 0o755)
    print(f"✓ Created master submission script: {submission_path}")
    return submission_path

def print_summary(manifest, script_paths, submission_path):
    """Print creation summary."""
    print("\n" + "="*60)
    print("SLURM SCRIPTS GENERATION SUMMARY")
    print("="*60)
    
    print(f"Created {len(script_paths)} SLURM scripts:")
    for path in script_paths:
        print(f"  ✓ {path}")
    
    print(f"\nMaster submission script: {submission_path}")
    
    print(f"\nTotal parameter combinations: {len(manifest['combinations'])}")
    print(f"Estimated runtime per job: ~3 hours")
    print(f"Total estimated compute time: ~{3 * len(manifest['groups'])} hours")
    
    print(f"\nTo submit all jobs:")
    print(f"  bash {submission_path}")
    
    print(f"\nTo monitor progress:")
    print(f"  squeue -u $USER")
    print(f"  python3 monitor_param_sweep.py  # (create this next)")

def main():
    """Main execution function."""
    print("Creating SLURM Array Job Scripts")
    print("=" * 50)
    
    # Load manifest
    manifest = load_manifest()
    if manifest is None:
        return
    
    # Create SLURM scripts
    script_paths = save_slurm_scripts(manifest)
    
    # Create submission script
    submission_path = create_submission_script(manifest, script_paths)
    
    # Print summary
    print_summary(manifest, script_paths, submission_path)
    
    print(f"\n✓ SLURM scripts created successfully!")
    print(f"✓ Ready to submit jobs with: bash {submission_path}")

if __name__ == "__main__":
    main()