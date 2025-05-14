"""
Training script for DG AMR using A2C with progressive episode scaling and monitoring.
"""

import os
from stable_baselines3 import A2C
from stable_baselines3.common.callbacks import BaseCallback
from stable_baselines3.common.logger import configure
import numpy as np
import traceback
import matplotlib.pyplot as plt
import sys
# Get absolute path to project root
# PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.insert(0, PROJECT_ROOT)

PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 
    '..',
    '..'
))
sys.path.append(PROJECT_ROOT)

from numerical.solvers.dg_wave_solver import DGWaveSolver
from numerical.environments.dg_amr_env import DGAMREnv

# [Previous imports remain the same]

class DetailedMonitorCallback(BaseCallback):
    def __init__(self, verbose=0):
        super().__init__(verbose)
        self.episode_count = 0
        self.episode_reward = 0
        self.element_counts = []
        self.budget_exceeded_count = 0
        self.condition_numbers = []
        self.balance_enforcements = 0
        self.max_elements_seen = 0
        
    def _on_step(self) -> bool:
        # Accumulate reward
        reward = self.locals.get("rewards")
        if reward is not None:
            self.episode_reward += reward[0]

        # Get info from environment
        info = self.locals.get("infos")[0]
        if info:
            # Track element counts
            self.element_counts.append(info['n_elements'])
            self.max_elements_seen = max(self.max_elements_seen, info['n_elements'])
            
            # Track budget exceedance
            if info.get('budget_exceeded', False):
                self.budget_exceeded_count += 1
            
            # Track condition numbers if available
            if 'condition_number' in info:
                self.condition_numbers.append(info['condition_number'])
            
            # Track balance enforcements
            if info.get('balance_enforced', False):
                self.balance_enforcements += 1

        # Check if episode ended
        done = self.locals.get("dones")
        if done is not None and done[0]:
            self.episode_count += 1
            print(f"\nEpisode {self.episode_count} completed")
            print(f"Episode reward: {self.episode_reward}")
            print(f"Max elements used: {self.max_elements_seen}")
            print(f"Budget exceeded count: {self.budget_exceeded_count}")
            print(f"Balance enforcements: {self.balance_enforcements}")
            if self.condition_numbers:
                print(f"Max condition number: {max(self.condition_numbers)}")
            print("-------------------------")
            
            # Reset episode-specific counters
            self.episode_reward = 0
            self.condition_numbers = []
            self.max_elements_seen = 0
            
        return True

    def plot_statistics(self):
        """Plot training statistics"""
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
        
        # Plot element count history
        ax1.plot(self.element_counts)
        ax1.set_title('Element Count History')
        ax1.set_xlabel('Step')
        ax1.set_ylabel('Number of Elements')
        
        # Plot condition numbers if available
        if self.condition_numbers:
            ax2.plot(self.condition_numbers)
            ax2.set_title('Matrix Condition Number History')
            ax2.set_xlabel('Step')
            ax2.set_ylabel('Condition Number')
            ax2.set_yscale('log')
        
        plt.tight_layout()
        plt.savefig('training_statistics.png')
        plt.close()

def progressive_training():
    """Training with progressive episode scaling"""
    # Initialize solver and environment
    nop = 3
    xelem = np.array([-1.0, -0.4, 0.0, 0.4, 1.0])
    max_elements = 25
    max_level = 3
    solver = DGWaveSolver(nop, xelem, max_elements, max_level)
    env = DGAMREnv(solver, element_budget=25, gamma_c=25.0)

    # Set up logging
    log_dir = "./tensorboard_logs/"
    os.makedirs(log_dir, exist_ok=True)
    new_logger = configure(log_dir, ["tensorboard", "stdout"])

    # Training phases with increasing episodes
    training_phases = [
        {"episodes": 3, "total_timesteps": 50},    # Very short initial phase
        {"episodes": 5, "total_timesteps": 100},   # Short testing phase
        {"episodes": 10, "total_timesteps": 200},  # Medium phase
        {"episodes": 20, "total_timesteps": 500}   # Full phase
    ]

    model = None
    callback = DetailedMonitorCallback()

    for phase_num, phase in enumerate(training_phases):
        print(f"\nStarting training phase {phase_num + 1}")
        print(f"Episodes: {phase['episodes']}")
        print(f"Total timesteps: {phase['total_timesteps']}")

        try:
            if model is None:
                # Initialize model
                model = A2C("MultiInputPolicy", env, verbose=1, tensorboard_log=log_dir)
            else:
                # Continue training existing model
                model.set_env(env)

            model.learn(
                total_timesteps=phase['total_timesteps'],
                callback=callback,
                reset_num_timesteps=False  # Continue counting timesteps
            )

            # Save model after each phase
            model.save(f"amr_model_phase_{phase_num + 1}")
            
            # Plot current statistics
            callback.plot_statistics()
            
            print(f"\nPhase {phase_num + 1} completed successfully")
            print(f"Total budget exceedances: {callback.budget_exceeded_count}")
            print(f"Total balance enforcements: {callback.balance_enforcements}")

        except Exception as e:
            print(f"Error during phase {phase_num + 1}: {e}")
            traceback.print_exc()
            break

if __name__ == "__main__":
    progressive_training()




# import os
# from stable_baselines3 import A2C
# from stable_baselines3.common.callbacks import BaseCallback
# from stable_baselines3.common.logger import configure
# import numpy as np
# import traceback

# import sys
# # Get absolute path to project root
# # PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# # sys.path.insert(0, PROJECT_ROOT)

# PROJECT_ROOT = os.path.abspath(os.path.join(
#     os.path.dirname(__file__), 
#     '..',
#     '..'
# ))
# sys.path.append(PROJECT_ROOT)

# from numerical.solvers.dg_wave_solver import DGWaveSolver
# from numerical.environments.dg_amr_env import DGAMREnv

# class DebugCallback(BaseCallback):
#     def __init__(self, verbose=0):
#         super().__init__(verbose)
#         self.episode_count = 0
#         self.episode_reward = 0
    
#     def _on_step(self) -> bool:
#         # Accumulate reward
#         reward = self.locals.get("rewards")
#         if reward is not None:
#             self.episode_reward += reward[0]

#         # Check if episode ended
#         done = self.locals.get("dones")
#         if done is not None and done[0]:
#             self.episode_count += 1
#             print(f"Episode {self.episode_count} completed")
#             print(f"Episode reward: {self.episode_reward}")
#             print(f"Number of timesteps: {self.num_timesteps}")
#             print("-------------------------")
#             self.episode_reward = 0  # Reset for next episode
            
#         return True

# # Initialize solver
# nop = 3  # Polynomial order
# xelem = np.array([-1.0, -0.4, 0.0, 0.4, 1.0])  # Domain boundaries
# max_elements = 25  # Maximum number of elements
# max_level = 3  # Maximum refinement level
# solver = DGWaveSolver(nop, xelem, max_elements, max_level)

# # Create and initialize the environment
# env = DGAMREnv(solver, element_budget=25, gamma_c = 25.0)

# # Set up logging directory
# log_dir = "./tensorboard_logs/"
# os.makedirs(log_dir, exist_ok=True)

# # Configure logger
# new_logger = configure(log_dir, ["tensorboard", "stdout"])

# # Initialize the model
# model = A2C("MultiInputPolicy", env, verbose=1, tensorboard_log=log_dir)
# model.set_logger(new_logger)

# # Create callback
# callback = DebugCallback()

# # Train for just a few episodes
# try:
#     model.learn(total_timesteps=10, callback=callback)
#     print("\nTraining completed successfully")
#     print(f"Tensorboard logs written to: {log_dir}")
# except Exception as e:
#     print(f"Error during training: {e}")
#     traceback.print_exc()