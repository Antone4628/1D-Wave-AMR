#!/usr/bin/env python3
"""
Generate Updated SLURM Scripts for Data Export Parameter Sweep
Creates 9 SLURM array job scripts with conditional timesteps and enhanced_callback_data.

Key Changes:
- Groups 1-3 (gamma_c=25.0): 100k timesteps
- Groups 4-9 (gamma_c=50.0, 100.0): 50k timesteps  
- Enhanced callback for structured data export
- Updated time limits for longer jobs

Usage: python3 create_data_export_scripts.py
"""

import yaml
import os
from datetime import datetime

# Parameter space definition (same as before)
PARAMETER_SPACE = {
    'gamma_c': [25.0, 50.0, 100.0],
    'step_domain_fraction': [0.025, 0.05, 0.1],
    'rl_iterations_per_timestep': [10, 25, 40],
    'element_budget': [25, 30, 40]
}

def generate_all_combinations():
    """Generate all 81 parameter combinations organized into 9 groups."""
    combinations = []
    
    for gamma_c in PARAMETER_SPACE['gamma_c']:
        for step_domain in PARAMETER_SPACE['step_domain_fraction']:
            for rl_iterations in PARAMETER_SPACE['rl_iterations_per_timestep']:
                for element_budget in PARAMETER_SPACE['element_budget']:
                    combinations.append({
                        'gamma_c': gamma_c,
                        'step_domain_fraction': step_domain,
                        'rl_iterations_per_timestep': rl_iterations,
                        'element_budget': element_budget
                    })
    
    # Group by gamma_c × step_domain_fraction (9 groups of 9 combinations each)
    groups = []
    group_id = 1
    
    for gamma_c in PARAMETER_SPACE['gamma_c']:
        for step_domain in PARAMETER_SPACE['step_domain_fraction']:
            group_combinations = [
                combo for combo in combinations 
                if combo['gamma_c'] == gamma_c and combo['step_domain_fraction'] == step_domain
            ]
            
            groups.append({
                'group_id': group_id,
                'group_name': f"gamma_{gamma_c}_step_{step_domain}",
                'combinations': group_combinations
            })
            group_id += 1
    
    return groups

def create_slurm_script_template():
    """Create the enhanced SLURM script template with conditional timesteps."""
    
    template = '''#!/bin/bash
#SBATCH --job-name=param_sweep_data_group_{group_id:02d}
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G
#SBATCH --time=5:00:00
#SBATCH --array=0-8
#SBATCH --output=logs/param_sweep_data/group_{group_id:02d}_%A_%a.out
#SBATCH --error=logs/param_sweep_data/group_{group_id:02d}_%A_%a.err

# Parameter Sweep Group {group_id}: {group_name} (WITH STRUCTURED DATA EXPORT)
# This script handles 9 parameter combinations using array indices 0-8
# Uses conditional timesteps: 100k for gamma_c=25.0, 50k for others

echo "=================================================="
echo "Parameter Sweep Group {group_id} (Data Export) - Job $SLURM_ARRAY_JOB_ID Task $SLURM_ARRAY_TASK_ID"
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

# Set timesteps based on gamma_c value (CONDITIONAL LOGIC)
if [ "$GAMMA_C" == "25.0" ]; then
    TOTAL_TIMESTEPS=100000
    echo "🎯 Using extended training: 100k timesteps for gamma_c=25.0"
else
    TOTAL_TIMESTEPS=50000
    echo "📊 Using standard training: 50k timesteps for gamma_c=$GAMMA_C"
fi

# Print current parameter configuration
echo "Current parameters:"
echo "  GAMMA_C: $GAMMA_C"
echo "  STEP_DOMAIN_FRACTION: $STEP_DOMAIN_FRACTION"  
echo "  RL_ITERATIONS: $RL_ITERATIONS"
echo "  ELEMENT_BUDGET: $ELEMENT_BUDGET"
echo "  TOTAL_TIMESTEPS: $TOTAL_TIMESTEPS"
echo ""

# Create unique timestamp for this sweep (NEW SWEEP WITH DATA EXPORT)
SWEEP_TIMESTAMP="{timestamp}"

# Create results directory structure
BASE_RESULTS_DIR="results/full_param_sweep_data_$SWEEP_TIMESTAMP"
CURRENT_RESULTS_DIR="$BASE_RESULTS_DIR/gamma_${{GAMMA_C}}_step_${{STEP_DOMAIN_FRACTION}}_rl_${{RL_ITERATIONS}}_budget_${{ELEMENT_BUDGET}}"

echo "Creating results directory: $CURRENT_RESULTS_DIR"
mkdir -p "$CURRENT_RESULTS_DIR"

# Copy and modify base configuration
BASE_CONFIG_TEMPLATE="experiments/configs/param_sweep/base_template.yaml"
CURRENT_CONFIG="/tmp/config_${{SLURM_JOB_ID}}_${{SLURM_ARRAY_TASK_ID}}.yaml"

echo "Creating configuration file: $CURRENT_CONFIG"
cp "$BASE_CONFIG_TEMPLATE" "$CURRENT_CONFIG"

# Substitute parameters in config file (INCLUDING TOTAL_TIMESTEPS)
sed -i "s/{{{{GAMMA_C}}}}/$GAMMA_C/g" "$CURRENT_CONFIG"
sed -i "s/{{{{STEP_DOMAIN_FRACTION}}}}/$STEP_DOMAIN_FRACTION/g" "$CURRENT_CONFIG"
sed -i "s/{{{{RL_ITERATIONS}}}}/$RL_ITERATIONS/g" "$CURRENT_CONFIG"
sed -i "s/{{{{MIN_RL_ITERATIONS}}}}/$RL_ITERATIONS/g" "$CURRENT_CONFIG"
sed -i "s/{{{{MAX_RL_ITERATIONS}}}}/$RL_ITERATIONS/g" "$CURRENT_CONFIG"
sed -i "s/{{{{ELEMENT_BUDGET}}}}/$ELEMENT_BUDGET/g" "$CURRENT_CONFIG"
sed -i "s/{{{{TOTAL_TIMESTEPS}}}}/$TOTAL_TIMESTEPS/g" "$CURRENT_CONFIG"

echo "✓ Configuration file prepared with $TOTAL_TIMESTEPS timesteps"

# Change to project directory
cd /bsuhome/antonechacartegu/projects/drl-amr/1D-Wave-AMR

# Run training with no-timestamp flag for predictable directory structure
echo "Starting training with enhanced_callback_data..."
python3 experiments/run_experiments_mixed_gpu.py \\
    --config "$CURRENT_CONFIG" \\
    --results-dir "$CURRENT_RESULTS_DIR" \\
    --no-timestamp

# Check if training completed successfully
if [ $? -eq 0 ]; then
    echo "✓ Training completed successfully"
    
    # Create completion marker with timesteps info
    echo "job_id: $SLURM_ARRAY_JOB_ID" > "$CURRENT_RESULTS_DIR/job_completed.yaml"
    echo "task_id: $SLURM_ARRAY_TASK_ID" >> "$CURRENT_RESULTS_DIR/job_completed.yaml"
    echo "completion_time: $(date -Iseconds)" >> "$CURRENT_RESULTS_DIR/job_completed.yaml"
    echo "parameters:" >> "$CURRENT_RESULTS_DIR/job_completed.yaml"
    echo "  gamma_c: $GAMMA_C" >> "$CURRENT_RESULTS_DIR/job_completed.yaml"
    echo "  step_domain_fraction: $STEP_DOMAIN_FRACTION" >> "$CURRENT_RESULTS_DIR/job_completed.yaml"
    echo "  rl_iterations: $RL_ITERATIONS" >> "$CURRENT_RESULTS_DIR/job_completed.yaml"
    echo "  element_budget: $ELEMENT_BUDGET" >> "$CURRENT_RESULTS_DIR/job_completed.yaml"
    echo "  total_timesteps: $TOTAL_TIMESTEPS" >> "$CURRENT_RESULTS_DIR/job_completed.yaml"
    
    # Verify expected files exist (INCLUDING NEW DATA FILES)
    expected_files=("final_model.zip" "training_report.pdf")
    data_files=()
    
    # Look for parameter-based data files
    for file in "$CURRENT_RESULTS_DIR"/*.json; do
        if [[ -f "$file" && "$file" == *"training_metrics.json" ]]; then
            data_files+=("$(basename "$file")")
        fi
    done
    
    for file in "$CURRENT_RESULTS_DIR"/*.csv; do
        if [[ -f "$file" && "$file" == *"training_summary.csv" ]]; then
            data_files+=("$(basename "$file")")
        fi
    done
    
    all_present=true
    for file in "${{expected_files[@]}}"; do
        if [ -f "$CURRENT_RESULTS_DIR/$file" ]; then
            echo "✓ Found: $file"
        else
            echo "❌ Missing: $file"
            all_present=false
        fi
    done
    
    if [ ${{#data_files[@]}} -gt 0 ]; then
        echo "✅ Enhanced data files found:"
        for file in "${{data_files[@]}}"; do
            echo "  📊 $file"
        done
    else
        echo "⚠️  No structured data files found"
        all_present=false
    fi
    
    if $all_present; then
        echo "🎉 All expected output files present (PDF + structured data)"
    else
        echo "⚠️  Some expected output files missing"
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
echo "Total timesteps used: $TOTAL_TIMESTEPS"
echo "=================================================="
'''
    
    return template

def generate_parameter_cases(group_combinations):
    """Generate the parameter case statements for the SLURM script."""
    cases = []
    
    for i, combo in enumerate(group_combinations):
        case_block = f'''    {i})
        GAMMA_C={combo['gamma_c']}
        STEP_DOMAIN_FRACTION={combo['step_domain_fraction']}
        RL_ITERATIONS={combo['rl_iterations_per_timestep']}
        ELEMENT_BUDGET={combo['element_budget']}
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

def save_slurm_scripts(groups):
    """Save all SLURM scripts."""
    
    # Create directories
    slurm_dir = "slurm_scripts/param_sweep_data"
    logs_dir = "logs/param_sweep_data"
    os.makedirs(slurm_dir, exist_ok=True)
    os.makedirs(logs_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    script_paths = []
    
    print(f"Creating enhanced SLURM scripts for {len(groups)} groups...")
    print(f"Timestamp: {timestamp}")
    
    for group in groups:
        # Generate script content
        script_content = create_group_slurm_script(group, timestamp)
        
        # Save script
        script_filename = f"data_group_{group['group_id']:02d}.slurm"
        script_path = os.path.join(slurm_dir, script_filename)
        
        with open(script_path, 'w') as f:
            f.write(script_content)
        
        # Make executable
        os.chmod(script_path, 0o755)
        
        script_paths.append(script_path)
        
        # Determine timesteps for this group
        gamma_c = group['combinations'][0]['gamma_c']  # All combinations in group have same gamma_c
        timesteps = "100k" if gamma_c == 25.0 else "50k"
        
        print(f"✓ Created: {script_path} (gamma_c={gamma_c}, {timesteps} timesteps)")
    
    return script_paths, timestamp

def create_submission_script(groups, timestamp):
    """Create master submission script."""
    
    submission_script = f'''#!/bin/bash
# Master submission script for parameter sweep WITH DATA EXPORT
# Submits all 9 group jobs with conditional timesteps and enhanced callback
# Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

echo "Starting 81-Parameter Sweep Submission (Data Export Version)"
echo "============================================================"
echo "🎯 gamma_c=25.0 jobs: 100k timesteps (Groups 1-3)" 
echo "📊 gamma_c=50.0/100.0 jobs: 50k timesteps (Groups 4-9)"
echo "📈 Using enhanced_callback_data for structured JSON/CSV export"
echo ""

# Array to store job IDs
declare -a JOB_IDS

# Submit each group
'''
    
    for group in groups:
        script_name = f"data_group_{group['group_id']:02d}.slurm"
        gamma_c = group['combinations'][0]['gamma_c']
        timesteps = "100k" if gamma_c == 25.0 else "50k"
        
        submission_script += f'''
echo "Submitting Group {group['group_id']}: {group['group_name']} ({timesteps})"
JOB_ID_{group['group_id']}=$(sbatch slurm_scripts/param_sweep_data/{script_name} | cut -d' ' -f4)
echo "  Job ID: $JOB_ID_{group['group_id']}"
JOB_IDS+=($JOB_ID_{group['group_id']})
sleep 2  # Brief pause between submissions
'''
    
    submission_script += f'''
echo ""
echo "All jobs submitted successfully!"
echo "Total jobs: {len(groups)}"
echo "Total parameter combinations: 81"
echo "Mixed timesteps: 27 × 100k + 54 × 50k = 5.4M total timesteps"
echo ""
echo "Job IDs:"
'''
    
    for group in groups:
        gamma_c = group['combinations'][0]['gamma_c']
        timesteps = "100k" if gamma_c == 25.0 else "50k"
        submission_script += f'echo "  Group {group["group_id"]:2d}: $JOB_ID_{group["group_id"]} ({timesteps})"' + '\n'
    
    submission_script += '''
echo ""
echo "Monitor jobs with:"
echo "  squeue -u $USER"
echo "  python3 monitor_param_sweep.py"
echo ""
echo "Expected completion time:"
echo "  Groups 1-3 (100k): ~4-5 hours each"
echo "  Groups 4-9 (50k):  ~2-3 hours each"
echo ""
echo "Data collection:"
echo "  Structured data: JSON + CSV files for immediate analysis"
echo "  PDF reports: Comprehensive training reports as before"
'''
    
    submission_path = "submit_param_sweep_data.sh"
    with open(submission_path, 'w') as f:
        f.write(submission_script)
    
    os.chmod(submission_path, 0o755)
    print(f"✓ Created master submission script: {submission_path}")
    return submission_path

def print_summary(groups, script_paths, submission_path, timestamp):
    """Print creation summary."""
    print("\n" + "="*70)
    print("DATA EXPORT PARAMETER SWEEP - GENERATION SUMMARY")
    print("="*70)
    
    print(f"✅ Created {len(script_paths)} enhanced SLURM scripts:")
    for i, path in enumerate(script_paths):
        group = groups[i]
        gamma_c = group['combinations'][0]['gamma_c']
        timesteps = "100k" if gamma_c == 25.0 else "50k"
        print(f"  📊 {path} (gamma_c={gamma_c}, {timesteps})")
    
    print(f"\n🎯 Key Enhancements:")
    print(f"  • Conditional timesteps: 100k for gamma_c=25.0, 50k for others")
    print(f"  • Enhanced callback: structured JSON/CSV data export")
    print(f"  • Extended time limits: 5 hours for longer jobs")
    print(f"  • Updated directory naming: full_param_sweep_data_{timestamp}")
    
    print(f"\n📈 Training Breakdown:")
    print(f"  • Groups 1-3 (gamma_c=25.0): 27 jobs × 100k timesteps = 2.7M timesteps")
    print(f"  • Groups 4-9 (gamma_c=50.0, 100.0): 54 jobs × 50k timesteps = 2.7M timesteps")
    print(f"  • Total: 81 jobs, 5.4M timesteps")
    
    print(f"\n🚀 To submit all jobs:")
    print(f"  bash {submission_path}")
    
    print(f"\n📊 Expected outputs per job:")
    print(f"  • final_model.zip (trained model)")
    print(f"  • gamma_X_step_Y_rl_Z_budget_W_Nk_training_report.pdf")
    print(f"  • gamma_X_step_Y_rl_Z_budget_W_Nk_training_metrics.json")
    print(f"  • gamma_X_step_Y_rl_Z_budget_W_Nk_training_summary.csv")

def main():
    """Main execution function."""
    print("Creating Data Export Parameter Sweep Scripts")
    print("=" * 60)
    
    # Generate all parameter combinations organized into groups
    groups = generate_all_combinations()
    print(f"\n✓ Generated {len(groups)} groups covering 81 parameter combinations")
    
    # Create SLURM scripts
    script_paths, timestamp = save_slurm_scripts(groups)
    
    # Create submission script
    submission_path = create_submission_script(groups, timestamp)
    
    # Print summary
    print_summary(groups, script_paths, submission_path, timestamp)
    
    print(f"\n🎉 Data export parameter sweep ready!")
    print(f"\n⏭️  Next steps:")
    print(f"  1. Review generated scripts in slurm_scripts/param_sweep_data/")
    print(f"  2. Submit all jobs: bash {submission_path}")
    print(f"  3. Monitor progress: python3 monitor_param_sweep.py")
    print(f"  4. Analyze structured data when complete!")

if __name__ == "__main__":
    main()
