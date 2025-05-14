import os
import sys
import numpy as np

PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 
    '..',
    '..'
))
sys.path.append(PROJECT_ROOT)
import matplotlib.pyplot as plt
from numerical.solvers.dg_wave_solver_clean import DGWaveSolver
from numerical.environments.dg_amr_env_clean import DGAMREnv  # New cleaned version

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

env = DGAMREnv(
    solver=solver,
    element_budget=25,
    gamma_c=25.0,
    max_episode_steps=20,
    verbose=True,
    debug_training_cycle=True
)

# Test barrier function
p_values = np.linspace(0, 0.99, 100)
barrier_values = [env.reward_calculator.calculate_barrier(p) for p in p_values]

plt.figure(figsize=(10, 6))
plt.plot(p_values, barrier_values)
plt.xlabel('Resource usage p')
plt.ylabel('Barrier function B(p)')
plt.title('Barrier Function: B(p) = √p/(1-p)')
plt.grid(True)
plt.savefig('barrier_function.png')
plt.close()

# Test environment functionality
obs, info = env.reset()
print(f"Initial state: {len(env.solver.active)}/{env.element_budget} elements")

# Try different actions and check rewards
actions = [1, 1, 0, -1]  # refine, refine, do nothing, coarsen
action_names = {1: "refine", 0: "do nothing", -1: "coarsen"}

for i, action in enumerate(actions):
    print(f"\nStep {i+1}: Taking action {action_names[action]}")
    
    # Store pre-action state
    pre_elements = len(env.solver.active)
    pre_resource = pre_elements / env.element_budget
    pre_barrier = env.reward_calculator.calculate_barrier(pre_resource)
    
    # Take action
    obs, reward, terminated, truncated, info = env.step(action + 1)  # Convert to 0-2 range
    
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