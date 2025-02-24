"""
Trainer class for DG AMR reinforcement learning.
"""

import os
import sys
import yaml
from datetime import datetime
import torch
from torch import nn
import csv
import json
import time
from stable_baselines3.common.monitor import Monitor
from typing import Tuple, Dict, Any, Optional, List

from stable_baselines3 import A2C
from stable_baselines3.common.monitor import Monitor


PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 
    # '.',
    '.'
))
sys.path.append(PROJECT_ROOT)

from training.utils.logger import TrainingLogger
from training.callback import CheckpointCallback, MetricsCallback

def get_activation_fn(activation_str: str):
    """Convert activation function string to actual function."""
    if activation_str == "torch.nn.Tanh":
        return nn.Tanh
    elif activation_str == "torch.nn.ReLU":
        return nn.ReLU
    elif activation_str == "torch.nn.LeakyReLU":
        return nn.LeakyReLU
    else:
        raise ValueError(f"Unsupported activation function: {activation_str}")

class TrainingConfig:
    """Configuration management for training."""
    
    def __init__(self, config_path: str):
        """Load config from YAML file."""
        with open(config_path) as f:
            self.config = yaml.safe_load(f)
            
        # Validate and set defaults
        self._validate_config()
        self._set_defaults()
        
    def _validate_config(self):
        """Validate required config parameters."""
        required = ['algorithm', 'total_timesteps', 'learning_rate', 'n_steps']
        for param in required:
            if param not in self.config:
                raise ValueError(f"Missing required config parameter: {param}")
                
    def _set_defaults(self):
        """Set default values for optional parameters."""
        defaults = {
            'gamma': 0.99,
            'verbose': 1,
            'tensorboard_log': "./logs/tensorboard/",
            'device': 'auto',
            'policy_kwargs': {
                'net_arch': {
                    'pi': [64, 64],
                    'vf': [64, 64]
                },
                'activation_fn': 'torch.nn.Tanh'
            }
        }
        for key, value in defaults.items():
            if key not in self.config:
                self.config[key] = value
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get value from config with optional default."""
        return self.config.get(key, default)
                
    def __getitem__(self, key: str) -> Any:
        """Get value from config."""
        return self.config[key]
    
    def save(self, path: str):
        """Save config to file."""
        with open(path, 'w') as f:
            yaml.dump(self.config, f)


class EnhancedMonitor(Monitor):
    """Enhanced monitoring wrapper for tracking detailed training metrics."""
    
    def __init__(
        self,
        env,
        filename: str,
        info_keywords: Tuple[str, ...] = ('resource_usage',),
        allow_early_resets: bool = True
    ):
        super().__init__(env, filename, info_keywords, allow_early_resets)
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        # Initialize CSV file with headers
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(("r", "l", "t") + tuple(self.info_keywords))
    
    def step(self, action) -> Tuple[Any, float, bool, Dict[str, Any]]:
        """
        Step the environment with enhanced monitoring.
        
        Returns:
            observation, reward, done, info
        """
        observation, reward, done, info = self.env.step(action)
        self.rewards.append(reward)
        
        if done:
            ep_rew = sum(self.rewards)
            ep_len = len(self.rewards)
            ep_info = {
                "r": round(ep_rew, 6),
                "l": ep_len,
                "t": round(time.time() - self.t_start, 6)
            }
            
            # Add custom info metrics
            for key in self.info_keywords:
                if key in info:
                    ep_info[key] = info[key]
                else:
                    # Compute metrics if not in info
                    if key == "resource_usage":
                        ep_info[key] = len(self.env.solver.active) / self.env.element_budget
                    elif key == "mean_reward":
                        ep_info[key] = ep_rew / ep_len if ep_len > 0 else 0
            
            self.episode_returns.append(ep_info)
            
            # Write to CSV
            with open(self.filename, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(
                    [ep_info["r"], ep_info["l"], ep_info["t"]] +
                    [ep_info.get(k, 0) for k in self.info_keywords]
                )
            
            # Reset episode-specific metrics
            self.rewards = []
            self.needs_reset = True
            
        return observation, reward, done, info

    def reset(self, **kwargs) -> Any:
        """
        Reset the environment with monitoring wrapper.
        """
        self.rewards = []
        self.needs_reset = False
        self.t_start = time.time()
        return self.env.reset(**kwargs)

class DGAMRTrainer:
    """Main training orchestration class."""
    
    def __init__(
        self,
        env,
        config_path: str,
        log_dir: Optional[str] = None,
        checkpoint_freq: int = 10000
    ):
        """
        Initialize trainer.
        
        Args:
            env: Gymnasium environment
            config_path: Path to training config file
            log_dir: Directory for logs and checkpoints
            checkpoint_freq: How often to save model checkpoints
        """
        self.config = TrainingConfig(config_path)
        
        # Set up logging
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_dir = log_dir or f"./logs/training_{timestamp}"
        self.logger = TrainingLogger(self.log_dir)

        # self.env = Monitor(
        #     env, 
        #     filename=os.path.join(self.log_dir, 'monitor.csv'),
        #     info_keywords=('resource_usage',)  # Track resource usage in logs
        # )
        self.env = EnhancedMonitor(
                env,
                filename=os.path.join(log_dir, 'monitor.csv'),
                info_keywords=('resource_usage', 'mean_reward')
            )
        
        
        # # Set up logging
        # timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # self.log_dir = log_dir or f"./logs/training_{timestamp}"
        # self.logger = TrainingLogger(self.log_dir)
        
        # Save config
        os.makedirs(self.log_dir, exist_ok=True)
        self.config.save(os.path.join(self.log_dir, 'config.yaml'))
        self.logger.log_config(self.config.config)
        
        # Set up model
        self.model = self._create_model()
        
        # Set up callbacks
        self.callbacks = [
            CheckpointCallback(
                save_freq=checkpoint_freq,
                save_path=os.path.join(self.log_dir, "checkpoints"),
                training_logger=self.logger,  # Changed from logger to training_logger
                verbose=self.config['verbose']
            ),
            MetricsCallback(
                training_logger=self.logger,  # Changed here too
                log_freq=self.config.get('log_interval', 100)
            )
        ]
        
    def _create_model(self):
        """Create RL model based on config."""
        if self.config['algorithm'].upper() != 'A2C':
            raise ValueError(f"Unsupported algorithm: {self.config['algorithm']}")
        
        # Get policy kwargs and convert activation function
        policy_kwargs = self.config.get('policy_kwargs', {}).copy()
        if 'activation_fn' in policy_kwargs:
            policy_kwargs['activation_fn'] = get_activation_fn(policy_kwargs['activation_fn'])
            
        return A2C(
            "MultiInputPolicy",
            self.env,
            learning_rate=self.config['learning_rate'],
            n_steps=self.config['n_steps'],
            gamma=self.config['gamma'],
            verbose=self.config['verbose'],
            tensorboard_log=self.config['tensorboard_log'],
            device=self.config['device'],
            policy_kwargs=policy_kwargs
        )
        
    def train(self):
        """Run training loop."""
        self.logger.logger.info("Starting training...")
        
        try:
            self.model.learn(
                total_timesteps=self.config['total_timesteps'],
                callback=self.callbacks
            )
            
            # Save final model
            final_model_path = os.path.join(self.log_dir, "final_model.zip")
            self.model.save(final_model_path)
            self.logger.logger.info(f"Saved final model to {final_model_path}")
            
        except Exception as e:
            self.logger.logger.error(f"Training failed: {str(e)}")
            raise
            
        self.logger.logger.info("Training completed")
        
    def save(self, path: str):
        """Save current model state."""
        self.model.save(path)
        
    def load(self, path: str):
        """Load model state."""
        self.model = A2C.load(path, env=self.env)
        
    def evaluate(self, n_episodes: int = 10):
        """
        Evaluate current model.
        
        Args:
            n_episodes: Number of episodes to evaluate
            
        Returns:
            dict: Evaluation metrics
        """
        episode_rewards = []
        episode_lengths = []
        
        for i in range(n_episodes):
            obs = self.env.reset()
            done = False
            episode_reward = 0
            episode_length = 0
            
            while not done:
                action, _states = self.model.predict(obs, deterministic=True)
                obs, reward, done, info = self.env.step(action)
                episode_reward += reward
                episode_length += 1
                
            episode_rewards.append(episode_reward)
            episode_lengths.append(episode_length)
            
        return {
            "mean_reward": float(np.mean(episode_rewards)),
            "std_reward": float(np.std(episode_rewards)),
            "mean_length": float(np.mean(episode_lengths))
        }