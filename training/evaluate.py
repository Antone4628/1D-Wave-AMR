"""
Evaluation script for trained DG AMR models.
"""

import os
import argparse
import numpy as np
from stable_baselines3 import A2C

from numerical.solvers.dg_wave_solver import DGWaveSolver
from numerical.environments.dg_amr_env import DGAMREnv
from utils.metrics import evaluate_model, calculate_mesh_metrics
from utils.visualization import plot_mesh_evolution, plot_error_convergence
from utils.logger import TrainingLogger

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-path", type=str, required=True,
                      help="Path to trained model")
    parser.add_argument("--n-episodes", type=int, default=10,
                      help="Number of episodes to evaluate")
    parser.add_argument("--output-dir", type=str, default="./evaluation",
                      help="Output directory for results")
    return parser.parse_args()

def main():
    args = parse_args()
    
    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)
    logger = TrainingLogger(args.output_dir)
    
    # Initialize solver and environment
    xelem = np.array([-1, -0.4, 0, 0.4, 1])
    solver = DGWaveSolver(
        nop=4,
        xelem=xelem,
        max_elements=40,
        max_level=4,
        courant_max=0.1,
        icase=1
    )
    env = DGAMREnv(solver=solver, element_budget=25, gamma_c=25.0)
    
    # Load model
    model = A2C.load(args.model_path, env=env)
    
    # Evaluate model
    metrics = evaluate_model(model, env, n_eval_episodes=args.n_episodes)
    logger.log_metrics(metrics)
    
    # Generate visualizations
    plot_mesh_evolution(env, save_dir=args.output_dir)
    
    # Track error convergence
    errors = []
    dofs = []
    
    for _ in range(args.n_episodes):
        obs = env.reset()
        done = False
        
        while not done:
            action, _states = model.predict(obs, deterministic=True)
            obs, reward, done, info = env.step(action)
            
            # Calculate error if exact solution available
            if hasattr(env.solver, 'get_exact_solution'):
                qe = env.solver.get_exact_solution()
                error = np.linalg.norm(env.solver.q - qe)
                errors.append(error)
                dofs.append(len(env.solver.active) * env.solver.ngl)
    
    # Plot error convergence
    if errors:
        plot_error_convergence(errors, dofs, save_dir=args.output_dir)
    
    # Log mesh metrics
    mesh_metrics = calculate_mesh_metrics(env)
    logger.log_metrics(mesh_metrics)

if __name__ == "__main__":
    main()