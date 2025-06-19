"""
Configuration for AMR Parameter Analysis
"""
import os

import os

# Get absolute path to project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
ANALYSIS_ROOT = os.path.join(PROJECT_ROOT, 'analysis')

# Use absolute paths
RAW_DATA_DIR = os.path.join(ANALYSIS_ROOT, "data", "raw")
PROCESSED_DATA_DIR = os.path.join(ANALYSIS_ROOT, "data", "processed")
OUTPUTS_DIR = os.path.join(ANALYSIS_ROOT, "outputs")

# HPC Connection Settings
HPC_HOST = "antonechacartegu@borah-login.boisestate.edu"
HPC_BASE_PATH = "/bsuhome/antonechacartegu/projects/drl-amr/1D-Wave-AMR"

# Analysis Settings
CURRENT_SWEEP = "full_param_sweep_data_20250601_105453"
PARAMETER_SPACE = {
    'gamma_c': [25.0, 50.0, 100.0],
    'step_domain_fraction': [0.025, 0.05, 0.1],
    'rl_iterations_per_timestep': [10, 25, 40],
    'element_budget': [25, 30, 40]
}

# Paths
# DATA_DIR = "data"
# RAW_DATA_DIR = "data/raw"
# PROCESSED_DATA_DIR = "data/processed"
# OUTPUTS_DIR = "outputs"

# Analysis Parameters
CONVERGENCE_THRESHOLDS = {
    'well_converged': 0.8,
    'moderate': 0.5,
    'under_trained': 0.2
}

# Visualization Settings
FIGURE_DPI = 300
FIGURE_FORMAT = 'png'
THESIS_FIGURE_FORMAT = 'pdf'
