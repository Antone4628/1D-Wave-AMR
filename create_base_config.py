#!/usr/bin/env python3
"""
Base Configuration Template Generator for Parameter Sweep
Creates the base YAML config template with parameter placeholders.

Usage: python3 create_base_config.py
"""

import yaml
import os
from pathlib import Path

def create_base_config_template():
    """Create base configuration template with placeholders."""
    
    base_config = {
        'environment': {
            'max_episode_steps': 200,
            'element_budget': '{{ELEMENT_BUDGET}}',  # Will be replaced by SLURM script
            'gamma_c': '{{GAMMA_C}}',  # Will be replaced by SLURM script
            'rl_iterations_per_timestep': '{{RL_ITERATIONS}}',  # Will be replaced by SLURM script
            'min_rl_iterations': '{{MIN_RL_ITERATIONS}}',  # Will be replaced by SLURM script
            'max_rl_iterations': '{{MAX_RL_ITERATIONS}}',  # Will be replaced by SLURM script
            'max_consecutive_no_action': 30,
            'step_domain_fraction': '{{STEP_DOMAIN_FRACTION}}',  # Will be replaced by SLURM script
            'initial_refinement': {
                'mode': 'random',
                'fixed_level': 2,
                'max_initial_level': 4,
                'probability': 0.7
            }
        },
        'training': {
            'total_timesteps': 20000,
            'algorithm': 'A2C',
            'learning_rate': 0.0003,
            'n_steps': 5,
            'ent_coef': 0.01,
            'callback': 'enhanced'  # Use enhanced callback with do-nothing tracking
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

def save_base_config():
    """Save base configuration template."""
    base_config = create_base_config_template()
    
    # Ensure directory exists
    config_dir = "experiments/configs/param_sweep"
    os.makedirs(config_dir, exist_ok=True)
    
    # Save base template
    template_path = f"{config_dir}/base_template.yaml"
    with open(template_path, 'w') as f:
        yaml.dump(base_config, f, default_flow_style=False, indent=2)
    
    print(f"✓ Base config template saved to: {template_path}")
    return template_path

def create_parameter_substitution_guide():
    """Create guide for parameter substitution in SLURM scripts."""
    
    substitution_guide = {
        'parameter_placeholders': {
            'GAMMA_C': {
                'description': 'Coefficient for resource penalty term',
                'values': [25.0, 50.0, 100.0],
                'sed_command': 'sed -i "s/{{GAMMA_C}}/$GAMMA_C/g" config.yaml'
            },
            'STEP_DOMAIN_FRACTION': {
                'description': 'Fraction of domain to timestep',
                'values': [0.025, 0.05, 0.1],
                'sed_command': 'sed -i "s/{{STEP_DOMAIN_FRACTION}}/$STEP_DOMAIN_FRACTION/g" config.yaml'
            },
            'RL_ITERATIONS': {
                'description': 'RL iterations per timestep',
                'values': [10, 25, 40],
                'sed_command': 'sed -i "s/{{RL_ITERATIONS}}/$RL_ITERATIONS/g" config.yaml'
            },
            'ELEMENT_BUDGET': {
                'description': 'Maximum number of elements allowed',
                'values': [25, 30, 40],
                'sed_command': 'sed -i "s/{{ELEMENT_BUDGET}}/$ELEMENT_BUDGET/g" config.yaml'
            },
            'MIN_RL_ITERATIONS': {
                'description': 'Minimum RL iterations (same as RL_ITERATIONS)',
                'note': 'Set to same value as RL_ITERATIONS',
                'sed_command': 'sed -i "s/{{MIN_RL_ITERATIONS}}/$RL_ITERATIONS/g" config.yaml'
            },
            'MAX_RL_ITERATIONS': {
                'description': 'Maximum RL iterations (same as RL_ITERATIONS)',
                'note': 'Set to same value as RL_ITERATIONS',
                'sed_command': 'sed -i "s/{{MAX_RL_ITERATIONS}}/$RL_ITERATIONS/g" config.yaml'
            }
        },
        'slurm_usage_example': [
            "# In SLURM script:",
            "cp $BASE_CONFIG_TEMPLATE config.yaml",
            "sed -i \"s/{{GAMMA_C}}/$GAMMA_C/g\" config.yaml",
            "sed -i \"s/{{STEP_DOMAIN_FRACTION}}/$STEP_DOMAIN_FRACTION/g\" config.yaml",
            "sed -i \"s/{{RL_ITERATIONS}}/$RL_ITERATIONS/g\" config.yaml",
            "sed -i \"s/{{MIN_RL_ITERATIONS}}/$RL_ITERATIONS/g\" config.yaml",
            "sed -i \"s/{{MAX_RL_ITERATIONS}}/$RL_ITERATIONS/g\" config.yaml",
            "sed -i \"s/{{ELEMENT_BUDGET}}/$ELEMENT_BUDGET/g\" config.yaml"
        ]
    }
    
    guide_path = "experiments/configs/param_sweep/substitution_guide.yaml"
    with open(guide_path, 'w') as f:
        yaml.dump(substitution_guide, f, default_flow_style=False, indent=2)
    
    print(f"✓ Parameter substitution guide saved to: {guide_path}")
    return guide_path

def verify_template():
    """Verify the template has all necessary placeholders."""
    template_path = "experiments/configs/param_sweep/base_template.yaml"
    
    with open(template_path, 'r') as f:
        content = f.read()
    
    required_placeholders = [
        '{{GAMMA_C}}',
        '{{STEP_DOMAIN_FRACTION}}',
        '{{RL_ITERATIONS}}',
        '{{MIN_RL_ITERATIONS}}',
        '{{MAX_RL_ITERATIONS}}',
        '{{ELEMENT_BUDGET}}'
    ]
    
    missing_placeholders = []
    for placeholder in required_placeholders:
        if placeholder not in content:
            missing_placeholders.append(placeholder)
    
    if missing_placeholders:
        print(f"⚠️  Missing placeholders: {missing_placeholders}")
        return False
    else:
        print(f"✓ All required placeholders present in template")
        return True

def main():
    """Main execution function."""
    print("Creating Base Configuration Template")
    print("=" * 50)
    
    # Create base config template
    template_path = save_base_config()
    
    # Create substitution guide
    guide_path = create_parameter_substitution_guide()
    
    # Verify template
    template_valid = verify_template()
    
    if template_valid:
        print(f"\n✓ Base configuration system created successfully!")
        print(f"✓ Template: {template_path}")
        print(f"✓ Guide: {guide_path}")
        print(f"\nNext step: Run python3 create_slurm_scripts.py")
    else:
        print(f"\n❌ Template validation failed. Please check the template.")

if __name__ == "__main__":
    main()