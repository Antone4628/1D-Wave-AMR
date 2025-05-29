#!/usr/bin/env python3
"""
Monitor Parameter Sweep Progress
Tracks job status and completion across all 81 parameter combinations.

Usage: python3 monitor_param_sweep.py
"""

import subprocess
import yaml
import os
import re
from datetime import datetime
import time

def load_manifest():
    """Load the latest manifest."""
    manifest_path = "experiments/manifests/latest_manifest.yaml"
    
    if not os.path.exists(manifest_path):
        print("❌ Manifest not found. Run create_manifest_system.py first.")
        return None
    
    with open(manifest_path, 'r') as f:
        return yaml.safe_load(f)

def get_slurm_job_status():
    """Get current SLURM job status for the user."""
    try:
        # Get user's jobs
        result = subprocess.run(['squeue', '-u', os.environ.get('USER', 'unknown')], 
                              capture_output=True, text=True)
        
        if result.returncode != 0:
            return {}
        
        jobs = {}
        lines = result.stdout.strip().split('\n')[1:]  # Skip header
        
        for line in lines:
            parts = line.split()
            if len(parts) >= 5:
                job_id = parts[0]
                status = parts[4]
                job_name = parts[2] if len(parts) > 2 else 'unknown'
                
                # Extract group number from job name if it's a param_sweep job
                if 'param_sweep_group' in job_name:
                    match = re.search(r'group_(\d+)', job_name)
                    if match:
                        group_id = int(match.group(1))
                        if group_id not in jobs:
                            jobs[group_id] = {}
                        jobs[group_id][job_id] = status
        
        return jobs
        
    except Exception as e:
        print(f"Error getting SLURM status: {e}")
        return {}

def check_completed_jobs(manifest):
    """Check for completed jobs by looking for completion markers."""
    timestamp = manifest['sweep_info']['timestamp']
    base_results_dir = f"results/full_param_sweep_{timestamp}"
    
    completed_combinations = []
    
    for combo in manifest['combinations']:
        params = combo['parameters']
        combo_dir = f"{base_results_dir}/gamma_{params['gamma_c']}_step_{params['step_domain_fraction']}_rl_{params['rl_iterations_per_timestep']}_budget_{params['element_budget']}"
        
        completion_marker = f"{combo_dir}/job_completed.yaml"
        failure_marker = f"{combo_dir}/job_failed.yaml"
        
        status = 'unknown'
        if os.path.exists(completion_marker):
            status = 'completed'
        elif os.path.exists(failure_marker):
            status = 'failed'
        elif os.path.exists(combo_dir):
            # Check if key files exist
            model_file = f"{combo_dir}/final_model.zip"
            report_file = f"{combo_dir}/training_report.pdf"
            if os.path.exists(model_file) and os.path.exists(report_file):
                status = 'completed'
            else:
                status = 'running'
        
        completed_combinations.append({
            'combo_id': combo['combo_id'],
            'group_id': combo['group_id'],
            'array_index': combo['array_index'],
            'parameters': params,
            'status': status,
            'directory': combo_dir
        })
    
    return completed_combinations

def print_status_summary(manifest, slurm_jobs, completed_combinations):
    """Print comprehensive status summary."""
    print("\n" + "="*70)
    print("PARAMETER SWEEP STATUS SUMMARY")
    print("="*70)
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Overall statistics
    total_combos = len(completed_combinations)
    completed_count = sum(1 for c in completed_combinations if c['status'] == 'completed')
    failed_count = sum(1 for c in completed_combinations if c['status'] == 'failed')
    running_count = sum(1 for c in completed_combinations if c['status'] == 'running')
    unknown_count = total_combos - completed_count - failed_count - running_count
    
    print(f"\nOverall Progress:")
    print(f"  Total combinations: {total_combos}")
    print(f"  Completed: {completed_count} ({completed_count/total_combos*100:.1f}%)")
    print(f"  Running: {running_count} ({running_count/total_combos*100:.1f}%)")
    print(f"  Failed: {failed_count} ({failed_count/total_combos*100:.1f}%)")
    print(f"  Unknown: {unknown_count} ({unknown_count/total_combos*100:.1f}%)")
    
    # Group-by-group status
    print(f"\nGroup Status:")
    for group in manifest['groups']:
        group_id = group['group_id']
        group_combos = [c for c in completed_combinations if c['group_id'] == group_id]
        
        group_completed = sum(1 for c in group_combos if c['status'] == 'completed')
        group_running = sum(1 for c in group_combos if c['status'] == 'running')
        group_failed = sum(1 for c in group_combos if c['status'] == 'failed')
        
        # SLURM job status for this group
        slurm_status = "N/A"
        if group_id in slurm_jobs:
            slurm_statuses = list(slurm_jobs[group_id].values())
            if slurm_statuses:
                slurm_status = f"{len(slurm_statuses)} jobs: {', '.join(set(slurm_statuses))}"
        
        print(f"  Group {group_id:2d} ({group['group_name'][:20]}...): "
              f"{group_completed}/9 complete, {group_running} running, {group_failed} failed | SLURM: {slurm_status}")
    
    # Recent completions
    recent_completed = [c for c in completed_combinations if c['status'] == 'completed']
    if recent_completed:
        print(f"\nRecent Completions (last 5):")
        for combo in recent_completed[-5:]:
            params = combo['parameters']
            print(f"  Combo {combo['combo_id']:2d}: γ={params['gamma_c']}, step={params['step_domain_fraction']}, rl={params['rl_iterations_per_timestep']}, budget={params['element_budget']}")
    
    # Failed jobs
    failed_jobs = [c for c in completed_combinations if c['status'] == 'failed']
    if failed_jobs:
        print(f"\nFailed Jobs:")
        for combo in failed_jobs:
            params = combo['parameters']
            print(f"  Combo {combo['combo_id']:2d}: γ={params['gamma_c']}, step={params['step_domain_fraction']}, rl={params['rl_iterations_per_timestep']}, budget={params['element_budget']}")

def create_progress_file(manifest, completed_combinations):
    """Create a progress tracking file."""
    progress_data = {
        'last_updated': datetime.now().isoformat(),
        'total_combinations': len(completed_combinations),
        'completed': len([c for c in completed_combinations if c['status'] == 'completed']),
        'running': len([c for c in completed_combinations if c['status'] == 'running']),
        'failed': len([c for c in completed_combinations if c['status'] == 'failed']),
        'combinations': completed_combinations
    }
    
    progress_path = "param_sweep_progress.yaml"
    with open(progress_path, 'w') as f:
        yaml.dump(progress_data, f, default_flow_style=False, indent=2)
    
    return progress_path

def main():
    """Main monitoring function."""
    print("Parameter Sweep Job Monitor")
    print("=" * 50)
    
    # Load manifest
    manifest = load_manifest()
    if manifest is None:
        return
    
    # Get SLURM job status
    print("Checking SLURM job status...")
    slurm_jobs = get_slurm_job_status()
    
    # Check completed jobs
    print("Checking completion status...")
    completed_combinations = check_completed_jobs(manifest)
    
    # Print status summary
    print_status_summary(manifest, slurm_jobs, completed_combinations)
    
    # Create progress file
    progress_path = create_progress_file(manifest, completed_combinations)
    print(f"\n✓ Progress saved to: {progress_path}")
    
    # Suggestions
    print(f"\nSuggestions:")
    print(f"  - Run 'squeue -u $USER' for detailed SLURM status")
    print(f"  - Check logs in logs/param_sweep/ for job details")
    print(f"  - Re-run this script periodically to track progress")
    print(f"  - Once jobs complete, run 'python3 collect_results.py'")

if __name__ == "__main__":
    main()