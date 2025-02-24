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
        
    # def _on_step(self) -> bool:
    #     self.step_count += 1
    #     print(f"\nTraining Timestep {self.step_count} (Total requested: {self.locals['total_timesteps']})")
        
    #     # Check for episode completion
    #     info = self.locals.get('info')
    #     if info is not None and 'episode' in info:
    #         self.episode_count += 1
    #         episode_info = info['episode']
    #         self.rewards.append(episode_info['r'])
    #         self.episode_lengths.append(episode_info['l'])
    #         self.last_info = info
            
    #         print(f"\nEpisode {self.episode_count} completed:")
    #         print(f"Reward: {episode_info['r']:.2f}")
    #         print(f"Length: {episode_info['l']}")
            
    #         # Create a plot after each episode (check_freq = 1)
    #         if self.episode_count % self.check_freq == 0:
    #             plot_path = self._plot_training_progress()
    #             if plot_path:
    #                 print(f"Saved training plot to: {plot_path}")
    #             else:
    #                 print("Failed to create training plot")
        
    #     return True
    def _on_step(self) -> bool:
        self.step_count += 1
        print(f"\nCallback step: {self.num_timesteps}")
    
        # Print locals to see what's available
        info = self.locals.get("info", {})
        dones = self.locals.get("dones", [])
        print(f"Info keys: {info.keys() if isinstance(info, dict) else 'not a dict'}")
        print(f"Dones: {dones if hasattr(dones, '__iter__') else 'not iterable'}")
        print(f"Episode info: {info.get('episode', 'none')}")
        
        # If we detect episode completion
        if 'episode' in info:
            print("*** EPISODE DETECTED IN CALLBACK ***")
            episode_info = info['episode']
            
            # Save the reward and episode length
            reward = episode_info.get('r', 0)
            ep_len = episode_info.get('l', 0)
            self.rewards.append(reward)
            self.episode_lengths.append(ep_len)
            
            # Create immediate test plot regardless of check_freq
            print("Creating direct test plot in callback...")
            try:
                import matplotlib.pyplot as plt
                plt.figure()
                plt.plot(self.rewards)
                test_path = os.path.join(self.log_dir, f"direct_test_{len(self.rewards)}.png")
                plt.savefig(test_path)
                plt.close()
                print(f"Direct test plot saved: {test_path}")
                print(f"File exists: {os.path.exists(test_path)}")
            except Exception as e:
                print(f"Direct plot error: {e}")
        
        return True
        
        # # Check for episode completion
        # info = self.locals.get('info')
        # if info is not None and 'episode' in info:
        #     self.episode_count += 1
        #     episode_info = info['episode']
        #     self.rewards.append(episode_info['r'])
        #     self.episode_lengths.append(episode_info['l'])
            
        #     print(f"\nEpisode {self.episode_count} completed:")
        #     print(f"Reward: {episode_info['r']:.2f}")
        #     print(f"Length: {episode_info['l']}")
        #     print(f"Total rewards collected: {len(self.rewards)}")
            
        #     # Add logic to check plot creation condition
        #     should_create_plot = self.episode_count % self.check_freq == 0
        #     print(f"Should create plot? episode_count={self.episode_count}, check_freq={self.check_freq}, result={should_create_plot}")
            
        #     if should_create_plot:
        #         plot_path = self._plot_training_progress()
        #         if plot_path:
        #             print(f"Saved training plot to: {plot_path}")
        #         else:
        #             print("Failed to create training plot")
        
        # return True

    def _plot_training_progress(self):
        """Create simple training progress plot with enhanced debugging."""
        try:
            print("\n=== DEBUG: PLOT CREATION ATTEMPT ===")
            print(f"Working directory: {os.getcwd()}")
            
            # Create plots directory with absolute path
            plots_dir = os.path.join(os.path.abspath(self.log_dir), "plots")
            os.makedirs(plots_dir, exist_ok=True)
            print(f"Created plots directory: {plots_dir}")
            print(f"Directory exists: {os.path.exists(plots_dir)}")
            
            # Check rewards data
            print(f"Rewards data: {self.rewards}")
            print(f"Episode lengths data: {self.episode_lengths}")
            if len(self.rewards) == 0:
                print("No reward data to plot yet")
                return None
            
            # Create figure
            print("Creating matplotlib figure...")
            plt.figure(figsize=(10, 5))
            
            # Plot rewards
            print("Adding rewards subplot...")
            plt.subplot(1, 2, 1)
            plt.plot(self.rewards, 'bo-')
            plt.title("Episode Rewards")
            plt.xlabel("Episode")
            plt.ylabel("Reward")
            
            # Plot episode lengths
            print("Adding episode lengths subplot...")
            plt.subplot(1, 2, 2)
            plt.plot(self.episode_lengths, 'ro-')
            plt.title("Episode Lengths")
            plt.xlabel("Episode")
            plt.ylabel("Length")
            
            plt.tight_layout()
            
            # Save plot with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            plot_path = os.path.join(plots_dir, f'training_progress_{timestamp}.png')
            print(f"Attempting to save plot to: {plot_path}")
            
            plt.savefig(plot_path)
            print(f"Plot saved successfully: {os.path.exists(plot_path)}")
            
            # Check file size to verify it's not empty
            if os.path.exists(plot_path):
                file_size = os.path.getsize(plot_path)
                print(f"Plot file size: {file_size} bytes")
            
            plt.close()
            print("=== PLOT CREATION COMPLETE ===\n")
            return plot_path
            
        except Exception as e:
            import traceback
            print(f"ERROR creating/saving plot: {str(e)}")
            traceback.print_exc()
            print(f"Current directory: {os.getcwd()}")
            print(f"Log directory: {self.log_dir}")
            return None
    
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

def train_amr_agent(total_timesteps=15, element_budget=25):
    """
    Train AMR agent with simplified setup.
    """
    try:
        import matplotlib.pyplot as plt
        plt.figure()
        plt.plot([1, 2, 3], [4, 5, 6])
        test_plot_path = os.path.join(".", "test_plot.png")
        plt.savefig(test_plot_path)
        plt.close()
        print(f"Test plot saved to: {test_plot_path}")
        print(f"Test plot exists: {os.path.exists(test_plot_path)}")
    except Exception as e:
        print(f"Matplotlib test failed: {e}")
    print(f"\nStarting training for {total_timesteps} timesteps...")
    
    # Create timestamp for this training run
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Create logs directory structure
    log_dir = os.path.join(PROJECT_ROOT, "logs", f"training_{timestamp}")
    os.makedirs(log_dir, exist_ok=True)
    print(f"Created log directory: {log_dir}")
    
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
    
    # Create callbacks
    training_callback = SimpleTrainingCallback(
        check_freq=5,
        log_dir=log_dir,
        verbose=1
    )

    timestep_limit_callback = TimestepLimitCallback(
        total_timesteps=total_timesteps,
        verbose=1
    )

    # Combine callbacks
    callbacks = [timestep_limit_callback, training_callback]
    
    # Initialize model
    model = A2C(
        "MultiInputPolicy",
        env,
        verbose=1,
        learning_rate=0.0003,
        n_steps=5,  # Set this small for testing
        ent_coef=0.01
    )
    
    print(f"\nModel parameters:")
    print(f"Learning rate: {model.learning_rate}")
    print(f"N steps: {model.n_steps}")
    print(f"Total timesteps requested: {total_timesteps}")
    
    try:
        # Train model with combined callbacks
        model.learn(
            total_timesteps=total_timesteps,
            callback=callbacks
        )
    except StopIteration as e:
        print(f"\nTraining stopped: {e}")
    except KeyboardInterrupt:
        print("\nTraining interrupted by user")
    except Exception as e:
        print(f"\nTraining error: {e}")
    finally:
        print(f"\nTraining completed or stopped:")
        print(f"Total episodes: {len(training_callback.rewards)}")
        print(f"Total steps: {timestep_limit_callback.num_timesteps}")
        
        # Save final model
        model_path = os.path.join(log_dir, "final_model.zip")
        model.save(model_path)
        print(f"Model saved to: {model_path}")
    
    return model, training_callback, timestep_limit_callback

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
    model, training_callback, timestep_callback = train_amr_agent()
    
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


