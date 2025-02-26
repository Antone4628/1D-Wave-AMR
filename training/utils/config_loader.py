# utils/config_loader.py
import yaml
import os
import numpy as np

def load_config(config_path):
    """Load configuration from YAML file"""
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    # Convert initial_elements to numpy array if present
    if 'solver' in config and 'initial_elements' in config['solver']:
        config['solver']['initial_elements'] = np.array(config['solver']['initial_elements'])
    
    return config

def get_parameter(config, parameter_path, default=None):
    """
    Get a parameter from the config using dot notation.
    Example: get_parameter(config, "solver.nop", 3)
    """
    parts = parameter_path.split('.')
    current = config
    
    try:
        for part in parts:
            current = current[part]
        return current
    except (KeyError, TypeError):
        return default