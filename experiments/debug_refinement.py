#!/usr/bin/env python
"""
Script to debug the early termination of highly refined mesh tests.
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

from numerical.solvers.dg_wave_solver_free import DGWaveSolver
from numerical.environments.dg_amr_env_clean import DGAMREnv, RewardCalculator

def debug_coarsening_behavior(verbose=True):
    """
    Debug the coarsening behavior with special focus on highly refined meshes.
    Adds extensive logging to identify when and why episodes terminate early.
    """
    print("\n" + "="*60)
    print("DEBUGGING COARSENING BEHAVIOR WITH INITIAL REFINEMENT")
    print("="*60)
    
    # Results directory
    results_dir = os.path.join(PROJECT_ROOT, 'experiments', 'results', 'debug_coarsening')
    os.makedirs(results_dir, exist_ok=True)
    
    # Test configurations - focus on highly refined case
    configs = [
        {"name": "No Refinement", "options": None},
        {"name": "Highly Refined (Lvl 3)", "options": {
            'refinement_mode': 'fixed',
            'refinement_level': 3,
        }}
    ]
    
    # Store detailed logs for each configuration
    debug_logs = {}
    coarsening_results = {}
    
    # Prepare log file
    log_path = os.path.join(results_dir, "debug_log.txt")
    with open(log_path, "w") as log_file:
        log_file.write("DEBUGGING COARSENING BEHAVIOR\n")
        log_file.write("="*60 + "\n\n")
    
    # Test each configuration with detailed logging
    for config in configs:
        print(f"\n{'-'*40}")
        print(f"Testing coarsening behavior with {config['name']}")
        print(f"{'-'*40}")
        
        # Log to file
        with open(log_path, "a") as log_file:
            log_file.write(f"\n{'-'*40}\n")
            log_file.write(f"Configuration: {config['name']}\n")
            log_file.write(f"{'-'*40}\n\n")
        
        # Create environment with smaller max_elements to ensure we can test buffer issues
        env = DGAMREnv(
            solver=DGWaveSolver(
                nop=3,
                xelem=np.array([-1, -0.4, 0, 0.4, 1]),
                max_elements=40,  # Deliberately smaller to check buffer issues
                max_level=4,
                courant_max=0.1,
                icase=1,
                verbose=False
            ),
            element_budget=30,
            gamma_c=25.0,
            max_episode_steps=100,
            verbose=verbose,
            rl_iterations_per_timestep=3,
            debug_training_cycle=verbose
        )
        
        # Reset environment with given options
        obs, info = env.reset(options=config["options"])
        
        # Extract initial state details
        initial_elements = len(env.solver.active)
        initial_resource = initial_elements / env.element_budget
        active_levels = get_active_levels(env.solver.active, env.solver.label_mat)
        level_distribution = {level: active_levels.count(level) for level in range(5)}
        
        # Log initial state
        initial_state = (
            f"Initial state:\n"
            f"  Elements: {initial_elements}/{env.element_budget}\n"
            f"  Resource usage: {initial_resource*100:.1f}%\n"
            f"  Level distribution: {level_distribution}\n"
            f"  Element count by level: {active_levels}\n"
            f"  Initial observation resource usage: {obs['resource_usage'][0]:.4f}\n"
        )
        print(initial_state)
        
        with open(log_path, "a") as log_file:
            log_file.write(initial_state)
        
        # Data collection
        steps = []
        element_counts = []
        resource_usages = []
        action_counts = {-1: 0, 0: 0, 1: 0}  # -1: coarsen, 0: no change, 1: refine
        rewards = []
        delta_us = []
        coarsening_rewards = []
        coarsening_success = []  # Track if coarsening actually reduced elements
        step_logs = []  # Detailed logs for each step
        
        # Run episode with specific coarsening tests
        for i in range(100):  # Increase max steps for testing
            # Choose action - try to coarsen more often
            if i % 5 < 4:  # Coarsen 4 out of 5 steps
                action = 0  # coarsen (0 maps to -1)
            else:
                action = np.random.choice([1, 2])  # no change or refine
            
            # Log pre-step state
            pre_elements = len(env.solver.active)
            pre_step_log = (
                f"Step {i} - Pre-action:\n"
                f"  Elements: {pre_elements}/{env.element_budget}\n"
                f"  Resource usage: {pre_elements/env.element_budget*100:.1f}%\n"
                f"  Action chosen: {action} (maps to {env.action_mapping[action]})\n"
            )
            if verbose:
                print(pre_step_log)
            
            # Take step
            obs, reward, term, trunc, info = env.step(action)
            
            # Map action to semantic value
            mapped_action = env.action_mapping[action]
            action_counts[mapped_action] += 1
            
            # Track if coarsening succeeded in reducing elements
            post_elements = len(env.solver.active)
            coarsening_success_flag = False
            if mapped_action == -1 and post_elements < pre_elements:
                coarsening_success_flag = True
                coarsening_success.append(1)
            elif mapped_action == -1:
                coarsening_success.append(0)
            
            # Collect data
            steps.append(i)
            element_counts.append(post_elements)
            resource_usages.append(post_elements / env.element_budget)
            rewards.append(reward)
            delta_us.append(info.get('delta_u', 0))
            
            # Only record rewards for coarsening actions
            if mapped_action == -1:
                coarsening_rewards.append(reward)
            
            # Log post-step state
            post_step_log = (
                f"Step {i} - Post-action:\n"
                f"  Elements: {post_elements}/{env.element_budget}\n"
                f"  Resource usage: {post_elements/env.element_budget*100:.1f}%\n"
                f"  Reward: {reward:.3f}\n"
                f"  Delta_u: {info.get('delta_u', 0):.6f}\n"
                f"  Took timestep: {info.get('took_timestep', False)}\n"
            )
            
            if mapped_action == -1:
                post_step_log += (
                    f"  Coarsening {'succeeded' if coarsening_success_flag else 'failed'}\n"
                    f"  Element change: {post_elements - pre_elements}\n"
                )
            
            if term or trunc:
                post_step_log += (
                    f"  Episode ended at step {i+1}.\n"
                    f"  Termination: {term}, Truncation: {trunc}\n"
                    f"  Reason: {info.get('reason', 'unknown')}\n"
                )
                
                if 'pre_termination_elements' in info:
                    post_step_log += (
                        f"  Pre-termination elements: {info['pre_termination_elements']}\n"
                        f"  Budget usage at violation: {info.get('budget_usage_percent', 0):.1f}%\n"
                        f"  Violation action: {info.get('violation_action', 'unknown')}\n"
                    )
            
            if verbose:
                print(post_step_log)
            
            # Combine logs and add to step logs
            step_logs.append(pre_step_log + post_step_log)
            
            # Write to log file
            with open(log_path, "a") as log_file:
                log_file.write(pre_step_log + post_step_log + "\n")
            
            if term or trunc:
                break
                
        # Calculate statistics
        action_distribution = {
            action: count / sum(action_counts.values()) 
            for action, count in action_counts.items()
        }
        avg_coarsening_reward = np.mean(coarsening_rewards) if coarsening_rewards else 0
        coarsening_success_rate = np.mean(coarsening_success) if coarsening_success else 0
        
        # Store detailed logs
        debug_logs[config["name"]] = {
            'initial_state': initial_state,
            'step_logs': step_logs,
            'coarsening_success_rate': coarsening_success_rate,
            'termination_reason': step_logs[-1] if step_logs else "No steps recorded"
        }
        
        # Store results for visualization
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
            'avg_coarsening_reward': avg_coarsening_reward,
            'coarsening_success': coarsening_success,
            'coarsening_success_rate': coarsening_success_rate
        }
        
        # Print summary
        summary = (
            f"\nSummary for {config['name']}:\n"
            f"  Steps completed: {len(steps)}\n"
            f"  Initial elements: {initial_elements}\n"
            f"  Final elements: {element_counts[-1] if element_counts else 'N/A'}\n"
            f"  Action distribution:\n"
        )
        for action, percentage in action_distribution.items():
            summary += f"    {action_name(action)}: {percentage*100:.1f}%\n"
        
        summary += (
            f"  Average coarsening reward: {avg_coarsening_reward:.3f}\n"
            f"  Coarsening success rate: {coarsening_success_rate*100:.1f}%\n"
        )
        
        print(summary)
        with open(log_path, "a") as log_file:
            log_file.write(summary + "\n")
    
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
    
    # Plot 4: Coarsening rewards and success rate
    plt.subplot(2, 2, 4)
    for name, result in coarsening_results.items():
        if result['coarsening_rewards']:
            plt.hist(result['coarsening_rewards'], alpha=0.5, label=name, bins=15)
    plt.xlabel('Reward')
    plt.ylabel('Count')
    plt.title('Distribution of Coarsening Rewards')
    plt.grid(True)
    plt.legend()
    
    # Add text annotation with success rates
    for i, name in enumerate(names):
        success_rate = coarsening_results[name]['coarsening_success_rate'] * 100
        plt.text(0.05, 0.9 - i*0.1, f"{name} success rate: {success_rate:.1f}%", 
                transform=plt.gca().transAxes)
    
    plt.tight_layout()
    plt.savefig(os.path.join(results_dir, 'debug_coarsening_behavior.png'))
    
    print(f"\nDebug complete. Results saved to {results_dir}")
    print(f"Detailed logs written to {log_path}")
    
    return coarsening_results, debug_logs

def inspect_element_levels(env, level):
    """
    Analyze the ability to coarsen elements at different refinement levels.
    Tests if elements can be coarsened and if siblings are properly identified.
    """
    print("\n" + "="*60)
    print(f"INSPECTING ELEMENTS AT LEVEL {level}")
    print("="*60)
    
    # Reset environment with fixed refinement
    options = {
        'refinement_mode': 'fixed',
        'refinement_level': level,
    }
    obs, info = env.reset(options=options)
    
    active = env.solver.active
    label_mat = env.solver.label_mat
    
    print(f"Initial state: {len(active)} elements")
    
    # Get refinement levels for active elements
    active_levels = []
    for elem in active:
        active_levels.append(label_mat[elem-1][4])  # Level is in column 4
    
    level_distribution = {level: active_levels.count(level) for level in range(5)}
    print(f"Level distribution: {level_distribution}")
    
    # Check parent-child relationships
    coarsenable_elements = 0
    non_coarsenable_elements = 0
    elements_with_siblings = 0
    
    for i, elem in enumerate(active):
        parent = label_mat[elem-1][1]
        level = label_mat[elem-1][4]
        
        print(f"\nElement {i} (real ID: {elem}):")
        print(f"  Level: {level}")
        print(f"  Parent: {parent}")
        
        # Find siblings
        sibling = None
        sibling_idx = None
        
        if parent != 0:
            if elem > 1 and label_mat[elem-2][1] == parent:
                sibling = elem - 1
                for idx, act_elem in enumerate(active):
                    if act_elem == sibling:
                        sibling_idx = idx
                        break
            elif elem < len(label_mat) and label_mat[elem][1] == parent:
                sibling = elem + 1
                for idx, act_elem in enumerate(active):
                    if act_elem == sibling:
                        sibling_idx = idx
                        break
        
        if sibling is not None and sibling_idx is not None:
            print(f"  Sibling: {sibling} (at index {sibling_idx})")
            elements_with_siblings += 1
            coarsenable_elements += 1
        else:
            print("  No active sibling found")
            if parent != 0:
                print(f"  Non-active sibling might be: {elem-1 if elem > 1 else elem+1}")
            non_coarsenable_elements += 1
    
    print("\nSummary:")
    print(f"  Elements with active siblings: {elements_with_siblings}/{len(active)} ({elements_with_siblings/len(active)*100:.1f}%)")
    print(f"  Coarsenable elements: {coarsenable_elements}/{len(active)} ({coarsenable_elements/len(active)*100:.1f}%)")
    print(f"  Non-coarsenable elements: {non_coarsenable_elements}/{len(active)} ({non_coarsenable_elements/len(active)*100:.1f}%)")
    
    # Perform test coarsening attempts
    print("\nPerforming test coarsening attempts:")
    
    for i in range(len(active)):
        # Create a copy of the initial environment for each test
        env_copy = DGAMREnv(
            solver=DGWaveSolver(
                nop=3,
                xelem=env.solver.xelem.copy(),
                max_elements=40,
                max_level=4,
                courant_max=0.1,
                icase=1,
                verbose=False
            ),
            element_budget=30,
            gamma_c=25.0,
            max_episode_steps=100,
            verbose=False
        )
        
        # Reset to same initial state
        env_copy.reset(options=options)
        
        # Set current element index
        env_copy.current_element_index = i
        
        # Attempt to coarsen
        print(f"\nAttempting to coarsen element {i} (real ID: {env_copy.solver.active[i]}):")
        pre_elements = len(env_copy.solver.active)
        
        # Take coarsening action (0 maps to -1)
        obs, reward, term, trunc, info = env_copy.step(0)
        
        post_elements = len(env_copy.solver.active)
        
        if post_elements < pre_elements:
            print(f"  SUCCESS: Elements reduced from {pre_elements} to {post_elements}")
            print(f"  Reward: {reward:.3f}")
        else:
            print(f"  FAILED: Elements remained at {post_elements}")
            print(f"  Reward: {reward:.3f}")
    
    return level_distribution

# Helper functions
def get_active_levels(active, label_mat):
    """Get refinement levels for active elements."""
    active_levels = []
    for elem in active:
        # Element number in active grid is 1-indexed, so subtract 1 for label_mat
        level = label_mat[elem-1][4]  # Level is stored in column 4
        active_levels.append(level)
    return active_levels

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
    """Run diagnostic tests."""
    # Debug coarsening behavior with detailed logging
    coarsening_results, debug_logs = debug_coarsening_behavior(verbose=True)
    
    # Create environment for element inspection
    env = DGAMREnv(
        solver=DGWaveSolver(
            nop=3,
            xelem=np.array([-1, -0.4, 0, 0.4, 1]),
            max_elements=40,
            max_level=4,
            courant_max=0.1,
            icase=1,
            verbose=False
        ),
        element_budget=30,
        gamma_c=25.0,
        max_episode_steps=100,
        verbose=False
    )
    
    # Inspect elements at different levels
    level_distribution_1 = inspect_element_levels(env, 1)
    level_distribution_3 = inspect_element_levels(env, 3)
    
    # Generate a comprehensive PDF report
    report_description = """
    This report contains diagnostic results for debugging the coarsening behavior
    with variable initial mesh refinement.
    
    Diagnostic tests included:
    1. Detailed coarsening behavior analysis with logging
    2. Element level inspection for level 1 refinement
    3. Element level inspection for level 3 refinement
    
    This debugging helps identify issues with the refinement initialization process
    and the coarsening action implementation.
    """
    
    generate_pdf_report(
        os.path.join(PROJECT_ROOT, 'experiments', 'results', 'debug_coarsening'),
        "Debug_Coarsening_Report",
        report_description
    )
    
    print("\nAll diagnostic tests complete. PDF report generated.")

if __name__ == "__main__":
    main()

# def main():
#     """Run diagnostic tests."""
#     # Debug coarsening behavior with detailed logging
#     coarsening_results, debug_logs = debug_coarsening_behavior(verbose=True)
    
#     # Create environment for element inspection
#     env = DGAMREnv(
#         solver=DGWaveSolver(
#             nop=3,
#             xelem=np.array([-1, -0.4, 0, 0.4, 1]),
#             max_elements=40,
#             max_level=4,
#             courant_max=0.1,
#             icase=1,
#             verbose=False
#         ),
#         element_budget=30,
#         gamma_c=25.0,
#         max_episode_steps=100,
#         verbose=False
#     )
    
#     # Inspect elements at different levels
#     level_distribution_1 = inspect_element_levels(env, 1)
#     level_distribution_3 = inspect_element_levels(env, 3)
    
#     print("\nAll diagnostic tests complete.")


# if __name__ == "__main__":
#     main()