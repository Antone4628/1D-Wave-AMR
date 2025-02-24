"""
Visualization utilities for DG AMR training.
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Optional, Tuple
from stable_baselines3.common.results_plotter import ts2xy, load_results
from stable_baselines3.common.monitor import LoadMonitorResultsError

class TrainingVisualizer:
    """Handles visualization of training metrics."""
    
    def __init__(self, log_dir: str):
        self.log_dir = log_dir
        self.monitor_path = os.path.join(log_dir, "monitor.csv")
        
    def load_data(self) -> Optional[pd.DataFrame]:
        """Load and process monitor data."""
        try:
            # Skip first row (metadata)
            df = pd.read_csv(self.monitor_path, skiprows=1)
            
            # Calculate timesteps
            df['timesteps'] = df['l'].cumsum()
            
            return df
        except Exception as e:
            print(f"Error loading monitor data: {e}")
            return None
            
    def smooth_data(self, data: np.ndarray, window: int = 10) -> np.ndarray:
        """Apply smoothing to noisy data."""
        if len(data) < window:
            return data
        return pd.Series(data).rolling(window=window, min_periods=1).mean().values
        
    def plot_training_results(self, save: bool = True) -> Optional[plt.Figure]:
        """Generate training visualization plots."""
        try:
            # Create figure with subplots
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
            
            try:
                # Try to load and plot results
                results = load_results(self.log_dir)
                if results is None or len(results) == 0:
                    raise LoadMonitorResultsError("No results found")
                    
                # Plot rewards
                x, y = ts2xy(results, 'timesteps')
                smoothed_rewards = self.smooth_data(y)
                
                ax1.plot(x, y, 'b-', alpha=0.3, label='Raw')
                ax1.plot(x, smoothed_rewards, 'r-', label='Smoothed')
                ax1.set_title('Training Rewards')
                ax1.set_xlabel('Timesteps')
                ax1.set_ylabel('Rewards')
                ax1.grid(True)
                ax1.legend()
                
                # Plot resource usage
                try:
                    x, y = ts2xy(results, 'resource_usage')
                    smoothed_usage = self.smooth_data(y)
                    
                    ax2.plot(x, y, 'b-', alpha=0.3, label='Raw')
                    ax2.plot(x, smoothed_usage, 'r-', label='Smoothed')
                    ax2.set_title('Resource Usage')
                    ax2.set_xlabel('Timesteps')
                    ax2.set_ylabel('Resource Usage')
                    ax2.grid(True)
                    ax2.legend()
                except:
                    ax2.text(0.5, 0.5, 'Resource usage data not available',
                            horizontalalignment='center',
                            verticalalignment='center')
                            
            except LoadMonitorResultsError:
                ax1.text(0.5, 0.5, 'No training data available yet',
                        horizontalalignment='center',
                        verticalalignment='center')
                ax2.text(0.5, 0.5, 'No training data available yet',
                        horizontalalignment='center',
                        verticalalignment='center')
                
            plt.tight_layout()
            
            if save:
                plot_path = os.path.join(self.log_dir, 'training_results.png')
                plt.savefig(plot_path)
                print(f"Saved training plots to {plot_path}")
                
            return fig
            
        except Exception as e:
            print(f"Error creating plots: {e}")
            return None

def plot_training_results(log_dir: str, total_timesteps: int):
    """
    Plot training metrics over time.
    This is kept for backward compatibility with existing code.
    """
    visualizer = TrainingVisualizer(log_dir)
    return visualizer.plot_training_results()

def plot_mesh_evolution(env, save_dir: str = None):
    """Plot mesh evolution over time."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
    
    # Plot solution
    ax1.plot(env.solver.coord, env.solver.q, 'b-', label='Numerical')
    if hasattr(env.solver, 'get_exact_solution'):
        qe = env.solver.get_exact_solution()
        ax1.plot(env.solver.coord, qe, 'r--', label='Exact')
    ax1.set_title('Solution')
    ax1.legend()
    
    # Plot mesh
    ax2.plot(env.solver.xelem, np.zeros_like(env.solver.xelem), 'k|', ms=20)
    ax2.set_title('Mesh')
    ax2.set_yticks([])
    
    plt.tight_layout()
    if save_dir:
        plt.savefig(os.path.join(save_dir, 'mesh_evolution.png'))
    return fig

def plot_error_convergence(errors, dofs, save_dir: str = None):
    """Plot error convergence vs degrees of freedom."""
    plt.figure(figsize=(8, 6))
    plt.loglog(dofs, errors, 'bo-')
    plt.grid(True)
    plt.xlabel('Degrees of Freedom')
    plt.ylabel('L2 Error')
    plt.title('Error Convergence')
    
    if save_dir:
        plt.savefig(os.path.join(save_dir, 'convergence.png'))
    return plt.gcf()






# """
# Visualization utilities for DG AMR training.
# """

# import os
# import numpy as np
# import matplotlib.pyplot as plt
# from stable_baselines3.common import results_plotter
# from stable_baselines3.common.results_plotter import load_results, ts2xy
# from stable_baselines3.common.monitor import LoadMonitorResultsError


# def plot_training_results(log_dir: str, total_timesteps: int):
#     """Plot training metrics over time."""
#     try:
#         # Create figure with subplots
#         fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
        
#         # Try to load and plot results
#         try:
#             # Plot rewards
#             x, y = ts2xy(load_results(log_dir), 'timesteps')
#             ax1.plot(x, y)
#             ax1.set_title('Training Rewards')
#             ax1.set_xlabel('Timesteps')
#             ax1.set_ylabel('Rewards')
            
#             # Plot resource usage if available
#             try:
#                 x, y = ts2xy(load_results(log_dir), 'resource_usage')
#                 ax2.plot(x, y)
#                 ax2.set_title('Resource Usage')
#                 ax2.set_xlabel('Timesteps')
#                 ax2.set_ylabel('Resource Usage')
#             except:
#                 ax2.text(0.5, 0.5, 'Resource usage data not available', 
#                         horizontalalignment='center',
#                         verticalalignment='center')
#         except LoadMonitorResultsError:
#             ax1.text(0.5, 0.5, 'No training data available yet', 
#                     horizontalalignment='center',
#                     verticalalignment='center')
#             ax2.text(0.5, 0.5, 'No training data available yet',
#                     horizontalalignment='center',
#                     verticalalignment='center')
            
#         plt.tight_layout()
        
#         # Save plot
#         plt.savefig(os.path.join(log_dir, 'training_results.png'))
#         return fig
#     except Exception as e:
#         print(f"Warning: Could not create training plots: {str(e)}")
#         return None
# # def plot_training_results(log_dir: str, total_timesteps: int):
# #     """Plot training metrics over time."""
# #     # Create figure with subplots
# #     fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
    
# #     # Plot rewards
# #     x, y = ts2xy(load_results(log_dir), 'timesteps')
# #     ax1.plot(x, y)
# #     ax1.set_title('Training Rewards')
# #     ax1.set_xlabel('Timesteps')
# #     ax1.set_ylabel('Rewards')
    
# #     # Plot resource usage
# #     x, y = ts2xy(load_results(log_dir), 'resource_usage')
# #     ax2.plot(x, y)
# #     ax2.set_title('Resource Usage')
# #     ax2.set_xlabel('Timesteps')
# #     ax2.set_ylabel('Resource Usage')
    
# #     plt.tight_layout()
# #     return fig

# def plot_mesh_evolution(env, save_dir: str = None):
#     """Plot mesh evolution over time."""
#     fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
    
#     # Plot solution
#     ax1.plot(env.solver.coord, env.solver.q, 'b-', label='Numerical')
#     if hasattr(env.solver, 'get_exact_solution'):
#         qe = env.solver.get_exact_solution()
#         ax1.plot(env.solver.coord, qe, 'r--', label='Exact')
#     ax1.set_title('Solution')
#     ax1.legend()
    
#     # Plot mesh
#     ax2.plot(env.solver.xelem, np.zeros_like(env.solver.xelem), 'k|', ms=20)
#     ax2.set_title('Mesh')
#     ax2.set_yticks([])
    
#     plt.tight_layout()
#     if save_dir:
#         plt.savefig(os.path.join(save_dir, 'mesh_evolution.png'))
#     return fig

# def plot_error_convergence(errors, dofs, save_dir: str = None):
#     """Plot error convergence vs degrees of freedom."""
#     plt.figure(figsize=(8, 6))
#     plt.loglog(dofs, errors, 'bo-')
#     plt.grid(True)
#     plt.xlabel('Degrees of Freedom')
#     plt.ylabel('L2 Error')
#     plt.title('Error Convergence')
    
#     if save_dir:
#         plt.savefig(os.path.join(save_dir, 'convergence.png'))
#     return plt.gcf()