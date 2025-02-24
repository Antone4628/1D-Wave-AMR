"""
Metrics calculation and tracking for DG AMR training.
"""

from typing import Dict, List, Any
import numpy as np
from stable_baselines3 import A2C

def calculate_episode_metrics(rewards: List[float], lengths: List[int]) -> Dict[str, float]:
    """Calculate metrics for a set of episodes."""
    return {
        "mean_reward": float(np.mean(rewards)),
        "std_reward": float(np.std(rewards)),
        "mean_length": float(np.mean(lengths)),
        "std_length": float(np.std(lengths))
    }

def evaluate_model(
    model: A2C,
    env,
    n_eval_episodes: int = 10
) -> Dict[str, float]:
    """Evaluate trained model performance."""
    episode_rewards = []
    episode_lengths = []
    
    for i in range(n_eval_episodes):
        obs = env.reset()
        done = False
        episode_reward = 0
        episode_length = 0
        
        while not done:
            action, _states = model.predict(obs, deterministic=True)
            obs, reward, done, info = env.step(action)
            episode_reward += reward
            episode_length += 1
            
        episode_rewards.append(episode_reward)
        episode_lengths.append(episode_length)
        
    return calculate_episode_metrics(episode_rewards, episode_lengths)

def calculate_mesh_metrics(env) -> Dict[str, Any]:
    """Calculate mesh-specific metrics."""
    return {
        "n_elements": len(env.solver.active),
        "resource_usage": len(env.solver.active) / env.element_budget,
        "mean_jump": float(np.mean([
            np.mean(env._get_element_jumps(i)[0]) 
            for i in range(len(env.solver.active))
        ]))
    }