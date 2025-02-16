"""
Test script for DG AMR Environment.
Verifies basic functionality and budget enforcement.
"""

import os
import sys
import numpy as np
from typing import Dict

PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 
    '..',
    '..'
))
sys.path.append(PROJECT_ROOT)

from numerical.solvers.dg_wave_solver import DGWaveSolver
from numerical.environments.dg_amr_env import DGAMREnv

def print_observation(obs: Dict):
    """Print observation details."""
    print("\nObservation Details:")
    print("-" * 50)
    for key, value in obs.items():
        print(f"{key}:")
        print(f"  shape: {value.shape}")
        print(f"  range: [{value.min():.3f}, {value.max():.3f}]")
        print(f"  mean:  {value.mean():.3f}")

def test_reset():
    """Test environment reset."""
    print("\nTesting Reset...")
    print("=" * 50)
    
    obs, info = env.reset()
    print_observation(obs)
    print("\nReset Info:", info)
    return obs

def test_actions():
    """Test each possible action."""
    print("\nTesting Actions...")
    print("=" * 50)
    
    for action in range(env.action_space.n):
        print(f"\nTaking action: {action}")
        print("-" * 30)
        
        obs, reward, terminated, truncated, info = env.step(action)
        
        print(f"Reward: {reward:.3f}")
        print("Info:")
        for key, value in info.items():
            print(f"  {key}: {value}")
        
        if terminated:
            print("Episode terminated!")
        if truncated:
            print("Episode truncated (exceeded resources)!")
            
        print_observation(obs)

def test_element_selection():
    """Test random element selection."""
    print("\nTesting Element Selection...")
    print("=" * 50)
    
    n_steps = 10
    selected_elements = []
    rewards = []
    
    obs = env.reset()[0]
    initial_element = env.current_element
    selected_elements.append(initial_element)
    
    print(f"Initial element: {initial_element}")
    
    for i in range(n_steps):
        action = np.random.randint(0, env.action_space.n)
        obs, reward, terminated, truncated, info = env.step(action)
        
        selected_elements.append(env.current_element)
        rewards.append(reward)
        
        print(f"\nStep {i+1}:")
        print(f"  Action taken: {action}")
        print(f"  Element selected: {env.current_element}")
        print(f"  Reward: {reward:.3f}")
        print(f"  Number of elements: {info['n_elements']}")
        
        if terminated or truncated:
            print("Episode ended!")
            break

def test_budget_enforcement():
    """Test that environment properly enforces element budget."""
    print("\nTesting Budget Enforcement...")
    print("=" * 50)
    
    # Initialize with small budget
    xelem = np.array([-1, -0.4, 0, 0.4, 1])
    solver = DGWaveSolver(
        nop=4,
        xelem=xelem,
        max_elements=25,
        max_level=4,
        courant_max=0.1,
        icase=1
    )
    
    test_budget = 10  # Small budget for clear testing
    env = DGAMREnv(solver=solver, element_budget=test_budget, gamma_c=25.0)
    
    # Test 1: Multiple Refinements
    print("\nTest 1: Multiple Refinement Actions")
    print("-" * 30)
    
    obs = env.reset()[0]
    initial_elements = len(env.solver.active)
    print(f"Initial elements: {initial_elements}")
    
    # Try multiple refinements
    actions_taken = 0
    for _ in range(10):  # Try more refinements than budget allows
        obs, reward, terminated, truncated, info = env.step(2)  # Always try to refine
        print(f"Elements: {info['n_elements']}, Budget: {test_budget}")
        print(f"Reward: {reward:.2f}, Truncated: {truncated}")
        actions_taken += 1
        if truncated:
            break
    
    assert info['n_elements'] <= test_budget, f"Element count {info['n_elements']} exceeds budget {test_budget}"
    print(f"Refinement test completed after {actions_taken} actions")

    # Test 2: Refinement with Balance Enforcement
    print("\nTest 2: Balance Enforcement within Budget")
    print("-" * 30)
    
    obs = env.reset()[0]
    
    # Try to create situation requiring balance enforcement
    actions = [(0, 2), (1, 2), (2, 2)]  # (element_index, action)
    for elem_idx, action in actions:
        env.current_element = elem_idx
        obs, reward, terminated, truncated, info = env.step(action)
        print(f"Action on element {elem_idx}: Elements: {info['n_elements']}, Budget: {test_budget}")
        assert info['n_elements'] <= test_budget, "Balance enforcement exceeded budget"

    # Test 3: Coarsening Behavior
    print("\nTest 3: Coarsening Behavior")
    print("-" * 30)
    
    obs = env.reset()[0]
    
    # First refine to near budget
    while len(env.solver.active) < test_budget - 1:
        obs, reward, terminated, truncated, info = env.step(2)
        if truncated:
            break
    
    print(f"Elements after refinement: {len(env.solver.active)}")
    
    # Now test coarsening
    obs, reward, terminated, truncated, info = env.step(0)  # Try to coarsen
    print(f"Elements after coarsening: {info['n_elements']}")
    assert not truncated, "Coarsening should not trigger truncation"

def test_edge_cases():
    """Test edge cases in budget enforcement."""
    print("\nTesting Edge Cases...")
    print("=" * 50)
    
    # Test 1: Minimum Budget
    print("\nTest 1: Minimum Budget")
    print("-" * 30)
    
    xelem = np.array([-1, -0.4, 0, 0.4, 1])
    solver = DGWaveSolver(
        nop=4,
        xelem=xelem,
        max_elements=25,
        max_level=4,
        courant_max=0.1,
        icase=1
    )
    
    min_elements = len(xelem) - 1  # Minimum possible elements
    env = DGAMREnv(solver=solver, element_budget=min_elements, gamma_c=25.0)
    
    obs = env.reset()[0]
    obs, reward, terminated, truncated, info = env.step(2)  # Try to refine
    print(f"Reward for impossible refinement: {reward}")
    assert reward < 0, "Should receive negative reward for impossible refinement"
    
    # Test 2: Large Budget
    print("\nTest 2: Large Budget")
    print("-" * 30)
    
    large_budget = 1000
    env = DGAMREnv(solver=solver, element_budget=large_budget, gamma_c=25.0)
    
    obs = env.reset()[0]
    elements_history = []
    
    # Try many refinements
    for _ in range(10):
        obs, reward, terminated, truncated, info = env.step(2)
        elements_history.append(info['n_elements'])
        print(f"Elements: {info['n_elements']}")
        if truncated:
            break
    
    # Should still see controlled growth
    assert all(n <= large_budget for n in elements_history), "Element count exceeded large budget"

if __name__ == "__main__":
    # Initialize environment for basic tests
    print("Initializing environment...")
    xelem = np.array([-1, -0.4, 0, 0.4, 1])
    solver = DGWaveSolver(
        nop=4,
        xelem=xelem,
        max_elements=25,
        max_level=4,
        courant_max=0.1,
        icase=1
    )
    
    env = DGAMREnv(solver=solver, element_budget=25, gamma_c=25.0)
    
    # Run all tests
    test_reset()
    test_actions()
    test_element_selection()
    test_budget_enforcement()
    test_edge_cases()





# """
# Test script for DG AMR Environment.
# Verifies basic functionality of the environment before RL training.
# Tests actual behavior beyond basic Gymnasium API compliance.
# """


# import os
# import sys
# import numpy as np
# from typing import Dict

# # Add project root to path
# # project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# # sys.path.append(project_root)
# PROJECT_ROOT = os.path.abspath(os.path.join(
#     os.path.dirname(__file__), 
#     '..',
#     '..'
# ))
# sys.path.append(PROJECT_ROOT)

# from numerical.solvers.dg_wave_solver import DGWaveSolver
# from numerical.environments.dg_amr_env import DGAMREnv

# def print_observation(obs: Dict):
#     """Print observation details."""
#     print("\nObservation Details:")
#     print("-" * 50)
#     for key, value in obs.items():
#         print(f"{key}:")
#         print(f"  shape: {value.shape}")
#         print(f"  range: [{value.min():.3f}, {value.max():.3f}]")
#         print(f"  mean:  {value.mean():.3f}")

# def test_reset():
#     """Test environment reset."""
#     print("\nTesting Reset...")
#     print("=" * 50)
    
#     obs, info = env.reset()
#     print_observation(obs)
#     print("\nReset Info:", info)
#     return obs

# def test_actions():
#     """Test each possible action."""
#     print("\nTesting Actions...")
#     print("=" * 50)
    
#     for action in range(env.action_space.n):
#         print(f"\nTaking action: {action}")
#         print("-" * 30)
        
#         # Take action
#         obs, reward, terminated, truncated, info = env.step(action)
        
#         # Print results
#         print(f"Reward: {reward:.3f}")
#         print("Info:")
#         for key, value in info.items():
#             print(f"  {key}: {value}")
        
#         if terminated:
#             print("Episode terminated!")
#         if truncated:
#             print("Episode truncated (exceeded resources)!")
            
#         print_observation(obs)

# def test_element_selection():
#     """Test random element selection."""
#     print("\nTesting Element Selection...")
#     print("=" * 50)
    
#     n_steps = 10
#     selected_elements = []
#     rewards = []
    
#     obs = env.reset()[0]
#     initial_element = env.current_element
#     selected_elements.append(initial_element)
    
#     print(f"Initial element: {initial_element}")
    
#     for i in range(n_steps):
#         action = np.random.randint(0, env.action_space.n)
#         obs, reward, terminated, truncated, info = env.step(action)
        
#         selected_elements.append(env.current_element)
#         rewards.append(reward)
        
#         print(f"\nStep {i+1}:")
#         print(f"  Action taken: {action}")
#         print(f"  Element selected: {env.current_element}")
#         print(f"  Reward: {reward:.3f}")
#         print(f"  Number of elements: {info['n_elements']}")
        
#         if terminated or truncated:
#             print("Episode ended!")
#             break
    
#     print("\nElement Selection Summary:")
#     print(f"Unique elements visited: {len(set(selected_elements))}")
#     print(f"Reward range: [{min(rewards):.3f}, {max(rewards):.3f}]")
#     print(f"Mean reward: {np.mean(rewards):.3f}")

# if __name__ == "__main__":
#     # Initialize solver and environment
#     print("Initializing environment...")
#     xelem = np.array([-1, -0.4, 0, 0.4, 1])
#     solver = DGWaveSolver(
#         nop=4,
#         xelem=xelem,
#         max_elements = 25,
#         max_level=4,
#         courant_max=0.1,
#         icase=1  # Gaussian test case
#     )
    
#     env = DGAMREnv(solver=solver, element_budget=25, gamma_c=25.0)
    
#     # Run tests
#     initial_obs = test_reset()
#     test_actions()
#     test_element_selection()





# # import numpy as np
# # from numerical.solvers.dg_wave_solver import DGWaveSolver
# # from numerical.environments import DGAMREnv

# # def test_environment():
# #     """Run basic tests on the DG AMR environment."""
    
# #     # Initialize solver with same parameters as your main script
# #     xelem = np.array([-1, -0.4, 0, 0.4, 1])
# #     solver = DGWaveSolver(
# #         nop=4,
# #         xelem=xelem,
# #         max_level=4,
# #         icase=1  # Gaussian test case
# #     )
    
# #     # Create environment
# #     env = DGAMREnv(solver=solver, gamma_c=25.0)
    
# #     # Test 1: Reset and Initial Observation
# #     print("\nTest 1: Reset and Initial Observation")
# #     print("--------------------------------------")
# #     obs, info = env.reset()
# #     print("Observation space components:")
# #     for key, value in obs.items():
# #         print(f"{key}: shape={value.shape}, range=[{value.min():.3f}, {value.max():.3f}]")
    
# #     # Test 2: Action Space
# #     print("\nTest 2: Action Space")
# #     print("--------------------")
# #     print(f"Number of actions: {env.action_space.n}")
# #     print("Actions: 0=coarsen, 1=do nothing, 2=refine")
    
# #     # Test 3: Step Through Multiple Actions
# #     print("\nTest 3: Testing Actions")
# #     print("----------------------")
    
# #     # Try each action
# #     for action in range(3):
# #         print(f"\nTaking action: {action}")
        
# #         # Take step
# #         obs, reward, terminated, truncated, info = env.step(action)
        
# #         # Print results
# #         print(f"Reward: {reward:.3f}")
# #         print(f"Resource usage: {info['resource_usage']:.3f}")
# #         print(f"Number of elements: {info['n_elements']}")
# #         print(f"Solution change: {info['delta_u']:.3e}")
        
# #         if terminated:
# #             print("Episode terminated")
# #         if truncated:
# #             print("Episode truncated (resources exceeded)")
            
# #     # Test 4: Element Selection
# #     print("\nTest 4: Element Selection")
# #     print("-------------------------")
# #     initial_element = env.current_element
    
# #     # Take several steps and track selected elements
# #     n_steps = 10
# #     selected_elements = [initial_element]
    
# #     for _ in range(n_steps):
# #         _, _, _, _, _ = env.step(1)  # Take "do nothing" action
# #         selected_elements.append(env.current_element)
    
# #     print(f"Elements selected: {selected_elements}")
# #     print(f"Unique elements selected: {len(set(selected_elements))}")
    
# #     # Test 5: Reward Function
# #     print("\nTest 5: Reward Range")
# #     print("-------------------")
# #     rewards = []
    
# #     # Take random actions and collect rewards
# #     for _ in range(10):
# #         action = np.random.randint(0, 3)
# #         _, reward, _, _, _ = env.step(action)
# #         rewards.append(reward)
    
# #     print(f"Reward range: [{min(rewards):.3f}, {max(rewards):.3f}]")
# #     print(f"Mean reward: {np.mean(rewards):.3f}")
    
# #     return env

# # if __name__ == "__main__":
# #     # Run tests
# #     env = test_environment()