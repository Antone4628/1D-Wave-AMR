#!/usr/bin/env python
"""
Script to run multiple AMR reinforcement learning experiments with different gamma_c values.
"""

import os
import sys
import yaml
import argparse
import datetime
import shutil
from pathlib import Path

# Get absolute path to project root and add to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    '..'
))
sys.path.append(PROJECT_ROOT)

# from numerical.solvers.dg_wave_solver_clean import DGWaveSolver
from numerical.solvers.dg_wave_solver_options import DGWaveSolver
from numerical.environments.dg_amr_env_clean import DGAMREnv
# from numerical.environments.dg_amr_env_clean import DGAMREnv
from stable_baselines3 import A2C, PPO, DQN
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.callbacks import BaseCallback, EvalCallback
import numpy as np
import matplotlib.pyplot as plt
from numerical.callbacks.enhanced_callback_options import EnhancedMonitorCallback



# class ExperimentCallback(BaseCallback):
#     """
#     Custom callback for logging and saving experiment progress.
#     """
#     def __init__(self, total_timesteps, log_dir, save_freq=10000, verbose=1):
#         super().__init__(verbose)
#         self.total_timesteps = total_timesteps
#         self.log_dir = log_dir
#         self.save_freq = save_freq
#         self.best_mean_reward = -float('inf')
        
#     def _on_step(self) -> bool:
#         # Print current progress periodically
#         if self.n_calls % 100 == 0:  
#             print(f"Progress: {self.num_timesteps}/{self.total_timesteps} steps ({self.num_timesteps/self.total_timesteps*100:.1f}%)")
        
#         # Save model periodically
#         if self.num_timesteps % self.save_freq == 0:
#             model_path = os.path.join(self.log_dir, f"model_{self.num_timesteps}_steps")
#             self.model.save(model_path)
#             if self.verbose > 0:
#                 print(f"Saved model at {model_path}")
        
#         # Check if we've exceeded total timesteps
#         if self.num_timesteps >= self.total_timesteps:
#             if self.verbose > 0:
#                 print(f"Reached {self.total_timesteps} timesteps, stopping training")
#             return False
        
#         # Track new metrics if available in info
#         if 'took_timestep' in self.locals['infos'][0]:
#             self.logger.record('time_step/took_timestep', 
#                               float(self.locals['infos'][0].get('took_timestep', False)))
        
        
#         return True


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


def run_experiment(config_path, results_dir=None):
    """Run a single experiment with the given configuration"""
    # Load configuration
    config = load_config(config_path)
    
    # Create timestamp for this training run
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Extract key parameters with defaults
    gamma_c = get_parameter(config, "environment.gamma_c", 25.0)
    element_budget = get_parameter(config, "environment.element_budget", 25)
    max_episode_steps = get_parameter(config, "environment.max_episode_steps", 200)
    
    total_timesteps = get_parameter(config, "training.total_timesteps", 100000)
    algorithm = get_parameter(config, "training.algorithm", "A2C")
    learning_rate = get_parameter(config, "training.learning_rate", 0.0003)
    n_steps = get_parameter(config, "training.n_steps", 5)
    ent_coef = get_parameter(config, "training.ent_coef", 0.01)
    
    nop = get_parameter(config, "solver.nop", 4)
    max_level = get_parameter(config, "solver.max_level", 4)
    courant_max = get_parameter(config, "solver.courant_max", 0.1)
    icase = get_parameter(config, "solver.icase", 1)
    balance = get_parameter(config, "solver.balance", True)  




    initial_elements = get_parameter(config, "solver.initial_elements", np.array([-1, -0.4, 0, 0.4, 1]))



    
    verbose = get_parameter(config, "solver.verbose", False)
    

    # Add new parameters to config or provide defaults
    rl_iterations_per_timestep = get_parameter(config, "environment.rl_iterations_per_timestep", "random")
    max_rl_iterations = get_parameter(config, "environment.max_rl_iterations", 200)
    max_consecutive_no_action = get_parameter(config, "environment.max_consecutive_no_action", 10)


    
    # Create experiment name
    experiment_name = f"gamma_c_{gamma_c}"
    
    # Create directories
    if results_dir is None:
        results_dir = os.path.join(PROJECT_ROOT, "experiments", "results")
    
    experiment_dir = os.path.join(results_dir, experiment_name)
    os.makedirs(experiment_dir, exist_ok=True)
    
    # Create subdirectories
    log_dir = os.path.join(experiment_dir, f"run_{timestamp}")
    model_dir = os.path.join(log_dir, "models")
    tensorboard_dir = os.path.join(log_dir, "tensorboard")
    
    os.makedirs(log_dir, exist_ok=True)
    os.makedirs(model_dir, exist_ok=True)
    os.makedirs(tensorboard_dir, exist_ok=True)
    
    # Copy config file for reproducibility
    shutil.copy(config_path, os.path.join(log_dir, "config.yaml"))
    
    # Print experiment info
    print(f"\n{'='*50}")
    print(f"Starting experiment: {experiment_name}")
    print(f"Timestamp: {timestamp}")
    print(f"Log directory: {log_dir}")
    print(f"{'='*50}\n")
    
    # Initialize solver
    print("Initializing DG Wave Solver...")
    solver = DGWaveSolver(
        nop=nop,
        xelem=initial_elements,
        max_elements=element_budget * 2,  # Buffer for exploration
        max_level=max_level,
        courant_max=courant_max,
        icase=icase,
        verbose=verbose,
        balance = balance
    )

    
    # Initialize environment
    print("Setting up environment...")
    env = DGAMREnv(
        solver=solver,
        element_budget=element_budget,
        gamma_c=gamma_c,
        max_episode_steps=max_episode_steps,
        verbose = False,
        rl_iterations_per_timestep = "random",  # Use random number of iterations before time-stepping
        max_rl_iterations=30,  # Maximum number of RL iterations before time-stepping
        max_consecutive_no_action=max_consecutive_no_action,  # Add this parameter
        debug_training_cycle = False
    )
    
    # Add monitoring
    monitor_path = os.path.join(log_dir, "monitor.csv")
    env = Monitor(env, monitor_path)

    # Extract refinement options from config
    refinement_mode = get_parameter(config, "environment.initial_refinement.mode", "none")
    refinement_level = get_parameter(config, "environment.initial_refinement.fixed_level", 0)
    refinement_max_level = get_parameter(config, "environment.initial_refinement.max_Initial_level", 3)
    refinement_probability = get_parameter(config, "environment.initial_refinement.probability", 0.5)

    # Add reset kwargs to env.reset call in the monitor wrapper
    env.reset_kwargs = {
        'options': {
            'refinement_mode': refinement_mode,
            'refinement_level': refinement_level,
            'refinement_probability': refinement_probability
        }
    }
    
    # Initialize model based on algorithm
    print(f"Creating {algorithm} model...")
    if algorithm.upper() == "A2C":
        model = A2C(
            "MultiInputPolicy",
            env,
            verbose=0,
            learning_rate=learning_rate,
            n_steps=n_steps,
            ent_coef=ent_coef,
            tensorboard_log=tensorboard_dir
        )
    elif algorithm.upper() == "PPO":
        model = PPO(
            "MultiInputPolicy",
            env,
            verbose=1,
            learning_rate=learning_rate,
            n_steps=n_steps,
            tensorboard_log=tensorboard_dir
        )
    elif algorithm.upper() == "DQN":
        model = DQN(
            "MultiInputPolicy",
            env,
            verbose=1,
            learning_rate=learning_rate,
            tensorboard_log=tensorboard_dir
        )
    else:
        raise ValueError(f"Unsupported algorithm: {algorithm}")
    
    # Create callback
    # callback = ExperimentCallback(
    #     total_timesteps=total_timesteps,
    #     log_dir=model_dir,
    #     save_freq=total_timesteps // 10  # Save 10 times during training
    # )
    # Create callback
    callback = EnhancedMonitorCallback(
        total_timesteps=total_timesteps,
        log_dir=log_dir,
        save_freq=total_timesteps // 10,  # Save 10 times during training
        window_size=100,  # Size of sliding window for metrics
        log_freq=1000     # Log statistics every 1000 steps
    )
    
    # Print training configuration
    print(f"\nTraining configuration:")
    print(f"Algorithm: {algorithm}")
    print(f"Element budget: {element_budget}")
    print(f"Gamma_c: {gamma_c}")
    print(f'Initial Refinement Configuration:')
    print(f' -mode: {refinement_mode}')
    print(f' -initial refinement level: {refinement_level}')
    print(f' -refinement probability: {refinement_probability}')
    print(f'2:1 balance enforced: {balance}')
    print(f"Learning rate: {learning_rate}")
    print(f"N steps: {n_steps}")
    print(f"Total timesteps: {total_timesteps}")
    
    try:
        # Train model
        print("\nStarting training...")
        model.learn(
            total_timesteps=total_timesteps,
            callback=callback,
            tb_log_name=experiment_name
        )
    except Exception as e:
        print(f"\nTraining error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print(f"\nTraining completed or stopped.")
        
        # Save final model
        final_model_path = os.path.join(model_dir, "final_model.zip")
        model.save(final_model_path)
        print(f"Final model saved to: {final_model_path}")
    
    # Basic evaluation
    print("\nRunning basic evaluation...")
    evaluate_model(model, env, num_episodes=5, log_dir=log_dir)
    
    return log_dir, model


def evaluate_model(model, env, num_episodes=5, log_dir=None):
    """Basic model evaluation."""
    rewards = []
    episode_lengths = []
    # Track time step related metrics
    total_rl_iterations = 0
    total_time_steps = 0
    
    for episode in range(num_episodes):
        obs = env.reset()[0]
        done = False
        total_reward = 0
        steps = 0
        
        while not done:
            action, _ = model.predict(obs, deterministic=True)
            obs, reward, done, truncated, info = env.step(action)
            total_reward += reward
            steps += 1
            
            if truncated:
                break
                       # Track time steps
            if info.get('took_timestep', False):
                total_time_steps += 1
            total_rl_iterations += 1

                
        rewards.append(total_reward)
        episode_lengths.append(steps)
        print(f"Episode {episode + 1}: reward={total_reward:.2f}, length={steps}")

    avg_rl_per_time = total_rl_iterations / max(1, total_time_steps)
    print(f"Average RL iterations per time step: {avg_rl_per_time:.2f}")
    
    print(f"\nEvaluation results:")
    print(f"Mean reward: {np.mean(rewards):.2f} ± {np.std(rewards):.2f}")
    print(f"Mean episode length: {np.mean(episode_lengths):.1f} ± {np.std(episode_lengths):.1f}")
    
    # Save evaluation results
    if log_dir:
        with open(os.path.join(log_dir, "evaluation.txt"), "w") as f:
            f.write(f"Average RL iterations per time step: {avg_rl_per_time:.2f}\n")
            f.write(f"Evaluation over {num_episodes} episodes:\n")
            f.write(f"Mean reward: {np.mean(rewards):.2f} ± {np.std(rewards):.2f}\n")
            f.write(f"Mean episode length: {np.mean(episode_lengths):.1f} ± {np.std(episode_lengths):.1f}\n\n")
            
            for i, (r, l) in enumerate(zip(rewards, episode_lengths)):
                f.write(f"Episode {i+1}: reward={r:.2f}, length={l}\n")
    
    return np.mean(rewards), np.std(rewards)


def run_all_experiments(config_dir=None, results_dir=None):
    """Run experiments for all config files"""
    if config_dir is None:
        config_dir = os.path.join(PROJECT_ROOT, "experiments", "configs")
    
    if results_dir is None:
        results_dir = os.path.join(PROJECT_ROOT, "experiments", "results")
    
    # Get all yaml files in config directory
    config_files = [f for f in os.listdir(config_dir) if f.endswith('.yaml')]
    config_files.sort()  # Ensure consistent order
    
    print(f"Found {len(config_files)} configuration files")
    
    results = {}
    
    for config_file in config_files:
        config_path = os.path.join(config_dir, config_file)
        print(f"\nProcessing configuration: {config_file}")
        
        try:
            log_dir, model = run_experiment(config_path, results_dir)
            results[config_file] = {
                'log_dir': log_dir,
                'success': True
            }
        except Exception as e:
            print(f"Error running experiment with {config_file}: {e}")
            results[config_file] = {
                'success': False,
                'error': str(e)
            }
    
    # Save summary
    summary_path = os.path.join(results_dir, f"summary_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    with open(summary_path, "w") as f:
        f.write("Experiment Summary\n")
        f.write("=================\n\n")
        
        for config_file, result in results.items():
            f.write(f"Configuration: {config_file}\n")
            f.write(f"Success: {result['success']}\n")
            
            if result['success']:
                f.write(f"Log directory: {result['log_dir']}\n")
            else:
                f.write(f"Error: {result['error']}\n")
            
            f.write("\n")
    
    print(f"\nExperiment summary written to: {summary_path}")
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run AMR reinforcement learning experiments")
    parser.add_argument("--config", type=str, help="Path to single config file")
    parser.add_argument("--all", action="store_true", help="Run all experiments in config directory")
    parser.add_argument("--config-dir", type=str, help="Path to config directory")
    parser.add_argument("--results-dir", type=str, help="Path to results directory")
    
    args = parser.parse_args()
    
    if args.all:
        run_all_experiments(args.config_dir, args.results_dir)
    elif args.config:
        run_experiment(args.config, args.results_dir)
    else:
        parser.print_help()