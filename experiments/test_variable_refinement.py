#!/usr/bin/env python
"""
Script to test variable initial mesh refinement functionality.
Tests the new initialization methods with different refinement strategies
and analyzes their effects on coarsening behavior.
"""

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

from numerical.solvers.dg_wave_solver_options import DGWaveSolver
from numerical.environments.dg_amr_env_clean import DGAMREnv, RewardCalculator

def test_reset_with_refinement():
    """
    Test the solver's reset method with different initial refinement strategies.
    Compare the resulting meshes and element distributions.
    """
    print("\n" + "="*60)
    print("TESTING SOLVER RESET WITH VARIABLE REFINEMENT")
    print("="*60)
    
    # Base parameters for all solvers
    nop = 3
    xelem = np.array([-1, -0.4, 0, 0.4, 1])
    max_elements = 50
    max_level = 4
    
    # Test configurations
    configs = [
        {"name": "Default (No Refinement)", "refinement_mode": "none", "refinement_level": 0},
        {"name": "Fixed Level 1", "refinement_mode": "fixed", "refinement_level": 1},
        {"name": "Fixed Level 2", "refinement_mode": "fixed", "refinement_level": 2},
        {"name": "Random (p=0.5, lvl=2)", "refinement_mode": "random", "refinement_level": 2, "probability": 0.5},
        {"name": "Random (p=0.8, lvl=3)", "refinement_mode": "random", "refinement_level": 3, "probability": 0.8}
    ]
    
    # Store results
    solver_results = {}
    
    # Directory for results
    results_dir = os.path.join(PROJECT_ROOT, 'experiments', 'results', 'variable_refinement_test')
    os.makedirs(results_dir, exist_ok=True)
    
    plt.figure(figsize=(15, 10))
    
    # Maximum refinement level for colorbar
    max_level = 4
    
    # Test each configuration
    for i, config in enumerate(configs):
        print(f"\nTesting {config['name']}")
        
        # Create solver
        solver = DGWaveSolver(
            nop=nop,
            xelem=xelem,
            max_elements=max_elements,
            max_level=max_level,
            courant_max=0.1,
            icase=1,
            verbose=False
        )
        
        # Apply reset with refinement options
        reset_options = {
            'refinement_mode': config["refinement_mode"],
            'refinement_level': config["refinement_level"]
        }
        if "probability" in config:
            reset_options["refinement_probability"] = config["probability"]
            
        solver.reset(**reset_options)
        
        # Store results
        element_count = len(solver.active)
        active_levels = get_active_levels(solver.active, solver.label_mat)
        max_actual_level = max(active_levels) if active_levels else 0
        level_distribution = {level: active_levels.count(level) for level in range(max_level+1)}
        
        solver_results[config["name"]] = {
            'element_count': element_count,
            'active_levels': active_levels,
            'max_level': max_actual_level,
            'level_distribution': level_distribution,
            'resource_usage': element_count / max_elements,
            'element_distribution': get_element_distribution(solver)
        }
        
        # Print summary
        print(f"  Element count: {element_count}")
        print(f"  Max refinement level: {max_actual_level}")
        print(f"  Level distribution: {level_distribution}")
        print(f"  Resource usage: {element_count / max_elements * 100:.1f}%")
        
        # Plot the mesh
        plt.subplot(len(configs), 1, i+1)
        element_sizes = np.diff(solver.xelem)
        element_positions = [(solver.xelem[i] + solver.xelem[i+1])/2 for i in range(len(element_sizes))]
        
        # Create a color map based on refinement level
        levels = []
        for elem in solver.active:
            # Element IDs in label_mat are 1-indexed, hence elem-1
            level = solver.label_mat[elem-1][4]  # Level is in column 4
            levels.append(level)
        
        # Create color-coded bars    
        plt.bar(element_positions, element_sizes, width=element_sizes*0.8, 
                alpha=0.7, color=plt.cm.viridis(np.array(levels)/max_level))
        
        # Create a proper colorbar with normalization
        from matplotlib.colors import Normalize
        norm = Normalize(vmin=0, vmax=max_level)
        sm = plt.cm.ScalarMappable(cmap=plt.cm.viridis, norm=norm)
        sm.set_array([])  # Set an empty array to avoid warning
        
        plt.xlabel('Position')
        plt.ylabel('Element Size')
        plt.title(f'{config["name"]} - {element_count} elements')
        plt.colorbar(sm, ax=plt.gca(), label='Refinement Level')
        plt.grid(True)
    
    plt.tight_layout()
    plt.savefig(os.path.join(results_dir, 'reset_with_refinement.png'))
    
    # Create summary plot of element counts
    plt.figure(figsize=(10, 6))
    names = list(solver_results.keys())
    element_counts = [solver_results[name]['element_count'] for name in names]
    
    plt.bar(names, element_counts)
    plt.xlabel('Refinement Method')
    plt.ylabel('Number of Elements')
    plt.title('Element Count by Refinement Method')
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, axis='y')
    plt.tight_layout()
    plt.savefig(os.path.join(results_dir, 'element_counts.png'))
    
    print(f"\nSolver reset test complete. Results saved to {results_dir}")
    return solver_results

def test_env_reset_with_refinement():
    """
    Test the environment reset method with different refinement options.
    Verify the environment correctly passes refinement options to the solver.
    """
    print("\n" + "="*60)
    print("TESTING ENVIRONMENT RESET WITH REFINEMENT")
    print("="*60)
    
    # Create environment
    env = DGAMREnv(
        solver=DGWaveSolver(
            nop=3,
            xelem=np.array([-1, -0.4, 0, 0.4, 1]),
            max_elements=50,
            max_level=4,
            courant_max=0.1,
            icase=1,
            verbose=False
        ),
        element_budget=30,
        gamma_c=25.0,
        max_episode_steps=50,
        verbose=False,
        rl_iterations_per_timestep=5,
        debug_training_cycle=False
    )
    
    # Test configurations
    configs = [
        {"name": "Default", "options": None},
        {"name": "Fixed Level 1", "options": {
            'refinement_mode': 'fixed',
            'refinement_level': 1,
        }},
        {"name": "Fixed Level 2", "options": {
            'refinement_mode': 'fixed',
            'refinement_level': 2,
        }},
        {"name": "Random (lvl=2, p=0.7)", "options": {
            'refinement_mode': 'random',
            'refinement_level': 2,
            'refinement_probability': 0.7
        }}
    ]
    
    # Maximum refinement level for reference
    max_level = 4
    
    # Directory for results
    results_dir = os.path.join(PROJECT_ROOT, 'experiments', 'results', 'env_reset_test')
    os.makedirs(results_dir, exist_ok=True)
    
    # Store results
    reset_results = {}
    
    for config in configs:
        print(f"\nTesting environment reset with {config['name']}")
        
        # Reset environment with given options
        obs, info = env.reset(options=config["options"])
        
        # Collect data
        element_count = len(env.solver.active)
        active_levels = get_active_levels(env.solver.active, env.solver.label_mat)
        max_actual_level = max(active_levels) if active_levels else 0
        level_distribution = {level: active_levels.count(level) for level in range(max_level+1)}
        resource_usage = element_count / env.element_budget
        
        reset_results[config["name"]] = {
            'element_count': element_count,
            'active_levels': active_levels,
            'max_level': max_actual_level,
            'level_distribution': level_distribution,
            'resource_usage': resource_usage,
            'observation': obs
        }
        
        # Print summary
        print(f"  Element count: {element_count}")
        print(f"  Max refinement level: {max_actual_level}")
        print(f"  Level distribution: {level_distribution}")
        print(f"  Resource usage: {resource_usage * 100:.1f}%")
        print(f"  Observation resource usage: {obs['resource_usage'][0]:.4f}")
        
        # Run a few steps to verify environment functions correctly
        print(f"  Running 5 test steps...")
        total_reward = 0
        for i in range(5):
            action = np.random.randint(0, 3)  # random action
            obs, reward, term, trunc, info = env.step(action)
            total_reward += reward
            
            if term or trunc:
                print(f"    Episode ended early at step {i+1}. Reason: {info.get('reason', 'unknown')}")
                break
                
        print(f"  Test steps complete. Total reward: {total_reward:.2f}")
    
    # Create summary visualization
    plt.figure(figsize=(12, 8))
    
    # Plot 1: Element counts and resource usage
    plt.subplot(2, 1, 1)
    names = list(reset_results.keys())
    element_counts = [reset_results[name]['element_count'] for name in names]
    resource_usages = [reset_results[name]['resource_usage'] * 100 for name in names]
    
    # Double bar chart
    x = np.arange(len(names))
    width = 0.35
    
    plt.bar(x - width/2, element_counts, width, label='Element Count')
    plt.bar(x + width/2, resource_usages, width, label='Resource Usage %')
    
    plt.xlabel('Reset Configuration')
    plt.ylabel('Value')
    plt.title('Element Count and Resource Usage by Reset Configuration')
    plt.xticks(x, names, rotation=45, ha='right')
    plt.legend()
    plt.grid(True, axis='y')
    
    # Plot 2: Level distributions
    plt.subplot(2, 1, 2)
    max_level = 4
    
    for i, name in enumerate(names):
        distribution = reset_results[name]['level_distribution']
        
        # Calculate percentage of elements at each level
        total = sum(distribution.values())
        
        levels = list(range(max_level + 1))
        percentages = [distribution.get(level, 0) / total * 100 if total > 0 else 0 
                      for level in levels]
        
        plt.bar([l + i*0.2 for l in levels], percentages, width=0.2, 
                label=name, alpha=0.7)
    
    plt.xlabel('Refinement Level')
    plt.ylabel('Percentage of Elements')
    plt.title('Element Level Distribution by Reset Configuration')
    plt.legend()
    plt.grid(True, axis='y')
    plt.tight_layout()
    
    plt.savefig(os.path.join(results_dir, 'env_reset_results.png'))
    
    print(f"\nEnvironment reset test complete. Results saved to {results_dir}")
    return reset_results

def test_coarsening_behavior():
    """
    Test how initial refinement affects coarsening behavior.
    Compare coarsening rewards between no refinement and high initial refinement.
    """
    print("\n" + "="*60)
    print("TESTING COARSENING BEHAVIOR WITH INITIAL REFINEMENT")
    print("="*60)
    
    # Create environment
    env = DGAMREnv(
        solver=DGWaveSolver(
            nop=3,
            xelem=np.array([-1, -0.4, 0, 0.4, 1]),
            max_elements=50,
            max_level=4,
            courant_max=0.1,
            icase=1,
            verbose=False
        ),
        element_budget=30,
        gamma_c=25.0,
        max_episode_steps=100,
        verbose=False,
        rl_iterations_per_timestep=3,
        debug_training_cycle=False
    )
    
    # Test configurations
    configs = [
        {"name": "No Refinement", "options": None},
        {"name": "Highly Refined (Lvl 2)", "options": {
            'refinement_mode': 'fixed',
            'refinement_level': 2,
        }}
    ]
    
    # Directory for results
    results_dir = os.path.join(PROJECT_ROOT, 'experiments', 'results', 'coarsening_test')
    os.makedirs(results_dir, exist_ok=True)
    
    # Store results
    coarsening_results = {}
    
    # Test each configuration
    for config in configs:
        print(f"\nTesting coarsening behavior with {config['name']}")
        
        # Reset environment with given options
        obs, info = env.reset(options=config["options"])
        
        # Initial state
        initial_elements = len(env.solver.active)
        initial_resource = initial_elements / env.element_budget
        print(f"  Initial state: {initial_elements} elements, {initial_resource*100:.1f}% resources")
        
        # Data collection
        steps = []
        element_counts = []
        resource_usages = []
        action_counts = {-1: 0, 0: 0, 1: 0}  # -1: coarsen, 0: no change, 1: refine
        rewards = []
        delta_us = []
        coarsening_rewards = []
        
        # Run episode with specific coarsening tests
        for i in range(50):
            # Choose action - try to coarsen periodically
            if i % 5 < 3:  # Coarsen 3 out of 5 steps
                action = 0  # coarsen (0 maps to -1)
            else:
                action = np.random.choice([1, 2])  # no change or refine
            
            # Take step
            obs, reward, term, trunc, info = env.step(action)
            
            # Map action to semantic value
            mapped_action = env.action_mapping[action]
            action_counts[mapped_action] += 1
            
            # Collect data
            steps.append(i)
            element_counts.append(len(env.solver.active))
            resource_usages.append(len(env.solver.active) / env.element_budget)
            rewards.append(reward)
            delta_us.append(info.get('delta_u', 0))
            
            # Only record rewards for coarsening actions
            if mapped_action == -1:
                coarsening_rewards.append(reward)
            
            # Print status every 10 steps
            if i % 10 == 0:
                print(f"  Step {i}: Elements={len(env.solver.active)}, "
                      f"Resource={resource_usages[-1]*100:.1f}%, "
                      f"Action={mapped_action}, Reward={reward:.3f}")
                
            if term or trunc:
                print(f"  Episode ended at step {i+1}. Reason: {info.get('reason', 'unknown')}")
                break
                
        # Calculate statistics
        action_distribution = {
            action: count / sum(action_counts.values()) 
            for action, count in action_counts.items()
        }
        avg_coarsening_reward = np.mean(coarsening_rewards) if coarsening_rewards else 0
        
        # Store results
        coarsening_results[config["name"]] = {
            'initial_elements': initial_elements,
            'initial_resource': initial_resource,
            'steps': steps,
            'element_counts': element_counts,
            'resource_usages': resource_usages,
            'action_counts': action_counts,
            'action_distribution': action_distribution,
            'rewards': rewards,
            'delta_us': delta_us,
            'coarsening_rewards': coarsening_rewards,
            'avg_coarsening_reward': avg_coarsening_reward
        }
        
        # Print summary
        print("  Action distribution:")
        for action, percentage in action_distribution.items():
            print(f"    {action_name(action)}: {percentage*100:.1f}%")
        print(f"  Average coarsening reward: {avg_coarsening_reward:.3f}")
    
    # Create visualization comparing the two strategies
    plt.figure(figsize=(15, 10))
    
    # Plot 1: Element counts over time
    plt.subplot(2, 2, 1)
    for name, result in coarsening_results.items():
        plt.plot(result['steps'], result['element_counts'], label=name)
    plt.xlabel('Steps')
    plt.ylabel('Element Count')
    plt.title('Element Count Over Time')
    plt.grid(True)
    plt.legend()
    
    # Plot 2: Resource usage over time
    plt.subplot(2, 2, 2)
    for name, result in coarsening_results.items():
        plt.plot(result['steps'], np.array(result['resource_usages'])*100, label=name)
    plt.xlabel('Steps')
    plt.ylabel('Resource Usage (%)')
    plt.title('Resource Usage Over Time')
    plt.grid(True)
    plt.legend()
    
    # Plot 3: Action distribution
    plt.subplot(2, 2, 3)
    names = list(coarsening_results.keys())
    x = np.arange(len(names))
    width = 0.25
    
    actions = [-1, 0, 1]
    for i, action in enumerate(actions):
        percentages = [coarsening_results[name]['action_distribution'][action] * 100 
                      for name in names]
        plt.bar(x + (i-1)*width, percentages, width, label=action_name(action))
    
    plt.xlabel('Configuration')
    plt.ylabel('Percentage')
    plt.title('Action Distribution by Configuration')
    plt.xticks(x, names)
    plt.legend()
    plt.grid(True, axis='y')
    
    # Plot 4: Coarsening rewards distribution
    plt.subplot(2, 2, 4)
    for name, result in coarsening_results.items():
        if result['coarsening_rewards']:
            plt.hist(result['coarsening_rewards'], alpha=0.5, label=name, bins=10)
    plt.xlabel('Reward')
    plt.ylabel('Count')
    plt.title('Distribution of Coarsening Rewards')
    plt.grid(True)
    plt.legend()
    
    plt.tight_layout()
    plt.savefig(os.path.join(results_dir, 'coarsening_behavior.png'))
    
    print(f"\nCoarsening behavior test complete. Results saved to {results_dir}")
    return coarsening_results

def test_barrier_function():
    """
    Test the barrier function with different initial refinement levels.
    Analyzes reward implications for both refinement and coarsening.
    """
    print("\n" + "="*60)
    print("TESTING BARRIER FUNCTION WITH VARIABLE REFINEMENT")
    print("="*60)
    
    reward_calc = RewardCalculator(gamma_c=25.0)
    
    # Generate points for plotting
    p_values = np.linspace(0.01, 0.99, 100)
    barrier_values = [reward_calc.calculate_barrier(p) for p in p_values]
    
    # Create results directory
    results_dir = os.path.join(PROJECT_ROOT, 'experiments', 'results', 'barrier_test')
    os.makedirs(results_dir, exist_ok=True)
    
    # Create plot showing barrier function
    plt.figure(figsize=(10, 6))
    plt.plot(p_values, barrier_values)
    plt.xlabel('Resource Usage (p)')
    plt.ylabel('Barrier Function B(p) = √p/(1-p)')
    plt.title('Non-hortative Barrier Function')
    plt.grid(True)
    plt.xlim(0, 1)
    
    # Highlight typical resource usage ranges for different refinement levels
    initial_points = [
        {"name": "No Refinement", "p": 0.2, "color": "blue"},
        {"name": "Level 1", "p": 0.35, "color": "green"},
        {"name": "Level 2", "p": 0.5, "color": "orange"},
        {"name": "Level 3", "p": 0.75, "color": "red"}
    ]
    
    for point in initial_points:
        plt.axvline(x=point["p"], color=point["color"], linestyle='--', 
                   alpha=0.7, label=f'{point["name"]} (p≈{point["p"]:.2f})')
    
    plt.legend()
    plt.savefig(os.path.join(results_dir, 'barrier_function.png'))
    
    # Analyze reward implications for refinement
    plt.figure(figsize=(10, 6))
    
    # Assumed delta_u for accuracy component
    delta_u_h = 0.1  # Arbitrary value for demonstration
    log_delta = np.log(delta_u_h + 1e-16) - np.log(1e-16)
    
    # Calculate rewards for refinement at different resource levels
    refine_rewards = []
    for i in range(len(p_values)-1):
        p = p_values[i]
        next_p = min(0.99, p + 0.05)  # Simulate resource increase from refinement
        
        barrier_diff = reward_calc.calculate_barrier(next_p) - reward_calc.calculate_barrier(p)
        reward = log_delta - 25.0 * barrier_diff
        refine_rewards.append(reward)
    
    # Plot refinement rewards curve
    plt.plot(p_values[:-1], refine_rewards, 'b-', label='Refinement Reward')
    
    # Highlight rewards at typical initial refinement levels
    for point in initial_points:
        p = point["p"]
        next_p = min(0.99, p + 0.05)
        
        barrier_diff = reward_calc.calculate_barrier(next_p) - reward_calc.calculate_barrier(p)
        reward = log_delta - 25.0 * barrier_diff
        
        plt.plot(p, reward, 'o', color=point["color"], 
                markersize=10, label=f'{point["name"]}: {reward:.2f}')
    
    # Add reference line for zero reward
    plt.axhline(y=0, color='gray', linestyle='-', alpha=0.5)
    
    plt.xlabel('Resource Usage (p)')
    plt.ylabel('Reward')
    plt.title('Refinement Reward vs Resource Usage')
    plt.grid(True)
    plt.legend(loc='best')
    plt.savefig(os.path.join(results_dir, 'refinement_rewards.png'))
    
    # Analyze reward implications for coarsening
    plt.figure(figsize=(10, 6))
    
    # Calculate rewards for coarsening at different resource levels
    coarsen_rewards = []
    for i in range(len(p_values)-1):
        p = p_values[i]
        prev_p = max(0.01, p - 0.05)  # Simulate resource decrease from coarsening
        
        barrier_diff = reward_calc.calculate_barrier(prev_p) - reward_calc.calculate_barrier(p)
        # Note negative sign for accuracy component (see equation 5 in paper)
        reward = -log_delta - 25.0 * barrier_diff
        coarsen_rewards.append(reward)
    
    # Plot coarsening rewards curve
    plt.plot(p_values[:-1], coarsen_rewards, 'r-', label='Coarsening Reward')
    
    # Highlight rewards at typical initial refinement levels
    for point in initial_points:
        p = point["p"]
        prev_p = max(0.01, p - 0.05)
        
        barrier_diff = reward_calc.calculate_barrier(prev_p) - reward_calc.calculate_barrier(p)
        reward = -log_delta - 25.0 * barrier_diff
        
        plt.plot(p, reward, 'o', color=point["color"], 
                markersize=10, label=f'{point["name"]}: {reward:.2f}')
    
    # Add reference line for zero reward
    plt.axhline(y=0, color='gray', linestyle='-', alpha=0.5)
    
    plt.xlabel('Resource Usage (p)')
    plt.ylabel('Reward')
    plt.title('Coarsening Reward vs Resource Usage')
    plt.grid(True)
    plt.legend(loc='best')
    plt.savefig(os.path.join(results_dir, 'coarsening_rewards.png'))
    
    print(f"\nBarrier function test complete. Results saved to {results_dir}")
    return barrier_values

# Helper functions
def get_active_levels(active, label_mat):
    """Get refinement levels for active elements."""
    active_levels = []
    for elem in active:
        # Element number in active grid is 1-indexed, so subtract 1 for label_mat
        level = label_mat[elem-1][4]  # Level is stored in column 4
        active_levels.append(level)
    return active_levels

def get_element_distribution(solver):
    """Get distribution of element sizes."""
    element_sizes = np.diff(solver.xelem)
    return {
        'min': np.min(element_sizes),
        'max': np.max(element_sizes),
        'mean': np.mean(element_sizes),
        'std': np.std(element_sizes),
        'sizes': element_sizes.tolist()
    }

def action_name(action):
    """Get human-readable name for an action value."""
    if action == -1:
        return "Coarsen"
    elif action == 0:
        return "No Change"
    elif action == 1:
        return "Refine"
    return f"Unknown ({action})"

def generate_pdf_report(results_dir, report_name, test_description=None):
    """
    Generate a consolidated PDF report containing all visualizations created by the test script.
    
    Args:
        results_dir: Directory containing the test results and images
        report_name: Name for the PDF report
        test_description: Optional description to include in the report
    """
    import os
    import glob
    import datetime
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_pdf import PdfPages
    
    # Ensure the directory exists
    if not os.path.exists(results_dir):
        print(f"Results directory {results_dir} not found. Cannot generate report.")
        return
    
    # Define the report path
    report_path = os.path.join(results_dir, f"{report_name}.pdf")
    
    # Find all image files in the results directory
    image_files = []
    for ext in ['png', 'jpg', 'jpeg']:
        image_files.extend(glob.glob(os.path.join(results_dir, f"*.{ext}")))
    
    # Sort files by modification time to maintain logical order
    image_files.sort(key=os.path.getmtime)
    
    if not image_files:
        print(f"No image files found in {results_dir}. Cannot generate report.")
        return
    
    # Create PDF
    with PdfPages(report_path) as pdf:
        # Add a cover page with test information
        plt.figure(figsize=(8.5, 11))
        plt.axis('off')
        
        # Title and date information
        title_text = [
            f"# {report_name}",
            f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"Test Directory: {os.path.basename(results_dir)}"
        ]
        
        # Add description if provided
        if test_description:
            title_text.append("\n## Test Description")
            title_text.append(test_description)
        
        # Add file list
        title_text.append("\n## Visualizations Included")
        for i, img_file in enumerate(image_files):
            title_text.append(f"{i+1}. {os.path.basename(img_file)}")
        
        # Display text
        plt.text(0.1, 0.5, '\n'.join(title_text), 
                 fontsize=12, va='center', ha='left',
                 transform=plt.gca().transAxes,
                 family='monospace')
        
        pdf.savefig()
        plt.close()
        
        # Add each image to the PDF
        for img_file in image_files:
            # Create a figure with the same size as the image
            img = plt.imread(img_file)
            height, width = img.shape[:2]
            dpi = 100
            figsize = (width/dpi, height/dpi)
            
            # Create figure and add the image
            plt.figure(figsize=figsize, dpi=dpi)
            plt.axis('off')
            plt.imshow(img)
            
            # Add caption with filename
            plt.figtext(0.5, 0.01, os.path.basename(img_file), 
                       ha='center', fontsize=8)
            
            # Save to PDF
            pdf.savefig()
            plt.close()
    
    print(f"PDF report generated: {report_path}")
    return report_path

# Add the generate_pdf_report function (paste the function above)

def main():
    """Run all tests."""
    # Test solver reset with different refinement options
    solver_results = test_reset_with_refinement()
    
    # Test environment reset with different refinement options
    reset_results = test_env_reset_with_refinement()
    
    # Test coarsening behavior with different initial refinements
    coarsening_results = test_coarsening_behavior()
    
    # Test barrier function implications with different refinement levels
    barrier_values = test_barrier_function()
    
    # Generate a consolidated PDF report
    report_description = """
    This report contains the results of variable initial mesh refinement tests.
    
    Tests included:
    1. Solver reset with different refinement options
    2. Environment reset with different refinement options
    3. Coarsening behavior with different initial refinements
    4. Barrier function implications for different refinement levels
    
    These tests evaluate the implementation of variable initial mesh refinement
    and its effects on the agent's ability to learn coarsening behavior.
    """
    
    # Generate the PDF report for each test
    generate_pdf_report(
        os.path.join(PROJECT_ROOT, 'experiments', 'results', 'variable_refinement_test'),
        "Variable_Refinement_Test_Report",
        report_description
    )
    
    generate_pdf_report(
        os.path.join(PROJECT_ROOT, 'experiments', 'results', 'env_reset_test'),
        "Environment_Reset_Test_Report",
        "Tests for environment reset with different refinement options."
    )
    
    generate_pdf_report(
        os.path.join(PROJECT_ROOT, 'experiments', 'results', 'coarsening_test'),
        "Coarsening_Behavior_Test_Report",
        "Tests examining coarsening behavior with different initial refinements."
    )
    
    generate_pdf_report(
        os.path.join(PROJECT_ROOT, 'experiments', 'results', 'barrier_test'),
        "Barrier_Function_Test_Report",
        "Analysis of the barrier function and its implications for refinement rewards."
    )
    
    print("\nAll tests complete. PDF reports generated for each test directory.")

if __name__ == "__main__":
    main()

# def main():
#     """Run all tests."""
#     # Test solver reset with different refinement options
#     solver_results = test_reset_with_refinement()
    
#     # Test environment reset with different refinement options
#     reset_results = test_env_reset_with_refinement()
    
#     # Test coarsening behavior with different initial refinements
#     coarsening_results = test_coarsening_behavior()
    
#     # Test barrier function implications with different refinement levels
#     barrier_values = test_barrier_function()
    
#     print("\nAll tests complete.")

# if __name__ == "__main__":
#     main()