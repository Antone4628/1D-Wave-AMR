# modified_test_training_cycle.py
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Get absolute path to project root and add to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    '..'
))
sys.path.append(PROJECT_ROOT)
from numerical.solvers.dg_wave_solver_clean import DGWaveSolver
from numerical.environments.dg_amr_env_clean import DGAMREnv, RewardCalculator

def test_barrier_function():
    """Test the barrier function directly and plot its curve."""
    print("\n" + "="*60)
    print("TESTING BARRIER FUNCTION B(p) = √p/(1-p)")
    print("="*60)
    
    reward_calc = RewardCalculator(gamma_c=25.0)
    
    # Generate points for plotting
    p_values = np.linspace(0.01, 0.99, 100)
    barrier_values = [reward_calc.calculate_barrier(p) for p in p_values]
    
    # Calculate barrier function values at key resource usage points
    key_points = [0.2, 0.4, 0.6, 0.8, 0.9, 0.95, 0.99]
    key_barriers = [reward_calc.calculate_barrier(p) for p in key_points]
    
    # Print values
    print("\nBarrier function values at different resource usages:")
    print(f"{'p':>6} | {'B(p)':>10}")
    print(f"{'-'*6} | {'-'*10}")
    for p, b in zip(key_points, key_barriers):
        print(f"{p:6.2f} | {b:10.4f}")
    
    # Calculate theoretical refinement rewards at different resource usages
    # assuming a constant Δu_h = 0.1
    delta_u_h = 0.1
    log_delta = np.log(delta_u_h + 1e-16) - np.log(1e-16)
    
    print("\nTheoretical refinement rewards at different resource usages (Δu_h=0.1):")
    print(f"{'p':>6} | {'B(p)':>10} | {'Reward':>10}")
    print(f"{'-'*6} | {'-'*10} | {'-'*10}")
    
    for p in key_points:
        next_p = min(0.99, p + 0.05)  # Simulate resource usage after refinement
        barrier_diff = reward_calc.calculate_barrier(next_p) - reward_calc.calculate_barrier(p)
        reward = log_delta - 25.0 * barrier_diff
        print(f"{p:6.2f} | {barrier_diff:10.4f} | {reward:10.4f}")
    
    # Create plot
    plt.figure(figsize=(10, 6))
    plt.plot(p_values, barrier_values)
    plt.xlabel('Resource Usage (p)')
    plt.ylabel('Barrier Function B(p) = √p/(1-p)')
    plt.title('Non-hortative Barrier Function')
    plt.grid(True)
    plt.xlim(0, 1)
    plt.axvline(x=0.8, color='r', linestyle='--', alpha=0.5, label='80% resources')
    plt.axvline(x=0.9, color='orange', linestyle='--', alpha=0.5, label='90% resources')
    
    # Create output directory
    output_dir = os.path.join(PROJECT_ROOT, 'experiments', 'results', 'barrier_test')
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, 'barrier_function.png'))
    
    # Create second plot showing reward implications
    plt.figure(figsize=(10, 6))
    
    # Calculate reward component from barrier function for refinement
    refine_costs = []
    for i in range(len(p_values)-1):
        p = p_values[i]
        next_p = p_values[i] + 0.01  # Small increment to simulate refinement
        if next_p >= 1.0:
            next_p = 0.99
        barrier_diff = reward_calc.calculate_barrier(next_p) - reward_calc.calculate_barrier(p)
        refine_costs.append(-25.0 * barrier_diff)  # Negative because it's a cost
    
    plt.plot(p_values[:-1], refine_costs)
    plt.axhline(y=log_delta, color='g', linestyle='--', 
                label=f'Accuracy reward for Δu_h={delta_u_h} (constant)')
    plt.xlabel('Resource Usage (p)')
    plt.ylabel('Reward Component')
    plt.title('Effect of Barrier Function on Refinement Reward')
    plt.grid(True)
    plt.legend()
    plt.savefig(os.path.join(output_dir, 'barrier_reward_effect.png'))
    
    print(f"\nBarrier function test complete. Plots saved to {output_dir}")
    return barrier_values

def test_refinement_behavior():
    """
    Test how the refinement behavior changes as resource usage increases.
    We'll use a simple policy of always refining and see how rewards change.
    """
    print("\n" + "="*60)
    print("TESTING REFINEMENT BEHAVIOR VS RESOURCE USAGE")
    print("="*60)
    
    # Initialize solver and environment
    solver = DGWaveSolver(
        nop=3,
        xelem=np.array([-1, -0.4, 0, 0.4, 1]),
        max_elements=50,  # Using a larger max_elements to see full barrier curve
        max_level=3,
        courant_max=0.1,
        icase=1,
        verbose=False
    )
    
    # Create environment with a tight budget to quickly reach high resource usage
    element_budget = 20
    gamma_c = 25.0
    
    env = DGAMREnv(
        solver=solver,
        element_budget=element_budget,
        gamma_c=gamma_c,
        max_episode_steps=100,
        verbose=False,
        rl_iterations_per_timestep=5,  # Fixed for this test
        max_rl_iterations=5,
        debug_training_cycle=True
    )
    
    # Results directory
    results_dir = os.path.join(PROJECT_ROOT, 'experiments', 'results', 'refinement_test')
    os.makedirs(results_dir, exist_ok=True)
    
    # Reset environment
    obs, info = env.reset()
    print(f"Initial state: {len(env.solver.active)}/{element_budget} elements")
    
    # Lists to store data
    steps = []
    resources = []
    barrier_values = []
    rewards = []
    delta_us = []
    action_history = []
    resource_costs = []
    accuracy_rewards = []
    
    # Helper to calculate components
    reward_calc = RewardCalculator(gamma_c=gamma_c)
    
    # Run with always-refine policy until we reach high resource usage
    for i in range(50):
        # Always choose refinement (action 2 maps to 1 which is refine)
        action = 2
        
        # Get pre-action state
        pre_resource = len(env.solver.active) / element_budget
        pre_barrier = reward_calc.calculate_barrier(pre_resource)
        
        # Take the action
        obs, reward, terminated, truncated, info = env.step(action)
        
        # Get post-action state
        post_resource = len(env.solver.active) / element_budget
        post_barrier = reward_calc.calculate_barrier(post_resource)
        barrier_diff = post_barrier - pre_barrier
        
        # Save data
        steps.append(i)
        resources.append(post_resource)
        barrier_values.append(post_barrier)
        rewards.append(reward)
        delta_us.append(info.get('delta_u', 0))
        resource_costs.append(-gamma_c * barrier_diff)
        
        # Approximate the accuracy reward component
        # (This is an approximation since we don't have direct access to the internal calculation)
        accuracy_rewards.append(reward + gamma_c * barrier_diff)
        
        # Save action taken (mapped value: 1 = refine)
        action_history.append(1)
        
        # Print periodic status
        if i % 5 == 0 or post_resource > 0.9:
            print(f"Step {i}: Elements={len(env.solver.active)}/{element_budget}, "
                  f"Resource={post_resource*100:.1f}%, Barrier={post_barrier:.3f}, "
                  f"Reward={reward:.3f}")
        
        if terminated or truncated:
            print(f"Episode ended after {i+1} steps. Reason: {info.get('reason', 'unknown')}")
            break
    
    # Create visualizations
    plt.figure(figsize=(12, 8))
    
    # Plot 1: Resources and barrier values
    plt.subplot(2, 1, 1)
    plt.plot(steps, np.array(resources) * 100, 'b-', label='Resource Usage (%)')
    plt.plot(steps, barrier_values, 'r--', label='Barrier Value B(p)')
    plt.xlabel('Steps')
    plt.ylabel('Value')
    plt.title('Resource Usage and Barrier Function Over Time')
    plt.grid(True)
    plt.legend()
    
    # Plot 2: Rewards
    plt.subplot(2, 1, 2)
    plt.plot(steps, rewards, 'g-', label='Total Reward')
    plt.plot(steps, resource_costs, 'r--', label='Resource Cost Component')
    plt.plot(steps, accuracy_rewards, 'b--', label='Accuracy Reward Component')
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.xlabel('Steps')
    plt.ylabel('Reward')
    plt.title('Reward Components vs Steps')
    plt.grid(True)
    plt.legend()
    
    plt.tight_layout()
    plt.savefig(os.path.join(results_dir, 'barrier_effect_over_time.png'))
    
    # Plot 3: Reward vs Resource Usage
    plt.figure(figsize=(10, 6))
    plt.plot(np.array(resources) * 100, rewards, 'o-', label='Total Reward')
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.xlabel('Resource Usage (%)')
    plt.ylabel('Reward')
    plt.title('Reward vs Resource Usage for Refinement Actions')
    plt.grid(True)
    
    # Find the crossover point where rewards become negative
    try:
        crossover_idx = next(i for i, r in enumerate(rewards) if r < 0)
        crossover_resource = resources[crossover_idx] * 100
        plt.axvline(x=crossover_resource, color='r', linestyle='--', 
                   label=f'Crossover at {crossover_resource:.1f}%')
        print(f"\nRefinement actions become disadvantageous at {crossover_resource:.1f}% resource usage")
    except (StopIteration, IndexError):
        print("\nNo crossover point found - refinement remained advantageous throughout the test")
    
    plt.legend()
    plt.savefig(os.path.join(results_dir, 'reward_vs_resource.png'))
    
    print(f"\nRefinement behavior test complete. Plots saved to {results_dir}")
    
    return resources, rewards, barrier_values

def test_rl_vs_solver_iterations():
    """
    Test how RL iterations relate to solver timesteps under different settings.
    This helps understand the training cycle and how often the physical solver is advanced.
    """
    print("\n" + "="*60)
    print("TESTING RL ITERATIONS VS SOLVER TIMESTEPS")
    print("="*60)
    
    # Initialize solver
    solver = DGWaveSolver(
        nop=3,
        xelem=np.array([-1, -0.4, 0, 0.4, 1]),
        max_elements=50,
        max_level=3,
        courant_max=0.1,
        icase=1,
        verbose=False
    )

    # Test configurations
    configs = [
        {"name": "Fixed (1)", "iterations": 1},
        {"name": "Fixed (3)", "iterations": 3},
        {"name": "Fixed (5)", "iterations": 5},
        {"name": "Random (1-5)", "iterations": "random", "max_iterations": 5}
    ]
    
    results_dir = os.path.join(PROJECT_ROOT, 'experiments', 'results', 'iterations_test')
    os.makedirs(results_dir, exist_ok=True)
    
    # Store results
    all_results = {}
    
    for config in configs:
        print(f"\nTesting with {config['name']} RL iterations per timestep")
        
        env = DGAMREnv(
            solver=solver,
            element_budget=25,
            gamma_c=25.0,
            max_episode_steps=50,
            verbose=False,
            rl_iterations_per_timestep=config["iterations"],
            max_rl_iterations=config.get("max_iterations", 5),
            debug_training_cycle=True
        )
        
        # Reset environment
        obs, info = env.reset()
        print(f"Initial state: {len(env.solver.active)} elements")
        
        # Data collection
        rl_steps = 0
        time_steps = 0
        time_step_history = []
        rl_step_history = []
        element_history = []
        
        # Run with a simple policy (cycle through actions)
        for i in range(50):
            # Cycle through different actions
            action = i % 3  # 0=coarsen, 1=no change, 2=refine
            
            # Take step
            obs, reward, terminated, truncated, info = env.step(action)
            rl_steps += 1
            
            # Track history
            rl_step_history.append(rl_steps)
            element_history.append(len(env.solver.active))
            
            # Record if timestep was taken
            if info.get('took_timestep', False):
                time_steps += 1
                time_step_history.append(rl_steps)
                print(f"Timestep {time_steps} after {rl_steps} RL iterations")
            
            if terminated or truncated:
                print(f"Episode ended after {i+1} steps. Reason: {info.get('reason', 'unknown')}")
                break
        
        # Calculate statistics
        avg_ratio = rl_steps / max(1, time_steps)
        
        # Store results
        all_results[config["name"]] = {
            'rl_steps': rl_steps,
            'time_steps': time_steps,
            'avg_ratio': avg_ratio,
            'time_step_history': time_step_history,
            'rl_step_history': rl_step_history,
            'element_history': element_history
        }
        
        # Print summary
        print(f"Summary for {config['name']}:")
        print(f"Total RL iterations: {rl_steps}")
        print(f"Physical time steps: {time_steps}")
        print(f"Average ratio: {avg_ratio:.2f} RL iterations per time step")
    
    # Create comparison visualization
    plt.figure(figsize=(10, 6))
    names = list(all_results.keys())
    ratios = [all_results[name]['avg_ratio'] for name in names]
    
    plt.bar(names, ratios)
    plt.xlabel('RL Iterations Setting')
    plt.ylabel('RL Iterations per Solver Timestep')
    plt.title('Efficiency of Different RL Iteration Settings')
    plt.grid(True, axis='y')
    plt.savefig(os.path.join(results_dir, 'iteration_ratios.png'))
    
    # Create detailed timeline visualization for random case
    if "Random (1-5)" in all_results:
        random_data = all_results["Random (1-5)"]
        plt.figure(figsize=(12, 8))
        
        # Timeline of RL steps with timestep markers
        plt.subplot(2, 1, 1)
        plt.plot(random_data['rl_step_history'], np.ones_like(random_data['rl_step_history']), 'bo', alpha=0.3, markersize=5)
        for ts in random_data['time_step_history']:
            plt.axvline(x=ts, color='r', linestyle='--', alpha=0.5)
        plt.xlabel('RL Step')
        plt.yticks([])
        plt.title('Timeline of RL Steps with Timestep Markers')
        
        # Element count over time
        plt.subplot(2, 1, 2)
        plt.plot(random_data['rl_step_history'], random_data['element_history'], 'g-')
        for ts in random_data['time_step_history']:
            plt.axvline(x=ts, color='r', linestyle='--', alpha=0.5)
        plt.xlabel('RL Step')
        plt.ylabel('Element Count')
        plt.title('Element Count vs RL Steps')
        
        plt.tight_layout()
        plt.savefig(os.path.join(results_dir, 'random_timeline.png'))
    
    print(f"\nRL vs Solver iterations test complete. Results saved to {results_dir}")
    
    return all_results

def main():
    """Run all tests."""
    # Test the barrier function directly
    barrier_values = test_barrier_function()
    
    # Test refinement behavior as resource usage increases
    resources, rewards, barriers = test_refinement_behavior()
    
    # Test RL iterations vs solver timesteps
    iteration_results = test_rl_vs_solver_iterations()
    
    print("\nAll tests complete.")

if __name__ == "__main__":
    main()