"""
Simplified training script for DG AMR reinforcement learning.
"""

import os
import sys
import numpy as np
import gymnasium as gym
from stable_baselines3 import A2C
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.callbacks import BaseCallback
import matplotlib.pyplot as plt
from datetime import datetime

# Get absolute path to project root and add to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    '..'
))
sys.path.append(PROJECT_ROOT)

from numerical.solvers.dg_wave_solver import DGWaveSolver
from numerical.environments.dg_amr_env import DGAMREnv


class SimpleTrainingCallback(BaseCallback):
    """
    Callback for tracking and visualizing training progress.
    """
    def __init__(self, check_freq, log_dir, verbose=1):
        super().__init__(verbose)
        self.check_freq = check_freq
        self.log_dir = log_dir
        self.rewards = []
        self.episode_lengths = []
        self.last_info = None
        self.step_count = 0
        self.episode_count = 0
        
        # Create log directory if it doesn't exist
        print(f"\nInitializing callback...")
        print(f"Log directory: {self.log_dir}")
        os.makedirs(self.log_dir, exist_ok=True)
    

    def _on_step(self) -> bool:
        """Callback at each step of training."""
        self.step_count += 1
        print(f"\nCallback step: {self.num_timesteps}")
        
        # Check for episode completion
        episode_info = None
        episode_detected = False
        
        # Check in standard infos list (for vectorized environments)
        dones = self.locals.get('dones', [])
        infos = self.locals.get('infos', [])
        
        print(f"Callback locals keys: {list(self.locals.keys())}")
        print(f"Dones type: {type(dones)}, length: {len(dones) if hasattr(dones, '__len__') else 'unknown'}")
        print(f"Infos type: {type(infos)}, length: {len(infos) if hasattr(infos, '__len__') else 'unknown'}")
        
        try:
            if isinstance(dones, list) and isinstance(infos, list) and len(dones) == len(infos):
                for i, (done, info) in enumerate(zip(dones, infos)):
                    print(f"  Checking env {i}: done={done}, info keys={info.keys() if isinstance(info, dict) else 'not a dict'}")
                    if done and isinstance(info, dict) and 'episode' in info:
                        episode_info = info['episode']
                        episode_detected = True
                        print(f"*** EPISODE DETECTED in env {i} (from infos) ***")
                        break
        except Exception as e:
            print(f"Error checking infos: {e}")
        
        # Also check single info (for non-vectorized environments)
        done = self.locals.get('done', False)
        info = self.locals.get('info', {})
        
        print(f"Single done: {done}")
        print(f"Single info type: {type(info)}")
        if isinstance(info, dict):
            print(f"Single info keys: {info.keys()}")
        
        if not episode_detected and done and isinstance(info, dict) and 'episode' in info:
            episode_info = info['episode']
            episode_detected = True
            print(f"*** EPISODE DETECTED (from single info) ***")
        
        # Try direct manual detection
        if hasattr(self.model, 'env') and hasattr(self.model.env, 'buf_dones'):
            print(f"Model env buf_dones: {self.model.env.buf_dones}")
        
        # Direct check for episode data in the monitor
        if hasattr(self.model, 'env') and hasattr(self.model.env, 'envs'):
            for i, env in enumerate(self.model.env.envs):
                if hasattr(env, 'episode_returns'):
                    print(f"Env {i} episode returns: {env.episode_returns}")
        
        # If we detected an episode completion
        if episode_info:
            reward = episode_info.get('r', 0)
            length = episode_info.get('l', 0)
            
            self.rewards.append(reward)
            self.episode_lengths.append(length)
            self.episode_count += 1
            
            print(f"\nEpisode {self.episode_count} completed and SAVED:")
            print(f"Reward: {reward:.2f}")
            print(f"Length: {length}")
            
            # Create immediate test plot
            try:
                # Create plots directory
                plots_dir = os.path.join(self.log_dir, "plots")
                os.makedirs(plots_dir, exist_ok=True)
                
                # Create simple test plot
                plt.figure(figsize=(8, 6))
                plt.plot(range(len(self.rewards)), self.rewards, 'b.-')
                plt.title(f"Episodes Rewards (Total: {self.episode_count})")
                
                # Save direct test plot
                test_plot_path = os.path.join(plots_dir, f"callback_test_plot_{self.episode_count}.png")
                plt.savefig(test_plot_path)
                plt.close()
                
                print(f"Direct test plot saved: {test_plot_path}")
                print(f"File exists: {os.path.exists(test_plot_path)}")
            except Exception as e:
                print(f"Error creating direct plot: {e}")
                import traceback
                traceback.print_exc()
            
            # Create regular plot if check_freq criterion is met
            if self.episode_count % self.check_freq == 0:
                plot_path = self._plot_training_progress()
                if plot_path:
                    print(f"Saved training plot to: {plot_path}")
                else:
                    print("Failed to create training plot")
        
        return True
    


    #This one below was working. 
    # def _on_step(self) -> bool:
    #     """Called at each step."""
    #     # Debug output to understand what's available
    #     print(f"Callback step: {self.num_timesteps}")
        
    #     # Check if this step completed an episode
    #     episode_info = None
        
    #     # Try to get episode info from 'dones' and 'infos'
    #     dones = self.locals.get('dones', [])
    #     infos = self.locals.get('infos', [])
        
    #     if isinstance(dones, list) and isinstance(infos, list) and len(dones) == len(infos):
    #         for i, (done, info) in enumerate(zip(dones, infos)):
    #             if done and isinstance(info, dict) and 'episode' in info:
    #                 episode_info = info['episode']
    #                 print(f"*** EPISODE COMPLETED (from infos) - Reward: {episode_info['r']}, Length: {episode_info['l']} ***")
    #                 break
        
    #     # Second approach: directly check the done and info values
    #     done = self.locals.get('done', False)
    #     info = self.locals.get('info', {})
        
    #     if done and isinstance(info, dict) and 'episode' in info:
    #         episode_info = info['episode']
    #         print(f"*** EPISODE COMPLETED (from info) - Reward: {episode_info['r']}, Length: {episode_info['l']} ***")
        
    #     # If we found episode info, store it and maybe create a plot
    #     if episode_info:
    #         reward = episode_info.get('r', 0)
    #         length = episode_info.get('l', 0)
            
    #         self.rewards.append(reward)
    #         self.episode_lengths.append(length)
    #         self.episode_count += 1
            
    #         print(f"Added episode #{self.episode_count} to records. Total rewards stored: {len(self.rewards)}")
            
    #         # Create an immediate test plot regardless of check_freq
    #         try:
    #             # Create plots directory
    #             plots_dir = os.path.join(self.log_dir, "plots")
    #             os.makedirs(plots_dir, exist_ok=True)
                
    #             # Create simple test plot
    #             plt.figure(figsize=(8, 6))
    #             plt.plot(self.rewards, 'b.-')
    #             plt.title(f"Episodes Rewards (Total: {self.episode_count})")
                
    #             # Save plot
    #             test_plot_path = os.path.join(plots_dir, f"episode_rewards_{self.episode_count}.png")
    #             plt.savefig(test_plot_path)
    #             plt.close()
                
    #             print(f"Direct test plot saved to: {test_plot_path}")
    #             print(f"File exists: {os.path.exists(test_plot_path)}")
    #         except Exception as e:
    #             print(f"Error saving direct plot: {e}")
    #             import traceback
    #             traceback.print_exc()
        
    #     return True
    

    # def _on_step(self) -> bool:
    #     self.step_count += 1
    #     print(f"\nCallback step: {self.num_timesteps}")
        
    #     # In Stable Baselines3, episode information is passed through the 'infos' list
    #     infos = self.locals.get('infos', [])
    #     dones = self.locals.get('dones', [])
        
    #     # Print debug information
    #     print(f"Infos type: {type(infos)}, length: {len(infos) if hasattr(infos, '__len__') else 'N/A'}")
    #     if isinstance(infos, list) and len(infos) > 0:
    #         print(f"First info keys: {infos[0].keys() if isinstance(infos[0], dict) else 'not a dict'}")
        
    #     # Check if any environment completed an episode
    #     episode_detected = False
    #     for i, (info, done) in enumerate(zip(infos, dones) if len(infos) == len(dones) else []):
    #         if done and isinstance(info, dict) and 'episode' in info:
    #             episode_detected = True
    #             print("*** EPISODE DETECTED IN CALLBACK ***")
    #             episode_info = info['episode']
                
    #             # Save episode statistics
    #             reward = episode_info.get('r', 0)
    #             ep_len = episode_info.get('l', 0)
    #             self.rewards.append(reward)
    #             self.episode_lengths.append(ep_len)
    #             self.episode_count += 1
                
    #             print(f"\nEpisode {self.episode_count} completed:")
    #             print(f"Reward: {reward:.2f}")
    #             print(f"Length: {ep_len}")
    #             print(f"Total rewards collected: {len(self.rewards)}")
                
    #             # Create plot if we've reached check frequency
    #             if self.episode_count % self.check_freq == 0:
    #                 plot_path = self._plot_training_progress()
    #                 if plot_path:
    #                     print(f"Saved training plot to: {plot_path}")
    #                 else:
    #                     print("Failed to create training plot")
                
    #             # Only handle one episode completion per step
    #             break
        
    #     # If no episode detected through standard means, check for a single info dict
    #     if not episode_detected:
    #         info = self.locals.get('info')
    #         done = self.locals.get('done', False)
            
    #         if done and isinstance(info, dict) and 'episode' in info:
    #             print("*** EPISODE DETECTED IN CALLBACK (single info) ***")
    #             episode_info = info['episode']
                
    #             # Save episode statistics
    #             reward = episode_info.get('r', 0)
    #             ep_len = episode_info.get('l', 0)
    #             self.rewards.append(reward)
    #             self.episode_lengths.append(ep_len)
    #             self.episode_count += 1
                
    #             print(f"\nEpisode {self.episode_count} completed:")
    #             print(f"Reward: {reward:.2f}")
    #             print(f"Length: {ep_len}")
    #             print(f"Total rewards collected: {len(self.rewards)}")
                
    #             # Create plot if we've reached check frequency 
    #             if self.episode_count % self.check_freq == 0:
    #                 plot_path = self._plot_training_progress()
    #                 if plot_path:
    #                     print(f"Saved training plot to: {plot_path}")
    #                 else:
    #                     print("Failed to create training plot")
        
    #     return True

    def _plot_training_progress(self):
        """Create plots of training progress."""
        try:
            # Create plots directory
            plots_dir = os.path.join(self.log_dir, "plots")
            os.makedirs(plots_dir, exist_ok=True)
            
            # Create figure
            plt.figure(figsize=(12, 5))
            
            # Plot rewards
            plt.subplot(1, 2, 1)
            plt.plot(self.rewards, 'bo-')
            plt.title(f"Episode Rewards (Total: {self.episode_count})")
            plt.xlabel("Episode")
            plt.ylabel("Reward")
            plt.grid(True, alpha=0.3)
            
            # Plot episode lengths
            plt.subplot(1, 2, 2)
            plt.plot(self.episode_lengths, 'ro-')
            plt.title("Episode Lengths")
            plt.xlabel("Episode")
            plt.ylabel("Steps")
            plt.grid(True, alpha=0.3)
            
            plt.tight_layout()
            
            # Save with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            plot_path = os.path.join(plots_dir, f"training_progress_ep{self.episode_count}_{timestamp}.png")
            plt.savefig(plot_path)
            plt.close()
            
            return plot_path
            
        except Exception as e:
            print(f"Error creating/saving plot: {e}")
            return None

    # def _plot_training_progress(self):
    #     """Create simple training progress plot with enhanced debugging."""
    #     try:
    #         print("\n=== DEBUG: PLOT CREATION ATTEMPT ===")
            
    #         # Create plots directory with absolute path - make sure this exists
    #         plots_dir = os.path.join(os.path.abspath(self.log_dir), "plots")
    #         os.makedirs(plots_dir, exist_ok=True)
    #         print(f"Created plots directory: {plots_dir}")
    #         print(f"Directory exists: {os.path.exists(plots_dir)}")
            
    #         # Check rewards data
    #         if len(self.rewards) == 0:
    #             print("No reward data to plot yet")
    #             return None
            
    #         # Create figure
    #         plt.figure(figsize=(10, 5))
            
    #         # Plot rewards
    #         plt.subplot(1, 2, 1)
    #         plt.plot(self.rewards, 'bo-')
    #         plt.title("Episode Rewards")
    #         plt.xlabel("Episode")
    #         plt.ylabel("Reward")
            
    #         # Plot episode lengths
    #         plt.subplot(1, 2, 2)
    #         plt.plot(self.episode_lengths, 'ro-')
    #         plt.title("Episode Lengths")
    #         plt.xlabel("Episode")
    #         plt.ylabel("Length")
            
    #         plt.tight_layout()
            
    #         # Save plot with a unique filename
    #         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    #         plot_path = os.path.join(plots_dir, f'training_progress_ep{self.episode_count}_{timestamp}.png')
    #         print(f"Attempting to save plot to: {plot_path}")
            
    #         plt.savefig(plot_path)
    #         print(f"Plot saved successfully: {os.path.exists(plot_path)}")
            
    #         # Check file size to verify it's not empty
    #         file_size = os.path.getsize(plot_path) if os.path.exists(plot_path) else 0
    #         print(f"Plot file size: {file_size} bytes")
            
    #         plt.close()
    #         print("=== PLOT CREATION COMPLETE ===\n")
    #         return plot_path
            
    #     except Exception as e:
    #         import traceback
    #         print(f"ERROR creating/saving plot: {str(e)}")
    #         traceback.print_exc()
    #         print(f"Current directory: {os.getcwd()}")
    #         print(f"Log directory: {self.log_dir}")
    #         return None

    # def _plot_training_progress(self):
    #     """Create simple training progress plot with enhanced debugging."""
    #     try:
    #         print("\n=== DEBUG: PLOT CREATION ATTEMPT ===")
            
    #         # Check if we have enough data to plot
    #         if len(self.rewards) == 0:
    #             print("No reward data to plot yet")
    #             return None
                
    #         print(f"Creating plot with {len(self.rewards)} episodes of reward data")
    #         print(f"Reward data: {self.rewards}")
    #         print(f"Episode length data: {self.episode_lengths}")
            
    #         # Create plots directory with absolute path
    #         plots_dir = os.path.join(os.path.abspath(self.log_dir), "plots")
    #         os.makedirs(plots_dir, exist_ok=True)
    #         print(f"Created plots directory: {plots_dir}")
    #         print(f"Directory exists: {os.path.exists(plots_dir)}")
            
    #         # Create figure with error handling
    #         try:
    #             plt.figure(figsize=(10, 5))
    #             print("Successfully created matplotlib figure")
    #         except Exception as fig_error:
    #             print(f"Error creating figure: {fig_error}")
    #             return None
            
    #         # Create plots with error handling
    #         try:
    #             # Plot rewards
    #             plt.subplot(1, 2, 1)
    #             plt.plot(self.rewards, 'bo-')
    #             plt.title("Episode Rewards")
    #             plt.xlabel("Episode")
    #             plt.ylabel("Reward")
    #             print("Successfully created rewards subplot")
                
    #             # Plot episode lengths
    #             plt.subplot(1, 2, 2)
    #             plt.plot(self.episode_lengths, 'ro-')
    #             plt.title("Episode Lengths")
    #             plt.xlabel("Episode")
    #             plt.ylabel("Length")
    #             print("Successfully created episode lengths subplot")
                
    #             plt.tight_layout()
    #             print("Applied tight_layout")
    #         except Exception as plot_error:
    #             print(f"Error creating subplots: {plot_error}")
    #             plt.close()
    #             return None
            
    #         # Save plot with informative filename
    #         try:
    #             # Use both timestamp and episode count in filename
    #             timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    #             plot_path = os.path.join(
    #                 plots_dir, 
    #                 f'training_progress_ep{self.episode_count}_{timestamp}.png'
    #             )
    #             print(f"Attempting to save plot to: {plot_path}")
                
    #             plt.savefig(plot_path)
                
    #             # Verify file was created
    #             if os.path.exists(plot_path):
    #                 file_size = os.path.getsize(plot_path)
    #                 print(f"Plot saved successfully! File size: {file_size} bytes")
    #             else:
    #                 print("File was not created despite no exception")
                    
    #         except Exception as save_error:
    #             print(f"Error saving plot: {save_error}")
    #             plt.close()
    #             return None
                
    #         # Clean up
    #         plt.close()
    #         print("=== PLOT CREATION COMPLETE ===\n")
    #         return plot_path
            
    #     except Exception as e:
    #         import traceback
    #         print(f"ERROR in _plot_training_progress: {str(e)}")
    #         traceback.print_exc()
    #         print(f"Current directory: {os.getcwd()}")
    #         print(f"Log directory: {self.log_dir}")
    #         return None

    # def _plot_training_progress(self):
    #     """Create simple training progress plot with enhanced debugging."""
    #     try:
    #         print("\n=== DEBUG: PLOT CREATION ATTEMPT ===")
    #         print(f"Working directory: {os.getcwd()}")
            
    #         # Create plots directory with absolute path
    #         plots_dir = os.path.join(os.path.abspath(self.log_dir), "plots")
    #         os.makedirs(plots_dir, exist_ok=True)
    #         print(f"Created plots directory: {plots_dir}")
    #         print(f"Directory exists: {os.path.exists(plots_dir)}")
            
    #         # Check rewards data
    #         print(f"Rewards data: {self.rewards}")
    #         print(f"Episode lengths data: {self.episode_lengths}")
    #         if len(self.rewards) == 0:
    #             print("No reward data to plot yet")
    #             return None
            
    #         # Create figure
    #         print("Creating matplotlib figure...")
    #         plt.figure(figsize=(10, 5))
            
    #         # Plot rewards
    #         print("Adding rewards subplot...")
    #         plt.subplot(1, 2, 1)
    #         plt.plot(self.rewards, 'bo-')
    #         plt.title("Episode Rewards")
    #         plt.xlabel("Episode")
    #         plt.ylabel("Reward")
            
    #         # Plot episode lengths
    #         print("Adding episode lengths subplot...")
    #         plt.subplot(1, 2, 2)
    #         plt.plot(self.episode_lengths, 'ro-')
    #         plt.title("Episode Lengths")
    #         plt.xlabel("Episode")
    #         plt.ylabel("Length")
            
    #         plt.tight_layout()
            
    #         # Save plot with timestamp
    #         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    #         plot_path = os.path.join(plots_dir, f'training_progress_{timestamp}.png')
    #         print(f"Attempting to save plot to: {plot_path}")
            
    #         plt.savefig(plot_path)
    #         print(f"Plot saved successfully: {os.path.exists(plot_path)}")
            
    #         # Check file size to verify it's not empty
    #         if os.path.exists(plot_path):
    #             file_size = os.path.getsize(plot_path)
    #             print(f"Plot file size: {file_size} bytes")
            
    #         plt.close()
    #         print("=== PLOT CREATION COMPLETE ===\n")
    #         return plot_path
            
    #     except Exception as e:
    #         import traceback
    #         print(f"ERROR creating/saving plot: {str(e)}")
    #         traceback.print_exc()
    #         print(f"Current directory: {os.getcwd()}")
    #         print(f"Log directory: {self.log_dir}")
    #         return None
    
    # def _plot_training_progress(self):
    #     """Create simple training progress plot."""
    #     try:
    #         print("\nAttempting to create training plot...")
            
    #         # Create plots directory
    #         plots_dir = os.path.join(self.log_dir, "plots")
    #         os.makedirs(plots_dir, exist_ok=True)
    #         print(f"Created plots directory: {plots_dir}")
            
    #         # Check if we have any data to plot
    #         print(f"Current rewards data: {self.rewards}")
    #         if len(self.rewards) == 0:
    #             print("No reward data to plot yet")
    #             return None
            
    #         # Create figure
    #         plt.figure(figsize=(10, 5))
            
    #         # Plot rewards
    #         plt.subplot(1, 2, 1)
    #         plt.plot(self.rewards, 'bo-')  # Blue line with circles
    #         plt.title("Episode Rewards")
    #         plt.xlabel("Episode")
    #         plt.ylabel("Reward")
            
    #         # Plot episode lengths
    #         plt.subplot(1, 2, 2)
    #         plt.plot(self.episode_lengths, 'ro-')  # Red line with circles
    #         plt.title("Episode Lengths")
    #         plt.xlabel("Episode")
    #         plt.ylabel("Length")
            
    #         plt.tight_layout()
            
    #         # Save plot with timestamp
    #         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    #         plot_path = os.path.join(plots_dir, f'training_progress_{timestamp}.png')
    #         print(f"Saving plot to: {plot_path}")
            
    #         plt.savefig(plot_path)
    #         print("Successfully saved plot")
            
    #         plt.close()
    #         return plot_path
            
    #     except Exception as e:
    #         import traceback
    #         print(f"Error creating/saving plot: {str(e)}")
    #         traceback.print_exc()
    #         print(f"Current directory: {os.getcwd()}")
    #         print(f"Log directory: {self.log_dir}")
    #         return None
# class SimpleTrainingCallback(BaseCallback):
#     """
#     Callback for tracking and visualizing training progress.
#     """
#     def __init__(self, check_freq, log_dir, verbose=1):
#         super().__init__(verbose)
#         self.check_freq = check_freq
#         self.log_dir = log_dir
#         self.rewards = []
#         self.episode_lengths = []
#         self.last_info = None
#         self.step_count = 0
#         self.episode_count = 0
        
#         print(f"\nInitializing callback...")
#         print(f"Log directory: {self.log_dir}")
#         os.makedirs(self.log_dir, exist_ok=True)
        
#     def _on_step(self) -> bool:
#             self.step_count += 1
#             print(f"\nTraining Timestep {self.step_count} (Total requested: {self.locals['total_timesteps']})")
            
#             # Check for episode completion
#             info = self.locals.get('info')
#             if info is not None and 'episode' in info:
#                 self.episode_count += 1
#                 episode_info = info['episode']
#                 self.rewards.append(episode_info['r'])
#                 self.episode_lengths.append(episode_info['l'])
#                 self.last_info = info
                
#                 print(f"\nEpisode {self.episode_count} completed:")
#                 print(f"Reward: {episode_info['r']:.2f}")
#                 print(f"Length: {episode_info['l']}")
                
#                 if len(self.rewards) % self.check_freq == 0:
#                     plot_path = self._plot_training_progress()
#                     if plot_path:
#                         print(f"Saved training plot to: {plot_path}")
            
#             return True
    
#     def _plot_training_progress(self):
#         """Create simple training progress plot."""
#         try:
#             print("\nAttempting to create training plot...")
            
#             # Check if we have any data to plot
#             if len(self.rewards) == 0:
#                 print("No reward data to plot yet")
#                 return None
                
#             print(f"Creating plot with {len(self.rewards)} episodes of data")
            
#             # Create plots directory
#             plots_dir = os.path.join(self.log_dir, "plots")
#             os.makedirs(plots_dir, exist_ok=True)
#             print(f"Created/verified plots directory: {plots_dir}")
            
#             # Create figure
#             plt.figure(figsize=(10, 5))
            
#             # Plot rewards
#             plt.subplot(1, 2, 1)
#             plt.plot(self.rewards)
#             plt.title("Episode Rewards")
#             plt.xlabel("Episode")
#             plt.ylabel("Reward")
#             print("Created rewards subplot")
            
#             # Plot episode lengths
#             plt.subplot(1, 2, 2)
#             plt.plot(self.episode_lengths)
#             plt.title("Episode Lengths")
#             plt.xlabel("Episode")
#             plt.ylabel("Length")
#             print("Created episode lengths subplot")
            
#             plt.tight_layout()
            
#             # Save plot with timestamp
#             timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#             plot_path = os.path.join(plots_dir, f'training_progress_{timestamp}.png')
#             print(f"Attempting to save plot to: {plot_path}")
            
#             plt.savefig(plot_path)
#             print("Successfully saved plot")
            
#             plt.close()
#             return plot_path
            
#         except Exception as e:
#             print(f"Error creating/saving plot: {str(e)}")
#             print(f"Current directory: {os.getcwd()}")
#             print(f"Log directory: {self.log_dir}")
#             return None

class TimestepLimitCallback(BaseCallback):
    """Callback for stopping training when total timesteps is reached."""
    
    def __init__(self, total_timesteps, verbose=0):
        super().__init__(verbose)
        self.total_timesteps = total_timesteps
        
    def _on_step(self) -> bool:
        # Check if we've exceeded total timesteps
        if self.num_timesteps >= self.total_timesteps:
            print(f"\nReached {self.total_timesteps} timesteps, stopping training")
            return False
        return True
    
# Add this after your callback classes but before the train_amr_agent function
class EpisodeTracker:
    def __init__(self):
        self.rewards = []
        self.lengths = []
        self.count = 0
        
    def __call__(self, reward, length):
        self.rewards.append(reward)
        self.lengths.append(length)
        self.count += 1
        print(f"EPISODE TRACKER: Episode {self.count} complete - Reward: {reward:.2f}, Length: {length}")
        
    def plot_progress(self, save_path):
        """Create a plot of episode rewards and lengths."""
        if len(self.rewards) == 0:
            return None
            
        plt.figure(figsize=(12, 5))
        
        # Plot rewards
        plt.subplot(1, 2, 1)
        plt.plot(self.rewards, 'bo-')
        plt.title("Episode Rewards")
        plt.xlabel("Episode")
        plt.ylabel("Reward")
        plt.grid(True, alpha=0.3)
        
        # Plot lengths
        plt.subplot(1, 2, 2)
        plt.plot(self.lengths, 'ro-')
        plt.title("Episode Lengths")
        plt.xlabel("Episode")
        plt.ylabel("Steps")
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
        
        return save_path
# class TimestepLimitCallback(BaseCallback):
#     """Callback for stopping training when total timesteps is reached."""
    
#     def __init__(self, total_timesteps, verbose=0):
#         super().__init__(verbose)
#         self.total_timesteps = total_timesteps
#         self._continue_training = True
        
#     def _on_step(self) -> bool:
#         # More assertive print to verify callback is executing
#         print(f"TimestepLimitCallback: Step {self.num_timesteps}/{self.total_timesteps}")
        
#         # Check if we've exceeded total timesteps
#         if self.num_timesteps >= self.total_timesteps:
#             print(f"\n*** LIMIT REACHED: {self.num_timesteps} >= {self.total_timesteps} ***")
#             print(f"*** STOPPING TRAINING NOW ***")
#             self._continue_training = False
#             # Force stop by raising an exception
#             raise StopIteration("Reached total timesteps limit")
            
#         return self._continue_training

# def train_amr_agent(total_timesteps=15, element_budget=25):
#     """
#     Train AMR agent with simplified setup.
#     """
#     print(f"\nStarting training for {total_timesteps} timesteps...")
    
#         # Create timestamp for this training run
#     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
#     # Create logs directory structure
#     log_dir = os.path.join(PROJECT_ROOT, "logs", f"training_{timestamp}")
#     os.makedirs(log_dir, exist_ok=True)
#     print(f"Created log directory: {log_dir}")
    
#     # ====== TEST PLOT CREATION DIRECTLY ======
#     print("\n=== TESTING DIRECT PLOT CREATION ===")
#     test_plots_dir = os.path.join(log_dir, "plots")
#     os.makedirs(test_plots_dir, exist_ok=True)
#     print(f"Test plots directory created: {test_plots_dir}")
#     print(f"Directory exists: {os.path.exists(test_plots_dir)}")
    
#     # Create a simple test plot
#     try:
#         plt.figure(figsize=(8, 6))
#         plt.plot([1, 2, 3, 4], [10, 20, 15, 25], 'bo-')
#         plt.title("Test Plot")
#         plt.xlabel("X")
#         plt.ylabel("Y")
        
#         # Save to test location
#         test_plot_path = os.path.join(test_plots_dir, "test_plot.png")
#         plt.savefig(test_plot_path)
#         plt.close()
        
#         print(f"Test plot saved to: {test_plot_path}")
#         print(f"Test plot file exists: {os.path.exists(test_plot_path)}")
#         print(f"Test plot file size: {os.path.getsize(test_plot_path) if os.path.exists(test_plot_path) else 0} bytes")
#     except Exception as e:
#         print(f"Error creating test plot: {e}")
#         import traceback
#         traceback.print_exc()
#     print("=== TEST PLOT CREATION COMPLETE ===\n")
#     # ==========================================

#         # Create the episode tracker
#     episode_tracker = EpisodeTracker()
    
#     # Initialize solver and environment
#     xelem = np.array([-1, -0.4, 0, 0.4, 1])
#     solver = DGWaveSolver(
#         nop=4,
#         xelem=xelem, 
#         max_elements=40,
#         max_level=4,
#         courant_max=0.1,
#         icase=1
#     )
    
#     # env = DGAMREnv(
#     #     solver=solver,
#     #     element_budget=element_budget,
#     #     gamma_c=25.0
#     # )

#     # Create the base environment
#     base_env = DGAMREnv(
#         solver=solver,
#         element_budget=element_budget,
#         gamma_c=25.0
#     )
    
#     # env.register_callback(episode_tracker)
#     # Add monitoring
#     # monitor_path = os.path.join(log_dir, "monitor.csv")
#     # print(f"Monitor log path: {monitor_path}")
#     # env = Monitor(env, monitor_path)
#     # Register the tracker with the BASE environment
#     base_env.register_callback(episode_tracker)
#     print("Episode tracker registered with base environment")
    
#     # IMPORTANT: Store a reference to the base env for direct access
#     # This ensures we can access it even after wrapping
#     global_env_ref = base_env  
    
#     # Now create monitor wrapper
#     monitor_path = os.path.join(log_dir, "monitor.csv")
#     monitored_env = Monitor(base_env, monitor_path)
    
#     # This is the environment that will be used by Stable Baselines
#     env = monitored_env
    
#     # Create callbacks
#     training_callback = SimpleTrainingCallback(
#         check_freq=1,
#         log_dir=log_dir,
#         verbose=1
#     )

#     timestep_limit_callback = TimestepLimitCallback(
#         total_timesteps=total_timesteps,
#         verbose=1
#     )

#     # Combine callbacks
#     callbacks = [timestep_limit_callback, training_callback]
    
#     # Initialize model
#     model = A2C(
#         "MultiInputPolicy",
#         env,
#         verbose=1,
#         learning_rate=0.0003,
#         n_steps=5,  # Set this small for testing
#         ent_coef=0.01
#     )
    
#     print(f"\nModel parameters:")
#     print(f"Learning rate: {model.learning_rate}")
#     print(f"N steps: {model.n_steps}")
#     print(f"Total timesteps requested: {total_timesteps}")
    
#     try:
#         # Train model with combined callbacks
#         model.learn(
#             total_timesteps=total_timesteps,
#             callback=callbacks
#         )
#     except StopIteration as e:
#         print(f"\nTraining stopped: {e}")
#     except KeyboardInterrupt:
#         print("\nTraining interrupted by user")
#     except Exception as e:
#         print(f"\nTraining error: {e}")
#     finally:
#         print(f"\nTraining completed or stopped:")
#         print(f"Total episodes: {len(training_callback.rewards)}")
#         print(f"Total steps: {timestep_limit_callback.num_timesteps}")
        
#         # Save final model
#         model_path = os.path.join(log_dir, "final_model.zip")
#         model.save(model_path)
#         print(f"Model saved to: {model_path}")

#     # After training completes, check if any episodes were stored
#     print(f"\nPost-training analysis:")
#     print(f"Callback episode count: {training_callback.episode_count}")
#     print(f"Rewards stored: {training_callback.rewards}")
#     print(f"Episode lengths stored: {training_callback.episode_lengths}")

#     # After training, create a plot from the tracker
#     if episode_tracker.count > 0:
#         plots_dir = os.path.join(log_dir, "plots")
#         os.makedirs(plots_dir, exist_ok=True)
        
#         tracker_plot_path = os.path.join(plots_dir, "episode_tracker_results.png")
#         episode_tracker.plot_progress(tracker_plot_path)
#         print(f"Episode tracker plot saved to: {tracker_plot_path}")
#         print(f"Total episodes tracked: {episode_tracker.count}")
#     else:
#         print("No episodes were tracked by the episode tracker.")

#     # Manually create a final plot
#     try:
#         plots_dir = os.path.join(log_dir, "plots")
#         os.makedirs(plots_dir, exist_ok=True)
        
#         # Create final plot
#         plt.figure(figsize=(8, 6))
#         if len(training_callback.rewards) > 0:
#             plt.bar(range(len(training_callback.rewards)), training_callback.rewards)
#             plt.title("Episode Rewards (Final)")
#             plt.xlabel("Episode")
#             plt.ylabel("Reward")
#         else:
#             plt.text(0.5, 0.5, "No episodes completed", ha='center', va='center')
#             plt.title("No Episode Data")
        
#         final_plot_path = os.path.join(plots_dir, "final_rewards_plot.png")
#         plt.savefig(final_plot_path)
#         plt.close()
        
#         print(f"Final plot saved to: {final_plot_path}")
#         print(f"Final plot exists: {os.path.exists(final_plot_path)}")
#     except Exception as e:
#         print(f"Error creating final plot: {e}")
#     # ===============================================


#     print(f"\nEpisode tracker status:")
#     print(f"Tracker count: {episode_tracker.count}")
#     print(f"Tracker rewards: {episode_tracker.rewards}")
#     print(f"Tracker lengths: {episode_tracker.lengths}")

#     # Attempt to directly call tracker to test it
#     print("\nTesting tracker with dummy data...")
#     episode_tracker(100.0, 20)
#     print(f"Tracker count after test: {episode_tracker.count}")

#     try:
#         # Get the unwrapped environment
#         if hasattr(model, 'get_env') and hasattr(model.get_env(), 'envs'):
#             # For vectorized environments
#             base_env = model.get_env().envs[0]
            
#             # Check if it has our tracking attributes
#             if hasattr(base_env, 'episode_rewards'):
#                 plots_dir = os.path.join(log_dir, "plots")
#                 os.makedirs(plots_dir, exist_ok=True)
                
#                 env_plot_path = os.path.join(plots_dir, "environment_episodes.png")
#                 base_env.plot_episodes(env_plot_path)
                
#                 print(f"Environment tracked {base_env.episode_count} episodes")
#                 print(f"Environment episode plot saved to: {env_plot_path}")
#     except Exception as e:
#         print(f"Error accessing environment data: {e}")
    
#     return model, training_callback, timestep_limit_callback

def train_amr_agent(total_timesteps=500, element_budget=25):
    """
    Train AMR agent with simplified setup and TensorBoard logging.
    """
    # Create timestamp for this training run
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Create logs directory structure
    log_dir = os.path.join(PROJECT_ROOT, "logs", f"training_{timestamp}")
    os.makedirs(log_dir, exist_ok=True)
    print(f"Created log directory: {log_dir}")
    
    # Create tensorboard log directory
    tensorboard_log = os.path.join(PROJECT_ROOT, "tensorboard_logs")
    os.makedirs(tensorboard_log, exist_ok=True)
    print(f"TensorBoard log directory: {tensorboard_log}")
    
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
    
    env = DGAMREnv(
        solver=solver,
        element_budget=element_budget,
        gamma_c=25.0
    )
    
    # Add monitoring
    monitor_path = os.path.join(log_dir, "monitor.csv")
    print(f"Monitor log path: {monitor_path}")
    env = Monitor(env, monitor_path)
    
    # Create callbacks - keep only the essential TimestepLimitCallback
    timestep_limit_callback = TimestepLimitCallback(
        total_timesteps=total_timesteps,
        verbose=1
    )
    
    # Initialize model with TensorBoard logging
    model = A2C(
        "MultiInputPolicy",
        env,
        verbose=1,
        learning_rate=0.0003,
        n_steps=5,
        ent_coef=0.01,
        tensorboard_log=tensorboard_log  # Add this line
    )
    
    print(f"\nModel parameters:")
    print(f"Learning rate: {model.learning_rate}")
    print(f"N steps: {model.n_steps}")
    print(f"Total timesteps requested: {total_timesteps}")
    
    try:
        # Train model with TensorBoard logging
        model.learn(
            total_timesteps=total_timesteps,
            callback=timestep_limit_callback,
            tb_log_name=f"A2C_run_{timestamp}"  # Add this line
        )
    except Exception as e:
        print(f"\nTraining error: {e}")
    finally:
        print(f"\nTraining completed or stopped.")
        
        # Save final model
        model_path = os.path.join(log_dir, "final_model.zip")
        model.save(model_path)
        print(f"Model saved to: {model_path}")
    
    return model, timestep_limit_callback

def evaluate_model(model, env, num_episodes=5):
    """
    Basic model evaluation.
    """
    print("\nStarting model evaluation...")
    rewards = []
    for episode in range(num_episodes):
        obs = env.reset()[0]
        done = False
        total_reward = 0
        
        while not done:
            action, _ = model.predict(obs, deterministic=True)
            obs, reward, done, truncated, info = env.step(action)
            total_reward += reward
            
            if truncated:
                break
                
        rewards.append(total_reward)
        print(f"Episode {episode + 1} reward: {total_reward:.2f}")
    
    print(f"\nMean reward: {np.mean(rewards):.2f}")
    print(f"Std reward: {np.std(rewards):.2f}")

if __name__ == "__main__":
    # Train model
    # model, training_callback, timestep_callback = train_amr_agent()
    model, timestep_callback = train_amr_agent()
    # model, timestep_callback = train_amr_agent(total_timesteps=500)
    
    # Create fresh environment for evaluation
    xelem = np.array([-1, -0.4, 0, 0.4, 1])
    solver = DGWaveSolver(
        nop=4,
        xelem=xelem,
        max_elements=40,
        max_level=4,
        courant_max=0.1,
        icase=1
    )
    
    eval_env = DGAMREnv(
        solver=solver,
        element_budget=25,
        gamma_c=25.0
    )
    
    # Evaluate model
    evaluate_model(model, eval_env)


