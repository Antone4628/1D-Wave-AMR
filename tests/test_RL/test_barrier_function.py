"""
Test script to validate the barrier function and reward calculations
in the simplified DG AMR environment.
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Get absolute path to project root and add to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 
    '..',
    '..'
))
sys.path.append(PROJECT_ROOT)

from numerical.solvers.dg_wave_solver_clean import DGWaveSolver
from numerical.environments.dg_amr_env_clean import DGAMREnv, RewardCalculator

# Test barrier function directly
def test_barrier_function():
    """Test the barrier function and visualize its behavior."""
    reward_calc = RewardCalculator(gamma_c=25.0)
    
    p_values = np.linspace(0, 0.99, 100)
    barrier_values = [reward_calc.calculate_barrier(p) for p in p_values]

    plt.figure(figsize=(10, 6))
    plt.plot(p_values, barrier_values)
    plt.xlabel('Resource usage p')
    plt.ylabel('Barrier function B(p)')
    plt.title('Barrier Function: B(p) = √p/(1-p)')
    plt.grid(True)
    
    # Create output directory if it doesn't exist
    output_dir = os.path.join(PROJECT_ROOT, 'tests', 'outputs')
    os.makedirs(output_dir, exist_ok=True)
    
    # Save the plot
    plt.savefig(os.path.join(output_dir, 'barrier_function.png'))
    plt.close()
    
    print("Barrier function test complete. Plot saved to tests/outputs/barrier_function.png")
    
    # Show some example values
    print("\nBarrier function values at different resource usages:")
    for p in [0.1, 0.5, 0.7, 0.8, 0.9, 0.95, 0.99]:
        barrier = reward_calc.calculate_barrier(p)
        print(f"  p = {p:.2f}: B(p) = {barrier:.4f}")

# Test environment functionality
def test_environment_functionality():
    """Test the environment's reward calculation and step function."""
    # Initialize solver and environment
    solver = DGWaveSolver(
        nop=3,
        xelem=np.array([-1, -0.4, 0, 0.4, 1]),
        max_elements=50,
        max_level=3,
        courant_max=0.1,
        icase=1,
        verbose=False
    )

    # Create environment with different gamma_c values to test sensitivity
    gamma_values = [10.0, 25.0, 50.0, 100.0]
    
    for gamma_c in gamma_values:
        print(f"\n=== Testing environment with gamma_c = {gamma_c} ===")
        
        env = DGAMREnv(
            solver=solver,
            element_budget=25,
            gamma_c=gamma_c,
            max_episode_steps=20,
            verbose=False,
            debug_training_cycle=True,
            rl_iterations_per_timestep=5  # Fixed for testing
        )
        
        # Reset environment
        obs, info = env.reset()
        print(f"Initial state: {len(env.solver.active)}/{env.element_budget} elements")

        # Try different actions and check rewards
        actions = [2, 2, 1, 0]  # refine, refine, do nothing, coarsen
        action_names = {0: "coarsen", 1: "do nothing", 2: "refine"}

        for i, action in enumerate(actions):
            print(f"\nStep {i+1}: Taking action {action_names[action]}")
            
            # Store pre-action state
            pre_elements = len(env.solver.active)
            pre_resource = pre_elements / env.element_budget
            pre_barrier = env.reward_calculator.calculate_barrier(pre_resource)
            
            # Take action
            obs, reward, terminated, truncated, info = env.step(action)
            
            # Calculate components
            post_elements = len(env.solver.active)
            post_resource = post_elements / env.element_budget
            post_barrier = env.reward_calculator.calculate_barrier(post_resource)
            
            # Print results
            print(f"  Elements: {pre_elements} -> {post_elements}")
            print(f"  Resource usage: {pre_resource:.3f} -> {post_resource:.3f}")
            print(f"  Barrier value: {pre_barrier:.3f} -> {post_barrier:.3f}")
            print(f"  Delta barrier: {post_barrier - pre_barrier:.3f}")
            print(f"  Reward: {reward:.3f}")
            print(f"  Observation: avg_local_jump={obs['avg_local_jump'][0]:.5f}, avg_jump={obs['avg_jump'][0]:.5f}")
            
            if terminated or truncated:
                print("Episode ended early")
                break

def test_rewards_vs_resource_use():
    """Test how the reward function behaves with increasing resource usage."""
    # Set up a simple test case
    reward_calc = RewardCalculator(gamma_c=25.0)
    
    # Fixed delta_u for testing
    delta_u = 0.1
    
    # Test refine action across different resource usages
    p_values = np.linspace(0.1, 0.95, 20)
    refine_rewards = []
    coarsen_rewards = []
    
    for p in p_values:
        # Test refinement (resource usage increases by 0.05)
        new_p = p + 0.05
        if new_p > 1.0:
            new_p = 1.0
            
        refine_reward = reward_calc.calculate_reward(delta_u, 1, p, new_p)
        refine_rewards.append(refine_reward)
        
        # Test coarsening (resource usage decreases by 0.05)
        new_p_coarsen = max(0, p - 0.05)
        coarsen_reward = reward_calc.calculate_reward(delta_u, -1, p, new_p_coarsen)
        coarsen_rewards.append(coarsen_reward)
    
    # Create plot
    plt.figure(figsize=(10, 6))
    plt.plot(p_values, refine_rewards, 'b-', label='Refine action reward')
    plt.plot(p_values, coarsen_rewards, 'r-', label='Coarsen action reward')
    plt.xlabel('Current Resource Usage (p)')
    plt.ylabel('Reward')
    plt.title(f'Reward vs Resource Usage (delta_u={delta_u}, gamma_c=25)')
    plt.grid(True)
    plt.legend()
    
    # Create output directory if it doesn't exist
    output_dir = os.path.join(PROJECT_ROOT, 'tests', 'outputs')
    os.makedirs(output_dir, exist_ok=True)
    
    # Save the plot
    plt.savefig(os.path.join(output_dir, 'reward_vs_resource.png'))
    plt.close()
    
    print("\nReward vs resource usage test complete.")
    print("Plot saved to tests/outputs/reward_vs_resource.png")
    
    # Print some representative values
    print("\nExample rewards at different resource usages:")
    print(f"  {'p':>5} | {'Refine':>10} | {'Coarsen':>10}")
    print(f"  {'-'*5} | {'-'*10} | {'-'*10}")
    
    for i, p in enumerate([0.1, 0.3, 0.5, 0.7, 0.8, 0.9, 0.95]):
        idx = np.abs(p_values - p).argmin()  # Find closest value in p_values
        print(f"  {p:5.2f} | {refine_rewards[idx]:10.4f} | {coarsen_rewards[idx]:10.4f}")

if __name__ == "__main__":
    # Run tests
    test_barrier_function()
    test_rewards_vs_resource_use()
    test_environment_functionality()