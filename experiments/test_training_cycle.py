# test_training_cycle.py
import os
import sys
import yaml
import argparse
import datetime
import shutil
from pathlib import Path
import numpy as np

# Get absolute path to project root and add to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    '..'
))
sys.path.append(PROJECT_ROOT)
from numerical.solvers.dg_wave_solver_clean import DGWaveSolver
from numerical.environments.dg_amr_env_clean import DGAMREnv

# Set up a simple test case
solver = DGWaveSolver(
    nop=3,
    xelem=np.array([-1, -0.4, 0, 0.4, 1]),
    max_elements=50,
    max_level=5,
    courant_max=0.1,
    icase=1,
    verbose=False
)

# Test configuration
print("Testing with fixed RL iterations per time step...")
env = DGAMREnv(
    solver=solver,
    element_budget=25,
    gamma_c=25.0,
    max_episode_steps=50,
    verbose=False,
    rl_iterations_per_timestep=3,  # Fixed for testing
    max_rl_iterations=5,
    debug_training_cycle=True  # Enable specific debugging
)

# Reset and run a test episode
obs, info = env.reset()
print(f"Initial state: {len(env.solver.active)} elements")
print("-" * 50)

# Run with a simple refine-only policy to see effect
time_steps_taken = 0
total_rl_iterations = 0

for i in range(30):  # Run 30 steps
    # Always choose refinement (action 2 maps to 1 which is refine)
    action = 2
    
    obs, reward, terminated, truncated, info = env.step(action)
    total_rl_iterations += 1
    
    if info.get('took_timestep', False):
        time_steps_taken += 1
    
    if terminated or truncated:
        print(f"Episode ended after {i+1} steps. Reason: {info.get('reason', 'unknown')}")
        break

print("-" * 50)
print(f"Test summary:")
print(f"Total RL iterations: {total_rl_iterations}")
print(f"Physical time steps taken: {time_steps_taken}")
print(f"Average RL iterations per time step: {total_rl_iterations/max(1, time_steps_taken):.2f}")
print(f"Final state: {len(env.solver.active)}/{env.element_budget} elements")
print("\nNow testing with random RL iterations per time step...")

# Reset with random iterations per time step
env = DGAMREnv(
    solver=solver,
    element_budget=35,
    # gamma_c=25.0,
    gamma_c=50.0,
    max_episode_steps=50,
    verbose=False,
    rl_iterations_per_timestep="random",
    max_rl_iterations=5,
    debug_training_cycle=True
)

# Run same test with random iterations
obs, info = env.reset()
print(f"Initial state: {len(env.solver.active)} elements")
print("-" * 50)

time_steps_taken = 0
total_rl_iterations = 0

for i in range(30):

    if i < 20:
        action = 2  # Always refine
    else:
        action = 0
    # action = 0  # Always coarsen
    
    obs, reward, terminated, truncated, info = env.step(action)
    total_rl_iterations += 1
    
    if info.get('took_timestep', False):
        time_steps_taken += 1
    
    if terminated or truncated:
        print(f"Episode ended after {i+1} steps. Reason: {info.get('reason', 'unknown')}")
        break

print("-" * 50)
print(f"Test summary:")
print(f"Total RL iterations: {total_rl_iterations}")
print(f"Physical time steps taken: {time_steps_taken}")
print(f"Average RL iterations per time step: {total_rl_iterations/max(1, time_steps_taken):.2f}")
print(f"Final state: {len(env.solver.active)}/{env.element_budget} elements")