#!/usr/bin/env python
"""
Debug script for analyzing reward calculation in the AMR environment.

This script runs a controlled sequence of actions while tracking:
- delta_u values (solution differences)
- Reward components (accuracy term vs resource penalty)
- Element counts and budget proximity
- Action validity and adaptation effects
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import time

# Get absolute path to project root and add to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    '..'
))
sys.path.append(PROJECT_ROOT)

from numerical.solvers.dg_wave_solver_mixed_clean import DGWaveSolverMixed
from numerical.environments.dg_amr_env_mixed import DGAMREnv, RewardCalculator

# Create output directory
output_dir = os.path.join(PROJECT_ROOT, "debug_output")
os.makedirs(output_dir, exist_ok=True)

# Configure logging
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(output_dir, "reward_debug.log")),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def run_controlled_action_sequence(gamma_c=25.0, element_budget=25, verbose=True):
    """
    Run a controlled sequence of actions and analyze rewards in detail.
    
    This function creates a solver and environment, then executes a predefined
    sequence of actions while recording detailed metrics about rewards, solution
    changes, element counts, and more.
    
    Args:
        gamma_c: Coefficient for resource penalty
        element_budget: Maximum number of elements allowed
        verbose: Whether to print detailed logs
        
    Returns:
        DataFrame with recorded metrics
    """
    logger.info(f"Starting controlled action sequence with gamma_c={gamma_c}, budget={element_budget}")
    
    # Initialize solver
    solver = DGWaveSolverMixed(
        nop=4,
        xelem=np.array([-1, -0.4, 0, 0.4, 1]),
        max_elements=element_budget * 2,  # Allow buffer
        max_level=4,
        courant_max=0.1,
        icase=1,
        verbose=verbose,
        balance=False  # Disable balance for simplicity
    )
    
    # Initialize environment
    env = DGAMREnv(
        solver=solver,
        element_budget=element_budget,
        gamma_c=gamma_c,
        max_episode_steps=50,
        verbose=verbose,
        rl_iterations_per_timestep="random",
        max_rl_iterations=10,
        max_consecutive_no_action=10,
        debug_training_cycle=True  # Enable detailed debugging
    )
    
    # Create reward calculator for direct access to calculation components
    reward_calc = RewardCalculator(gamma_c=gamma_c)
    
    # Reset environment
    obs, info = env.reset(options={
        'refinement_mode': 'fixed',
        'refinement_level': 1
    })
    
    # Define action sequence
    # We'll try a mix of refine, do nothing, and coarsen actions
    action_sequence = [
        # First try refinement a few times
        (2, "Refine"),      # 2 maps to 1 (refine)
        (2, "Refine"),
        (2, "Refine"),
        (2, "Refine"),
        # Then try some coarsening
        (0, "Coarsen"),     # 0 maps to -1 (coarsen)
        (0, "Coarsen"),
        # Now try no-change actions
        (1, "No Change"),   # 1 maps to 0 (no change)
        (1, "No Change"),
        # Back to refinement
        (2, "Refine"),
        (2, "Refine"),
    ]
    
    # Initialize data collection
    data = []
    
    # Run the action sequence
    for step, (action, action_name) in enumerate(action_sequence):
        logger.info(f"\n--- Step {step+1}: {action_name} (action {action}) ---")
        logger.info(f"Current state: {len(env.solver.active)}/{element_budget} elements")
        
        # Capture pre-action state
        pre_action_elements = len(env.solver.active)
        pre_action_resource = pre_action_elements / element_budget
        pre_action_solution = env.solver.q.copy()
        pre_action_grid = env.solver.coord.copy()
        
        # Take action and record data
        before_step = time.time()
        obs, reward, terminated, truncated, info = env.step(action)
        step_time = time.time() - before_step
        
        # Capture post-action state
        post_action_elements = len(env.solver.active)
        post_action_resource = post_action_elements / element_budget
        delta_elements = post_action_elements - pre_action_elements
        
        # Get the mapped action value (-1, 0, 1)
        mapped_action = env.action_mapping[action]
        original_action = info.get('original_action', mapped_action)
        actual_action = info.get('actual_action', mapped_action)
        
        # Extract delta_u from info
        delta_u = info.get('delta_u', 0.0)
        
        # Compute reward components manually for verification
        old_barrier = reward_calc.calculate_barrier(pre_action_resource)
        new_barrier = reward_calc.calculate_barrier(post_action_resource)
        resource_penalty = new_barrier - old_barrier
        
        # Calculate expected accuracy term
        if delta_u > 0:
            accuracy_term = np.log(abs(delta_u) + reward_calc.machine_eps) - np.log(reward_calc.machine_eps)
        else:
            accuracy_term = 0.0
            
        # Apply sign based on action
        if actual_action == 1:  # refine
            expected_accuracy = +accuracy_term
        elif actual_action == -1:  # coarsen
            expected_accuracy = -accuracy_term
        else:  # do nothing
            expected_accuracy = 0.0
            
        # Calculate expected reward
        expected_reward = expected_accuracy - gamma_c * resource_penalty
            
        # Check if action produced expected behavior
        is_valid = original_action == actual_action
        
        # Collect data
        step_data = {
            'step': step + 1,
            'action': action,
            'action_name': action_name,
            'original_action': original_action,
            'actual_action': actual_action,
            'is_valid': is_valid,
            'pre_elements': pre_action_elements,
            'post_elements': post_action_elements,
            'delta_elements': delta_elements,
            'pre_resource': pre_action_resource,
            'post_resource': post_action_resource,
            'delta_resource': post_action_resource - pre_action_resource,
            'old_barrier': old_barrier,
            'new_barrier': new_barrier,
            'resource_penalty': resource_penalty,
            'accuracy_term': accuracy_term,
            'expected_accuracy': expected_accuracy,
            'expected_reward': expected_reward,
            'actual_reward': reward,
            'delta_u': delta_u,
            'took_timestep': info.get('took_timestep', False),
            'step_time': step_time,
            'terminated': terminated,
            'truncated': truncated,
            'reason': info.get('reason', 'ongoing')
        }
        
        # Log detailed information
        logger.info(f"Elements: {pre_action_elements} -> {post_action_elements} (Δ{delta_elements})")
        logger.info(f"Resource: {pre_action_resource:.4f} -> {post_action_resource:.4f}")
        logger.info(f"Delta_u: {delta_u:.6e}")
        logger.info(f"Accuracy term: {accuracy_term:.4f}")
        logger.info(f"Expected accuracy: {expected_accuracy:.4f}")
        logger.info(f"Resource penalty: {resource_penalty:.4f} (old_barrier={old_barrier:.4f}, new_barrier={new_barrier:.4f})")
        logger.info(f"Expected reward: {expected_reward:.4f}")
        logger.info(f"Actual reward: {reward:.4f}")
        logger.info(f"Action valid: {is_valid} (original={original_action}, actual={actual_action})")
        
        data.append(step_data)
        
        # Break if terminated
        if terminated or truncated:
            logger.info(f"Episode ended at step {step+1}. Reason: {info.get('reason', 'unknown')}")
            break
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Save data to CSV
    csv_path = os.path.join(output_dir, f"reward_debug_gamma_{gamma_c}.csv")
    df.to_csv(csv_path, index=False)
    logger.info(f"Saved debug data to {csv_path}")
    
    return df

def visualize_results(df, gamma_c):
    """
    Create visualizations for reward analysis.
    
    Args:
        df: DataFrame with collected metrics
        gamma_c: Resource penalty coefficient used
    """
    # Create subfolder for plots
    plots_dir = os.path.join(output_dir, "plots")
    os.makedirs(plots_dir, exist_ok=True)
    
    # 1. Plot reward components
    plt.figure(figsize=(12, 6))
    plt.plot(df['step'], df['expected_accuracy'], 'b-', label='Accuracy Term')
    plt.plot(df['step'], -gamma_c * df['resource_penalty'], 'r-', label=f'Resource Penalty (scaled by gamma_c={gamma_c})')
    plt.plot(df['step'], df['actual_reward'], 'g-', label='Actual Reward')
    plt.plot(df['step'], df['expected_reward'], 'k--', label='Expected Reward')
    
    # Mark different actions with vertical lines
    for i, row in df.iterrows():
        if i > 0 and row['action_name'] != df.iloc[i-1]['action_name']:
            plt.axvline(x=row['step'], color='gray', linestyle=':', alpha=0.5)
    
    plt.xlabel('Step')
    plt.ylabel('Value')
    plt.title('Reward Components by Step')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, f"reward_components_gamma_{gamma_c}.png"))
    
    # 2. Plot delta_u vs reward
    plt.figure(figsize=(10, 6))
    plt.scatter(df['delta_u'], df['actual_reward'], c=df['actual_action'], cmap='viridis')
    plt.colorbar(label='Action (-1: Coarsen, 0: No Change, 1: Refine)')
    plt.xscale('log')
    plt.xlabel('Delta U (log scale)')
    plt.ylabel('Reward')
    plt.title('Reward vs Delta U')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, f"reward_vs_delta_u_gamma_{gamma_c}.png"))
    
    # 3. Plot element count and resource usage
    fig, ax1 = plt.subplots(figsize=(12, 6))
    
    # Element count on left y-axis
    ax1.set_xlabel('Step')
    ax1.set_ylabel('Element Count', color='b')
    ax1.plot(df['step'], df['post_elements'], 'b-', label='Elements')
    ax1.tick_params(axis='y', labelcolor='b')
    
    # Add horizontal line at budget
    ax1.axhline(y=element_budget, color='b', linestyle='--', label='Element Budget')
    
    # Resource on right y-axis
    ax2 = ax1.twinx()
    ax2.set_ylabel('Resource Usage', color='r')
    ax2.plot(df['step'], df['post_resource'], 'r-', label='Resource')
    ax2.tick_params(axis='y', labelcolor='r')
    
    # Add horizontal line at resource = 1.0
    ax2.axhline(y=1.0, color='r', linestyle='--', label='Resource Limit')
    
    # Combine legends
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    plt.title('Element Count and Resource Usage by Step')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, f"elements_resources_gamma_{gamma_c}.png"))
    
    # 4. Plot log(delta_u) vs step with action annotation
    plt.figure(figsize=(12, 6))
    
    # Plot log(delta_u)
    delta_u_log = np.log10(df['delta_u'].replace(0, 1e-10))
    plt.plot(df['step'], delta_u_log, 'b-', marker='o')
    
    # Annotate with actions
    for i, row in df.iterrows():
        plt.annotate(row['action_name'], 
                     (row['step'], delta_u_log.iloc[i]),
                     textcoords="offset points",
                     xytext=(0, 10),
                     ha='center')
    
    plt.xlabel('Step')
    plt.ylabel('log10(Delta U)')
    plt.title('Log of Solution Change by Step')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, f"log_delta_u_gamma_{gamma_c}.png"))
    
    logger.info(f"Saved visualizations to {plots_dir}")

def compare_gamma_values():
    """Run reward debug with different gamma_c values and compare."""
    gamma_values = [5.0, 25.0, 50.0, 100.0]
    results = {}
    
    for gamma_c in gamma_values:
        logger.info(f"\n=== Testing with gamma_c = {gamma_c} ===\n")
        results[gamma_c] = run_controlled_action_sequence(gamma_c=gamma_c, element_budget=25)
        visualize_results(results[gamma_c], gamma_c)
    
    # Create comparison visualization
    plt.figure(figsize=(12, 8))
    
    for gamma_c, df in results.items():
        plt.plot(df['step'], df['actual_reward'], marker='o', label=f'gamma_c = {gamma_c}')
    
    plt.xlabel('Step')
    plt.ylabel('Reward')
    plt.title('Reward Comparison Across Different Gamma Values')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "plots", "gamma_comparison.png"))
    
    # Create comparison of accuracy vs. resource penalty
    plt.figure(figsize=(14, 10))
    
    # Set up subplot grid
    fig, axes = plt.subplots(len(gamma_values), 1, figsize=(12, 4*len(gamma_values)), sharex=True)
    
    for i, (gamma_c, df) in enumerate(results.items()):
        ax = axes[i] if len(gamma_values) > 1 else axes
        
        # Plot components
        ax.plot(df['step'], df['expected_accuracy'], 'b-', label='Accuracy Term')
        ax.plot(df['step'], -gamma_c * df['resource_penalty'], 'r-', 
                label=f'Resource Penalty (gamma_c={gamma_c})')
        ax.plot(df['step'], df['actual_reward'], 'g-', label='Actual Reward')
        
        ax.set_title(f'Reward Components with gamma_c = {gamma_c}')
        ax.grid(True)
        ax.legend()
        
        if i == len(gamma_values) - 1:
            ax.set_xlabel('Step')
        
        ax.set_ylabel('Value')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "plots", "reward_components_comparison.png"))
    
    logger.info("Completed gamma comparison")



def test_budget_boundary_behavior(element_budget=12, gamma_c=25.0, verbose=True):
    """
    Run a controlled sequence of actions that deliberately exceeds the element budget.
    
    This function creates a solver and environment with a lower element budget,
    then repeatedly applies refinement actions until the budget is exceeded.
    
    Args:
        element_budget: Low budget to make it easier to exceed (default: 12)
        gamma_c: Coefficient for resource penalty
        verbose: Whether to print detailed logs
        
    Returns:
        DataFrame with recorded metrics
    """
    logger.info(f"Starting budget boundary test with budget={element_budget}, gamma_c={gamma_c}")
    
    # Initialize solver
    # Start with fewer elements to make it easier to exceed budget
    solver = DGWaveSolverMixed(
        nop=4,
        xelem=np.array([-1, -0.4, 0, 0.4, 1]),  # 4 initial elements
        max_elements=element_budget * 2,  # Allow buffer
        max_level=4,
        courant_max=0.1,
        icase=1,
        verbose=verbose,
        balance=False  # Disable balance for simplicity
    )
    
    # Initialize environment with a low budget
    env = DGAMREnv(
        solver=solver,
        element_budget=element_budget,
        gamma_c=gamma_c,
        max_episode_steps=50,
        verbose=verbose,
        rl_iterations_per_timestep="random",
        max_rl_iterations=10,
        max_consecutive_no_action=10,
        debug_training_cycle=True
    )
    
    # Create reward calculator for direct access
    reward_calc = RewardCalculator(gamma_c=gamma_c)
    
    # Reset environment with minimal refinement
    obs, info = env.reset(options={
        'refinement_mode': 'none',  # Start with base grid
        'refinement_level': 0
    })
    
    # Initialize data collection
    data = []
    
    # Track whether budget has been exceeded
    budget_exceeded = False
    
    # Run refine actions until we exceed the budget and a few steps beyond
    for step in range(25):  # Limit to 25 steps maximum
        logger.info(f"\n--- Step {step+1}: Budget Test ---")
        
        # Track current element count
        current_elements = len(env.solver.active)
        current_resource = current_elements / element_budget
        
        logger.info(f"Current state: {current_elements}/{element_budget} elements ({current_resource:.2f} of budget)")
        
        # Determine action - always refine until we exceed budget by 2 elements
        if budget_exceeded and current_elements > element_budget + 2:
            # After exceeding budget by a margin, try some coarsen actions
            action = 0  # Coarsen (maps to -1)
            action_name = "Coarsen"
        else:
            # Keep refining until we exceed budget
            action = 2  # Refine (maps to 1)
            action_name = "Refine"
        
        # Capture pre-action state
        pre_action_elements = current_elements
        pre_action_resource = pre_action_elements / element_budget
        pre_action_solution = env.solver.q.copy()
        pre_action_grid = env.solver.coord.copy()
        
        # Take action and record data
        obs, reward, terminated, truncated, info = env.step(action)
        
        # Capture post-action state
        post_action_elements = len(env.solver.active)
        post_action_resource = post_action_elements / element_budget
        delta_elements = post_action_elements - pre_action_elements
        
        # Check if we exceeded budget
        if post_action_elements > element_budget and not budget_exceeded:
            budget_exceeded = True
            logger.info(f"BUDGET EXCEEDED: {post_action_elements} > {element_budget}")
        
        # Get the mapped action value (-1, 0, 1)
        mapped_action = env.action_mapping[action]
        original_action = info.get('original_action', mapped_action)
        actual_action = info.get('actual_action', mapped_action)
        
        # Extract delta_u from info
        delta_u = info.get('delta_u', 0.0)
        
        # Compute reward components manually for verification
        old_barrier = reward_calc.calculate_barrier(pre_action_resource)
        new_barrier = reward_calc.calculate_barrier(post_action_resource)
        resource_penalty = new_barrier - old_barrier
        
        # Calculate expected accuracy term
        if delta_u > 0:
            accuracy_term = np.log(abs(delta_u) + reward_calc.machine_eps) - np.log(reward_calc.machine_eps)
        else:
            accuracy_term = 0.0
            
        # Apply sign based on action
        if actual_action == 1:  # refine
            expected_accuracy = +accuracy_term
        elif actual_action == -1:  # coarsen
            expected_accuracy = -accuracy_term
        else:  # do nothing
            expected_accuracy = 0.0
            
        # Calculate expected reward
        expected_reward = expected_accuracy - gamma_c * resource_penalty
        
        # Add budget proximity and threshold metrics
        budget_proximity = post_action_resource
        over_budget = 1 if post_action_elements > element_budget else 0
        distance_from_budget = post_action_elements - element_budget
        
        # Log detailed information with focus on budget
        logger.info(f"Elements: {pre_action_elements} -> {post_action_elements} (Δ{delta_elements})")
        logger.info(f"Resource: {pre_action_resource:.4f} -> {post_action_resource:.4f}")
        logger.info(f"Budget status: {'EXCEEDED' if over_budget else 'Under'} by {abs(distance_from_budget)} elements")
        logger.info(f"Delta_u: {delta_u:.6e}")
        logger.info(f"Accuracy term: {accuracy_term:.4f}")
        logger.info(f"Resource penalty: {resource_penalty:.4f} (old_barrier={old_barrier:.4f}, new_barrier={new_barrier:.4f})")
        logger.info(f"Expected reward: {expected_reward:.4f}")
        logger.info(f"Actual reward: {reward:.4f}")
        
        # Collect all data
        step_data = {
            'step': step + 1,
            'action': action,
            'action_name': action_name,
            'original_action': original_action,
            'actual_action': actual_action,
            'is_valid': original_action == actual_action,
            'pre_elements': pre_action_elements,
            'post_elements': post_action_elements,
            'delta_elements': delta_elements,
            'pre_resource': pre_action_resource,
            'post_resource': post_action_resource,
            'delta_resource': post_action_resource - pre_action_resource,
            'old_barrier': old_barrier,
            'new_barrier': new_barrier,
            'resource_penalty': resource_penalty,
            'accuracy_term': accuracy_term,
            'expected_accuracy': expected_accuracy,
            'expected_reward': expected_reward,
            'actual_reward': reward,
            'delta_u': delta_u,
            'budget_proximity': budget_proximity,
            'over_budget': over_budget,
            'distance_from_budget': distance_from_budget,
            'took_timestep': info.get('took_timestep', False),
            'terminated': terminated,
            'truncated': truncated,
            'reason': info.get('reason', 'ongoing')
        }
        
        data.append(step_data)
        
        # Break if episode terminated
        if terminated or truncated:
            logger.info(f"Episode ended at step {step+1}. Reason: {info.get('reason', 'unknown')}")
            break
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Save data to CSV
    csv_path = os.path.join(output_dir, f"budget_test_gamma_{gamma_c}.csv")
    df.to_csv(csv_path, index=False)
    logger.info(f"Saved budget test data to {csv_path}")
    
    # Create specialized visualizations for budget testing
    visualize_budget_results(df, gamma_c, element_budget)
    
    return df

def visualize_budget_results(df, gamma_c, element_budget):
    """
    Create visualizations specifically focused on budget boundary behavior.
    
    Args:
        df: DataFrame with collected metrics
        gamma_c: Resource penalty coefficient
        element_budget: Element budget used in test
    """
    # Create subfolder for plots
    plots_dir = os.path.join(output_dir, "plots")
    os.makedirs(plots_dir, exist_ok=True)
    
    # 1. Plot resource usage with budget threshold highlighted
    plt.figure(figsize=(12, 6))
    
    # Create bar chart of element counts with color based on budget status
    colors = ['green' if row['post_elements'] <= element_budget else 'red' 
              for _, row in df.iterrows()]
    
    plt.bar(df['step'], df['post_elements'], color=colors)
    plt.axhline(y=element_budget, color='r', linestyle='--', label='Budget Limit')
    
    plt.xlabel('Step')
    plt.ylabel('Element Count')
    plt.title('Element Count vs Budget Threshold')
    plt.legend()
    plt.grid(True, axis='y')
    plt.tight_layout()
    
    # Add exact count labels on bars
    for i, v in enumerate(df['post_elements']):
        plt.text(i+1, v + 0.5, str(int(v)), ha='center')
    
    plt.savefig(os.path.join(plots_dir, f"budget_threshold_elements_gamma_{gamma_c}.png"))
    plt.close()
    
    # 2. Plot barrier function values as resource usage increases
    plt.figure(figsize=(12, 6))
    
    # Calculate barrier values across resource range from 0 to 1.2
    resource_range = np.linspace(0, 1.2, 100)
    barrier_values = [RewardCalculator(gamma_c=gamma_c).calculate_barrier(r) for r in resource_range]
    
    # Plot full barrier function curve
    plt.plot(resource_range, barrier_values, 'b-', label='Barrier Function B(p)')
    
    # Overlay actual barrier values from our test
    plt.scatter(df['post_resource'], df['new_barrier'], c='red', s=50, 
                label='Observed Values')
    
    # Mark the budget threshold
    plt.axvline(x=1.0, color='r', linestyle='--', label='Budget Threshold')
    
    # Add labels for each point
    for i, row in df.iterrows():
        plt.annotate(f"Step {row['step']}", 
                    (row['post_resource'], row['new_barrier']),
                    textcoords="offset points",
                    xytext=(0, 10),
                    ha='center')
    
    plt.xlabel('Resource Usage (p)')
    plt.ylabel('Barrier Function Value B(p)')
    plt.title('Barrier Function Values Near Budget Threshold')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    
    plt.savefig(os.path.join(plots_dir, f"barrier_function_gamma_{gamma_c}.png"))
    plt.close()
    
    # 3. Plot reward and components with focus on budget threshold crossing
    plt.figure(figsize=(12, 8))
    
    # Create a marker for when budget is exceeded
    budget_exceeded_step = df[df['post_elements'] > element_budget]['step'].min() \
                           if any(df['post_elements'] > element_budget) else None
    
    # Plot reward components
    plt.plot(df['step'], df['expected_accuracy'], 'b-', label='Accuracy Term')
    plt.plot(df['step'], -gamma_c * df['resource_penalty'], 'r-', 
            label=f'Resource Penalty (scaled by gamma_c={gamma_c})')
    plt.plot(df['step'], df['actual_reward'], 'g-', linewidth=2, label='Actual Reward')
    
    # Add vertical line at budget exceeded point
    if budget_exceeded_step:
        plt.axvline(x=budget_exceeded_step, color='red', linestyle='--', 
                   label='Budget Exceeded')
    
    plt.xlabel('Step')
    plt.ylabel('Value')
    plt.title('Reward Components Near Budget Threshold')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    
    # Add annotations for key points
    for i, row in df.iterrows():
        if row['over_budget'] == 1 and i > 0 and df.iloc[i-1]['over_budget'] == 0:
            # First point that exceeds budget
            plt.annotate('Budget Exceeded', 
                        (row['step'], row['actual_reward']),
                        textcoords="offset points",
                        xytext=(0, 30),
                        ha='center',
                        arrowprops=dict(arrowstyle="->", color='black'))
    
    plt.savefig(os.path.join(plots_dir, f"reward_at_budget_gamma_{gamma_c}.png"))
    plt.close()
    
    # 4. Plot the ratio of accuracy term to resource penalty
    plt.figure(figsize=(12, 6))
    
    # Calculate the absolute ratio (avoid division by zero)
    df['accuracy_to_penalty_ratio'] = df.apply(
        lambda row: abs(row['expected_accuracy']) / max(1e-10, abs(gamma_c * row['resource_penalty'])), 
        axis=1
    )
    
    plt.plot(df['step'], df['accuracy_to_penalty_ratio'], 'b-', marker='o')
    
    # Add vertical line at budget exceeded point
    if budget_exceeded_step:
        plt.axvline(x=budget_exceeded_step, color='red', linestyle='--', 
                   label='Budget Exceeded')
    
    plt.xlabel('Step')
    plt.ylabel('|Accuracy Term| / |Resource Penalty|')
    plt.title('Ratio of Accuracy Term to Resource Penalty')
    plt.yscale('log')  # Use log scale for better visualization
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    
    plt.savefig(os.path.join(plots_dir, f"accuracy_penalty_ratio_gamma_{gamma_c}.png"))
    plt.close()

if __name__ == "__main__":
    print(f"Running reward debug tests...")
    print(f"Debug output will be saved to: {os.path.abspath(output_dir)}")
    
    # Choose which tests to run
    run_standard_test = True
    run_budget_test = True
    
    if run_standard_test:
        print("\n=== Running standard reward component analysis ===")
        # Run single experiment with default gamma_c
        element_budget = 25
        gamma_c = 25.0
        
        df = run_controlled_action_sequence(gamma_c=gamma_c, element_budget=element_budget)
        visualize_results(df, gamma_c)
    
    if run_budget_test:
        print("\n=== Running budget boundary tests ===")
        # Test with different gamma values
        for gamma_c in [25.0, 50.0, 100.0]:
            print(f"\nTesting with gamma_c = {gamma_c}")
            # Use a small budget that's easy to exceed
            element_budget = 12
            
            # Run the budget test
            df = test_budget_boundary_behavior(
                element_budget=element_budget,
                gamma_c=gamma_c,
                verbose=True
            )
    
    print(f"All tests completed! Results saved to {os.path.abspath(output_dir)}")

# if __name__ == "__main__":
#     print(f"Running budget boundary tests...")
#     print(f"Debug output will be saved to: {os.path.abspath(output_dir)}")
    
#     # Test with different gamma values
#     for gamma_c in [25.0, 50.0, 100.0]:
#         # Use a small budget that's easy to exceed
#         element_budget = 12
        
#         # Run the budget test
#         df = test_budget_boundary_behavior(
#             element_budget=element_budget,
#             gamma_c=gamma_c,
#             verbose=True
#         )
    
#     print(f"Budget tests completed! Results saved to {os.path.abspath(output_dir)}")

# if __name__ == "__main__":
#     print(f"Running reward debug tests...")
#     print(f"Debug output will be saved to: {os.path.abspath(output_dir)}")
    
#     # Run main experiment with default gamma_c
#     element_budget = 25
#     gamma_c = 25.0
    
#     # Run single experiment
#     df = run_controlled_action_sequence(gamma_c=gamma_c, element_budget=element_budget)
#     visualize_results(df, gamma_c)
    
#     # Uncomment to run comparison across different gamma values
#     # compare_gamma_values()
    
#     print(f"Debug completed! Results saved to {os.path.abspath(output_dir)}")