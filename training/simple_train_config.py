"""
Training script for DG AMR reinforcement learning with YAML configuration.
"""

import os
import sys
import numpy as np
import gymnasium as gym
from stable_baselines3 import A2C, PPO, DQN
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.callbacks import BaseCallback
import matplotlib.pyplot as plt
from datetime import datetime

# Get absolute path to project root and add to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    '..'
))
sys.path.append(PROJECT_ROOT)

from numerical.solvers.dg_wave_solver_clean import DGWaveSolver
from numerical.environments.dg_amr_env_clean import DGAMREnv
from utils.config_loader import load_config, get_parameter


class TimestepLimitCallback(BaseCallback):
    """Callback for stopping training when total timesteps is reached."""
    
    def __init__(self, total_timesteps, verbose=0):
        super().__init__(verbose)
        self.total_timesteps = total_timesteps
        
    def _on_step(self) -> bool:
        # Print current step count periodically
        if self.n_calls % 10 == 0:  
            print(f"Current steps: {self.num_timesteps}/{self.total_timesteps}")
        
        # Check if we've exceeded total timesteps
        if self.num_timesteps >= self.total_timesteps:
            print(f"\nReached {self.total_timesteps} timesteps, stopping training")
            return False
        return True


def parse_args():
    """Parse command line arguments"""
    import argparse
    import os
    
    # Get the directory containing the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Build the path to the config file in the training/configs directory
    default_config_path = os.path.join(script_dir, "configs", "default_config.yaml")
    
    parser = argparse.ArgumentParser(description="Train AMR agent with configuration")
    parser.add_argument("--config", type=str, default=default_config_path, 
                        help="Path to configuration file")
    parser.add_argument("--gamma_c", type=float, 
                        help="Override gamma_c value")
    parser.add_argument("--element_budget", type=int, 
                        help="Override element budget")
    parser.add_argument("--total_timesteps", type=int, 
                        help="Override total timesteps")
    parser.add_argument("--algorithm", type=str, choices=["A2C", "PPO", "DQN"], 
                        help="Override RL algorithm")
    
    return parser.parse_args()


def train_amr_agent(config):
    """
    Train AMR agent with configuration.
    
    Args:
        config: Configuration dictionary loaded from YAML
    
    Returns:
        tuple: (model, env, config)
    """
    # Extract parameters with defaults
    element_budget = get_parameter(config, "environment.element_budget", 25)
    max_episode_steps = get_parameter(config, "environment.max_episode_steps", 100)
    gamma_c = get_parameter(config, "environment.gamma_c", 25.0)
    
    total_timesteps = get_parameter(config, "training.total_timesteps", 500)
    algorithm = get_parameter(config, "training.algorithm", "A2C")
    learning_rate = get_parameter(config, "training.learning_rate", 0.0003)
    n_steps = get_parameter(config, "training.n_steps", 5)
    ent_coef = get_parameter(config, "training.ent_coef", 0.01)
    
    nop = get_parameter(config, "solver.nop", 4)
    max_level = get_parameter(config, "solver.max_level", 4)
    courant_max = get_parameter(config, "solver.courant_max", 0.1)
    icase = get_parameter(config, "solver.icase", 1)
    initial_elements = get_parameter(config, "solver.initial_elements", np.array([-1, -0.4, 0, 0.4, 1]))
    verbose = get_parameter(config, "solver.verbose", False)
    
    # Create timestamp for this training run
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Create logs directory structure
    log_dir = os.path.join(PROJECT_ROOT, "logs", f"training_{timestamp}")
    os.makedirs(log_dir, exist_ok=True)
    print(f"Created log directory: {log_dir}")
    
    # Create tensorboard log directory
    tensorboard_log = os.path.join(PROJECT_ROOT, "tensorboard_logs")
    os.makedirs(tensorboard_log, exist_ok=True)
    print(f"TensorBoard log directory: {tensorboard_log}")
    
    # Initialize solver
    solver = DGWaveSolver(
        nop=nop,
        xelem=initial_elements,
        max_elements=element_budget * 2,  # Some buffer
        max_level=max_level,
        courant_max=courant_max,
        icase=icase,
        verbose=verbose
    )
    
    # Initialize environment
    env = DGAMREnv(
        solver=solver,
        element_budget=element_budget,
        gamma_c=gamma_c,
        max_episode_steps=max_episode_steps
    )
    
    # Add monitoring
    monitor_path = os.path.join(log_dir, "monitor.csv")
    print(f"Monitor log path: {monitor_path}")
    env = Monitor(env, monitor_path)
    
    # Initialize model based on algorithm
    if algorithm.upper() == "A2C":
        model = A2C(
            "MultiInputPolicy",
            env,
            verbose=1,
            learning_rate=learning_rate,
            n_steps=n_steps,
            ent_coef=ent_coef,
            tensorboard_log=tensorboard_log
        )
    elif algorithm.upper() == "PPO":
        model = PPO(
            "MultiInputPolicy",
            env,
            verbose=1,
            learning_rate=learning_rate,
            n_steps=n_steps,
            tensorboard_log=tensorboard_log
        )
    elif algorithm.upper() == "DQN":
        model = DQN(
            "MultiInputPolicy",
            env,
            verbose=1,
            learning_rate=learning_rate,
            tensorboard_log=tensorboard_log
        )
    else:
        raise ValueError(f"Unsupported algorithm: {algorithm}")
    
    # Create timestep limit callback
    timestep_limit_callback = TimestepLimitCallback(
        total_timesteps=total_timesteps,
        verbose=1
    )
    
    # Print training configuration
    print(f"\nModel parameters:")
    print(f"Algorithm: {algorithm}")
    print(f"Element budget: {element_budget}")
    print(f"Gamma_c: {gamma_c}")
    print(f"Learning rate: {learning_rate}")
    print(f"N steps: {n_steps}")
    print(f"Total timesteps requested: {total_timesteps}")
    
    try:
        # Train model
        model.learn(
            total_timesteps=total_timesteps,
            callback=timestep_limit_callback,
            tb_log_name=f"{algorithm}_run_{timestamp}"
        )
    except Exception as e:
        print(f"\nTraining error: {e}")
    finally:
        print(f"\nTraining completed or stopped.")
        
        # Save final model
        model_path = os.path.join(log_dir, "final_model.zip")
        model.save(model_path)
        print(f"Model saved to: {model_path}")
    
    return model, env, config


def evaluate_model(model, env, num_episodes=5):
    """
    Basic model evaluation.
    """
    print("\nStarting model evaluation...")
    rewards = []
    for episode in range(num_episodes):
        obs = env.reset()[0]
        done = False
        total_reward = 0
        
        while not done:
            action, _ = model.predict(obs, deterministic=True)
            obs, reward, done, truncated, info = env.step(action)
            total_reward += reward
            
            if truncated:
                break
                
        rewards.append(total_reward)
        print(f"Episode {episode + 1} reward: {total_reward:.2f}")
    
    print(f"\nMean reward: {np.mean(rewards):.2f}")
    print(f"Std reward: {np.std(rewards):.2f}")


if __name__ == "__main__":
    # Parse command line arguments
    args = parse_args()
    
    # Load config from file
    config = load_config(args.config)
    
    # Override with command line arguments if provided
    if args.gamma_c is not None:
        config["environment"]["gamma_c"] = args.gamma_c
    if args.element_budget is not None:
        config["environment"]["element_budget"] = args.element_budget
    if args.total_timesteps is not None:
        config["training"]["total_timesteps"] = args.total_timesteps
    if args.algorithm is not None:
        config["training"]["algorithm"] = args.algorithm
    
    # Train model using config
    model, env, config = train_amr_agent(config)
    
    # Create fresh environment for evaluation with same config
    # Note: We're using the trained model on the same environment for evaluation
    # This is sufficient for basic testing
    
    # Evaluate model
    evaluate_model(model, env)