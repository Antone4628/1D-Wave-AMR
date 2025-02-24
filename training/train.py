"""
Training script for DG AMR reinforcement learning.
"""

import os
import argparse
import numpy as np


# Get absolute path to project root
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 
    '..'
))

from numerical.solvers.dg_wave_solver import DGWaveSolver
from numerical.environments.dg_amr_env import DGAMREnv
from .trainer import DGAMRTrainer
from .utils.visualization import plot_training_results

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="configs/test_config.yaml",
                      help="Path to config file")
    parser.add_argument("--log-dir", type=str, default=None,
                      help="Directory for logs and checkpoints")
    parser.add_argument("--checkpoint-freq", type=int, default=10000,
                      help="Frequency of model checkpoints")
    return parser.parse_args()

def main():
    args = parse_args()
    
    # Convert config path to absolute path
    config_path = os.path.join(PROJECT_ROOT, 'training', args.config)
    
    # Initialize solver
    xelem = np.array([-1, -0.4, 0, 0.4, 1])
    solver = DGWaveSolver(
        nop=4,
        xelem=xelem,
        max_elements=40,
        max_level=4,
        courant_max=0.1,
        icase=1
    )
    
    # Create environment
    env = DGAMREnv(
        solver=solver,
        element_budget=25,
        gamma_c=25.0
    )
    
    # Create trainer
    trainer = DGAMRTrainer(
        env=env,
        config_path=config_path,
        log_dir=args.log_dir,
        checkpoint_freq=args.checkpoint_freq
    )
    
    # Run training
    trainer.train()
    
    # Plot results
    plot_training_results(
        trainer.log_dir,
        trainer.config['total_timesteps']
    )

if __name__ == "__main__":
    main()