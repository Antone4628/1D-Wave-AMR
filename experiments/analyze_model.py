import numpy as np
import os
import sys
from stable_baselines3 import A2C

# Get absolute path to project root and add to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    '..'
))
sys.path.append(PROJECT_ROOT)

# Import your environment and solver classes
from numerical.solvers.dg_wave_solver_clean import DGWaveSolver
from numerical.environments.dg_amr_env_clean import DGAMREnv

def analyze_agent_behavior(model_path, gamma_c=10.0, num_episodes=3):
    """Analyze what actions the trained agent is taking"""
    
    # Initialize solver with standard parameters (same as in training)
    solver = DGWaveSolver(
        nop=4,
        xelem=np.array([-1, -0.4, 0, 0.4, 1]),
        max_elements=50,
        max_level=4,
        courant_max=0.1,
        icase=1,
        verbose=False
    )
    
    # Initialize environment
    env = DGAMREnv(
        solver=solver,
        element_budget=25,
        gamma_c=gamma_c,
        max_episode_steps=100
    )
    
    # Load trained model
    model = A2C.load(model_path)
    
    # Action mapping (adjust based on your actual action space)
    action_names = {
        -1: "Coarsen",
        0: "No change",
        1: "Refine"
    }
    
    # Track actions across episodes
    all_actions = []
    
    for episode in range(num_episodes):
        # Reset environment
        obs, _ = env.reset()
        done = False
        episode_actions = []
        step = 0
        
        print(f"\nEpisode {episode+1}:")
        print("-" * 50)
        
        while not done:
            # Get action from model
            action_array, _ = model.predict(obs, deterministic=True)
            action = int(action_array)  # Convert numpy array to integer
            
            # Store action
            episode_actions.append(action)  # Use the integer version
            
            # Print step info
            print(f"Step {step+1}: Action = {action} ({action_names.get(action, 'Unknown')})")
            print(f"  Current mesh size: {len(env.solver.xelem)-1} elements")
            
            # Take step
            obs, reward, done, truncated, info = env.step(action)
            
            # Print outcome of action
            print(f"  Result: reward = {reward:.2f}, mesh size after action: {len(env.solver.xelem)-1} elements")
            print()
            
            step += 1
            if truncated:
                break
        
        all_actions.extend(episode_actions)
    
    # Summarize action distribution
    action_counts = {}
    for action in all_actions:
        action_counts[action] = action_counts.get(action, 0) + 1
    
    print("\nAction Distribution Summary:")
    print("=" * 50)
    total_actions = len(all_actions)
    for action, count in sorted(action_counts.items()):
        percentage = (count / total_actions) * 100
        print(f"Action {action} ({action_names.get(action, 'Unknown')}): {count} times ({percentage:.1f}%)")
    
    return all_actions, action_counts

# Example usage
if __name__ == "__main__":
    import argparse
    import os
    
    # Get the path to the experiments directory (where this script is located)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    parser = argparse.ArgumentParser(description="Analyze agent behavior")
    parser.add_argument("--model", type=str, help="Path to trained model")
    parser.add_argument("--gamma-c", type=float, default=10.0, help="gamma_c value")
    parser.add_argument("--episodes", type=int, default=3, help="Number of episodes to analyze")
    
    args = parser.parse_args()
    
    # If model path is provided, use it, otherwise use default
    if args.model:
        model_path = args.model
        # Check if the path is relative to experiments directory
        if not os.path.isabs(model_path) and not model_path.startswith("experiments/"):
            # Convert relative path to absolute path
            model_path = os.path.join(current_dir, model_path)
    else:
        # Default model path
        model_path = os.path.join(current_dir, "results/gamma_c_10.0/run_20250226_101107/models/final_model.zip")
    
    # Ensure the model file exists
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at: {model_path}")
        
    print(f"Loading model from: {model_path}")
    analyze_agent_behavior(model_path, gamma_c=args.gamma_c, num_episodes=args.episodes)
# if __name__ == "__main__":
#     # Path to your trained model
#     model_path = "results/gamma_c_10.0/run_20250226_101107/models/final_model.zip"
    
#     # Run analysis
#     analyze_agent_behavior(model_path, gamma_c=10.0, num_episodes=2)