#!/usr/bin/env python3
"""
HPC Manifest Generator for 81-Parameter Sweep
Run this script on HPC to generate the complete manifest system.

Usage: python3 create_manifest_system.py
"""

import yaml
import os
import itertools
from datetime import datetime
from pathlib import Path

def generate_parameter_combinations():
    """Generate all 81 parameter combinations."""
    gamma_c_values = [25.0, 50.0, 100.0]
    step_domain_fraction_values = [0.025, 0.05, 0.1]
    rl_iterations_per_timestep_values = [10, 25, 40]
    element_budget_values = [25, 30, 40]
    
    combinations = list(itertools.product(
        gamma_c_values,
        step_domain_fraction_values,
        rl_iterations_per_timestep_values,
        element_budget_values
    ))
    
    print(f"✓ Generated {len(combinations)} parameter combinations")
    return combinations

def create_parameter_groups(combinations):
    """Group combinations for SLURM array jobs (9 groups of 9 combinations each)."""
    groups = []
    gamma_c_values = [25.0, 50.0, 100.0]
    step_domain_values = [0.025, 0.05, 0.1]
    
    group_id = 1
    for gamma_c in gamma_c_values:
        for step_domain in step_domain_values:
            group_combinations = [
                combo for combo in combinations 
                if combo[0] == gamma_c and combo[1] == step_domain
            ]
            
            if len(group_combinations) == 9:
                groups.append({
                    'group_id': group_id,
                    'group_name': f"gamma_{gamma_c}_step_{step_domain}",
                    'combinations': group_combinations
                })
                group_id += 1
    
    print(f"✓ Created {len(groups)} parameter groups")
    return groups

def generate_manifest(combinations, groups, timestamp):
    """Generate comprehensive manifest YAML."""
    manifest = {
        'sweep_info': {
            'timestamp': timestamp,
            'total_combinations': len(combinations),
            'total_groups': len(groups),
            'total_timesteps': 20000,
            'parameters': {
                'gamma_c': [25.0, 50.0, 100.0],
                'step_domain_fraction': [0.025, 0.05, 0.1],
                'rl_iterations_per_timestep': [10, 25, 40],
                'element_budget': [25, 30, 40]
            }
        },
        'directory_structure': {
            'base_path': f"results/full_param_sweep_{timestamp}",
            'naming_convention': "gamma_{gamma_c}_step_{step_domain}_rl_{rl_iterations}_budget_{budget}",
            'collection_naming': "gamma_{gamma_c}_step_{step_domain}_rl_{rl_iterations}_budget_{budget}_20k"
        },
        'groups': [],
        'combinations': []
    }
    
    # Add group information
    for group in groups:
        group_info = {
            'group_id': group['group_id'],
            'group_name': group['group_name'],
            'slurm_script': f"group_{group['group_id']:02d}.slurm",
            'job_id': None,
            'status': 'not_submitted',
            'combinations_count': len(group['combinations'])
        }
        manifest['groups'].append(group_info)
    
    # Add detailed combination information
    combo_id = 1
    for group in groups:
        for i, combo in enumerate(group['combinations']):
            gamma_c, step_domain, rl_iterations, element_budget = combo
            
            combo_info = {
                'combo_id': combo_id,
                'group_id': group['group_id'],
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
                    'final_model_name': f"gamma_{gamma_c}_step_{step_domain}_rl_{rl_iterations}_budget_{element_budget}_20k_final_model.zip",
                    'report_name': f"gamma_{gamma_c}_step_{step_domain}_rl_{rl_iterations}_budget_{element_budget}_20k_training_report.pdf"
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
            combo_id += 1
    
    return manifest

def create_directories():
    """Create necessary directory structure."""
    dirs = [
        'experiments/manifests',
        'experiments/configs/param_sweep',
        'slurm_scripts/param_sweep',
        'results'
    ]
    
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        print(f"✓ Created directory: {dir_path}")

def save_manifest(manifest, timestamp):
    """Save manifest to YAML file."""
    manifest_path = f"experiments/manifests/full_param_sweep_{timestamp}.yaml"
    
    with open(manifest_path, 'w') as f:
        yaml.dump(manifest, f, default_flow_style=False, indent=2)
    
    # Also save as latest for easy access
    latest_path = "experiments/manifests/latest_manifest.yaml"
    with open(latest_path, 'w') as f:
        yaml.dump(manifest, f, default_flow_style=False, indent=2)
    
    print(f"✓ Manifest saved to: {manifest_path}")
    print(f"✓ Latest manifest: {latest_path}")
    return manifest_path

def print_summary(manifest):
    """Print manifest summary."""
    print("\n" + "="*60)
    print("PARAMETER SWEEP MANIFEST SUMMARY")
    print("="*60)
    
    sweep_info = manifest['sweep_info']
    print(f"Timestamp: {sweep_info['timestamp']}")
    print(f"Total combinations: {sweep_info['total_combinations']}")
    print(f"Total groups: {sweep_info['total_groups']}")
    print(f"Timesteps per job: {sweep_info['total_timesteps']:,}")
    
    print(f"\nParameter ranges:")
    for param, values in sweep_info['parameters'].items():
        print(f"  {param}: {values}")
    
    print(f"\nGroup structure:")
    for i, group in enumerate(manifest['groups'][:3]):  # Show first 3
        print(f"  Group {group['group_id']}: {group['group_name']} ({group['combinations_count']} combinations)")
    if len(manifest['groups']) > 3:
        print(f"  ... and {len(manifest['groups']) - 3} more groups")
    
    print(f"\nDirectory structure:")
    print(f"  Base: {manifest['directory_structure']['base_path']}")
    print(f"  Naming: {manifest['directory_structure']['naming_convention']}")
    
    print(f"\nFirst 3 combinations:")
    for combo in manifest['combinations'][:3]:
        params = combo['parameters']
        print(f"  {combo['combo_id']}: gamma_c={params['gamma_c']}, step_domain={params['step_domain_fraction']}, rl_iter={params['rl_iterations_per_timestep']}, budget={params['element_budget']}")
    
    print(f"\nNext steps:")
    print(f"  1. Run: python3 create_base_config.py")
    print(f"  2. Run: python3 create_slurm_scripts.py")
    print(f"  3. Run: bash submit_param_sweep.sh")

def main():
    """Main execution function."""
    print("Creating 81-Parameter Sweep Manifest System")
    print("=" * 50)
    
    # Create directories
    create_directories()
    
    # Generate timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    
    # Generate combinations and groups
    combinations = generate_parameter_combinations()
    groups = create_parameter_groups(combinations)
    
    # Generate manifest
    manifest = generate_manifest(combinations, groups, timestamp)
    
    # Save manifest
    manifest_path = save_manifest(manifest, timestamp)
    
    # Print summary
    print_summary(manifest)
    
    print(f"\n✓ Manifest system created successfully!")
    print(f"✓ Ready for next step: Base configuration template")

if __name__ == "__main__":
    main()