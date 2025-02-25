"""
Simplified training script for DG AMR reinforcement learning.
"""

import os
import sys
import numpy as np
import gymnasium as gym
from stable_baselines3 import A2C
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

from numerical.solvers.dg_wave_solver import DGWaveSolver
from numerical.environments.dg_amr_env import DGAMREnv



class TimestepLimitCallback(BaseCallback):
    """Callback for stopping training when total timesteps is reached."""
    
    def __init__(self, total_timesteps, verbose=0):
        super().__init__(verbose)
        self.total_timesteps = total_timesteps
        
    def _on_step(self) -> bool:
        # Check if we've exceeded total timesteps
        if self.num_timesteps >= self.total_timesteps:
            print(f"\nReached {self.total_timesteps} timesteps, stopping training")
            return False
        return True
    

def train_amr_agent(total_timesteps=5000, element_budget=25):
    """
    Train AMR agent with simplified setup and TensorBoard logging.
    """
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
    
    # Initialize solver and environment
    xelem = np.array([-1, -0.4, 0, 0.4, 1])
    solver = DGWaveSolver(
        nop=4,
        xelem=xelem, 
        max_elements=40,
        max_level=4,
        courant_max=0.1,
        icase=1
    )
    
    env = DGAMREnv(
        solver=solver,
        element_budget=element_budget,
        gamma_c=25.0
    )
    
    # Add monitoring
    monitor_path = os.path.join(log_dir, "monitor.csv")
    print(f"Monitor log path: {monitor_path}")
    env = Monitor(env, monitor_path)
    
    # Create callbacks - keep only the essential TimestepLimitCallback
    timestep_limit_callback = TimestepLimitCallback(
        total_timesteps=total_timesteps,
        verbose=1
    )
    
    # Initialize model with TensorBoard logging
    model = A2C(
        "MultiInputPolicy",
        env,
        verbose=1,
        learning_rate=0.0003,
        n_steps=5,
        ent_coef=0.01,
        tensorboard_log=tensorboard_log  # Add this line
    )
    
    print(f"\nModel parameters:")
    print(f"Learning rate: {model.learning_rate}")
    print(f"N steps: {model.n_steps}")
    print(f"Total timesteps requested: {total_timesteps}")
    
    try:
        # Train model with TensorBoard logging
        model.learn(
            total_timesteps=total_timesteps,
            callback=timestep_limit_callback,
            tb_log_name=f"A2C_run_{timestamp}"  # Add this line
        )
    except Exception as e:
        print(f"\nTraining error: {e}")
    finally:
        print(f"\nTraining completed or stopped.")
        
        # Save final model
        model_path = os.path.join(log_dir, "final_model.zip")
        model.save(model_path)
        print(f"Model saved to: {model_path}")
    
    return model, timestep_limit_callback

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
    # Train model
    # model, training_callback, timestep_callback = train_amr_agent()
    model, timestep_callback = train_amr_agent()
    # model, timestep_callback = train_amr_agent(total_timesteps=500)
    
    # Create fresh environment for evaluation
    xelem = np.array([-1, -0.4, 0, 0.4, 1])
    solver = DGWaveSolver(
        nop=4,
        xelem=xelem,
        max_elements=40,
        max_level=4,
        courant_max=0.1,
        icase=1
    )
    
    eval_env = DGAMREnv(
        solver=solver,
        element_budget=25,
        gamma_c=25.0
    )
    
    # Evaluate model
    evaluate_model(model, eval_env)


