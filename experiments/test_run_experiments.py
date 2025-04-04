#!/usr/bin/env python
"""
Test script to verify initial mesh refinement in training.
Simplified version of run_experiments.py with additional debug output.
"""

import os
import sys
import yaml
import argparse
import datetime
import numpy as np
from pathlib import Path

# Get absolute path to project root and add to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    '..'
))
sys.path.append(PROJECT_ROOT)

from numerical.solvers.dg_wave_solver_free import DGWaveSolver
from numerical.environments.dg_amr_env_clean import DGAMREnv
from stable_baselines3 import A2C, PPO, DQN
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.callbacks import BaseCallback

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

def create_environment(config, verbose=True):
    """Create the environment with specified configuration"""
    # Extract key parameters with defaults
    element_budget = get_parameter(config, "environment.element_budget", 25)
    gamma_c = get_parameter(config, "environment.gamma_c", 25.0)
    max_episode_steps = get_parameter(config, "environment.max_episode_steps", 200)
    
    rl_iterations_per_timestep = get_parameter(config, "environment.rl_iterations_per_timestep", "random")
    max_rl_iterations = get_parameter(config, "environment.max_rl_iterations", 200)
    max_consecutive_no_action = get_parameter(config, "environment.max_consecutive_no_action", 10)
    
    nop = get_parameter(config, "solver.nop", 4)
    max_level = get_parameter(config, "solver.max_level", 4)
    courant_max = get_parameter(config, "solver.courant_max", 0.1)
    icase = get_parameter(config, "solver.icase", 1)
    initial_elements = get_parameter(config, "solver.initial_elements", np.array([-1, -0.4, 0, 0.4, 1]))
    solver_verbose = get_parameter(config, "solver.verbose", False)
    
    # Initialize solver
    if verbose:
        print("Initializing DG Wave Solver...")
    
    solver = DGWaveSolver(
        nop=nop,
        xelem=initial_elements,
        max_elements=element_budget * 2,  # Buffer for exploration
        max_level=max_level,
        courant_max=courant_max,
        icase=icase,
        verbose=solver_verbose
    )

    # Initialize environment
    if verbose:
        print("Setting up environment...")
    
    env = DGAMREnv(
        solver=solver,
        element_budget=element_budget,
        gamma_c=gamma_c,
        max_episode_steps=max_episode_steps,
        verbose=solver_verbose,
        rl_iterations_per_timestep=rl_iterations_per_timestep,
        max_rl_iterations=max_rl_iterations,
        max_consecutive_no_action=max_consecutive_no_action,
        debug_training_cycle=False
    )
    
    return env

class DebugCallback(BaseCallback):
    """Callback for printing debug information during training"""
    def __init__(self, verbose=0):
        super().__init__(verbose)
        self.episode_count = 0
        self.episode_rewards = []
        self.episode_lengths = []
        self.episode_initial_elements = []
        self.episode_initial_levels = []
    
    def _on_step(self):
        # Check if episode completed
        if self.locals['dones'][0]:
            info = self.locals['infos'][0]
            reward = info.get('episode', {}).get('r', 0)
            length = info.get('episode_steps', 0)
            self.episode_count += 1
            self.episode_rewards.append(reward)
            self.episode_lengths.append(length)
            
            # Print episode info
            if self.verbose > 0 or self.episode_count % 10 == 0:
                print(f"\nEpisode {self.episode_count} completed:")
                print(f"  Reward: {reward:.2f}")
                print(f"  Length: {length}")
                print(f"  Mean Reward: {np.mean(self.episode_rewards[-100:]):.2f}")
        
        return True

def run_test(config_path, results_dir=None, verbose=True):
    """Run a short training test with the given configuration"""
    # Load configuration
    config = load_config(config_path)
    
    # Create timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Extract training parameters
    total_timesteps = get_parameter(config, "training.total_timesteps", 10000)
    algorithm = get_parameter(config, "training.algorithm", "A2C")
    learning_rate = get_parameter(config, "training.learning_rate", 0.0003)
    
    # Extract refinement settings
    refinement_mode = get_parameter(config, "environment.initial_refinement.mode", "none")
    refinement_level = get_parameter(config, "environment.initial_refinement.fixed_level", 0)
    refinement_probability = get_parameter(config, "environment.initial_refinement.probability", 0.5)
    
    # Create experiment name
    gamma_c = get_parameter(config, "environment.gamma_c", 25.0)
    experiment_name = f"test_gamma_c_{gamma_c}_refine_{refinement_mode}_level{refinement_level}"
    
    # Setup directories
    if results_dir is None:
        results_dir = os.path.join(PROJECT_ROOT, "experiments", "results")
    
    test_dir = os.path.join(results_dir, experiment_name)
    os.makedirs(test_dir, exist_ok=True)
    
    # Copy config for reference
    with open(os.path.join(test_dir, "config.yaml"), "w") as f:
        yaml.dump(config, f)
    
    # Create environment
    env = create_environment(config, verbose)
    
    # Add monitoring
    monitor_path = os.path.join(test_dir, "monitor.csv")
    env = Monitor(env, monitor_path)
    
    # Set up refinement options
    env.reset_kwargs = {
        'options': {
            'refinement_mode': refinement_mode,
            'refinement_level': refinement_level,
            'refinement_probability': refinement_probability
        }
    }
    
    # Print refinement settings
    if verbose:
        print(f"\nInitial Refinement Settings:")
        print(f"  Mode: {refinement_mode}")
        print(f"  Level: {refinement_level}")
        print(f"  Probability: {refinement_probability}")
    
    # Test initial reset to verify refinement
    obs, info = env.reset()
    
    # Display initial state
    if verbose:
        print("\nInitial State:")
        print(f"  Elements: {info.get('refinement_info', {}).get('initial_elements', 'unknown')}")
        print(f"  Resource usage: {info.get('refinement_info', {}).get('resource_usage', 0) * 100:.1f}%")
        
        # Get level distribution if available
        level_distribution = info.get('refinement_info', {}).get('level_distribution', {})
        if level_distribution:
            print(f"  Level distribution: {level_distribution}")
    
    # Create model
    if verbose:
        print(f"\nCreating {algorithm} model...")
    
    if algorithm.upper() == "A2C":
        model = A2C(
            "MultiInputPolicy",
            env,
            verbose=0,
            learning_rate=learning_rate
        )
    elif algorithm.upper() == "PPO":
        model = PPO(
            "MultiInputPolicy",
            env,
            verbose=0,
            learning_rate=learning_rate
        )
    else:
        raise ValueError(f"Unsupported algorithm: {algorithm}")
    
    # Create callback
    callback = DebugCallback(verbose=1)
    
    # Print settings
    if verbose:
        print(f"\nTraining for {total_timesteps} steps...")
    
    # Train model
    try:
        model.learn(
            total_timesteps=total_timesteps,
            callback=callback
        )
    except Exception as e:
        print(f"Error during training: {e}")
        raise
    
    # Save final model
    model_path = os.path.join(test_dir, "final_model.zip")
    model.save(model_path)
    
    print(f"\nTest completed. Results saved to {test_dir}")
    return test_dir, model

def main():
    parser = argparse.ArgumentParser(description="Test initial mesh refinement in training")
    parser.add_argument("--config", type=str, required=True, help="Path to config file")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    config_path = args.config
    verbose = args.verbose
    
    print(f"Testing with config: {config_path}")
    run_test(config_path, verbose=verbose)

if __name__ == "__main__":
    main()