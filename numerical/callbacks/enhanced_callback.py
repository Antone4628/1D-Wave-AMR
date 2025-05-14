import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
from typing import Dict, List, Tuple, Any, Optional
from collections import deque
from stable_baselines3.common.callbacks import BaseCallback
from matplotlib.backends.backend_pdf import PdfPages


class EnhancedMonitorCallback(BaseCallback):
    """
    Enhanced callback for monitoring RL training in adaptive mesh refinement.
    
    Tracks:
    - Action distribution over time
    - Resource usage statistics
    - Termination reasons
    - Reward breakdown by action type
    - Budget proximity at decision time
    
    Provides visualization capabilities and periodic reporting.
    """
    
    def __init__(
        self, 
        total_timesteps: int,
        log_dir: str,
        save_freq: int = 10000,
        verbose: int = 0,
        window_size: int = 100,
        action_mapping: Dict[int, int] = {0: -1, 1: 0, 2: 1},
        log_freq: int = 1000
    ):
        """
        Initialize the callback with monitoring parameters.
        
        Args:
            total_timesteps: Total timesteps for the training run
            log_dir: Directory to save logs and visualizations
            save_freq: Frequency (in timesteps) to save the model
            verbose: Verbosity level (0: no output, 1: info, 2: debug)
            window_size: Window size for moving averages
            action_mapping: Mapping from action space integers to semantic values
            log_freq: Frequency (in timesteps) to log statistics
        """
        super().__init__(verbose)
        self.total_timesteps = total_timesteps
        self.log_dir = log_dir
        self.save_freq = save_freq
        self.window_size = window_size
        self.log_freq = log_freq
        self.action_mapping = action_mapping
        self.action_names = {-1: "Coarsen", 0: "No Change", 1: "Refine"}

        # Add new variables to track refinement configuration
        self.refinement_mode = "unknown"
        self.refinement_level = "unknown"
        self.refinement_probability = "unknown"
        
        # Create metrics directory
        self.metrics_dir = os.path.join(log_dir, "metrics")
        os.makedirs(self.metrics_dir, exist_ok=True)
        
        # Create plots directory
        self.plots_dir = os.path.join(log_dir, "plots")
        os.makedirs(self.plots_dir, exist_ok=True)
        
        # Initialize tracking variables
        self.reset_tracking()
        
    def reset_tracking(self):
        """Reset all tracking metrics."""
        # Action tracking
        self.action_counts = {action: 0 for action in self.action_mapping.values()}
        self.action_history = []
        self.mapped_action_history = []
        
        # Reward tracking
        self.rewards_by_action = {action: [] for action in self.action_mapping.values()}
        self.episode_rewards = []
        self.cumulative_reward = 0
        self.reward_history = []
        
        # Resource tracking
        self.resource_usage_history = []
        self.element_count_history = []
        self.budget_proximity_history = []  # % of budget used
        
        # Episode tracking
        self.episode_lengths = []
        self.termination_reasons = {}
        self.episodes_completed = 0
        
        # Time step tracking
        self.timestep_history = []  # Track when physical time steps occur
        
        # Moving windows for recent statistics
        self.recent_rewards = deque(maxlen=self.window_size)
        self.recent_actions = deque(maxlen=self.window_size)
        self.recent_resources = deque(maxlen=self.window_size)
        
        # Initialize tracking dataframes
        self.metrics_df = pd.DataFrame()
        self.episode_df = pd.DataFrame()

        # Add these new tracking variables
        self.pre_termination_elements = []
        self.budget_usage_at_violation = []
        self.violation_actions = []

        # Episode statistics tracking
        self.current_episode_start_step = 0
        self.current_episode_actions = {action: 0 for action in self.action_mapping.values()}
        self.current_episode_reward = 0
        
    def _on_training_start(self) -> None:
        """Called when training starts. Add configuration info to TensorBoard."""
        # Initialize dataframes with correct columns
        self.metrics_df = pd.DataFrame(columns=[
            'timestep', 'action', 'mapped_action', 'reward', 
            'resource_usage', 'element_count', 'budget_proximity',
            'took_timestep', 'episode'
        ])
        
        self.episode_df = pd.DataFrame(columns=[
            'episode', 'total_reward', 'length', 'termination_reason',
            'final_element_count', 'final_resource_usage',
            'refine_count', 'coarsen_count', 'no_change_count',
            'refine_pct', 'coarsen_pct', 'no_change_pct'
        ])
        
        # Set plot style
        sns.set(style="whitegrid")
        plt.rcParams.update({'figure.figsize': (12, 8)})
        
        # Log configuration parameters
        if self.logger is not None:
            # Log element budget
            try:
                budget = self.model.env.unwrapped.element_budget
            except (AttributeError, KeyError):
                try:
                    budget = self.model.env.get_wrapper_attr('element_budget')
                except (AttributeError, KeyError):
                    budget = self.model.env.envs[0].unwrapped.element_budget
            
            self.logger.record("environment/element_budget", budget)
            
            # Log gamma_c
            try:
                gamma_c = self.model.env.unwrapped.gamma_c
            except (AttributeError, KeyError):
                try:
                    gamma_c = self.model.env.get_wrapper_attr('gamma_c')
                except (AttributeError, KeyError):
                    gamma_c = self.model.env.envs[0].unwrapped.gamma_c
            
            self.logger.record("environment/gamma_c", gamma_c)
            
            # Log max episode steps
            try:
                max_steps = self.model.env.unwrapped.max_episode_steps
            except (AttributeError, KeyError):
                try:
                    max_steps = self.model.env.get_wrapper_attr('max_episode_steps')
                except (AttributeError, KeyError):
                    max_steps = self.model.env.envs[0].unwrapped.max_episode_steps
            
            self.logger.record("environment/max_episode_steps", max_steps)
            
            # Log RL algorithm information
            if hasattr(self.model, 'ent_coef'):
                self.logger.record("hyperparameters/entropy_coefficient", self.model.ent_coef)
            
            if hasattr(self.model, 'learning_rate'):
                self.logger.record("hyperparameters/learning_rate", self.model.learning_rate)
    
    def _on_step(self) -> bool:
        """
        Called after each step of the environment.
        
        Returns:
            bool: Whether training should continue
        """
        # Extract current step information
        info = self.locals['infos'][0]
        action = self.locals['actions'][0]
        reward = self.locals['rewards'][0]
        obs = self.locals['new_obs']

        # Capture pre-termination metrics if available
        if 'pre_termination_elements' in info:
            self.pre_termination_elements.append(info['pre_termination_elements'])
            self.budget_usage_at_violation.append(info.get('budget_usage_percent', 0) / 100.0)
            self.violation_actions.append(info.get('violation_action', 0))
        
        # Map raw action to semantic action (-1, 0, 1)
        mapped_action = self.action_mapping[action.item() if hasattr(action, 'item') else int(action)]
        
        # Update action counters
        self.action_counts[mapped_action] += 1
        self.action_history.append(action)
        self.mapped_action_history.append(mapped_action)
        self.recent_actions.append(mapped_action)
        
        # Update current episode action counts
        self.current_episode_actions[mapped_action] += 1
        
        # Update reward tracking
        self.rewards_by_action[mapped_action].append(reward)
        self.reward_history.append(reward)
        self.recent_rewards.append(reward)
        self.cumulative_reward += reward
        self.current_episode_reward += reward
        
        # Update resource tracking
        resource_usage = info.get('resource_usage', 0)
        element_count = info.get('n_elements', 0)

        # Get element budget from environment
        try:
            budget = self.model.env.unwrapped.element_budget
        except (AttributeError, KeyError):
            # Fallback for vectorized environments
            try:
                budget = self.model.env.get_wrapper_attr('element_budget')
            except (AttributeError, KeyError):
                # Last resort for vectorized envs
                budget = self.model.env.envs[0].unwrapped.element_budget

        budget_proximity = element_count / budget if budget > 0 else 0
        
        self.resource_usage_history.append(resource_usage)
        self.element_count_history.append(element_count)
        self.budget_proximity_history.append(budget_proximity)
        self.recent_resources.append(resource_usage)
        
        # Track physical time steps
        took_timestep = int(info.get('took_timestep', False))
        self.timestep_history.append(took_timestep)
        
        # Update metrics dataframe
        new_row = {
            'timestep': self.num_timesteps,
            'action': action,
            'mapped_action': mapped_action,
            'reward': reward,
            'resource_usage': resource_usage,
            'element_count': element_count,
            'budget_proximity': budget_proximity,
            'took_timestep': took_timestep,
            'episode': self.episodes_completed
        }
        self.metrics_df = pd.concat([self.metrics_df, pd.DataFrame([new_row])], ignore_index=True)
        
        # Check for episode completion
        done = self.locals['dones'][0]
        if done:
            self._on_episode_end(info)
        
        # Periodic logging and visualization
        if self.num_timesteps % self.log_freq == 0:
            self._log_statistics()
            
        # Save model periodically
        if self.num_timesteps % self.save_freq == 0:
            model_path = os.path.join(self.log_dir, f"model_{self.num_timesteps}_steps")
            self.model.save(model_path)
            
            # Save datasets
            self._save_datasets()
            
            # Generate visualizations
            self._generate_visualizations()
            
            if self.verbose > 0:
                print(f"Saved model and metrics at {model_path}")
        
        # Print progress periodically
        if self.num_timesteps % 100 == 0:
            if self.verbose > 0:
                progress = self.num_timesteps / self.total_timesteps * 100
                print(f"Progress: {self.num_timesteps}/{self.total_timesteps} steps ({progress:.1f}%)")
        
        # Check if we've exceeded total timesteps
        if self.num_timesteps >= self.total_timesteps:
            if self.verbose > 0:
                print(f"Reached {self.total_timesteps} timesteps, stopping training")
            return False
            
        return True
    
    def _on_episode_end(self, info: Dict[str, Any]) -> None:
        """
        Called when an episode ends.
        
        Args:
            info: Information from the last step
        """
        # Calculate episode length
        episode_length = self.num_timesteps - self.current_episode_start_step
        
        # Get termination reason
        termination_reason = info.get('reason', 'unknown')
        
        # Update episode counters
        self.episodes_completed += 1
        self.episode_rewards.append(self.current_episode_reward)
        self.episode_lengths.append(episode_length)
        
        # Update termination statistics
        if termination_reason not in self.termination_reasons:
            self.termination_reasons[termination_reason] = 0
        self.termination_reasons[termination_reason] += 1
        
        # Calculate action distribution for this episode
        total_actions = sum(self.current_episode_actions.values())
        refine_count = self.current_episode_actions[1]
        coarsen_count = self.current_episode_actions[-1]
        no_change_count = self.current_episode_actions[0]
        
        refine_pct = refine_count / total_actions if total_actions > 0 else 0
        coarsen_pct = coarsen_count / total_actions if total_actions > 0 else 0
        no_change_pct = no_change_count / total_actions if total_actions > 0 else 0
        
        # Get final resource state
        final_resource_usage = self.resource_usage_history[-1] if self.resource_usage_history else 0
        final_element_count = self.element_count_history[-1] if self.element_count_history else 0
        
        # Update episode dataframe
        new_row = {
            'episode': self.episodes_completed,
            'total_reward': self.current_episode_reward,
            'length': episode_length,
            'termination_reason': termination_reason,
            'final_element_count': final_element_count,
            'final_resource_usage': final_resource_usage,
            'refine_count': refine_count,
            'coarsen_count': coarsen_count,
            'no_change_count': no_change_count,
            'refine_pct': refine_pct,
            'coarsen_pct': coarsen_pct,
            'no_change_pct': no_change_pct
        }
        self.episode_df = pd.concat([self.episode_df, pd.DataFrame([new_row])], ignore_index=True)
        
        # Log episode statistics to TensorBoard
        if self.logger is not None:
            self.logger.record("rollout/ep_rew_mean", self.current_episode_reward)
            self.logger.record("rollout/ep_len_mean", episode_length)
            self.logger.record("actions/refine_proportion", refine_pct)
            self.logger.record("actions/coarsen_proportion", coarsen_pct)
            self.logger.record("actions/no_change_proportion", no_change_pct)
            self.logger.record("resources/usage", final_resource_usage)
            
            # Log termination reason
            sanitized_reason = termination_reason.lower().replace(" ", "_")
            self.logger.record(f"termination/{sanitized_reason}", 1)
            
            # Log step counts
            self.logger.record("train/steps", self.num_timesteps)
            self.logger.record("train/episodes", self.episodes_completed)
            
            # Ensure we dump to disk
            self.logger.dump(self.num_timesteps)
        
        # Log episode completion
        if self.verbose > 0 and (self.episodes_completed % 10 == 0):
            print(f"\nEpisode {self.episodes_completed} completed:")
            print(f"  Reward: {self.current_episode_reward:.2f}")
            print(f"  Length: {episode_length}")
            print(f"  Termination: {termination_reason}")
            print(f"  Final elements: {final_element_count}")
            print(f"  Action distribution: Refine={refine_pct:.1%}, No Change={no_change_pct:.1%}, Coarsen={coarsen_pct:.1%}")
        
        # Reset episode-specific tracking
        self.current_episode_start_step = self.num_timesteps
        self.current_episode_actions = {action: 0 for action in self.action_mapping.values()}
        self.current_episode_reward = 0
    
    def _log_statistics(self) -> None:
        """Log current training statistics with consistent naming conventions."""
        if not self.recent_rewards:
            return
            
        # Calculate statistics
        recent_reward_mean = np.mean(self.recent_rewards)
        
        # Calculate action distribution
        action_counts = {self.action_names[a]: 0 for a in self.action_mapping.values()}
        for action in self.recent_actions:
            action_counts[self.action_names[action]] += 1
        total_actions = len(self.recent_actions)
        action_dist = {k: v/total_actions for k, v in action_counts.items()} if total_actions > 0 else action_counts
        
        # Calculate average resource usage
        avg_resource = np.mean(self.recent_resources) if self.recent_resources else 0
        
        # Log to console
        if self.verbose > 0:
            print(f"\nStatistics at step {self.num_timesteps}:")
            print(f"  Recent mean reward: {recent_reward_mean:.2f}")
            print(f"  Episodes completed: {self.episodes_completed}")
            print(f"  Action distribution: {', '.join([f'{k}: {v:.1%}' for k, v in action_dist.items()])}")
            print(f"  Average resource usage: {avg_resource:.1%}")
            
            # Print termination statistics if available
            if self.termination_reasons:
                total_episodes = sum(self.termination_reasons.values())
                print(f"  Termination reasons:")
                for reason, count in self.termination_reasons.items():
                    print(f"    {reason}: {count/total_episodes:.1%}")
        
        # Log to stable-baselines logger using consistent naming conventions
        if self.logger is not None:
            # Action proportions - use standard naming format
            for action_name, proportion in action_dist.items():
                action_key = action_name.lower().replace(" ", "_")
                self.logger.record(f"actions/{action_key}_proportion", proportion)
            
            # Resources - use standard naming
            self.logger.record("resources/usage", avg_resource)
            
            # Training progress
            self.logger.record("training/episodes_completed", self.episodes_completed)
            self.logger.record("training/recent_reward_mean", recent_reward_mean)
            
            # Episode stats - use standard naming
            if self.episode_rewards:
                self.logger.record("rollout/ep_rew_mean", np.mean(self.episode_rewards[-20:] if len(self.episode_rewards) > 20 else self.episode_rewards))
            
            if self.episode_lengths:
                self.logger.record("rollout/ep_len_mean", np.mean(self.episode_lengths[-20:] if len(self.episode_lengths) > 20 else self.episode_lengths))
            
            # Termination reasons - ensure consistent naming
            total_episodes = sum(self.termination_reasons.values()) if self.termination_reasons else 1
            for reason, count in self.termination_reasons.items():
                if len(reason) > 30:
                    import hashlib
                    short_hash = hashlib.md5(reason.encode()).hexdigest()[:8]
                    sanitized_reason = f"error_type_{short_hash}"
                else:
                    sanitized_reason = reason.lower().replace(" ", "_")
                
                # Log both raw count and percentage
                self.logger.record(f"termination/{sanitized_reason}", count)
                self.logger.record(f"termination/{sanitized_reason}_pct", count/total_episodes)
            
            # Ensure we dump to disk
            self.logger.dump(self.num_timesteps)
    
    def _save_datasets(self) -> None:
        """Save collected data to CSV files."""
        # Save metrics dataframe
        metrics_path = os.path.join(self.metrics_dir, f"metrics_{self.num_timesteps}.csv")
        self.metrics_df.to_csv(metrics_path, index=False)
        
        # Save episode dataframe
        episode_path = os.path.join(self.metrics_dir, f"episodes_{self.num_timesteps}.csv")
        self.episode_df.to_csv(episode_path, index=False)
    
    def _generate_visualizations(self) -> None:
        """Generate and save visualizations of training progress."""
        timestamp = self.num_timesteps
        
        # 1. Action distribution over time
        self._plot_action_distribution(timestamp)
        
        # 2. Rewards by action type
        self._plot_rewards_by_action(timestamp)
        
        # 3. Resource usage over time
        self._plot_resource_usage(timestamp)
        
        # 4. Termination reasons
        self._plot_termination_reasons(timestamp)
        
        # 5. Budget proximity histogram
        self._plot_budget_proximity(timestamp)
        
        # 6. Episode lengths over time
        self._plot_episode_lengths(timestamp)
        
        # 7. Combined dashboard
        self._plot_dashboard(timestamp)
    
    def _plot_action_distribution(self, timestamp: int) -> None:
        """Plot action distribution over time."""
        if len(self.mapped_action_history) < 10:
            return
            
        plt.figure(figsize=(10, 6))
        
        # Convert action history to dataframe for easier plotting
        df = pd.DataFrame({
            'timestep': range(len(self.mapped_action_history)),
            'action': [self.action_names[a] for a in self.mapped_action_history]
        })
        
        # Calculate rolling window of action proportions
        window = min(1000, len(df) // 10)
        action_counts = df.groupby('timestep')['action'].value_counts().unstack().fillna(0)
        
        # Apply rolling window
        if window > 0:
            action_counts = action_counts.rolling(window=window, min_periods=1).mean()
        
        # Plot
        for column in action_counts.columns:
            plt.plot(action_counts.index, action_counts[column], label=column)
        
        plt.xlabel('Timestep')
        plt.ylabel('Proportion')
        plt.title('Action Distribution Over Time')
        plt.legend()
        plt.grid(True)
        
        # Save figure
        plt.savefig(os.path.join(self.plots_dir, f"action_distribution_{timestamp}.png"))
        plt.close()
    
    def _plot_rewards_by_action(self, timestamp: int) -> None:
        """Plot rewards by action type."""
        plt.figure(figsize=(10, 6))
        
        # Prepare data
        data = []
        for action, rewards in self.rewards_by_action.items():
            if rewards:
                data.append({
                    'Action': self.action_names[action],
                    'Rewards': rewards
                })
        
        # Plot boxplots
        if data:
            df = pd.DataFrame(data)
            sns.boxplot(x='Action', y='Rewards', data=pd.DataFrame({
                'Action': np.concatenate([[d['Action']] * len(d['Rewards']) for d in data]),
                'Rewards': np.concatenate([d['Rewards'] for d in data])
            }))
            
            plt.title('Reward Distribution by Action Type')
            plt.xlabel('Action')
            plt.ylabel('Reward')
            plt.grid(True)
            
            # Save figure
            plt.savefig(os.path.join(self.plots_dir, f"rewards_by_action_{timestamp}.png"))
        
        plt.close()
    
    def _plot_resource_usage(self, timestamp: int) -> None:
        """Plot resource usage over time."""
        if not self.resource_usage_history:
            return
            
        plt.figure(figsize=(10, 6))
        
        # Plot resource usage
        plt.plot(range(len(self.resource_usage_history)), self.resource_usage_history)
        
        # Add reference line at 100%
        plt.axhline(y=1.0, color='r', linestyle='--', label='Budget limit')
        
        plt.xlabel('Timestep')
        plt.ylabel('Resource Usage')
        plt.title('Resource Usage Over Time')
        plt.legend()
        plt.grid(True)
        
        # Save figure
        plt.savefig(os.path.join(self.plots_dir, f"resource_usage_{timestamp}.png"))
        plt.close()
        
        # Also plot element count
        plt.figure(figsize=(10, 6))
        plt.plot(range(len(self.element_count_history)), self.element_count_history)
        
        # Add reference line at budget
        try:
            budget = self.model.env.unwrapped.element_budget
        except (AttributeError, KeyError):
            # Fallback for vectorized environments
            try:
                budget = self.model.env.get_wrapper_attr('element_budget')
            except (AttributeError, KeyError):
                # Last resort for vectorized envs
                budget = self.model.env.envs[0].unwrapped.element_budget

        plt.axhline(y=budget, color='r', linestyle='--', label='Element budget')
        
        plt.xlabel('Timestep')
        plt.ylabel('Element Count')
        plt.title('Element Count Over Time')
        plt.legend()
        plt.grid(True)
        
        # Save figure
        plt.savefig(os.path.join(self.plots_dir, f"element_count_{timestamp}.png"))
        plt.close()

        # Add new visualization for pre-termination element counts if data exists
        if self.pre_termination_elements:
            plt.figure(figsize=(10, 6))
            
            # Plot histogram of element counts at termination
            plt.hist(self.pre_termination_elements, bins=range(0, max(self.pre_termination_elements) + 5, 1), 
                    alpha=0.7, color='purple')
            
            # Add reference line at budget
            try:
                budget = self.model.env.unwrapped.element_budget
            except (AttributeError, KeyError):
                # Fallback for vectorized environments
                try:
                    budget = self.model.env.get_wrapper_attr('element_budget')
                except (AttributeError, KeyError):
                    # Last resort for vectorized envs
                    budget = self.model.env.envs[0].unwrapped.element_budget

            plt.axvline(x=budget, color='r', linestyle='--', label='Element budget')
            
            plt.xlabel('Elements at Budget Violation')
            plt.ylabel('Count')
            plt.title('Distribution of Element Counts at Budget Violation')
            plt.legend()
            plt.grid(True)
            
            # Save figure
            plt.savefig(os.path.join(self.plots_dir, f"pre_termination_elements_{timestamp}.png"))
            plt.close()
        
        # Also visualize the actions that led to budget violations
        if self.violation_actions:
            plt.figure(figsize=(10, 6))
            
            # Map actions to names
            action_names = ['-1 (Coarsen)', '0 (No Change)', '1 (Refine)']
            action_counts = [0, 0, 0]
            for action in self.violation_actions:
                # Adjust for action mapping (usually -1, 0, 1)
                idx = action + 1
                if 0 <= idx < 3:
                    action_counts[idx] += 1
            
            # Plot bar chart
            plt.bar(action_names, action_counts, color=['green', 'gray', 'red'])
            plt.xlabel('Action Type')
            plt.ylabel('Count')
            plt.title('Actions That Triggered Budget Violations')
            plt.grid(True, axis='y')
            
            # Save figure
            plt.savefig(os.path.join(self.plots_dir, f"violation_actions_{timestamp}.png"))
            plt.close()
    
    def _plot_termination_reasons(self, timestamp: int) -> None:
        """Plot distribution of episode termination reasons."""
        if not self.termination_reasons:
            return
            
        plt.figure(figsize=(10, 6))
        
        # Prepare data
        reasons = list(self.termination_reasons.keys())
        counts = list(self.termination_reasons.values())
        
        # Plot
        plt.bar(reasons, counts)
        plt.xticks(rotation=45, ha='right')
        plt.xlabel('Termination Reason')
        plt.ylabel('Count')
        plt.title('Episode Termination Reasons')
        plt.tight_layout()
        
        # Save figure
        plt.savefig(os.path.join(self.plots_dir, f"termination_reasons_{timestamp}.png"))
        plt.close()
        
        # Also plot as pie chart
        plt.figure(figsize=(8, 8))
        plt.pie(counts, labels=reasons, autopct='%1.1f%%')
        plt.title('Episode Termination Reasons')
        
        # Save figure
        plt.savefig(os.path.join(self.plots_dir, f"termination_pie_{timestamp}.png"))
        plt.close()
    
    def _plot_budget_proximity(self, timestamp: int) -> None:
        """Plot histogram of budget proximity at termination."""
        if not self.episode_df.empty:
            plt.figure(figsize=(10, 6))
            
            # Plot histogram of final resource usage
            sns.histplot(self.episode_df['final_resource_usage'], bins=20)
            
            plt.xlabel('Resource Usage (at episode end)')
            plt.ylabel('Count')
            plt.title('Distribution of Resource Usage at Episode Termination')
            
            # Add reference line at 100%
            plt.axvline(x=1.0, color='r', linestyle='--', label='Budget limit')
            plt.legend()
            
            # Save figure
            plt.savefig(os.path.join(self.plots_dir, f"budget_proximity_{timestamp}.png"))
            plt.close()
    
    def _plot_episode_lengths(self, timestamp: int) -> None:
        """Plot episode lengths over time."""
        if not self.episode_lengths:
            return
            
        plt.figure(figsize=(10, 6))
        
        # Plot episode lengths
        plt.plot(range(1, len(self.episode_lengths) + 1), self.episode_lengths)
        
        plt.xlabel('Episode')
        plt.ylabel('Length')
        plt.title('Episode Lengths Over Time')
        plt.grid(True)
        
        # Save figure
        plt.savefig(os.path.join(self.plots_dir, f"episode_lengths_{timestamp}.png"))
        plt.close()
        
        # Also plot episode rewards
        if self.episode_rewards:
            plt.figure(figsize=(10, 6))
            plt.plot(range(1, len(self.episode_rewards) + 1), self.episode_rewards)
            
            # Add smoothed line
            window = min(25, len(self.episode_rewards) // 4)
            if window > 0:
                smoothed = pd.Series(self.episode_rewards).rolling(window=window, min_periods=1).mean()
                plt.plot(range(1, len(self.episode_rewards) + 1), smoothed, 'r-', label=f'{window}-episode moving avg')
            
            plt.xlabel('Episode')
            plt.ylabel('Total Reward')
            plt.title('Episode Rewards Over Time')
            plt.legend()
            plt.grid(True)
            
            # Save figure
            plt.savefig(os.path.join(self.plots_dir, f"episode_rewards_{timestamp}.png"))
            plt.close()
    
    def _plot_dashboard(self, timestamp: int) -> None:
        """Create a comprehensive dashboard of training metrics."""
        if not self.metrics_df.empty and self.episodes_completed > 5:
            # Create a multi-panel dashboard
            fig = plt.figure(figsize=(16, 12))
            gs = fig.add_gridspec(3, 2)
            
            # 1. Rewards over time (smoothed)
            ax1 = fig.add_subplot(gs[0, 0])
            if self.episode_rewards:
                ax1.plot(range(1, len(self.episode_rewards) + 1), self.episode_rewards, 'b-', alpha=0.3)
                
                # Add smoothed line
                window = min(25, len(self.episode_rewards) // 4)
                if window > 0:
                    smoothed = pd.Series(self.episode_rewards).rolling(window=window, min_periods=1).mean()
                    ax1.plot(range(1, len(self.episode_rewards) + 1), smoothed, 'b-', label=f'Moving avg')
                
                ax1.set_xlabel('Episode')
                ax1.set_ylabel('Total Reward')
                ax1.set_title('Episode Rewards')
                ax1.legend()
                ax1.grid(True)
            
            # 2. Action distribution (most recent window)
            ax2 = fig.add_subplot(gs[0, 1])
            if self.episode_df.empty:
                action_data = [
                    self.action_counts.get(-1, 0),
                    self.action_counts.get(0, 0),
                    self.action_counts.get(1, 0)
                ]
                labels = ['Coarsen', 'No Change', 'Refine']
            else:
                # Get recent episodes
                recent_n = min(20, len(self.episode_df))
                recent_df = self.episode_df.tail(recent_n)
                action_data = [
                    recent_df['coarsen_count'].sum(),
                    recent_df['no_change_count'].sum(),
                    recent_df['refine_count'].sum()
                ]
                labels = ['Coarsen', 'No Change', 'Refine']
            
            # Ensure we have some data
            if sum(action_data) > 0:
                ax2.pie(action_data, labels=labels, autopct='%1.1f%%')
                ax2.set_title('Recent Action Distribution')
            
            # 3. Episode termination reasons
            ax3 = fig.add_subplot(gs[1, 0])
            if self.termination_reasons:
                reasons = list(self.termination_reasons.keys())
                counts = list(self.termination_reasons.values())
                ax3.bar(reasons, counts)
                positions = np.arange(len(reasons))
                ax3.set_xticks(positions)
                ax3.set_xticklabels(reasons, rotation=45, ha='right')
                ax3.set_xlabel('Reason')
                ax3.set_ylabel('Count')
                ax3.set_title('Episode Termination Reasons')
            
            # 4. Resource usage distribution by termination reason
            ax4 = fig.add_subplot(gs[1, 1])
            if not self.episode_df.empty:
                # Group by termination reason
                term_groups = self.episode_df.groupby('termination_reason')
                
                # Boxplot of final resource usage by termination reason
                if len(term_groups) > 0:
                    sns.boxplot(x='termination_reason', y='final_resource_usage', data=self.episode_df, ax=ax4)
                    current_ticks = ax4.get_xticks()  # Get current tick positions
                    ax4.set_xticks(current_ticks)
                    ax4.set_xticklabels(ax4.get_xticklabels(), rotation=45, ha='right')
                    ax4.set_xlabel('Termination Reason')
                    ax4.set_ylabel('Final Resource Usage')
                    ax4.set_title('Resource Usage by Termination Reason')
                    ax4.axhline(y=1.0, color='r', linestyle='--', label='Budget limit')
                    ax4.legend()
            
            # 5. Episode length vs reward scatter
            ax5 = fig.add_subplot(gs[2, 0])
            if not self.episode_df.empty:
                sns.scatterplot(
                    x='length', 
                    y='total_reward',
                    hue='termination_reason',
                    data=self.episode_df,
                    ax=ax5
                )
                ax5.set_xlabel('Episode Length')
                ax5.set_ylabel('Total Reward')
                ax5.set_title('Episode Length vs Reward')
                
                # Keep legend readable
                if len(self.episode_df['termination_reason'].unique()) > 3:
                    ax5.legend(loc='upper left', bbox_to_anchor=(1, 1))
            
            # 6. Training progress metrics
            ax6 = fig.add_subplot(gs[2, 1])
            progress_text = [
                f"Training Progress: {self.num_timesteps}/{self.total_timesteps} steps ({self.num_timesteps/self.total_timesteps*100:.1f}%)",
                f"Episodes Completed: {self.episodes_completed}",
                f"Termination Reasons:"
            ]
            
            # Add termination stats
            if self.termination_reasons:
                total_episodes = sum(self.termination_reasons.values())
                for reason, count in self.termination_reasons.items():
                    progress_text.append(f"  - {reason}: {count} ({count/total_episodes*100:.1f}%)")
            
            # Add action stats
            total_actions = sum(self.action_counts.values())
            if total_actions > 0:
                progress_text.append("\nAction Distribution:")
                for action, name in self.action_names.items():
                    count = self.action_counts.get(action, 0)
                    progress_text.append(f"  - {name}: {count} ({count/total_actions*100:.1f}%)")
                
            # Add reward stats
            if self.episode_rewards:
                progress_text.append("\nReward Statistics:")
                progress_text.append(f"  - Mean Reward: {np.mean(self.episode_rewards):.2f}")
                progress_text.append(f"  - Min Reward: {np.min(self.episode_rewards):.2f}")
                progress_text.append(f"  - Max Reward: {np.max(self.episode_rewards):.2f}")
            
            # Create text box
            ax6.axis('off')
            ax6.text(0, 1, '\n'.join(progress_text), fontsize=10, va='top')
            
            # Adjust layout and save
            plt.tight_layout()
            plt.savefig(os.path.join(self.plots_dir, f"dashboard_{timestamp}.png"))
            plt.close()
    
    def on_training_end(self) -> None:
        """Called when training ends."""
        # Save final datasets
        self._save_datasets()
        
        # Generate final visualizations
        self._generate_visualizations()
        
        # Create final comprehensive report
        self._create_final_report()
        
        # Save metadata for analysis
        self._save_analysis_metadata()
        
    def _save_analysis_metadata(self) -> None:
        """Save metadata to aid in analysis."""
        import json
        
        try:
            # Collect metadata
            metadata = {
                "training_steps": self.num_timesteps,
                "episodes_completed": self.episodes_completed,
                "element_budget": 0,
                "gamma_c": 0,
                "max_episode_steps": 0,
                "termination_reasons": {k: v for k, v in self.termination_reasons.items()},
                "action_counts": {str(k): v for k, v in self.action_counts.items()},
                "reward_stats": {
                    "mean": float(np.mean(self.episode_rewards)) if self.episode_rewards else 0,
                    "min": float(np.min(self.episode_rewards)) if self.episode_rewards else 0,
                    "max": float(np.max(self.episode_rewards)) if self.episode_rewards else 0,
                }
            }
            
            # Try to get environment parameters
            try:
                metadata["element_budget"] = self.model.env.unwrapped.element_budget
                metadata["gamma_c"] = self.model.env.unwrapped.gamma_c
                metadata["max_episode_steps"] = self.model.env.unwrapped.max_episode_steps
            except (AttributeError, KeyError):
                try:
                    metadata["element_budget"] = self.model.env.get_wrapper_attr('element_budget')
                    metadata["gamma_c"] = self.model.env.get_wrapper_attr('gamma_c')
                    metadata["max_episode_steps"] = self.model.env.get_wrapper_attr('max_episode_steps')
                except (AttributeError, KeyError):
                    try:
                        metadata["element_budget"] = self.model.env.envs[0].unwrapped.element_budget
                        metadata["gamma_c"] = self.model.env.envs[0].unwrapped.gamma_c
                        metadata["max_episode_steps"] = self.model.env.envs[0].unwrapped.max_episode_steps
                    except:
                        pass
            
            # Save to file
            metadata_path = os.path.join(self.log_dir, "training_metadata.json")
            with open(metadata_path, 'w') as f:
                json.dump(metadata, f, indent=2)
                
            if self.verbose > 0:
                print(f"Analysis metadata saved to: {metadata_path}")
                
        except Exception as e:
            print(f"Error saving analysis metadata: {e}")
        
    def _create_final_report(self) -> None:
        """Create a comprehensive final report with training statistics."""
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_pdf import PdfPages
        
        report_path = os.path.join(self.log_dir, "training_report.pdf")
        
        with PdfPages(report_path) as pdf:
            # 1. Summary Page with metadata
            plt.figure(figsize=(10, 12))
            plt.axis('off')
            
            # Prepare metadata and summary text
            # Get environment parameters
            try:
                budget = self.model.env.unwrapped.element_budget
                gamma_c = self.model.env.unwrapped.gamma_c
                max_steps = self.model.env.unwrapped.max_episode_steps
            except (AttributeError, KeyError):
                try:
                    budget = self.model.env.get_wrapper_attr('element_budget')
                    gamma_c = self.model.env.get_wrapper_attr('gamma_c')
                    max_steps = self.model.env.get_wrapper_attr('max_episode_steps')
                except (AttributeError, KeyError):
                    budget = self.model.env.envs[0].unwrapped.element_budget
                    gamma_c = self.model.env.envs[0].unwrapped.gamma_c
                    max_steps = self.model.env.envs[0].unwrapped.max_episode_steps
            
            # Create metadata section
            metadata_text = [
                "# Experiment Configuration",
                f"Element Budget: {budget}",
                f"Gamma_C: {gamma_c}",
                f"Max Episode Steps: {max_steps}",
            ]
            
            if hasattr(self.model, 'ent_coef'):
                metadata_text.append(f"Entropy Coefficient: {self.model.ent_coef}")
            
            if hasattr(self.model, 'learning_rate'):
                metadata_text.append(f"Learning Rate: {self.model.learning_rate}")
                
            # Create summary section
            summary_text = [
                "# Adaptive Mesh Refinement RL Training Summary",
                f"Date: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}",
                f"Total Steps: {self.num_timesteps}",
                f"Episodes Completed: {self.episodes_completed}",
                "\n## Termination Statistics"
            ]
            
            # Add termination stats
            if self.termination_reasons:
                total_episodes = sum(self.termination_reasons.values())
                for reason, count in self.termination_reasons.items():
                    summary_text.append(f"- {reason}: {count} ({count/total_episodes*100:.1f}%)")
            
            # Add action stats
            total_actions = sum(self.action_counts.values())
            if total_actions > 0:
                summary_text.append("\n## Action Distribution")
                for action, name in self.action_names.items():
                    count = self.action_counts.get(action, 0)
                    summary_text.append(f"- {name}: {count} ({count/total_actions*100:.1f}%)")
                
            # Add reward stats
            if self.episode_rewards:
                summary_text.append("\n## Reward Statistics")
                summary_text.append(f"- Mean Reward: {np.mean(self.episode_rewards):.2f}")
                summary_text.append(f"- Min Reward: {np.min(self.episode_rewards):.2f}")
                summary_text.append(f"- Max Reward: {np.max(self.episode_rewards):.2f}")
                
                # Last 20% of episodes
                last_n = max(5, int(len(self.episode_rewards) * 0.2))
                last_rewards = self.episode_rewards[-last_n:]
                summary_text.append(f"- Mean Reward (last {last_n} episodes): {np.mean(last_rewards):.2f}")
            
            # Add resource usage stats
            if self.resource_usage_history:
                summary_text.append("\n## Resource Usage")
                summary_text.append(f"- Mean Resource Usage: {np.mean(self.resource_usage_history):.2f}")
                summary_text.append(f"- Max Resource Usage: {np.max(self.resource_usage_history):.2f}")
                
                # Resource usage at termination
                if not self.episode_df.empty:
                    budget_exceeded = (self.episode_df['final_resource_usage'] > 1).sum()
                    summary_text.append(f"- Episodes ending with budget exceeded: {budget_exceeded} ({budget_exceeded/len(self.episode_df)*100:.1f}%)")
            
            # Add metadata at the top
            plt.text(0.05, 0.95, '\n'.join(metadata_text), transform=plt.gca().transAxes, 
                     fontsize=12, verticalalignment='top', family='monospace',
                     bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
            
            # Add summary text below metadata
            plt.text(0.05, 0.7, '\n'.join(summary_text), transform=plt.gca().transAxes, 
                     fontsize=12, verticalalignment='top', family='monospace',
                     bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
            
            # Add page to PDF
            pdf.savefig()
            plt.close()
            
            # 2. Reward Trends
            if self.episode_rewards:
                plt.figure(figsize=(10, 6))
                plt.plot(range(1, len(self.episode_rewards) + 1), self.episode_rewards, 'b-', alpha=0.3)
                
                # Add smoothed line
                window = min(25, len(self.episode_rewards) // 4)
                if window > 0:
                    smoothed = pd.Series(self.episode_rewards).rolling(window=window, min_periods=1).mean()
                    plt.plot(range(1, len(self.episode_rewards) + 1), smoothed, 'b-', label=f'{window}-episode moving avg')
                
                plt.xlabel('Episode')
                plt.ylabel('Total Reward')
                plt.title('Episode Rewards Over Time')
                plt.legend()
                plt.grid(True)
                pdf.savefig()
                plt.close()
                
            # 3. Action Distribution Page
            action_counts = pd.Series(self.mapped_action_history).map(self.action_names).value_counts()
            
            plt.figure(figsize=(10, 8))
            
            # Pie chart of overall distribution
            plt.subplot(2, 1, 1)
            action_counts.plot.pie(autopct='%1.1f%%', ylabel='')
            plt.title('Overall Action Distribution')
            
            # Action distribution evolution
            if len(self.mapped_action_history) > 100:
                plt.subplot(2, 1, 2)
                
                # Convert action history to dataframe for easier plotting
                df = pd.DataFrame({
                    'timestep': range(len(self.mapped_action_history)),
                    'action': [self.action_names[a] for a in self.mapped_action_history]
                })
                
                # Calculate rolling window of action proportions
                window = min(1000, len(df) // 10)
                action_counts_over_time = df.groupby('timestep')['action'].value_counts().unstack().fillna(0)
                
                # Normalize to percentages
                action_sums = action_counts_over_time.sum(axis=1)
                for col in action_counts_over_time.columns:
                    action_counts_over_time[col] = action_counts_over_time[col] / action_sums * 100
                
                # Apply rolling window
                if window > 0:
                    action_counts_over_time = action_counts_over_time.rolling(window=window, min_periods=1).mean()
                
                # Plot
                for column in action_counts_over_time.columns:
                    plt.plot(action_counts_over_time.index, action_counts_over_time[column], label=column)
                
                plt.xlabel('Timestep')
                plt.ylabel('Percentage (%)')
                plt.title('Action Distribution Evolution')
                plt.legend()
                plt.grid(True)
            
            pdf.savefig()
            plt.close()
            
            # 4. Resource Usage Page
            if self.resource_usage_history:
                plt.figure(figsize=(10, 12))
                
                # Resource usage over time
                plt.subplot(3, 1, 1)
                plt.plot(range(len(self.resource_usage_history)), self.resource_usage_history, 'g-')
                plt.axhline(y=1.0, color='r', linestyle='--', label='Budget limit')
                plt.xlabel('Timestep')
                plt.ylabel('Resource Usage')
                plt.title('Resource Usage Over Time')
                plt.legend()
                plt.grid(True)
                
                # Element count over time
                plt.subplot(3, 1, 2)
                plt.plot(range(len(self.element_count_history)), self.element_count_history, 'b-')
                
                # Add reference line at budget
                try:
                    budget = self.model.env.unwrapped.element_budget
                except (AttributeError, KeyError):
                    # Fallback for vectorized environments
                    try:
                        budget = self.model.env.get_wrapper_attr('element_budget')
                    except (AttributeError, KeyError):
                        # Last resort for vectorized envs
                        budget = self.model.env.envs[0].unwrapped.element_budget

                plt.axhline(y=budget, color='r', linestyle='--', label='Element budget')
                
                plt.xlabel('Timestep')
                plt.ylabel('Element Count')
                plt.title('Element Count Over Time')
                plt.legend()
                plt.grid(True)
                
                # Distribution of final resource usage
                if not self.episode_df.empty:
                    plt.subplot(3, 1, 3)
                    sns.histplot(self.episode_df['final_resource_usage'], bins=20)
                    plt.axvline(x=1.0, color='r', linestyle='--', label='Budget limit')
                    plt.xlabel('Resource Usage (at episode end)')
                    plt.ylabel('Count')
                    plt.title('Distribution of Resource Usage at Episode Termination')
                    plt.legend()
                
                pdf.savefig()
                plt.close()
            
            # 5. Termination Analysis
            if self.termination_reasons:
                plt.figure(figsize=(10, 12))
                
                # Pie chart of termination reasons
                plt.subplot(2, 1, 1)
                reasons = list(self.termination_reasons.keys())
                counts = list(self.termination_reasons.values())
                plt.pie(counts, labels=reasons, autopct='%1.1f%%')
                plt.title('Episode Termination Reasons')
                
                # Resource usage by termination reason
                if not self.episode_df.empty:
                    plt.subplot(2, 1, 2)
                    sns.boxplot(x='termination_reason', y='final_resource_usage', data=self.episode_df)
                    plt.xticks(rotation=45, ha='right')
                    plt.axhline(y=1.0, color='r', linestyle='--', label='Budget limit')
                    plt.xlabel('Termination Reason')
                    plt.ylabel('Final Resource Usage')
                    plt.title('Resource Usage by Termination Reason')
                    plt.legend()
                    plt.tight_layout()
                
                pdf.savefig()
                plt.close()
            
            # 6. Reward Analysis
            if not self.episode_df.empty and len(self.rewards_by_action) > 0:
                plt.figure(figsize=(10, 12))
                
                # Boxplot of rewards by action
                plt.subplot(2, 1, 1)
                
                # Prepare data
                reward_data = []
                for action, rewards in self.rewards_by_action.items():
                    if rewards:
                        for r in rewards:
                            reward_data.append({
                                'Action': self.action_names[action],
                                'Reward': r
                            })
                
                if reward_data:
                    reward_df = pd.DataFrame(reward_data)
                    sns.boxplot(x='Action', y='Reward', data=reward_df)
                    plt.title('Reward Distribution by Action Type')
                    plt.grid(True)
                
                # Scatter plot of episode length vs reward
                plt.subplot(2, 1, 2)
                sns.scatterplot(
                    x='length', 
                    y='total_reward',
                    hue='termination_reason',
                    data=self.episode_df
                )
                plt.xlabel('Episode Length')
                plt.ylabel('Total Reward')
                plt.title('Episode Length vs Reward')
                
                pdf.savefig()
                plt.close()
            
            # 7. Action behavior analysis
            if not self.episode_df.empty:
                plt.figure(figsize=(10, 12))
                
                # Action breakdown by termination reason
                plt.subplot(3, 1, 1)
                term_reasons = self.episode_df['termination_reason'].unique()
                
                # Calculate average action percentages by termination reason
                action_by_term = {reason: {'Refine': 0, 'No Change': 0, 'Coarsen': 0} for reason in term_reasons}
                
                for _, row in self.episode_df.iterrows():
                    reason = row['termination_reason']
                    total = row['refine_count'] + row['coarsen_count'] + row['no_change_count']
                    if total > 0:
                        action_by_term[reason]['Refine'] += row['refine_count'] / total
                        action_by_term[reason]['No Change'] += row['no_change_count'] / total
                        action_by_term[reason]['Coarsen'] += row['coarsen_count'] / total
                
                # Average across episodes with same termination
                for reason in term_reasons:
                    term_count = self.termination_reasons.get(reason, 1)
                    for action in action_by_term[reason]:
                        action_by_term[reason][action] /= term_count
                
                # Create dataframe for plotting
                action_term_data = []
                for reason in term_reasons:
                    for action, value in action_by_term[reason].items():
                        action_term_data.append({
                            'Termination': reason,
                            'Action': action,
                            'Percentage': value * 100
                        })
                
                action_term_df = pd.DataFrame(action_term_data)
                
                # Plot
                sns.barplot(x='Termination', y='Percentage', hue='Action', data=action_term_df)
                plt.xticks(rotation=45, ha='right')
                plt.title('Action Distribution by Termination Reason')
                plt.ylabel('Average Percentage (%)')
                
                # Resource usage vs. refine percentage
                plt.subplot(3, 1, 2)
                sns.scatterplot(
                    x='refine_pct', 
                    y='final_resource_usage',
                    hue='termination_reason',
                    data=self.episode_df
                )
                plt.axhline(y=1.0, color='r', linestyle='--', label='Budget limit')
                plt.xlabel('Refine Action Percentage')
                plt.ylabel('Final Resource Usage')
                plt.title('Resource Usage vs. Refine Action Percentage')
                
                # Refine percentage by episode (trend)
                plt.subplot(3, 1, 3)
                plt.scatter(self.episode_df['episode'], self.episode_df['refine_pct'] * 100, label='Refine')
                plt.scatter(self.episode_df['episode'], self.episode_df['coarsen_pct'] * 100, label='Coarsen')
                plt.scatter(self.episode_df['episode'], self.episode_df['no_change_pct'] * 100, label='No Change')
                
                # Add trend lines
                if len(self.episode_df) > 5:
                    window = min(20, len(self.episode_df) // 5)
                    if window > 0:
                        plt.plot(
                            self.episode_df['episode'], 
                            self.episode_df['refine_pct'].rolling(window=window, min_periods=1).mean() * 100,
                            'r-', label='Refine Trend'
                        )
                        plt.plot(
                            self.episode_df['episode'],
                            self.episode_df['coarsen_pct'].rolling(window=window, min_periods=1).mean() * 100,
                            'g-', label='Coarsen Trend'
                        )
                        plt.plot(
                            self.episode_df['episode'],
                            self.episode_df['no_change_pct'].rolling(window=window, min_periods=1).mean() * 100,
                            'b-', label='No Change Trend'
                        )
                
                plt.xlabel('Episode')
                plt.ylabel('Action Percentage (%)')
                plt.title('Action Percentages by Episode')
                plt.legend()
                plt.grid(True)
                
                plt.tight_layout()
                pdf.savefig()
                plt.close()

            #8. Add a new page for budget violation analysis if we have data
            if self.pre_termination_elements:
                plt.figure(figsize=(10, 12))
                
                # Subplot 1: Histogram of element counts at violation
                plt.subplot(3, 1, 1)
                plt.hist(self.pre_termination_elements, bins=range(0, max(self.pre_termination_elements) + 5, 1), 
                        alpha=0.7, color='purple')
                
                # Add reference line at budget
                if hasattr(self.model.env, 'element_budget'):
                    budget = self.model.env.element_budget
                else:
                    budget = self.model.env.envs[0].element_budget
                plt.axvline(x=budget, color='r', linestyle='--', label='Element budget')
                
                plt.xlabel('Elements at Budget Violation')
                plt.ylabel('Count')
                plt.title('Distribution of Element Counts at Budget Violation')
                plt.legend()
                plt.grid(True)
                
                # Subplot 2: Actions that triggered violations
                plt.subplot(3, 1, 2)
                action_names = ['-1 (Coarsen)', '0 (No Change)', '1 (Refine)']
                action_counts = [0, 0, 0]
                for action in self.violation_actions:
                    # Adjust for action mapping
                    idx = action + 1
                    if 0 <= idx < 3:
                        action_counts[idx] += 1
                
                plt.bar(action_names, action_counts, color=['green', 'gray', 'red'])
                plt.xlabel('Action Type')
                plt.ylabel('Count')
                plt.title('Actions That Triggered Budget Violations')
                plt.grid(True, axis='y')
                
                # Subplot 3: Budget usage percentage at violation
                plt.subplot(3, 1, 3)
                plt.hist(self.budget_usage_at_violation, bins=20, alpha=0.7, color='blue')
                plt.axvline(x=1.0, color='r', linestyle='--', label='Budget limit (100%)')
                plt.xlabel('Budget Usage at Violation (percentage)')
                plt.ylabel('Count')
                plt.title('Budget Usage Percentage at Violation')
                plt.legend()
                plt.grid(True)
                
                plt.tight_layout()
                pdf.savefig()
                plt.close()
                
        if self.verbose > 0:
            print(f"Final report generated and saved to: {report_path}")
            
        # Also save raw data as Excel with multiple sheets
        excel_path = os.path.join(self.log_dir, "training_data.xlsx")
        with pd.ExcelWriter(excel_path) as writer:
            # Episode data
            if not self.episode_df.empty:
                self.episode_df.to_excel(writer, sheet_name='Episodes', index=False)
            
            # Create action summary sheet
            action_summary = pd.DataFrame({
                'Action': list(self.action_names.values()),
                'Count': [self.action_counts.get(a, 0) for a in self.action_names.keys()],
                'Percentage': [self.action_counts.get(a, 0) / max(1, sum(self.action_counts.values())) * 100 
                              for a in self.action_names.keys()],
                'Avg Reward': [np.mean(self.rewards_by_action.get(a, [0])) for a in self.action_names.keys()]
            })
            action_summary.to_excel(writer, sheet_name='Action Summary', index=False)
            
            # Termination summary
            if self.termination_reasons:
                term_summary = pd.DataFrame({
                    'Reason': list(self.termination_reasons.keys()),
                    'Count': list(self.termination_reasons.values()),
                    'Percentage': [count / max(1, sum(self.termination_reasons.values())) * 100 
                                  for count in self.termination_reasons.values()]
                })
                term_summary.to_excel(writer, sheet_name='Termination Summary', index=False)
            
            # Aggregate metrics sampled at intervals
            if not self.metrics_df.empty:
                # Sample metrics to avoid excessive file size
                sample_size = min(10000, len(self.metrics_df))
                sample_interval = max(1, len(self.metrics_df) // sample_size)
                sampled_metrics = self.metrics_df.iloc[::sample_interval].copy()
                sampled_metrics.to_excel(writer, sheet_name='Metrics Sample', index=False)
        
        if self.verbose > 0:
            print(f"Raw data saved to: {excel_path}")
            
        # Save path to a text file for easier programmatic access
        with open(os.path.join(self.log_dir, "report_path.txt"), "w") as f:
            f.write(report_path)



# import os
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from typing import Dict, List, Tuple, Any, Optional
# from collections import deque
# from stable_baselines3.common.callbacks import BaseCallback


# class EnhancedMonitorCallback(BaseCallback):
#     """
#     Enhanced callback for monitoring RL training in adaptive mesh refinement.
    
#     Tracks:
#     - Action distribution over time
#     - Resource usage statistics
#     - Termination reasons
#     - Reward breakdown by action type
#     - Budget proximity at decision time
    
#     Provides visualization capabilities and periodic reporting.
#     """
    
#     def __init__(
#         self, 
#         total_timesteps: int,
#         log_dir: str,
#         save_freq: int = 10000,
#         verbose: int = 1,
#         window_size: int = 100,
#         action_mapping: Dict[int, int] = {0: -1, 1: 0, 2: 1},
#         log_freq: int = 1000
#     ):
#         """
#         Initialize the callback with monitoring parameters.
        
#         Args:
#             total_timesteps: Total timesteps for the training run
#             log_dir: Directory to save logs and visualizations
#             save_freq: Frequency (in timesteps) to save the model
#             verbose: Verbosity level (0: no output, 1: info, 2: debug)
#             window_size: Window size for moving averages
#             action_mapping: Mapping from action space integers to semantic values
#             log_freq: Frequency (in timesteps) to log statistics
#         """
#         super().__init__(verbose)
#         self.total_timesteps = total_timesteps
#         self.log_dir = log_dir
#         self.save_freq = save_freq
#         self.window_size = window_size
#         self.log_freq = log_freq
#         self.action_mapping = action_mapping
#         self.action_names = {-1: "Coarsen", 0: "No Change", 1: "Refine"}
        
#         # Create metrics directory
#         self.metrics_dir = os.path.join(log_dir, "metrics")
#         os.makedirs(self.metrics_dir, exist_ok=True)
        
#         # Create plots directory
#         self.plots_dir = os.path.join(log_dir, "plots")
#         os.makedirs(self.plots_dir, exist_ok=True)
        
#         # Initialize tracking variables
#         self.reset_tracking()
        
#     def reset_tracking(self):
#         """Reset all tracking metrics."""
#         # Action tracking
#         self.action_counts = {action: 0 for action in self.action_mapping.values()}
#         self.action_history = []
#         self.mapped_action_history = []
        
#         # Reward tracking
#         self.rewards_by_action = {action: [] for action in self.action_mapping.values()}
#         self.episode_rewards = []
#         self.cumulative_reward = 0
#         self.reward_history = []
        
#         # Resource tracking
#         self.resource_usage_history = []
#         self.element_count_history = []
#         self.budget_proximity_history = []  # % of budget used
        
#         # Episode tracking
#         self.episode_lengths = []
#         self.termination_reasons = {}
#         self.episodes_completed = 0
        
#         # Time step tracking
#         self.timestep_history = []  # Track when physical time steps occur
        
#         # Moving windows for recent statistics
#         self.recent_rewards = deque(maxlen=self.window_size)
#         self.recent_actions = deque(maxlen=self.window_size)
#         self.recent_resources = deque(maxlen=self.window_size)
        
#         # Initialize tracking dataframes
#         self.metrics_df = pd.DataFrame()
#         self.episode_df = pd.DataFrame()

#         # Add these new tracking variables
#         self.pre_termination_elements = []
#         self.budget_usage_at_violation = []
#         self.violation_actions = []
#     def _on_training_start(self) -> None:
#         """Called when training starts. Add configuration info to TensorBoard."""
#         # Initialize dataframes with correct columns
#         self.metrics_df = pd.DataFrame(columns=[
#             'timestep', 'action', 'mapped_action', 'reward', 
#             'resource_usage', 'element_count', 'budget_proximity',
#             'took_timestep', 'episode'
#         ])
        
#         self.episode_df = pd.DataFrame(columns=[
#             'episode', 'total_reward', 'length', 'termination_reason',
#             'final_element_count', 'final_resource_usage',
#             'refine_count', 'coarsen_count', 'no_change_count',
#             'refine_pct', 'coarsen_pct', 'no_change_pct'
#         ])
        
#         # Set plot style
#         sns.set(style="whitegrid")
#         plt.rcParams.update({'figure.figsize': (12, 8)})
        
#         # Log configuration parameters
#         if self.logger is not None:
#             # Log element budget
#             try:
#                 budget = self.model.env.unwrapped.element_budget
#             except (AttributeError, KeyError):
#                 try:
#                     budget = self.model.env.get_wrapper_attr('element_budget')
#                 except (AttributeError, KeyError):
#                     budget = self.model.env.envs[0].unwrapped.element_budget
            
#             self.logger.record("environment/element_budget", budget)
            
#             # Log gamma_c
#             try:
#                 gamma_c = self.model.env.unwrapped.gamma_c
#             except (AttributeError, KeyError):
#                 try:
#                     gamma_c = self.model.env.get_wrapper_attr('gamma_c')
#                 except (AttributeError, KeyError):
#                     gamma_c = self.model.env.envs[0].unwrapped.gamma_c
            
#             self.logger.record("environment/gamma_c", gamma_c)
            
#             # Log max episode steps
#             try:
#                 max_steps = self.model.env.unwrapped.max_episode_steps
#             except (AttributeError, KeyError):
#                 try:
#                     max_steps = self.model.env.get_wrapper_attr('max_episode_steps')
#                 except (AttributeError, KeyError):
#                     max_steps = self.model.env.envs[0].unwrapped.max_episode_steps
            
#             self.logger.record("environment/max_episode_steps", max_steps)
            
#             # Log RL algorithm information
#             if hasattr(self.model, 'ent_coef'):
#                 self.logger.record("hyperparameters/entropy_coefficient", self.model.ent_coef)
            
#             if hasattr(self.model, 'learning_rate'):
#                 self.logger.record("hyperparameters/learning_rate", self.model.learning_rate)  
#     # def _on_training_start(self) -> None:
#     #     """Called when training starts."""
#     #     # Initialize dataframes with correct columns
#     #     self.metrics_df = pd.DataFrame(columns=[
#     #         'timestep', 'action', 'mapped_action', 'reward', 
#     #         'resource_usage', 'element_count', 'budget_proximity',
#     #         'took_timestep', 'episode'
#     #     ])
        
#     #     self.episode_df = pd.DataFrame(columns=[
#     #         'episode', 'total_reward', 'length', 'termination_reason',
#     #         'final_element_count', 'final_resource_usage',
#     #         'refine_count', 'coarsen_count', 'no_change_count',
#     #         'refine_pct', 'coarsen_pct', 'no_change_pct'
#     #     ])
        
#     #     # Set plot style
#     #     sns.set(style="whitegrid")
#     #     plt.rcParams.update({'figure.figsize': (12, 8)})

    
#     def _on_step(self) -> bool:
#         """
#         Called after each step of the environment.
        
#         Returns:
#             bool: Whether training should continue
#         """
#         # Extract current step information
#         info = self.locals['infos'][0]
#         action = self.locals['actions'][0]
#         reward = self.locals['rewards'][0]
#         obs = self.locals['new_obs']

#         # Capture pre-termination metrics if available
#         if 'pre_termination_elements' in info:
#             self.pre_termination_elements.append(info['pre_termination_elements'])
#             self.budget_usage_at_violation.append(info.get('budget_usage_percent', 0) / 100.0)
#             self.violation_actions.append(info.get('violation_action', 0))
        
#         # Map raw action to semantic action (-1, 0, 1)
#         mapped_action = self.action_mapping[action.item() if hasattr(action, 'item') else int(action)]
        
#         # Update action counters
#         self.action_counts[mapped_action] += 1
#         self.action_history.append(action)
#         self.mapped_action_history.append(mapped_action)
#         self.recent_actions.append(mapped_action)
        
#         # Update reward tracking
#         self.rewards_by_action[mapped_action].append(reward)
#         self.reward_history.append(reward)
#         self.recent_rewards.append(reward)
#         self.cumulative_reward += reward
        
#         # Update resource tracking
#         resource_usage = info.get('resource_usage', 0)
#         element_count = info.get('n_elements', 0)

#         # if hasattr(self.model.env, 'element_budget'):
#         #     budget = self.model.env.element_budget
#         # else:
#         #     budget = self.model.env.envs[0].element_budget
#         try:
#             budget = self.model.env.unwrapped.element_budget
#         except (AttributeError, KeyError):
#             # Fallback for vectorized environments
#             try:
#                 budget = self.model.env.get_wrapper_attr('element_budget')
#             except (AttributeError, KeyError):
#                 # Last resort for vectorized envs
#                 budget = self.model.env.envs[0].unwrapped.element_budget

#         budget_proximity = element_count / budget if budget > 0 else 0
        
#         self.resource_usage_history.append(resource_usage)
#         self.element_count_history.append(element_count)
#         self.budget_proximity_history.append(budget_proximity)
#         self.recent_resources.append(resource_usage)
        
#         # Track physical time steps
#         took_timestep = int(info.get('took_timestep', False))
#         self.timestep_history.append(took_timestep)
        
#         # Update metrics dataframe
#         new_row = {
#             'timestep': self.num_timesteps,
#             'action': action,
#             'mapped_action': mapped_action,
#             'reward': reward,
#             'resource_usage': resource_usage,
#             'element_count': element_count,
#             'budget_proximity': budget_proximity,
#             'took_timestep': took_timestep,
#             'episode': self.episodes_completed
#         }
#         self.metrics_df = pd.concat([self.metrics_df, pd.DataFrame([new_row])], ignore_index=True)
        
#         # Check for episode completion
#         done = self.locals['dones'][0]
#         if done:
#             self._on_episode_end(info)
        
#         # Periodic logging and visualization
#         if self.num_timesteps % self.log_freq == 0:
#             self._log_statistics()
            
#         # Save model periodically
#         if self.num_timesteps % self.save_freq == 0:
#             model_path = os.path.join(self.log_dir, f"model_{self.num_timesteps}_steps")
#             self.model.save(model_path)
            
#             # Save datasets
#             self._save_datasets()
            
#             # Generate visualizations
#             self._generate_visualizations()
            
#             if self.verbose > 0:
#                 print(f"Saved model and metrics at {model_path}")
        
#         # Print progress periodically
#         if self.num_timesteps % 100 == 0:
#             if self.verbose > 0:
#                 progress = self.num_timesteps / self.total_timesteps * 100
#                 print(f"Progress: {self.num_timesteps}/{self.total_timesteps} steps ({progress:.1f}%)")
        
#         # Check if we've exceeded total timesteps
#         if self.num_timesteps >= self.total_timesteps:
#             if self.verbose > 0:
#                 print(f"Reached {self.total_timesteps} timesteps, stopping training")
#             return False
            
#         return True
    
#     def _on_episode_end(self, info: Dict[str, Any]) -> None:
#         """
#         Called when an episode ends.
        
#         Args:
#             info: Information from the last step
#         """
#         # Get episode information
#         episode_info = info.get('episode', {})
#         episode_length = episode_info.get('l', 0)
#         episode_reward = episode_info.get('r', 0)
#         termination_reason = info.get('reason', 'unknown')
        
#         # Update episode counters
#         self.episodes_completed += 1
#         self.episode_rewards.append(episode_reward)
#         self.episode_lengths.append(episode_length)
        
#         # Update termination statistics
#         if termination_reason not in self.termination_reasons:
#             self.termination_reasons[termination_reason] = 0
#         self.termination_reasons[termination_reason] += 1
        
#         # Calculate action distribution for this episode
#         episode_actions = self.mapped_action_history[-episode_length:] if episode_length > 0 else []
#         refine_count = sum(1 for a in episode_actions if a == 1)
#         coarsen_count = sum(1 for a in episode_actions if a == -1)
#         no_change_count = sum(1 for a in episode_actions if a == 0)
#         total_actions = len(episode_actions)
        
#         refine_pct = refine_count / total_actions if total_actions > 0 else 0
#         coarsen_pct = coarsen_count / total_actions if total_actions > 0 else 0
#         no_change_pct = no_change_count / total_actions if total_actions > 0 else 0
        
#         # Get final resource state
#         final_resource_usage = self.resource_usage_history[-1] if self.resource_usage_history else 0
#         final_element_count = self.element_count_history[-1] if self.element_count_history else 0
        
#         # Update episode dataframe
#         new_row = {
#             'episode': self.episodes_completed,
#             'total_reward': episode_reward,
#             'length': episode_length,
#             'termination_reason': termination_reason,
#             'final_element_count': final_element_count,
#             'final_resource_usage': final_resource_usage,
#             'refine_count': refine_count,
#             'coarsen_count': coarsen_count,
#             'no_change_count': no_change_count,
#             'refine_pct': refine_pct,
#             'coarsen_pct': coarsen_pct,
#             'no_change_pct': no_change_pct
#         }
#         self.episode_df = pd.concat([self.episode_df, pd.DataFrame([new_row])], ignore_index=True)
        
#         # Log episode completion
#         if self.verbose > 0 and (self.episodes_completed % 10 == 0):
#             print(f"\nEpisode {self.episodes_completed} completed:")
#             print(f"  Reward: {episode_reward:.2f}")
#             print(f"  Length: {episode_length}")
#             print(f"  Termination: {termination_reason}")
#             print(f"  Final elements: {final_element_count}")
#             print(f"  Action distribution: Refine={refine_pct:.1%}, No Change={no_change_pct:.1%}, Coarsen={coarsen_pct:.1%}")
    


#     def _log_statistics(self) -> None:
#         """Log current training statistics with consistent naming conventions."""
#         if not self.recent_rewards:
#             return
            
#         # Calculate statistics
#         recent_reward_mean = np.mean(self.recent_rewards)
        
#         # Calculate action distribution
#         action_counts = {self.action_names[a]: 0 for a in self.action_mapping.values()}
#         for action in self.recent_actions:
#             action_counts[self.action_names[action]] += 1
#         total_actions = len(self.recent_actions)
#         action_dist = {k: v/total_actions for k, v in action_counts.items()} if total_actions > 0 else action_counts
        
#         # Calculate average resource usage
#         avg_resource = np.mean(self.recent_resources) if self.recent_resources else 0
        
#         # Log to console
#         if self.verbose > 0:
#             print(f"\nStatistics at step {self.num_timesteps}:")
#             print(f"  Recent mean reward: {recent_reward_mean:.2f}")
#             print(f"  Episodes completed: {self.episodes_completed}")
#             print(f"  Action distribution: {', '.join([f'{k}: {v:.1%}' for k, v in action_dist.items()])}")
#             print(f"  Average resource usage: {avg_resource:.1%}")
            
#             # Print termination statistics if available
#             if self.termination_reasons:
#                 total_episodes = sum(self.termination_reasons.values())
#                 print(f"  Termination reasons:")
#                 for reason, count in self.termination_reasons.items():
#                     print(f"    {reason}: {count/total_episodes:.1%}")
        
#         # Log to stable-baselines logger using consistent naming conventions
#         if self.logger is not None:
#             # Action proportions - use standard naming format
#             for action_name, proportion in action_dist.items():
#                 action_key = action_name.lower().replace(" ", "_")
#                 self.logger.record(f"actions/{action_key}_proportion", proportion)
            
#             # Resources - use standard naming
#             self.logger.record("resources/usage", avg_resource)
            
#             # Training progress
#             self.logger.record("training/episodes_completed", self.episodes_completed)
#             self.logger.record("training/recent_reward_mean", recent_reward_mean)
            
#             # Termination reasons - ensure consistent naming
#             total_episodes = sum(self.termination_reasons.values()) if self.termination_reasons else 1
#             for reason, count in self.termination_reasons.items():
#                 if len(reason) > 30:
#                     import hashlib
#                     short_hash = hashlib.md5(reason.encode()).hexdigest()[:8]
#                     sanitized_reason = f"error_type_{short_hash}"
#                 else:
#                     sanitized_reason = reason.lower().replace(" ", "_")
                
#                 # Log both raw count and percentage
#                 self.logger.record(f"termination/{sanitized_reason}", count)
#                 self.logger.record(f"termination/{sanitized_reason}_pct", count/total_episodes)

#     # def _log_statistics(self) -> None:
#     #     """Log current training statistics."""
#     #     if not self.recent_rewards:
#     #         return
            
#     #     # Calculate statistics
#     #     recent_reward_mean = np.mean(self.recent_rewards)
        
#     #     # Calculate action distribution
#     #     action_counts = {self.action_names[a]: 0 for a in self.action_mapping.values()}
#     #     for action in self.recent_actions:
#     #         action_counts[self.action_names[action]] += 1
#     #     total_actions = len(self.recent_actions)
#     #     action_dist = {k: v/total_actions for k, v in action_counts.items()} if total_actions > 0 else action_counts
        
#     #     # Calculate average resource usage
#     #     avg_resource = np.mean(self.recent_resources) if self.recent_resources else 0
        
#     #     # Log to console
#     #     if self.verbose > 0:
#     #         print(f"\nStatistics at step {self.num_timesteps}:")
#     #         print(f"  Recent mean reward: {recent_reward_mean:.2f}")
#     #         print(f"  Episodes completed: {self.episodes_completed}")
#     #         print(f"  Action distribution: {', '.join([f'{k}: {v:.1%}' for k, v in action_dist.items()])}")
#     #         print(f"  Average resource usage: {avg_resource:.1%}")
            
#     #         # Print termination statistics if available
#     #         if self.termination_reasons:
#     #             total_episodes = sum(self.termination_reasons.values())
#     #             print(f"  Termination reasons:")
#     #             for reason, count in self.termination_reasons.items():
#     #                 print(f"    {reason}: {count/total_episodes:.1%}")
        
#     #     # Log to stable-baselines logger
#     #     if self.logger is not None:
#     #         for action_name, proportion in action_dist.items():
#     #             self.logger.record(f"actions/{action_name.lower()}_proportion", proportion)
            
#     #         self.logger.record("resources/usage", avg_resource)
#     #         self.logger.record("training/episodes_completed", self.episodes_completed)
            
#     #         # for reason, count in self.termination_reasons.items():
#     #         #     sanitized_reason = reason.lower().replace(" ", "_")
#     #         #     self.logger.record(f"termination/{sanitized_reason}", count)
#     #         for reason, count in self.termination_reasons.items():
#     #             # Create a shorter, hash-based key for long termination reasons
#     #             if len(reason) > 30:
#     #                 import hashlib
#     #                 short_hash = hashlib.md5(reason.encode()).hexdigest()[:8]
#     #                 sanitized_reason = f"error_type_{short_hash}"
#     #             else:
#     #                 sanitized_reason = reason.lower().replace(" ", "_")
                
#     #             self.logger.record(f"termination/{sanitized_reason}", count)
                
#     #             # Also log the mapping for reference (optional)
#     #             if len(reason) > 30:
#     #                 print(f"Mapped long error '{reason}' to '{sanitized_reason}'")
    
#     def _save_datasets(self) -> None:
#         """Save collected data to CSV files."""
#         # Save metrics dataframe
#         metrics_path = os.path.join(self.metrics_dir, f"metrics_{self.num_timesteps}.csv")
#         self.metrics_df.to_csv(metrics_path, index=False)
        
#         # Save episode dataframe
#         episode_path = os.path.join(self.metrics_dir, f"episodes_{self.num_timesteps}.csv")
#         self.episode_df.to_csv(episode_path, index=False)
    
#     def _generate_visualizations(self) -> None:
#         """Generate and save visualizations of training progress."""
#         timestamp = self.num_timesteps
        
#         # 1. Action distribution over time
#         self._plot_action_distribution(timestamp)
        
#         # 2. Rewards by action type
#         self._plot_rewards_by_action(timestamp)
        
#         # 3. Resource usage over time
#         self._plot_resource_usage(timestamp)
        
#         # 4. Termination reasons
#         self._plot_termination_reasons(timestamp)
        
#         # 5. Budget proximity histogram
#         self._plot_budget_proximity(timestamp)
        
#         # 6. Episode lengths over time
#         self._plot_episode_lengths(timestamp)
        
#         # 7. Combined dashboard
#         self._plot_dashboard(timestamp)
    
#     def _plot_action_distribution(self, timestamp: int) -> None:
#         """Plot action distribution over time."""
#         if len(self.mapped_action_history) < 10:
#             return
            
#         plt.figure(figsize=(10, 6))
        
#         # Convert action history to dataframe for easier plotting
#         df = pd.DataFrame({
#             'timestep': range(len(self.mapped_action_history)),
#             'action': [self.action_names[a] for a in self.mapped_action_history]
#         })
        
#         # Calculate rolling window of action proportions
#         window = min(1000, len(df) // 10)
#         action_counts = df.groupby('timestep')['action'].value_counts().unstack().fillna(0)
        
#         # Apply rolling window
#         if window > 0:
#             action_counts = action_counts.rolling(window=window, min_periods=1).mean()
        
#         # Plot
#         for column in action_counts.columns:
#             plt.plot(action_counts.index, action_counts[column], label=column)
        
#         plt.xlabel('Timestep')
#         plt.ylabel('Proportion')
#         plt.title('Action Distribution Over Time')
#         plt.legend()
#         plt.grid(True)
        
#         # Save figure
#         plt.savefig(os.path.join(self.plots_dir, f"action_distribution_{timestamp}.png"))
#         plt.close()
    
#     def _plot_rewards_by_action(self, timestamp: int) -> None:
#         """Plot rewards by action type."""
#         plt.figure(figsize=(10, 6))
        
#         # Prepare data
#         data = []
#         for action, rewards in self.rewards_by_action.items():
#             if rewards:
#                 data.append({
#                     'Action': self.action_names[action],
#                     'Rewards': rewards
#                 })
        
#         # Plot boxplots
#         if data:
#             df = pd.DataFrame(data)
#             sns.boxplot(x='Action', y='Rewards', data=pd.DataFrame({
#                 'Action': np.concatenate([[d['Action']] * len(d['Rewards']) for d in data]),
#                 'Rewards': np.concatenate([d['Rewards'] for d in data])
#             }))
            
#             plt.title('Reward Distribution by Action Type')
#             plt.xlabel('Action')
#             plt.ylabel('Reward')
#             plt.grid(True)
            
#             # Save figure
#             plt.savefig(os.path.join(self.plots_dir, f"rewards_by_action_{timestamp}.png"))
        
#         plt.close()
    
#     def _plot_resource_usage(self, timestamp: int) -> None:
#         """Plot resource usage over time."""
#         if not self.resource_usage_history:
#             return
            
#         plt.figure(figsize=(10, 6))
        
#         # Plot resource usage
#         plt.plot(range(len(self.resource_usage_history)), self.resource_usage_history)
        
#         # Add reference line at 100%
#         plt.axhline(y=1.0, color='r', linestyle='--', label='Budget limit')
        
#         plt.xlabel('Timestep')
#         plt.ylabel('Resource Usage')
#         plt.title('Resource Usage Over Time')
#         plt.legend()
#         plt.grid(True)
        
#         # Save figure
#         plt.savefig(os.path.join(self.plots_dir, f"resource_usage_{timestamp}.png"))
#         plt.close()
        
#         # Also plot element count
#         plt.figure(figsize=(10, 6))
#         plt.plot(range(len(self.element_count_history)), self.element_count_history)
        
#         # Add reference line at budget
#         # if hasattr(self.model.env, 'element_budget'):
#         #     budget = self.model.env.element_budget
#         # else:
#         #     budget = self.model.env.envs[0].element_budget
#         try:
#             budget = self.model.env.unwrapped.element_budget
#         except (AttributeError, KeyError):
#             # Fallback for vectorized environments
#             try:
#                 budget = self.model.env.get_wrapper_attr('element_budget')
#             except (AttributeError, KeyError):
#                 # Last resort for vectorized envs
#                 budget = self.model.env.envs[0].unwrapped.element_budget


#         plt.axhline(y=budget, color='r', linestyle='--', label='Element budget')
        
#         plt.xlabel('Timestep')
#         plt.ylabel('Element Count')
#         plt.title('Element Count Over Time')
#         plt.legend()
#         plt.grid(True)
        
#         # Save figure
#         plt.savefig(os.path.join(self.plots_dir, f"element_count_{timestamp}.png"))
#         plt.close()

#         # Add new visualization for pre-termination element counts if data exists
#         if self.pre_termination_elements:
#             plt.figure(figsize=(10, 6))
            
#             # Plot histogram of element counts at termination
#             plt.hist(self.pre_termination_elements, bins=range(0, max(self.pre_termination_elements) + 5, 1), 
#                     alpha=0.7, color='purple')
            
#             # Add reference line at budget
#             # if hasattr(self.model.env, 'element_budget'):
#             #     budget = self.model.env.element_budget
#             # else:
#             #     budget = self.model.env.envs[0].element_budget
#             try:
#                 budget = self.model.env.unwrapped.element_budget
#             except (AttributeError, KeyError):
#                 # Fallback for vectorized environments
#                 try:
#                     budget = self.model.env.get_wrapper_attr('element_budget')
#                 except (AttributeError, KeyError):
#                     # Last resort for vectorized envs
#                     budget = self.model.env.envs[0].unwrapped.element_budget


#             plt.axvline(x=budget, color='r', linestyle='--', label='Element budget')
            
#             plt.xlabel('Elements at Budget Violation')
#             plt.ylabel('Count')
#             plt.title('Distribution of Element Counts at Budget Violation')
#             plt.legend()
#             plt.grid(True)
            
#             # Save figure
#             plt.savefig(os.path.join(self.plots_dir, f"pre_termination_elements_{timestamp}.png"))
#             plt.close()
        
#         # Also visualize the actions that led to budget violations
#         if self.violation_actions:
#             plt.figure(figsize=(10, 6))
            
#             # Map actions to names
#             action_names = ['-1 (Coarsen)', '0 (No Change)', '1 (Refine)']
#             action_counts = [0, 0, 0]
#             for action in self.violation_actions:
#                 # Adjust for action mapping (usually -1, 0, 1)
#                 idx = action + 1
#                 if 0 <= idx < 3:
#                     action_counts[idx] += 1
            
#             # Plot bar chart
#             plt.bar(action_names, action_counts, color=['green', 'gray', 'red'])
#             plt.xlabel('Action Type')
#             plt.ylabel('Count')
#             plt.title('Actions That Triggered Budget Violations')
#             plt.grid(True, axis='y')
            
#             # Save figure
#             plt.savefig(os.path.join(self.plots_dir, f"violation_actions_{timestamp}.png"))
#             plt.close()
    
#     def _plot_termination_reasons(self, timestamp: int) -> None:
#         """Plot distribution of episode termination reasons."""
#         if not self.termination_reasons:
#             return
            
#         plt.figure(figsize=(10, 6))
        
#         # Prepare data
#         reasons = list(self.termination_reasons.keys())
#         counts = list(self.termination_reasons.values())
        
#         # Plot
#         plt.bar(reasons, counts)
#         plt.xticks(rotation=45, ha='right')
#         plt.xlabel('Termination Reason')
#         plt.ylabel('Count')
#         plt.title('Episode Termination Reasons')
#         plt.tight_layout()
        
#         # Save figure
#         plt.savefig(os.path.join(self.plots_dir, f"termination_reasons_{timestamp}.png"))
#         plt.close()
        
#         # Also plot as pie chart
#         plt.figure(figsize=(8, 8))
#         plt.pie(counts, labels=reasons, autopct='%1.1f%%')
#         plt.title('Episode Termination Reasons')
        
#         # Save figure
#         plt.savefig(os.path.join(self.plots_dir, f"termination_pie_{timestamp}.png"))
#         plt.close()
    
#     def _plot_budget_proximity(self, timestamp: int) -> None:
#         """Plot histogram of budget proximity at termination."""
#         if not self.episode_df.empty:
#             plt.figure(figsize=(10, 6))
            
#             # Plot histogram of final resource usage
#             sns.histplot(self.episode_df['final_resource_usage'], bins=20)
            
#             plt.xlabel('Resource Usage (at episode end)')
#             plt.ylabel('Count')
#             plt.title('Distribution of Resource Usage at Episode Termination')
            
#             # Add reference line at 100%
#             plt.axvline(x=1.0, color='r', linestyle='--', label='Budget limit')
#             plt.legend()
            
#             # Save figure
#             plt.savefig(os.path.join(self.plots_dir, f"budget_proximity_{timestamp}.png"))
#             plt.close()
    
#     def _plot_episode_lengths(self, timestamp: int) -> None:
#         """Plot episode lengths over time."""
#         if not self.episode_lengths:
#             return
            
#         plt.figure(figsize=(10, 6))
        
#         # Plot episode lengths
#         plt.plot(range(1, len(self.episode_lengths) + 1), self.episode_lengths)
        
#         plt.xlabel('Episode')
#         plt.ylabel('Length')
#         plt.title('Episode Lengths Over Time')
#         plt.grid(True)
        
#         # Save figure
#         plt.savefig(os.path.join(self.plots_dir, f"episode_lengths_{timestamp}.png"))
#         plt.close()
        
#         # Also plot episode rewards
#         if self.episode_rewards:
#             plt.figure(figsize=(10, 6))
#             plt.plot(range(1, len(self.episode_rewards) + 1), self.episode_rewards)
            
#             # Add smoothed line
#             window = min(25, len(self.episode_rewards) // 4)
#             if window > 0:
#                 smoothed = pd.Series(self.episode_rewards).rolling(window=window, min_periods=1).mean()
#                 plt.plot(range(1, len(self.episode_rewards) + 1), smoothed, 'r-', label=f'{window}-episode moving avg')
            
#             plt.xlabel('Episode')
#             plt.ylabel('Total Reward')
#             plt.title('Episode Rewards Over Time')
#             plt.legend()
#             plt.grid(True)
            
#             # Save figure
#             plt.savefig(os.path.join(self.plots_dir, f"episode_rewards_{timestamp}.png"))
#             plt.close()
    
#     def _plot_dashboard(self, timestamp: int) -> None:
#         """Create a comprehensive dashboard of training metrics."""
#         if not self.metrics_df.empty and self.episodes_completed > 5:
#             # Create a multi-panel dashboard
#             fig = plt.figure(figsize=(16, 12))
#             gs = fig.add_gridspec(3, 2)
            
#             # 1. Rewards over time (smoothed)
#             ax1 = fig.add_subplot(gs[0, 0])
#             if self.episode_rewards:
#                 ax1.plot(range(1, len(self.episode_rewards) + 1), self.episode_rewards, 'b-', alpha=0.3)
                
#                 # Add smoothed line
#                 window = min(25, len(self.episode_rewards) // 4)
#                 if window > 0:
#                     smoothed = pd.Series(self.episode_rewards).rolling(window=window, min_periods=1).mean()
#                     ax1.plot(range(1, len(self.episode_rewards) + 1), smoothed, 'b-', label=f'Moving avg')
                
#                 ax1.set_xlabel('Episode')
#                 ax1.set_ylabel('Total Reward')
#                 ax1.set_title('Episode Rewards')
#                 ax1.legend()
#                 ax1.grid(True)
            
#             # 2. Action distribution (most recent window)
#             ax2 = fig.add_subplot(gs[0, 1])
#             if self.episode_df.empty:
#                 action_data = [
#                     self.action_counts.get(-1, 0),
#                     self.action_counts.get(0, 0),
#                     self.action_counts.get(1, 0)
#                 ]
#                 labels = ['Coarsen', 'No Change', 'Refine']
#             else:
#                 # Get recent episodes
#                 recent_n = min(20, len(self.episode_df))
#                 recent_df = self.episode_df.tail(recent_n)
#                 action_data = [
#                     recent_df['coarsen_count'].sum(),
#                     recent_df['no_change_count'].sum(),
#                     recent_df['refine_count'].sum()
#                 ]
#                 labels = ['Coarsen', 'No Change', 'Refine']
            
#             # Ensure we have some data
#             if sum(action_data) > 0:
#                 ax2.pie(action_data, labels=labels, autopct='%1.1f%%')
#                 ax2.set_title('Recent Action Distribution')
            
#             # 3. Episode termination reasons
#             ax3 = fig.add_subplot(gs[1, 0])
#             if self.termination_reasons:
#                 reasons = list(self.termination_reasons.keys())
#                 counts = list(self.termination_reasons.values())
#                 ax3.bar(reasons, counts)
#                 positions = np.arange(len(reasons))
#                 ax3.set_xticks(positions)
#                 ax3.set_xticklabels(reasons, rotation=45, ha='right')
#                 ax3.set_xlabel('Reason')
#                 ax3.set_ylabel('Count')
#                 ax3.set_title('Episode Termination Reasons')
            
#             # 4. Resource usage distribution by termination reason
#             ax4 = fig.add_subplot(gs[1, 1])
#             if not self.episode_df.empty:
#                 # Group by termination reason
#                 term_groups = self.episode_df.groupby('termination_reason')
                
#                 # Boxplot of final resource usage by termination reason
#                 if len(term_groups) > 0:
#                     sns.boxplot(x='termination_reason', y='final_resource_usage', data=self.episode_df, ax=ax4)
#                     current_ticks = ax4.get_xticks()  # Get current tick positions
#                     ax4.set_xticks(current_ticks)
#                     ax4.set_xticklabels(ax4.get_xticklabels(), rotation=45, ha='right')
#                     ax4.set_xlabel('Termination Reason')
#                     ax4.set_ylabel('Final Resource Usage')
#                     ax4.set_title('Resource Usage by Termination Reason')
#                     ax4.axhline(y=1.0, color='r', linestyle='--', label='Budget limit')
#                     ax4.legend()
            
#             # 5. Episode length vs reward scatter
#             ax5 = fig.add_subplot(gs[2, 0])
#             if not self.episode_df.empty:
#                 sns.scatterplot(
#                     x='length', 
#                     y='total_reward',
#                     hue='termination_reason',
#                     data=self.episode_df,
#                     ax=ax5
#                 )
#                 ax5.set_xlabel('Episode Length')
#                 ax5.set_ylabel('Total Reward')
#                 ax5.set_title('Episode Length vs Reward')
                
#                 # Keep legend readable
#                 if len(self.episode_df['termination_reason'].unique()) > 3:
#                     ax5.legend(loc='upper left', bbox_to_anchor=(1, 1))
            
#             # 6. Training progress metrics
#             ax6 = fig.add_subplot(gs[2, 1])
#             progress_text = [
#                 f"Training Progress: {self.num_timesteps}/{self.total_timesteps} steps ({self.num_timesteps/self.total_timesteps*100:.1f}%)",
#                 f"Episodes Completed: {self.episodes_completed}",
#                 f"Termination Reasons:"
#             ]
            
#             # Add termination stats
#             if self.termination_reasons:
#                 total_episodes = sum(self.termination_reasons.values())
#                 for reason, count in self.termination_reasons.items():
#                     progress_text.append(f"  - {reason}: {count} ({count/total_episodes*100:.1f}%)")
            
#             # Add action stats
#             total_actions = sum(self.action_counts.values())
#             if total_actions > 0:
#                 progress_text.append("\nAction Distribution:")
#                 for action, name in self.action_names.items():
#                     count = self.action_counts.get(action, 0)
#                     progress_text.append(f"  - {name}: {count} ({count/total_actions*100:.1f}%)")
                
#             # Add reward stats
#             if self.episode_rewards:
#                 progress_text.append("\nReward Statistics:")
#                 progress_text.append(f"  - Mean Reward: {np.mean(self.episode_rewards):.2f}")
#                 progress_text.append(f"  - Min Reward: {np.min(self.episode_rewards):.2f}")
#                 progress_text.append(f"  - Max Reward: {np.max(self.episode_rewards):.2f}")
            
#             # Create text box
#             ax6.axis('off')
#             ax6.text(0, 1, '\n'.join(progress_text), fontsize=10, va='top')
            
#             # Adjust layout and save
#             plt.tight_layout()
#             plt.savefig(os.path.join(self.plots_dir, f"dashboard_{timestamp}.png"))
#             plt.close()
#     def on_training_end(self) -> None:
#         """Called when training ends."""
#         # Save final datasets
#         self._save_datasets()
        
#         # Generate final visualizations
#         self._generate_visualizations()
        
#         # Create final comprehensive report
#         self._create_final_report()
        
#         # Save a metadata file to help the analysis script
#         self._save_analysis_metadata()


#     # def on_training_end(self) -> None:
#     #     """Called when training ends."""
#     #     # Save final datasets
#     #     self._save_datasets()
        
#     #     # Generate final visualizations
#     #     self._generate_visualizations()
        
#     #     # Create final comprehensive report
#     #     self._create_final_report()
#     def _create_final_report(self) -> None:
#         """Create a comprehensive final report with training statistics and added metadata."""
#         import matplotlib.pyplot as plt
#         from matplotlib.backends.backend_pdf import PdfPages
#         import datetime
        
#         report_path = os.path.join(self.log_dir, "training_report.pdf")
        
#         with PdfPages(report_path) as pdf:
#             # 1. Summary Page with metadata
#             plt.figure(figsize=(10, 12))
#             plt.axis('off')
            
#             # Prepare metadata and summary text
#             # Get environment parameters
#             try:
#                 budget = self.model.env.unwrapped.element_budget
#                 gamma_c = self.model.env.unwrapped.gamma_c
#                 max_steps = self.model.env.unwrapped.max_episode_steps
#             except (AttributeError, KeyError):
#                 try:
#                     budget = self.model.env.get_wrapper_attr('element_budget')
#                     gamma_c = self.model.env.get_wrapper_attr('gamma_c')
#                     max_steps = self.model.env.get_wrapper_attr('max_episode_steps')
#                 except (AttributeError, KeyError):
#                     budget = self.model.env.envs[0].unwrapped.element_budget
#                     gamma_c = self.model.env.envs[0].unwrapped.gamma_c
#                     max_steps = self.model.env.envs[0].unwrapped.max_episode_steps
            
#             # Create metadata section
#             metadata_text = [
#                 "# Experiment Configuration",
#                 f"Element Budget: {budget}",
#                 f"Gamma_C: {gamma_c}",
#                 f"Max Episode Steps: {max_steps}",
#             ]
            
#             if hasattr(self.model, 'ent_coef'):
#                 metadata_text.append(f"Entropy Coefficient: {self.model.ent_coef}")
            
#             if hasattr(self.model, 'learning_rate'):
#                 metadata_text.append(f"Learning Rate: {self.model.learning_rate}")
                
#             # Create summary section
#             summary_text = [
#                 "# Adaptive Mesh Refinement RL Training Summary",
#                 f"Date: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}",
#                 f"Total Steps: {self.num_timesteps}",
#                 f"Episodes Completed: {self.episodes_completed}",
#                 "\n## Termination Statistics"
#             ]
            
#             # Add termination stats
#             if self.termination_reasons:
#                 total_episodes = sum(self.termination_reasons.values())
#                 for reason, count in self.termination_reasons.items():
#                     summary_text.append(f"- {reason}: {count} ({count/total_episodes*100:.1f}%)")
            
#             # Add action stats
#             total_actions = sum(self.action_counts.values())
#             if total_actions > 0:
#                 summary_text.append("\n## Action Distribution")
#                 for action, name in self.action_names.items():
#                     count = self.action_counts.get(action, 0)
#                     summary_text.append(f"- {name}: {count} ({count/total_actions*100:.1f}%)")
                
#             # Add reward stats
#             if self.episode_rewards:
#                 summary_text.append("\n## Reward Statistics")
#                 summary_text.append(f"- Mean Reward: {np.mean(self.episode_rewards):.2f}")
#                 summary_text.append(f"- Min Reward: {np.min(self.episode_rewards):.2f}")
#                 summary_text.append(f"- Max Reward: {np.max(self.episode_rewards):.2f}")
                
#                 # Last 20% of episodes
#                 last_n = max(5, int(len(self.episode_rewards) * 0.2))
#                 last_rewards = self.episode_rewards[-last_n:]
#                 summary_text.append(f"- Mean Reward (last {last_n} episodes): {np.mean(last_rewards):.2f}")
            
#             # Add resource usage stats
#             if self.resource_usage_history:
#                 summary_text.append("\n## Resource Usage")
#                 summary_text.append(f"- Mean Resource Usage: {np.mean(self.resource_usage_history):.2f}")
#                 summary_text.append(f"- Max Resource Usage: {np.max(self.resource_usage_history):.2f}")
                
#                 # Resource usage at termination
#                 if not self.episode_df.empty:
#                     budget_exceeded = (self.episode_df['final_resource_usage'] > 1).sum()
#                     summary_text.append(f"- Episodes ending with budget exceeded: {budget_exceeded} ({budget_exceeded/len(self.episode_df)*100:.1f}%)")
            
#             # Add metadata at the top
#             plt.text(0.05, 0.95, '\n'.join(metadata_text), transform=plt.gca().transAxes, 
#                     fontsize=12, verticalalignment='top', family='monospace',
#                     bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
            
#             # Add summary text below metadata
#             plt.text(0.05, 0.7, '\n'.join(summary_text), transform=plt.gca().transAxes, 
#                     fontsize=12, verticalalignment='top', family='monospace',
#                     bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
            
#             # Add page to PDF
#             pdf.savefig()
#             plt.close()
            
#             # Continue with the rest of the existing report generation...
            
#             # Save the path to a text file for easier programmatic access
#             with open(os.path.join(self.log_dir, "report_path.txt"), "w") as f:
#                 f.write(report_path)
            
#             if self.verbose > 0:
#                 print(f"Final report generated and saved to: {report_path}")
#     # def _create_final_report(self) -> None:
#     #     """Create a comprehensive final report with training statistics."""
#     #     import matplotlib.pyplot as plt
#     #     from matplotlib.backends.backend_pdf import PdfPages
        
#     #     report_path = os.path.join(self.log_dir, "training_report.pdf")
        
#     #     with PdfPages(report_path) as pdf:
#     #         # 1. Summary Page
#     #         plt.figure(figsize=(10, 12))
#     #         plt.axis('off')
            
#     #         # Prepare summary text
#     #         summary_text = [
#     #             "# Adaptive Mesh Refinement RL Training Summary",
#     #             f"Date: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}",
#     #             f"Total Steps: {self.num_timesteps}",
#     #             f"Episodes Completed: {self.episodes_completed}",
#     #             "\n## Termination Statistics"
#     #         ]
            
#     #         # Add termination stats
#     #         if self.termination_reasons:
#     #             total_episodes = sum(self.termination_reasons.values())
#     #             for reason, count in self.termination_reasons.items():
#     #                 summary_text.append(f"- {reason}: {count} ({count/total_episodes*100:.1f}%)")
            
#     #         # Add action stats
#     #         total_actions = sum(self.action_counts.values())
#     #         if total_actions > 0:
#     #             summary_text.append("\n## Action Distribution")
#     #             for action, name in self.action_names.items():
#     #                 count = self.action_counts.get(action, 0)
#     #                 summary_text.append(f"- {name}: {count} ({count/total_actions*100:.1f}%)")
                
#     #         # Add reward stats
#     #         if self.episode_rewards:
#     #             summary_text.append("\n## Reward Statistics")
#     #             summary_text.append(f"- Mean Reward: {np.mean(self.episode_rewards):.2f}")
#     #             summary_text.append(f"- Min Reward: {np.min(self.episode_rewards):.2f}")
#     #             summary_text.append(f"- Max Reward: {np.max(self.episode_rewards):.2f}")
                
#     #             # Last 20% of episodes
#     #             last_n = max(5, int(len(self.episode_rewards) * 0.2))
#     #             last_rewards = self.episode_rewards[-last_n:]
#     #             summary_text.append(f"- Mean Reward (last {last_n} episodes): {np.mean(last_rewards):.2f}")
            
#     #         # Add resource usage stats
#     #         if self.resource_usage_history:
#     #             summary_text.append("\n## Resource Usage")
#     #             summary_text.append(f"- Mean Resource Usage: {np.mean(self.resource_usage_history):.2f}")
#     #             summary_text.append(f"- Max Resource Usage: {np.max(self.resource_usage_history):.2f}")
                
#     #             # Resource usage at termination
#     #             if not self.episode_df.empty:
#     #                 budget_exceeded = (self.episode_df['final_resource_usage'] > 1).sum()
#     #                 summary_text.append(f"- Episodes ending with budget exceeded: {budget_exceeded} ({budget_exceeded/len(self.episode_df)*100:.1f}%)")
            
#     #         # Add text to figure
#     #         plt.text(0.05, 0.95, '\n'.join(summary_text), transform=plt.gca().transAxes, 
#     #                  fontsize=12, verticalalignment='top', family='monospace',
#     #                  bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
            
#     #         # Add page to PDF
#     #         pdf.savefig()
#     #         plt.close()
            
#     #         # 2. Reward Trends
#     #         if self.episode_rewards:
#     #             plt.figure(figsize=(10, 6))
#     #             plt.plot(range(1, len(self.episode_rewards) + 1), self.episode_rewards, 'b-', alpha=0.3)
                
#     #             # Add smoothed line
#     #             window = min(25, len(self.episode_rewards) // 4)
#     #             if window > 0:
#     #                 smoothed = pd.Series(self.episode_rewards).rolling(window=window, min_periods=1).mean()
#     #                 plt.plot(range(1, len(self.episode_rewards) + 1), smoothed, 'b-', label=f'{window}-episode moving avg')
                
#     #             plt.xlabel('Episode')
#     #             plt.ylabel('Total Reward')
#     #             plt.title('Episode Rewards Over Time')
#     #             plt.legend()
#     #             plt.grid(True)
#     #             pdf.savefig()
#     #             plt.close()
                
#     #         # 3. Action Distribution Page
#     #         action_counts = pd.Series(self.mapped_action_history).map(self.action_names).value_counts()
            
#     #         plt.figure(figsize=(10, 8))
            
#     #         # Pie chart of overall distribution
#     #         plt.subplot(2, 1, 1)
#     #         action_counts.plot.pie(autopct='%1.1f%%', ylabel='')
#     #         plt.title('Overall Action Distribution')
            
#     #         # Action distribution evolution
#     #         if len(self.mapped_action_history) > 100:
#     #             plt.subplot(2, 1, 2)
                
#     #             # Convert action history to dataframe for easier plotting
#     #             df = pd.DataFrame({
#     #                 'timestep': range(len(self.mapped_action_history)),
#     #                 'action': [self.action_names[a] for a in self.mapped_action_history]
#     #             })
                
#     #             # Calculate rolling window of action proportions
#     #             window = min(1000, len(df) // 10)
#     #             action_counts_over_time = df.groupby('timestep')['action'].value_counts().unstack().fillna(0)
                
#     #             # Normalize to percentages
#     #             action_sums = action_counts_over_time.sum(axis=1)
#     #             for col in action_counts_over_time.columns:
#     #                 action_counts_over_time[col] = action_counts_over_time[col] / action_sums * 100
                
#     #             # Apply rolling window
#     #             if window > 0:
#     #                 action_counts_over_time = action_counts_over_time.rolling(window=window, min_periods=1).mean()
                
#     #             # Plot
#     #             for column in action_counts_over_time.columns:
#     #                 plt.plot(action_counts_over_time.index, action_counts_over_time[column], label=column)
                
#     #             plt.xlabel('Timestep')
#     #             plt.ylabel('Percentage (%)')
#     #             plt.title('Action Distribution Evolution')
#     #             plt.legend()
#     #             plt.grid(True)
            
#     #         pdf.savefig()
#     #         plt.close()
            
#     #         # 4. Resource Usage Page
#     #         if self.resource_usage_history:
#     #             plt.figure(figsize=(10, 12))
                
#     #             # Resource usage over time
#     #             plt.subplot(3, 1, 1)
#     #             plt.plot(range(len(self.resource_usage_history)), self.resource_usage_history, 'g-')
#     #             plt.axhline(y=1.0, color='r', linestyle='--', label='Budget limit')
#     #             plt.xlabel('Timestep')
#     #             plt.ylabel('Resource Usage')
#     #             plt.title('Resource Usage Over Time')
#     #             plt.legend()
#     #             plt.grid(True)
                
#     #             # Element count over time
#     #             plt.subplot(3, 1, 2)
#     #             plt.plot(range(len(self.element_count_history)), self.element_count_history, 'b-')
                
#     #             # Add reference line at budget
#     #             # if hasattr(self.model.env, 'element_budget'):
#     #             #     budget = self.model.env.element_budget
#     #             # else:
#     #             #     budget = self.model.env.envs[0].element_budget
#     #             try:
#     #                 budget = self.model.env.unwrapped.element_budget
#     #             except (AttributeError, KeyError):
#     #                 # Fallback for vectorized environments
#     #                 try:
#     #                     budget = self.model.env.get_wrapper_attr('element_budget')
#     #                 except (AttributeError, KeyError):
#     #                     # Last resort for vectorized envs
#     #                     budget = self.model.env.envs[0].unwrapped.element_budget

#     #             plt.axhline(y=budget, color='r', linestyle='--', label='Element budget')
                
#     #             plt.xlabel('Timestep')
#     #             plt.ylabel('Element Count')
#     #             plt.title('Element Count Over Time')
#     #             plt.legend()
#     #             plt.grid(True)
                
#     #             # Distribution of final resource usage
#     #             if not self.episode_df.empty:
#     #                 plt.subplot(3, 1, 3)
#     #                 sns.histplot(self.episode_df['final_resource_usage'], bins=20)
#     #                 plt.axvline(x=1.0, color='r', linestyle='--', label='Budget limit')
#     #                 plt.xlabel('Resource Usage (at episode end)')
#     #                 plt.ylabel('Count')
#     #                 plt.title('Distribution of Resource Usage at Episode Termination')
#     #                 plt.legend()
                
#     #             pdf.savefig()
#     #             plt.close()
            
#     #         # 5. Termination Analysis
#     #         if self.termination_reasons:
#     #             plt.figure(figsize=(10, 12))
                
#     #             # Pie chart of termination reasons
#     #             plt.subplot(2, 1, 1)
#     #             reasons = list(self.termination_reasons.keys())
#     #             counts = list(self.termination_reasons.values())
#     #             plt.pie(counts, labels=reasons, autopct='%1.1f%%')
#     #             plt.title('Episode Termination Reasons')
                
#     #             # Resource usage by termination reason
#     #             if not self.episode_df.empty:
#     #                 plt.subplot(2, 1, 2)
#     #                 sns.boxplot(x='termination_reason', y='final_resource_usage', data=self.episode_df)
#     #                 plt.xticks(rotation=45, ha='right')
#     #                 plt.axhline(y=1.0, color='r', linestyle='--', label='Budget limit')
#     #                 plt.xlabel('Termination Reason')
#     #                 plt.ylabel('Final Resource Usage')
#     #                 plt.title('Resource Usage by Termination Reason')
#     #                 plt.legend()
#     #                 plt.tight_layout()
                
#     #             pdf.savefig()
#     #             plt.close()
            
#     #         # 6. Reward Analysis
#     #         if not self.episode_df.empty and len(self.rewards_by_action) > 0:
#     #             plt.figure(figsize=(10, 12))
                
#     #             # Boxplot of rewards by action
#     #             plt.subplot(2, 1, 1)
                
#     #             # Prepare data
#     #             reward_data = []
#     #             for action, rewards in self.rewards_by_action.items():
#     #                 if rewards:
#     #                     for r in rewards:
#     #                         reward_data.append({
#     #                             'Action': self.action_names[action],
#     #                             'Reward': r
#     #                         })
                
#     #             if reward_data:
#     #                 reward_df = pd.DataFrame(reward_data)
#     #                 sns.boxplot(x='Action', y='Reward', data=reward_df)
#     #                 plt.title('Reward Distribution by Action Type')
#     #                 plt.grid(True)
                
#     #             # Scatter plot of episode length vs reward
#     #             plt.subplot(2, 1, 2)
#     #             sns.scatterplot(
#     #                 x='length', 
#     #                 y='total_reward',
#     #                 hue='termination_reason',
#     #                 data=self.episode_df
#     #             )
#     #             plt.xlabel('Episode Length')
#     #             plt.ylabel('Total Reward')
#     #             plt.title('Episode Length vs Reward')
                
#     #             pdf.savefig()
#     #             plt.close()
            
#     #         # 7. Action behavior analysis
#     #         if not self.episode_df.empty:
#     #             plt.figure(figsize=(10, 12))
                
#     #             # Action breakdown by termination reason
#     #             plt.subplot(3, 1, 1)
#     #             term_reasons = self.episode_df['termination_reason'].unique()
                
#     #             # Calculate average action percentages by termination reason
#     #             action_by_term = {reason: {'Refine': 0, 'No Change': 0, 'Coarsen': 0} for reason in term_reasons}
                
#     #             for _, row in self.episode_df.iterrows():
#     #                 reason = row['termination_reason']
#     #                 total = row['refine_count'] + row['coarsen_count'] + row['no_change_count']
#     #                 if total > 0:
#     #                     action_by_term[reason]['Refine'] += row['refine_count'] / total
#     #                     action_by_term[reason]['No Change'] += row['no_change_count'] / total
#     #                     action_by_term[reason]['Coarsen'] += row['coarsen_count'] / total
                
#     #             # Average across episodes with same termination
#     #             for reason in term_reasons:
#     #                 term_count = self.termination_reasons.get(reason, 1)
#     #                 for action in action_by_term[reason]:
#     #                     action_by_term[reason][action] /= term_count
                
#     #             # Create dataframe for plotting
#     #             action_term_data = []
#     #             for reason in term_reasons:
#     #                 for action, value in action_by_term[reason].items():
#     #                     action_term_data.append({
#     #                         'Termination': reason,
#     #                         'Action': action,
#     #                         'Percentage': value * 100
#     #                     })
                
#     #             action_term_df = pd.DataFrame(action_term_data)
                
#     #             # Plot
#     #             sns.barplot(x='Termination', y='Percentage', hue='Action', data=action_term_df)
#     #             plt.xticks(rotation=45, ha='right')
#     #             plt.title('Action Distribution by Termination Reason')
#     #             plt.ylabel('Average Percentage (%)')
                
#     #             # Resource usage vs. refine percentage
#     #             plt.subplot(3, 1, 2)
#     #             sns.scatterplot(
#     #                 x='refine_pct', 
#     #                 y='final_resource_usage',
#     #                 hue='termination_reason',
#     #                 data=self.episode_df
#     #             )
#     #             plt.axhline(y=1.0, color='r', linestyle='--', label='Budget limit')
#     #             plt.xlabel('Refine Action Percentage')
#     #             plt.ylabel('Final Resource Usage')
#     #             plt.title('Resource Usage vs. Refine Action Percentage')
                
#     #             # Refine percentage by episode (trend)
#     #             plt.subplot(3, 1, 3)
#     #             plt.scatter(self.episode_df['episode'], self.episode_df['refine_pct'] * 100, label='Refine')
#     #             plt.scatter(self.episode_df['episode'], self.episode_df['coarsen_pct'] * 100, label='Coarsen')
#     #             plt.scatter(self.episode_df['episode'], self.episode_df['no_change_pct'] * 100, label='No Change')
                
#     #             # Add trend lines
#     #             if len(self.episode_df) > 5:
#     #                 window = min(20, len(self.episode_df) // 5)
#     #                 if window > 0:
#     #                     plt.plot(
#     #                         self.episode_df['episode'], 
#     #                         self.episode_df['refine_pct'].rolling(window=window, min_periods=1).mean() * 100,
#     #                         'r-', label='Refine Trend'
#     #                     )
#     #                     plt.plot(
#     #                         self.episode_df['episode'],
#     #                         self.episode_df['coarsen_pct'].rolling(window=window, min_periods=1).mean() * 100,
#     #                         'g-', label='Coarsen Trend'
#     #                     )
#     #                     plt.plot(
#     #                         self.episode_df['episode'],
#     #                         self.episode_df['no_change_pct'].rolling(window=window, min_periods=1).mean() * 100,
#     #                         'b-', label='No Change Trend'
#     #                     )
                
#     #             plt.xlabel('Episode')
#     #             plt.ylabel('Action Percentage (%)')
#     #             plt.title('Action Percentages by Episode')
#     #             plt.legend()
#     #             plt.grid(True)
                
#     #             plt.tight_layout()
#     #             pdf.savefig()
#     #             plt.close()

#     #         #8. Add a new page for budget violation analysis if we have data
#     #         if self.pre_termination_elements:
#     #             plt.figure(figsize=(10, 12))
                
#     #             # Subplot 1: Histogram of element counts at violation
#     #             plt.subplot(3, 1, 1)
#     #             plt.hist(self.pre_termination_elements, bins=range(0, max(self.pre_termination_elements) + 5, 1), 
#     #                     alpha=0.7, color='purple')
                
#     #             # Add reference line at budget
#     #             if hasattr(self.model.env, 'element_budget'):
#     #                 budget = self.model.env.element_budget
#     #             else:
#     #                 budget = self.model.env.envs[0].element_budget
#     #             plt.axvline(x=budget, color='r', linestyle='--', label='Element budget')
                
#     #             plt.xlabel('Elements at Budget Violation')
#     #             plt.ylabel('Count')
#     #             plt.title('Distribution of Element Counts at Budget Violation')
#     #             plt.legend()
#     #             plt.grid(True)
                
#     #             # Subplot 2: Actions that triggered violations
#     #             plt.subplot(3, 1, 2)
#     #             action_names = ['-1 (Coarsen)', '0 (No Change)', '1 (Refine)']
#     #             action_counts = [0, 0, 0]
#     #             for action in self.violation_actions:
#     #                 # Adjust for action mapping
#     #                 idx = action + 1
#     #                 if 0 <= idx < 3:
#     #                     action_counts[idx] += 1
                
#     #             plt.bar(action_names, action_counts, color=['green', 'gray', 'red'])
#     #             plt.xlabel('Action Type')
#     #             plt.ylabel('Count')
#     #             plt.title('Actions That Triggered Budget Violations')
#     #             plt.grid(True, axis='y')
                
#     #             # Subplot 3: Budget usage percentage at violation
#     #             plt.subplot(3, 1, 3)
#     #             plt.hist(self.budget_usage_at_violation, bins=20, alpha=0.7, color='blue')
#     #             plt.axvline(x=1.0, color='r', linestyle='--', label='Budget limit (100%)')
#     #             plt.xlabel('Budget Usage at Violation (percentage)')
#     #             plt.ylabel('Count')
#     #             plt.title('Budget Usage Percentage at Violation')
#     #             plt.legend()
#     #             plt.grid(True)
                
#     #             plt.tight_layout()
#     #             pdf.savefig()
#     #             plt.close()
                
#     #     if self.verbose > 0:
#     #         print(f"Final report generated and saved to: {report_path}")
            
#         # Also save raw data as Excel with multiple sheets
#         excel_path = os.path.join(self.log_dir, "training_data.xlsx")
#         with pd.ExcelWriter(excel_path) as writer:
#             # Episode data
#             if not self.episode_df.empty:
#                 self.episode_df.to_excel(writer, sheet_name='Episodes', index=False)
            
#             # Create action summary sheet
#             action_summary = pd.DataFrame({
#                 'Action': list(self.action_names.values()),
#                 'Count': [self.action_counts.get(a, 0) for a in self.action_names.keys()],
#                 'Percentage': [self.action_counts.get(a, 0) / max(1, sum(self.action_counts.values())) * 100 
#                               for a in self.action_names.keys()],
#                 'Avg Reward': [np.mean(self.rewards_by_action.get(a, [0])) for a in self.action_names.keys()]
#             })
#             action_summary.to_excel(writer, sheet_name='Action Summary', index=False)
            
#             # Termination summary
#             if self.termination_reasons:
#                 term_summary = pd.DataFrame({
#                     'Reason': list(self.termination_reasons.keys()),
#                     'Count': list(self.termination_reasons.values()),
#                     'Percentage': [count / max(1, sum(self.termination_reasons.values())) * 100 
#                                   for count in self.termination_reasons.values()]
#                 })
#                 term_summary.to_excel(writer, sheet_name='Termination Summary', index=False)
            
#             # Aggregate metrics sampled at intervals
#             if not self.metrics_df.empty:
#                 # Sample metrics to avoid excessive file size
#                 sample_size = min(10000, len(self.metrics_df))
#                 sample_interval = max(1, len(self.metrics_df) // sample_size)
#                 sampled_metrics = self.metrics_df.iloc[::sample_interval].copy()
#                 sampled_metrics.to_excel(writer, sheet_name='Metrics Sample', index=False)
        
#         if self.verbose > 0:
#             print(f"Raw data saved to: {excel_path}")


#     def _save_analysis_metadata(self) -> None:
#         """Save metadata to aid in analysis."""
#         import json
        
#         try:
#             # Collect metadata
#             metadata = {
#                 "training_steps": self.num_timesteps,
#                 "episodes_completed": self.episodes_completed,
#                 "element_budget": 0,
#                 "gamma_c": 0,
#                 "max_episode_steps": 0,
#                 "termination_reasons": self.termination_reasons,
#                 "action_counts": {str(k): v for k, v in self.action_counts.items()},
#                 "reward_stats": {
#                     "mean": float(np.mean(self.episode_rewards)) if self.episode_rewards else 0,
#                     "min": float(np.min(self.episode_rewards)) if self.episode_rewards else 0,
#                     "max": float(np.max(self.episode_rewards)) if self.episode_rewards else 0,
#                 }
#             }
            
#             # Try to get environment parameters
#             try:
#                 metadata["element_budget"] = self.model.env.unwrapped.element_budget
#                 metadata["gamma_c"] = self.model.env.unwrapped.gamma_c
#                 metadata["max_episode_steps"] = self.model.env.unwrapped.max_episode_steps
#             except (AttributeError, KeyError):
#                 try:
#                     metadata["element_budget"] = self.model.env.get_wrapper_attr('element_budget')
#                     metadata["gamma_c"] = self.model.env.get_wrapper_attr('gamma_c')
#                     metadata["max_episode_steps"] = self.model.env.get_wrapper_attr('max_episode_steps')
#                 except (AttributeError, KeyError):
#                     try:
#                         metadata["element_budget"] = self.model.env.envs[0].unwrapped.element_budget
#                         metadata["gamma_c"] = self.model.env.envs[0].unwrapped.gamma_c
#                         metadata["max_episode_steps"] = self.model.env.envs[0].unwrapped.max_episode_steps
#                     except:
#                         pass
            
#             # Save to file
#             metadata_path = os.path.join(self.log_dir, "training_metadata.json")
#             with open(metadata_path, 'w') as f:
#                 json.dump(metadata, f, indent=2)
                
#             if self.verbose > 0:
#                 print(f"Analysis metadata saved to: {metadata_path}")
                
#         except Exception as e:
#             print(f"Error saving analysis metadata: {e}")