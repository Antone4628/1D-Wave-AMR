#!/usr/bin/env python3
"""
Base Configuration Template Generator for Parameter Sweep
Creates the base YAML config template with parameter placeholders.

CRITICAL FIX: Generate YAML template as string to ensure unquoted numeric placeholders.

Usage: python3 create_base_config.py
"""

import yaml
import os
from pathlib import Path

def create_base_config_template_string():
    """Create base configuration template as raw YAML string with unquoted placeholders."""
    
    template_string = """environment:
  max_episode_steps: 200
  element_budget: {{ELEMENT_BUDGET}}
  gamma_c: {{GAMMA_C}}
  rl_iterations_per_timestep: {{RL_ITERATIONS}}
  min_rl_iterations: {{MIN_RL_ITERATIONS}}
  max_rl_iterations: {{MAX_RL_ITERATIONS}}
  max_consecutive_no_action: 30
  step_domain_fraction: {{STEP_DOMAIN_FRACTION}}
  initial_refinement:
    mode: random
    fixed_level: 2
    max_initial_level: 4
    probability: 0.7
training:
  total_timesteps: {{TOTAL_TIMESTEPS}}
  algorithm: A2C
  learning_rate: 0.0003
  n_steps: 5
  ent_coef: 0.01
  callback: enhanced
solver:
  nop: 4
  max_level: 8
  courant_max: 0.1
  icase: 1
  initial_elements:
  - -1
  - -0.4
  - 0
  - 0.4
  - 1
  verbose: false
  balance: false
"""
    
    return template_string

def save_base_config():
    """Save base configuration template as raw YAML string."""
    template_content = create_base_config_template_string()
    
    # Ensure directory exists
    config_dir = "experiments/configs/param_sweep"
    os.makedirs(config_dir, exist_ok=True)
    
    # Save base template as raw string (not using yaml.dump)
    template_path = f"{config_dir}/base_template.yaml"
    with open(template_path, 'w') as f:
        f.write(template_content)
    
    print(f"✓ Base config template saved to: {template_path}")
    print(f"✓ Numeric placeholders are now unquoted for proper data types")
    return template_path

def create_parameter_substitution_guide():
    """Create guide for parameter substitution in SLURM scripts."""
    
    substitution_guide = {
        'parameter_placeholders': {
            'GAMMA_C': {
                'description': 'Coefficient for resource penalty term',
                'values': [25.0, 50.0, 100.0],
                'data_type': 'float',
                'sed_command': 'sed -i "s/{{GAMMA_C}}/$GAMMA_C/g" config.yaml'
            },
            'STEP_DOMAIN_FRACTION': {
                'description': 'Fraction of domain to timestep',
                'values': [0.025, 0.05, 0.1],
                'data_type': 'float',
                'sed_command': 'sed -i "s/{{STEP_DOMAIN_FRACTION}}/$STEP_DOMAIN_FRACTION/g" config.yaml'
            },
            'RL_ITERATIONS': {
                'description': 'RL iterations per timestep',
                'values': [10, 25, 40],
                'data_type': 'integer',
                'sed_command': 'sed -i "s/{{RL_ITERATIONS}}/$RL_ITERATIONS/g" config.yaml'
            },
            'ELEMENT_BUDGET': {
                'description': 'Maximum number of elements allowed',
                'values': [25, 30, 40],
                'data_type': 'integer',
                'sed_command': 'sed -i "s/{{ELEMENT_BUDGET}}/$ELEMENT_BUDGET/g" config.yaml'
            },
            'MIN_RL_ITERATIONS': {
                'description': 'Minimum RL iterations (same as RL_ITERATIONS)',
                'note': 'Set to same value as RL_ITERATIONS',
                'data_type': 'integer',
                'sed_command': 'sed -i "s/{{MIN_RL_ITERATIONS}}/$RL_ITERATIONS/g" config.yaml'
            },
            'MAX_RL_ITERATIONS': {
                'description': 'Maximum RL iterations (same as RL_ITERATIONS)',
                'note': 'Set to same value as RL_ITERATIONS', 
                'data_type': 'integer',
                'sed_command': 'sed -i "s/{{MAX_RL_ITERATIONS}}/$RL_ITERATIONS/g" config.yaml'
            },
            'TOTAL_TIMESTEPS': {
                'description': 'Total training timesteps',
                'note': 'Configurable via --timesteps parameter',
                'data_type': 'integer',
                'sed_command': 'sed -i "s/{{TOTAL_TIMESTEPS}}/$TOTAL_TIMESTEPS/g" config.yaml'
            }
        },
        'fix_note': 'Template now generated as raw YAML string to ensure unquoted numeric placeholders',
        'slurm_usage_example': [
            "# In SLURM script:",
            "cp $BASE_CONFIG_TEMPLATE config.yaml",
            "sed -i \"s/{{GAMMA_C}}/$GAMMA_C/g\" config.yaml",
            "sed -i \"s/{{STEP_DOMAIN_FRACTION}}/$STEP_DOMAIN_FRACTION/g\" config.yaml",
            "sed -i \"s/{{RL_ITERATIONS}}/$RL_ITERATIONS/g\" config.yaml",
            "sed -i \"s/{{MIN_RL_ITERATIONS}}/$RL_ITERATIONS/g\" config.yaml",
            "sed -i \"s/{{MAX_RL_ITERATIONS}}/$RL_ITERATIONS/g\" config.yaml",
            "sed -i \"s/{{ELEMENT_BUDGET}}/$ELEMENT_BUDGET/g\" config.yaml",
            "sed -i \"s/{{TOTAL_TIMESTEPS}}/$TOTAL_TIMESTEPS/g\" config.yaml"
        ]
    }
    
    guide_path = "experiments/configs/param_sweep/substitution_guide.yaml"
    with open(guide_path, 'w') as f:
        yaml.dump(substitution_guide, f, default_flow_style=False, indent=2)
    
    print(f"✓ Parameter substitution guide saved to: {guide_path}")
    return guide_path

def verify_template():
    """Verify the template has all necessary placeholders and proper format."""
    template_path = "experiments/configs/param_sweep/base_template.yaml"
    
    if not os.path.exists(template_path):
        print(f"❌ Template file not found: {template_path}")
        return False
    
    with open(template_path, 'r') as f:
        content = f.read()
    
    required_placeholders = [
        '{{GAMMA_C}}',
        '{{STEP_DOMAIN_FRACTION}}',
        '{{RL_ITERATIONS}}',
        '{{MIN_RL_ITERATIONS}}',
        '{{MAX_RL_ITERATIONS}}',
        '{{ELEMENT_BUDGET}}',
        '{{TOTAL_TIMESTEPS}}'
    ]
    
    missing_placeholders = []
    quoted_placeholders = []
    
    for placeholder in required_placeholders:
        if placeholder not in content:
            missing_placeholders.append(placeholder)
        # Check if placeholder is quoted (bad)
        if f"'{placeholder}'" in content or f'"{placeholder}"' in content:
            quoted_placeholders.append(placeholder)
    
    # Test YAML parsing with mock substitution (placeholders -> valid values)
    test_content = content
    test_substitutions = {
        '{{GAMMA_C}}': '25.0',
        '{{STEP_DOMAIN_FRACTION}}': '0.05',
        '{{RL_ITERATIONS}}': '25',
        '{{MIN_RL_ITERATIONS}}': '25',
        '{{MAX_RL_ITERATIONS}}': '25',
        '{{ELEMENT_BUDGET}}': '30',
        '{{TOTAL_TIMESTEPS}}': '100000'
    }
    
    for placeholder, value in test_substitutions.items():
        test_content = test_content.replace(placeholder, value)
    
    try:
        yaml.safe_load(test_content)
        yaml_valid = True
    except yaml.YAMLError as e:
        print(f"❌ YAML parsing error after mock substitution: {e}")
        yaml_valid = False
    
    if missing_placeholders:
        print(f"⚠️  Missing placeholders: {missing_placeholders}")
        return False
    elif quoted_placeholders:
        print(f"⚠️  Quoted placeholders (will cause type errors): {quoted_placeholders}")
        return False
    elif not yaml_valid:
        print(f"❌ Invalid YAML syntax after substitution")
        return False
    else:
        print(f"✓ All required placeholders present and unquoted")
        print(f"✓ YAML syntax is valid after substitution")
        
        # Show a sample of what the template looks like
        print(f"\nSample template content:")
        lines = content.split('\n')
        for line in lines[:15]:  # Show first 15 lines
            if '{{' in line:
                print(f"  {line}")
        
        return True

def main():
    """Main execution function."""
    print("Creating Base Configuration Template (String-Based Fix)")
    print("=" * 60)
    
    # Create base config template
    template_path = save_base_config()
    
    # Create substitution guide
    guide_path = create_parameter_substitution_guide()
    
    # Verify template
    template_valid = verify_template()
    
    if template_valid:
        print(f"\n✅ Base configuration system created successfully!")
        print(f"✓ Template: {template_path}")
        print(f"✓ Guide: {guide_path}")
        print(f"✓ Data type issue fixed: numeric placeholders are unquoted")
        print(f"\nNext steps:")
        print(f"1. Run: python3 create_data_export_scripts.py --timesteps 100000 --uniform-timesteps --sweep-name 'session4_100k_uniform'")
        print(f"2. Run: bash submit_param_sweep_data.sh")
        print(f"3. Monitor with: squeue -u $USER")
    else:
        print(f"\n❌ Template validation failed. Please check the template.")

if __name__ == "__main__":
    main()




# #!/usr/bin/env python3
# """
# Base Configuration Template Generator for Parameter Sweep
# Creates the base YAML config template with parameter placeholders.

# Usage: python3 create_base_config.py
# """

# import yaml
# import os
# from pathlib import Path

# def create_base_config_template():
#     """Create base configuration template with placeholders."""
    
#     base_config = {
#         'environment': {
#             'max_episode_steps': 200,
#             'element_budget': '{{ELEMENT_BUDGET}}',  # Will be replaced by SLURM script
#             'gamma_c': '{{GAMMA_C}}',  # Will be replaced by SLURM script
#             'rl_iterations_per_timestep': '{{RL_ITERATIONS}}',  # Will be replaced by SLURM script
#             'min_rl_iterations': '{{MIN_RL_ITERATIONS}}',  # Will be replaced by SLURM script
#             'max_rl_iterations': '{{MAX_RL_ITERATIONS}}',  # Will be replaced by SLURM script
#             'max_consecutive_no_action': 30,
#             'step_domain_fraction': '{{STEP_DOMAIN_FRACTION}}',  # Will be replaced by SLURM script
#             'initial_refinement': {
#                 'mode': 'random',
#                 'fixed_level': 2,
#                 'max_initial_level': 4,
#                 'probability': 0.7
#             }
#         },
#         'training': {
#             'total_timesteps': 100000,
#             'algorithm': 'A2C',
#             'learning_rate': 0.0003,
#             'n_steps': 5,
#             'ent_coef': 0.01,
#             'callback': 'enhanced'  # Use enhanced callback with do-nothing tracking
#         },
#         'solver': {
#             'nop': 4,
#             'max_level': 8,
#             'courant_max': 0.1,
#             'icase': 1,
#             'initial_elements': [-1, -0.4, 0, 0.4, 1],
#             'verbose': False,
#             'balance': False
#         }
#     }
    
#     return base_config

# def save_base_config():
#     """Save base configuration template."""
#     base_config = create_base_config_template()
    
#     # Ensure directory exists
#     config_dir = "experiments/configs/param_sweep"
#     os.makedirs(config_dir, exist_ok=True)
    
#     # Save base template
#     template_path = f"{config_dir}/base_template.yaml"
#     with open(template_path, 'w') as f:
#         yaml.dump(base_config, f, default_flow_style=False, indent=2)
    
#     print(f"✓ Base config template saved to: {template_path}")
#     return template_path

# def create_parameter_substitution_guide():
#     """Create guide for parameter substitution in SLURM scripts."""
    
#     substitution_guide = {
#         'parameter_placeholders': {
#             'GAMMA_C': {
#                 'description': 'Coefficient for resource penalty term',
#                 'values': [25.0, 50.0, 100.0],
#                 'sed_command': 'sed -i "s/{{GAMMA_C}}/$GAMMA_C/g" config.yaml'
#             },
#             'STEP_DOMAIN_FRACTION': {
#                 'description': 'Fraction of domain to timestep',
#                 'values': [0.025, 0.05, 0.1],
#                 'sed_command': 'sed -i "s/{{STEP_DOMAIN_FRACTION}}/$STEP_DOMAIN_FRACTION/g" config.yaml'
#             },
#             'RL_ITERATIONS': {
#                 'description': 'RL iterations per timestep',
#                 'values': [10, 25, 40],
#                 'sed_command': 'sed -i "s/{{RL_ITERATIONS}}/$RL_ITERATIONS/g" config.yaml'
#             },
#             'ELEMENT_BUDGET': {
#                 'description': 'Maximum number of elements allowed',
#                 'values': [25, 30, 40],
#                 'sed_command': 'sed -i "s/{{ELEMENT_BUDGET}}/$ELEMENT_BUDGET/g" config.yaml'
#             },
#             'MIN_RL_ITERATIONS': {
#                 'description': 'Minimum RL iterations (same as RL_ITERATIONS)',
#                 'note': 'Set to same value as RL_ITERATIONS',
#                 'sed_command': 'sed -i "s/{{MIN_RL_ITERATIONS}}/$RL_ITERATIONS/g" config.yaml'
#             },
#             'MAX_RL_ITERATIONS': {
#                 'description': 'Maximum RL iterations (same as RL_ITERATIONS)',
#                 'note': 'Set to same value as RL_ITERATIONS',
#                 'sed_command': 'sed -i "s/{{MAX_RL_ITERATIONS}}/$RL_ITERATIONS/g" config.yaml'
#             }
#         },
#         'slurm_usage_example': [
#             "# In SLURM script:",
#             "cp $BASE_CONFIG_TEMPLATE config.yaml",
#             "sed -i \"s/{{GAMMA_C}}/$GAMMA_C/g\" config.yaml",
#             "sed -i \"s/{{STEP_DOMAIN_FRACTION}}/$STEP_DOMAIN_FRACTION/g\" config.yaml",
#             "sed -i \"s/{{RL_ITERATIONS}}/$RL_ITERATIONS/g\" config.yaml",
#             "sed -i \"s/{{MIN_RL_ITERATIONS}}/$RL_ITERATIONS/g\" config.yaml",
#             "sed -i \"s/{{MAX_RL_ITERATIONS}}/$RL_ITERATIONS/g\" config.yaml",
#             "sed -i \"s/{{ELEMENT_BUDGET}}/$ELEMENT_BUDGET/g\" config.yaml"
#         ]
#     }
    
#     guide_path = "experiments/configs/param_sweep/substitution_guide.yaml"
#     with open(guide_path, 'w') as f:
#         yaml.dump(substitution_guide, f, default_flow_style=False, indent=2)
    
#     print(f"✓ Parameter substitution guide saved to: {guide_path}")
#     return guide_path

# def verify_template():
#     """Verify the template has all necessary placeholders."""
#     template_path = "experiments/configs/param_sweep/base_template.yaml"
    
#     with open(template_path, 'r') as f:
#         content = f.read()
    
#     required_placeholders = [
#         '{{GAMMA_C}}',
#         '{{STEP_DOMAIN_FRACTION}}',
#         '{{RL_ITERATIONS}}',
#         '{{MIN_RL_ITERATIONS}}',
#         '{{MAX_RL_ITERATIONS}}',
#         '{{ELEMENT_BUDGET}}'
#     ]
    
#     missing_placeholders = []
#     for placeholder in required_placeholders:
#         if placeholder not in content:
#             missing_placeholders.append(placeholder)
    
#     if missing_placeholders:
#         print(f"⚠️  Missing placeholders: {missing_placeholders}")
#         return False
#     else:
#         print(f"✓ All required placeholders present in template")
#         return True

# def main():
#     """Main execution function."""
#     print("Creating Base Configuration Template")
#     print("=" * 50)
    
#     # Create base config template
#     template_path = save_base_config()
    
#     # Create substitution guide
#     guide_path = create_parameter_substitution_guide()
    
#     # Verify template
#     template_valid = verify_template()
    
#     if template_valid:
#         print(f"\n✓ Base configuration system created successfully!")
#         print(f"✓ Template: {template_path}")
#         print(f"✓ Guide: {guide_path}")
#         print(f"\nNext step: Run python3 create_slurm_scripts.py")
#     else:
#         print(f"\n❌ Template validation failed. Please check the template.")

# if __name__ == "__main__":
#     main()