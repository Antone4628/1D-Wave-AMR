#!/usr/bin/env python
"""
Test script for validating the new RL-AMR approach with DGWaveSolverMixed.
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Get path to project root
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    '..'
))
sys.path.append(PROJECT_ROOT)

from numerical.solvers.dg_wave_solver_mixed_clean import DGWaveSolverMixed
from numerical.environments.dg_amr_env_mixed import DGAMREnv
from stable_baselines3 import A2C

def test_steady_solve():
    """Test the steady-state solver functionality."""
    # Initialize solver
    xelem = np.array([-1, -0.4, 0, 0.4, 1])
    solver = DGWaveSolverMixed(
        nop=4,
        xelem=xelem,
        max_elements=50,
        max_level=4,
        courant_max=0.1,
        icase=1,
        verbose=True,
        balance=False
    )
    
    # Initialize with some refinement
    solver.initialize_with_refinement(refinement_mode='fixed', refinement_level=1)
    
    # Solve for steady-state
    q_steady = solver.steady_solve()
    
    # Get exact solution for comparison
    q_exact = solver.get_exact_solution()
    
    # Plot results
    plt.figure(figsize=(12, 6))
    plt.plot(solver.coord, q_steady, 'bo-', label='Steady Solution')
    plt.plot(solver.coord, q_exact, 'r-', label='Exact Solution')
    plt.grid(True)
    plt.legend()
    plt.title('Steady-State Solution Test')
    plt.savefig('steady_solution_test.png')
    
    return solver, q_steady, q_exact

def test_wave_advancement():
    """Test the wave advancement by 1/8 of the domain."""
    # Initialize solver
    xelem = np.array([-1, -0.4, 0, 0.4, 1])
    solver = DGWaveSolverMixed(
        nop=4,
        xelem=xelem,
        max_elements=50,
        max_level=4,
        courant_max=0.1,
        icase=1,
        verbose=True,
        balance=False
    )
    
    # Initialize with some refinement
    solver.initialize_with_refinement(refinement_mode='fixed', refinement_level=2)
    
    # Store initial solution
    q_initial = solver.q.copy()
    
    # Calculate steps to advance by 1/8 of domain
    domain_fraction = 1.0/8.0
    total_domain = 2.0
    distance_to_travel = domain_fraction * total_domain
    time_to_travel = distance_to_travel / solver.wave_speed
    n_steps = max(1, int(np.ceil(time_to_travel / solver.dt)))
    
    # Take steps
    for _ in range(n_steps):
        solver.step()
    
    # Store advanced solution
    q_advanced = solver.q.copy()
    
    # Plot results
    plt.figure(figsize=(12, 6))
    plt.plot(solver.coord, q_initial, 'bo-', label='Initial Solution')
    plt.plot(solver.coord, q_advanced, 'ro-', label=f'Advanced Solution ({n_steps} steps)')
    plt.grid(True)
    plt.legend()
    plt.title(f'Wave Advancement Test (1/8 domain = {time_to_travel:.4f} time units)')
    plt.savefig('wave_advancement_test.png')
    
    return solver, q_initial, q_advanced, n_steps

def test_environment_step():
    """Test a single environment step with the new approach."""
    # Initialize solver
    xelem = np.array([-1, -0.4, 0, 0.4, 1])
    solver = DGWaveSolverMixed(
        nop=4,
        xelem=xelem,
        max_elements=50,
        max_level=4,
        courant_max=0.1,
        icase=1,
        verbose=True,
        balance=False
    )
    
    # Initialize environment
    env = DGAMREnv(
        solver=solver,
        element_budget=25,
        gamma_c=25.0,
        max_episode_steps=200,
        verbose=True,
        rl_iterations_per_timestep="random",
        max_rl_iterations=100,  # Small value for testing
        max_consecutive_no_action=10
    )
    
    # Reset environment
    obs, _ = env.reset(options={
        'refinement_mode': 'fixed',
        'refinement_level': 2
    })
    
    # Take a refinement action
    action = 2  # Refine action
    next_obs, reward, done, truncated, info = env.step(action)
    
    # Print results
    print(f"Action: {action} (Refine)")
    print(f"Reward: {reward}")
    print(f"Delta U: {info['delta_u']}")
    print(f"Resource usage: {info['resource_usage']}")
    print(f"Elements: {info['n_elements']}")
    
    if info.get('took_timestep', False):
        print(f"Took {info.get('n_physical_steps', 0)} physical timesteps")
    
    return env, obs, next_obs, reward, info

def test_mini_training():
    """Run a mini training session to validate the approach."""
    # Initialize solver
    xelem = np.array([-1, -0.4, 0, 0.4, 1])
    solver = DGWaveSolverMixed(
        nop=4,
        xelem=xelem,
        max_elements=50,
        max_level=4,
        courant_max=0.1,
        icase=1,
        verbose=False,
        balance=False
    )
    
    # Initialize environment
    env = DGAMREnv(
        solver=solver,
        element_budget=25,
        gamma_c=25.0,
        max_episode_steps=200,
        verbose=False,
        rl_iterations_per_timestep="random",
        max_rl_iterations=100,
        max_consecutive_no_action=10
    )
    
    # Create A2C model
    model = A2C("MultiInputPolicy", env, verbose=1, learning_rate=0.0003, n_steps=5)
    
    # Train for a small number of steps
    model.learn(total_timesteps=1000)
    
    # Evaluate for a few episodes
    rewards = []
    for _ in range(3):
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
    
    print(f"Mean evaluation reward: {np.mean(rewards)}")
    
    return model, env, rewards

if __name__ == "__main__":
    # Run tests
    print("\nTesting steady-state solver...")
    solver_steady, q_steady, q_exact = test_steady_solve()
    
    print("\nTesting wave advancement...")
    solver_wave, q_initial, q_advanced, n_steps = test_wave_advancement()
    
    print("\nTesting environment step...")
    env, obs, next_obs, reward, info = test_environment_step()
    
    print("\nRunning mini training session...")
    model, env_train, rewards = test_mini_training()
    
    print("\nAll tests completed!")