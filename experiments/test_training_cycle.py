# test_training_cycle.py
import os
import sys
import yaml
import argparse
import datetime
import shutil
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# Get absolute path to project root and add to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    '..'
))
sys.path.append(PROJECT_ROOT)
# from numerical.solvers.dg_wave_solver_clean import DGWaveSolver
# from numerical.solvers.dg_wave_solver_free import DGWaveSolver
# from numerical.solvers.dg_wave_solver_options import DGWaveSolver
# from numerical.environments.dg_amr_env_clean import DGAMREnv
from numerical.solvers.dg_wave_solver_mixed_clean import DGWaveSolverMixed
from numerical.environments.dg_amr_env_mixed import DGAMREnv

def run_standard_test():
    """Run the original standard test"""
    # Set up a simple test case
    solver = DGWaveSolverMixed(
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
        gamma_c=50.0,
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

    for i in range(40):

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

def visualize_mesh(solver, title):
    """Visualize the current mesh structure"""
    plt.figure(figsize=(10, 3))
    
    # Get element boundaries
    xelem = solver.xelem
    
    # Get element levels
    levels = []
    for elem in solver.active:
        # Active element IDs are 1-indexed
        level = solver.label_mat[elem-1][4]
        levels.append(level)
    
    # Plot element boundaries
    for i in range(len(xelem)-1):
        plt.axvline(x=xelem[i], color='k', linestyle='-', alpha=0.5)
    plt.axvline(x=xelem[-1], color='k', linestyle='-', alpha=0.5)
    
    # Plot element levels as horizontal lines
    for i, elem in enumerate(solver.active):
        left_idx = i
        right_idx = i + 1
        if left_idx < len(xelem) and right_idx < len(xelem):
            x_left = xelem[left_idx]
            x_right = xelem[right_idx]
            level = levels[i]
            plt.plot([x_left, x_right], [level, level], 'o-', linewidth=2)
    
    plt.ylim(-0.5, solver.max_level + 0.5)
    plt.ylabel('Refinement Level')
    plt.xlabel('x coordinate')
    plt.title(title)
    plt.grid(True)
    return plt

def test_balance_enforcement():
    """Test the effect of balance enforcement flag with progressive visualization"""
    print("\n" + "="*70)
    print("TESTING BALANCE ENFORCEMENT")
    print("="*70)
    
    # Create output directory for visualizations
    vis_dir = "mesh_evolution"
    os.makedirs(vis_dir, exist_ok=True)
    
    # Create two solvers - one with balance=True (default) and one with balance=False
    solver_with_balance = DGWaveSolverMixed(
        nop=3,
        xelem=np.array([-1, -0.4, 0, 0.4, 1]),
        max_elements=50,
        max_level=5,
        courant_max=0.1,
        icase=1,
        verbose=True,
        balance=True  # Explicitly set balance flag to True
    )
    
    solver_without_balance = DGWaveSolverMixed(
        nop=3,
        xelem=np.array([-1, -0.4, 0, 0.4, 1]),
        max_elements=50,
        max_level=5,
        courant_max=0.1,
        icase=1,
        verbose=True,
        balance=False  # Explicitly set balance flag to False
    )
    
    # Initial state visualization
    print("\nInitial state:")
    print(f"With balance: {len(solver_with_balance.active)} elements")
    print(f"Without balance: {len(solver_without_balance.active)} elements")
    
    # Save initial state visualization
    visualize_mesh(solver_with_balance, "Initial Mesh with Balance Enforcement").savefig(
        os.path.join(vis_dir, "0_initial_with_balance.png"))
    plt.close()
    
    visualize_mesh(solver_without_balance, "Initial Mesh without Balance Enforcement").savefig(
        os.path.join(vis_dir, "0_initial_without_balance.png"))
    plt.close()
    
    # Series of refinements with visualization at each step
    refinement_steps = [
        {"step": 1, "description": "Refine center element", "marks": {2: 1}},
        {"step": 2, "description": "Refine left child of center", "marks": {2: 1}},
        {"step": 3, "description": "Further refine same element", "marks": {2: 1}},
        {"step": 4, "description": "Refine neighboring element", "marks": {3: 1}},
        {"step": 5, "description": "Create extreme level difference", "marks": {2: 1}}
    ]
    
    # Perform refinement sequence with visualization at each step
    for step_info in refinement_steps:
        step_num = step_info["step"]
        description = step_info["description"]
        marks = step_info["marks"]
        
        print(f"\nStep {step_num}: {description}")
        
        # Apply to balanced solver
        solver_with_balance.adapt_mesh(marks_override=marks)
        balanced_count = len(solver_with_balance.active)
        print(f"  With balance: {balanced_count} elements")
        
        # Save visualization for balanced solver
        visualize_mesh(solver_with_balance, f"Step {step_num}: {description} (With Balance)").savefig(
            os.path.join(vis_dir, f"{step_num}_with_balance.png"))
        plt.close()
        
        # Apply to unbalanced solver
        solver_without_balance.adapt_mesh(marks_override=marks)
        unbalanced_count = len(solver_without_balance.active)
        print(f"  Without balance: {unbalanced_count} elements")
        
        # Save visualization for unbalanced solver
        visualize_mesh(solver_without_balance, f"Step {step_num}: {description} (Without Balance)").savefig(
            os.path.join(vis_dir, f"{step_num}_without_balance.png"))
        plt.close()
        
        # Note any differences
        if balanced_count != unbalanced_count:
            print(f"  Difference detected: {balanced_count - unbalanced_count} additional elements required for balance")
    
    # Create a combined visualization showing the evolution
    def create_evolution_grid(solver_type, step_count):
        """Create a grid of meshes showing evolution"""
        fig, axes = plt.subplots(step_count + 1, 1, figsize=(12, 3*(step_count+1)))
        fig.suptitle(f"Mesh Evolution with {solver_type} Balance Enforcement", fontsize=16)
        
        # Initial state
        img_path = os.path.join(vis_dir, f"0_initial_{solver_type}_balance.png")
        if os.path.exists(img_path):
            img = plt.imread(img_path)
            axes[0].imshow(img)
            axes[0].axis('off')
            axes[0].set_title("Initial State")
        
        # Each refinement step
        for i in range(step_count):
            step_num = i + 1
            img_path = os.path.join(vis_dir, f"{step_num}_{solver_type}_balance.png")
            if os.path.exists(img_path):
                img = plt.imread(img_path)
                axes[step_num].imshow(img)
                axes[step_num].axis('off')
                axes[step_num].set_title(f"Step {step_num}: {refinement_steps[i]['description']}")
        
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        return fig
    
    # Create and save evolution grids
    with_balance_evolution = create_evolution_grid("with", len(refinement_steps))
    with_balance_evolution.savefig(os.path.join(vis_dir, "evolution_with_balance.png"))
    plt.close()
    
    without_balance_evolution = create_evolution_grid("without", len(refinement_steps))
    without_balance_evolution.savefig(os.path.join(vis_dir, "evolution_without_balance.png"))
    plt.close()
    
    # Analyze the final mesh structure
    print("\nAnalyzing final mesh structure:")
    
    # Get element levels for both solvers
    balanced_levels = []
    for elem in solver_with_balance.active:
        level = solver_with_balance.label_mat[elem-1][4]
        balanced_levels.append(level)
    
    unbalanced_levels = []
    for elem in solver_without_balance.active:
        level = solver_without_balance.label_mat[elem-1][4]
        unbalanced_levels.append(level)
    
    print(f"With balance - Element count: {len(balanced_levels)}, Element levels: {balanced_levels}")
    print(f"Without balance - Element count: {len(unbalanced_levels)}, Element levels: {unbalanced_levels}")
    
    # Check for 2:1 balance
    print("\nChecking for 2:1 balance violations:")
    
    # Function to check for level jumps greater than 1
    def has_balance_violation(solver):
        violations = []
        for i in range(len(solver.active) - 1):
            elem1 = solver.active[i]
            elem2 = solver.active[i+1]
            level1 = solver.label_mat[elem1-1][4]
            level2 = solver.label_mat[elem2-1][4]
            if abs(level1 - level2) > 1:
                violations.append((i, i+1, level1, level2))
        return violations
    
    balanced_violations = has_balance_violation(solver_with_balance)
    unbalanced_violations = has_balance_violation(solver_without_balance)
    
    print(f"With balance - Number of 2:1 balance violations: {len(balanced_violations)}")
    for v in balanced_violations:
        print(f"  Violation between elements {v[0]}-{v[1]}: Level jump {v[2]}->{v[3]}")
    
    print(f"Without balance - Number of 2:1 balance violations: {len(unbalanced_violations)}")
    for v in unbalanced_violations:
        print(f"  Violation between elements {v[0]}-{v[1]}: Level jump {v[2]}->{v[3]}")
    
    print("\nBalance enforcement test complete!")
    print(f"Mesh evolution visualizations saved to: {os.path.abspath(vis_dir)}")
    print("="*70)

# def test_balance_enforcement():
#     """Test the effect of balance enforcement flag"""
#     print("\n" + "="*70)
#     print("TESTING BALANCE ENFORCEMENT")
#     print("="*70)
    
#     # Create two solvers - one with balance=True (default) and one with balance=False
#     solver_with_balance = DGWaveSolver(
#         nop=3,
#         xelem=np.array([-1, -0.4, 0, 0.4, 1]),
#         max_elements=50,
#         max_level=5,
#         courant_max=0.1,
#         icase=1,
#         verbose=True,
#         balance=True  # Explicitly set balance flag to True
#     )
    
#     solver_without_balance = DGWaveSolver(
#         nop=3,
#         xelem=np.array([-1, -0.4, 0, 0.4, 1]),
#         max_elements=50,
#         max_level=5,
#         courant_max=0.1,
#         icase=1,
#         verbose=True,
#         balance=False  # Explicitly set balance flag to False
#     )
    
#     # Print initial state
#     print("\nInitial state:")
#     print(f"With balance: {len(solver_with_balance.active)} elements")
#     print(f"Without balance: {len(solver_without_balance.active)} elements")
    
#     # Perform a sequence of targeted refinements to demonstrate the difference
#     # We'll focus on refining specific elements to create level jumps
    
#     print("\nRefining specific elements to create level differences...")
    
#     # Mark the central element for refinement in both solvers
#     center_elem_idx = 2  # Index of central element (0-based)
    
#     # First refinement - should behave the same for both solvers
#     marks = {center_elem_idx: 1}  # 1 = refine
    
#     # Apply to balanced solver
#     solver_with_balance.adapt_mesh(marks_override=marks)
#     print(f"After first refinement (with balance): {len(solver_with_balance.active)} elements")
    
#     # Apply to unbalanced solver
#     solver_without_balance.adapt_mesh(marks_override=marks)
#     print(f"After first refinement (without balance): {len(solver_without_balance.active)} elements")
    
#     # Now refine one of the newly created elements to create a level difference
#     # After the first refinement, the central element is split into element indices 2 and 3
#     marks = {2: 1}  # Target the left child of the previously refined element
    
#     # Apply to balanced solver
#     print("\nRefining a child element to create a potential level jump...")
#     solver_with_balance.adapt_mesh(marks_override=marks)
#     print(f"After second refinement (with balance): {len(solver_with_balance.active)} elements")
    
#     # Apply to unbalanced solver
#     solver_without_balance.adapt_mesh(marks_override=marks)
#     print(f"After second refinement (without balance): {len(solver_without_balance.active)} elements")
    
#     # Refine once more to make the level difference more pronounced
#     marks = {2: 1}  # Refine the same element again
    
#     print("\nRefinining once more to create even greater level differences...")
    
#     # Apply to balanced solver
#     solver_with_balance.adapt_mesh(marks_override=marks)
#     print(f"After third refinement (with balance): {len(solver_with_balance.active)} elements")
    
#     # Apply to unbalanced solver
#     solver_without_balance.adapt_mesh(marks_override=marks)
#     print(f"After third refinement (without balance): {len(solver_without_balance.active)} elements")
    
#     # Analyze the mesh structure
#     print("\nAnalyzing mesh structure:")
    
#     # Get element levels for both solvers
#     balanced_levels = []
#     for elem in solver_with_balance.active:
#         level = solver_with_balance.label_mat[elem-1][4]
#         balanced_levels.append(level)
    
#     unbalanced_levels = []
#     for elem in solver_without_balance.active:
#         level = solver_without_balance.label_mat[elem-1][4]
#         unbalanced_levels.append(level)
    
#     print(f"With balance - Element count: {len(balanced_levels)}, Element levels: {balanced_levels}")
#     print(f"Without balance - Element count: {len(unbalanced_levels)}, Element levels: {unbalanced_levels}")
    
#     # Check for 2:1 balance
#     print("\nChecking for 2:1 balance violations:")
    
#     # Function to check for level jumps greater than 1
#     def has_balance_violation(solver):
#         violations = 0
#         for i in range(len(solver.active) - 1):
#             elem1 = solver.active[i]
#             elem2 = solver.active[i+1]
#             level1 = solver.label_mat[elem1-1][4]
#             level2 = solver.label_mat[elem2-1][4]
#             if abs(level1 - level2) > 1:
#                 violations += 1
#         return violations
    
#     balanced_violations = has_balance_violation(solver_with_balance)
#     unbalanced_violations = has_balance_violation(solver_without_balance)
    
#     print(f"With balance - Number of 2:1 balance violations: {balanced_violations}")
#     print(f"Without balance - Number of 2:1 balance violations: {unbalanced_violations}")
    
#     # Visualize the meshes
#     plt_balanced = visualize_mesh(solver_with_balance, "Mesh with Balance Enforcement")
#     plt.savefig("mesh_with_balance.png")
#     plt.close()
    
#     plt_unbalanced = visualize_mesh(solver_without_balance, "Mesh without Balance Enforcement")
#     plt.savefig("mesh_without_balance.png")
#     plt.close()
    
#     print("\nMesh visualization saved to:")
#     print("- mesh_with_balance.png")
#     print("- mesh_without_balance.png")
    
#     # Test in environment context
#     print("\nTesting in environment context...")
    
#     env_with_balance = DGAMREnv(
#         solver=solver_with_balance,
#         element_budget=35,
#         gamma_c=50.0,
#         max_episode_steps=50,
#         verbose=False,
#         rl_iterations_per_timestep="random",
#         max_rl_iterations=5,
#         debug_training_cycle=True
#     )
    
#     env_without_balance = DGAMREnv(
#         solver=solver_without_balance,
#         element_budget=35,
#         gamma_c=50.0,
#         max_episode_steps=50,
#         verbose=False,
#         rl_iterations_per_timestep="random",
#         max_rl_iterations=5,
#         debug_training_cycle=True
#     )
    
#     # Reset environments
#     print("\nResetting environments and running a few refine actions:")
#     obs_balanced, _ = env_with_balance.reset()
#     obs_unbalanced, _ = env_without_balance.reset()
    
#     # Run a few refine actions on both
#     for i in range(5):
#         action = 2  # Always refine
        
#         # With balance
#         _, reward_balanced, _, _, info_balanced = env_with_balance.step(action)
        
#         # Without balance
#         _, reward_unbalanced, _, _, info_unbalanced = env_without_balance.step(action)
        
#         print(f"Step {i+1}:")
#         print(f"  With balance: Elements={len(env_with_balance.solver.active)}, Reward={reward_balanced:.2f}")
#         print(f"  Without balance: Elements={len(env_without_balance.solver.active)}, Reward={reward_unbalanced:.2f}")
    
#     print("\nBalance enforcement test complete!")
#     print("="*70)

if __name__ == "__main__":
    # Run standard tests
    run_standard_test()
    
    # Run balance enforcement test
    test_balance_enforcement()

# # test_training_cycle.py
# import os
# import sys
# import yaml
# import argparse
# import datetime
# import shutil
# from pathlib import Path
# import numpy as np

# # Get absolute path to project root and add to Python path
# PROJECT_ROOT = os.path.abspath(os.path.join(
#     os.path.dirname(__file__),
#     '..'
# ))
# sys.path.append(PROJECT_ROOT)
# # from numerical.solvers.dg_wave_solver_clean import DGWaveSolver
# from numerical.solvers.dg_wave_solver_free import DGWaveSolver
# from numerical.environments.dg_amr_env_clean import DGAMREnv

# # Set up a simple test case
# solver = DGWaveSolver(
#     nop=3,
#     xelem=np.array([-1, -0.4, 0, 0.4, 1]),
#     max_elements=50,
#     max_level=5,
#     courant_max=0.1,
#     icase=1,
#     verbose=False
# )

# # Test configuration
# print("Testing with fixed RL iterations per time step...")
# env = DGAMREnv(
#     solver=solver,
#     element_budget=25,
#     gamma_c=50.0,
#     max_episode_steps=50,
#     verbose=False,
#     rl_iterations_per_timestep=3,  # Fixed for testing
#     max_rl_iterations=5,
#     debug_training_cycle=True  # Enable specific debugging
# )

# # Reset and run a test episode
# obs, info = env.reset()
# print(f"Initial state: {len(env.solver.active)} elements")
# print("-" * 50)

# # Run with a simple refine-only policy to see effect
# time_steps_taken = 0
# total_rl_iterations = 0

# for i in range(30):  # Run 30 steps
#     # Always choose refinement (action 2 maps to 1 which is refine)
#     action = 2
    
#     obs, reward, terminated, truncated, info = env.step(action)
#     total_rl_iterations += 1
    
#     if info.get('took_timestep', False):
#         time_steps_taken += 1
    
#     if terminated or truncated:
#         print(f"Episode ended after {i+1} steps. Reason: {info.get('reason', 'unknown')}")
#         break

# print("-" * 50)
# print(f"Test summary:")
# print(f"Total RL iterations: {total_rl_iterations}")
# print(f"Physical time steps taken: {time_steps_taken}")
# print(f"Average RL iterations per time step: {total_rl_iterations/max(1, time_steps_taken):.2f}")
# print(f"Final state: {len(env.solver.active)}/{env.element_budget} elements")
# print("\nNow testing with random RL iterations per time step...")

# # Reset with random iterations per time step
# env = DGAMREnv(
#     solver=solver,
#     element_budget=35,
#     # gamma_c=25.0,
#     gamma_c=50.0,
#     max_episode_steps=50,
#     verbose=False,
#     rl_iterations_per_timestep="random",
#     max_rl_iterations=5,
#     debug_training_cycle=True
# )

# # Run same test with random iterations
# obs, info = env.reset()
# print(f"Initial state: {len(env.solver.active)} elements")
# print("-" * 50)

# time_steps_taken = 0
# total_rl_iterations = 0

# for i in range(40):

#     if i < 20:
#         action = 2  # Always refine
#     else:
#         action = 0
#     # action = 0  # Always coarsen
    
#     obs, reward, terminated, truncated, info = env.step(action)
#     total_rl_iterations += 1
    
#     if info.get('took_timestep', False):
#         time_steps_taken += 1
    
#     if terminated or truncated:
#         print(f"Episode ended after {i+1} steps. Reason: {info.get('reason', 'unknown')}")
#         break

# print("-" * 50)
# print(f"Test summary:")
# print(f"Total RL iterations: {total_rl_iterations}")
# print(f"Physical time steps taken: {time_steps_taken}")
# print(f"Average RL iterations per time step: {total_rl_iterations/max(1, time_steps_taken):.2f}")
# print(f"Final state: {len(env.solver.active)}/{env.element_budget} elements")