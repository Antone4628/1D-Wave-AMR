import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
from typing import Dict, List, Tuple, Any, Optional
from collections import deque, defaultdict
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
    - Initial refinement configuration impact
    
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
        
        # Create metrics directory
        self.metrics_dir = os.path.join(log_dir, "metrics")
        os.makedirs(self.metrics_dir, exist_ok=True)
        
        # Create plots directory
        self.plots_dir = os.path.join(log_dir, "plots")
        os.makedirs(self.plots_dir, exist_ok=True)
        
        # Create refinement analysis directory
        self.refinement_dir = os.path.join(log_dir, "refinement")
        os.makedirs(self.refinement_dir, exist_ok=True)
        
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
        self._episode_steps = 0  # Initialize episode step counter
        
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
        
        # Refinement configuration tracking
        self.refinement_stats = defaultdict(list)  # Will hold all refinement-related data
        self.current_episode_refinement = None     # Will hold current episode's refinement config
        
        # Coarsening success tracking by refinement config
        self.coarsening_attempts = defaultdict(int)  # (mode, level) -> attempts
        self.coarsening_successes = defaultdict(int) # (mode, level) -> successes
        
    def _on_training_start(self) -> None:
        """Called when training starts. Add configuration info to TensorBoard."""
        # Initialize dataframes with correct columns
        self.metrics_df = pd.DataFrame(columns=[
            'timestep', 'action', 'mapped_action', 'reward', 
            'resource_usage', 'element_count', 'budget_proximity',
            'took_timestep', 'episode'
        ])
        
        # Add refinement configuration columns to episode dataframe
        self.episode_df = pd.DataFrame(columns=[
            'episode', 'total_reward', 'length', 'termination_reason',
            'final_element_count', 'final_resource_usage',
            'refine_count', 'coarsen_count', 'no_change_count',
            'refine_pct', 'coarsen_pct', 'no_change_pct',
            # New refinement tracking columns
            'refinement_mode', 'refinement_level', 'refinement_probability', 
            'initial_elements', 'initial_resource_usage', 'element_growth_ratio'
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
        done = self.locals['dones'][0]

        # Update episode steps counter
        self._episode_steps += 1

        # Check if this is the first step of an episode (first step after reset)
        if self._episode_steps == 1:
            # Capture refinement info if available from the reset
            if 'refinement_info' in info:
                self.current_episode_refinement = info['refinement_info'].copy()
        
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
        
        # Track coarsening attempts and successes
        if mapped_action == -1 and self.current_episode_refinement:
            # Get refinement config key
            config_key = (
                self.current_episode_refinement.get('mode', 'none'),
                self.current_episode_refinement.get('level', 0)
            )
            
            # Increment attempt counter
            self.coarsening_attempts[config_key] += 1
            
            # Check if coarsening was successful (element count decreased)
            if len(self.element_count_history) >= 2 and self.element_count_history[-1] < self.element_count_history[-2]:
                self.coarsening_successes[config_key] += 1
        
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

        # In EnhancedMonitorCallback._on_step
        # Add tracking for invalid actions
        original_action = info.get('original_action', None)
        actual_action = info.get('actual_action', info.get('mapped_action', None))
        is_valid_action = info.get('is_valid_action', original_action == actual_action)

        if not is_valid_action and original_action is not None:
            # Track invalid action occurrences
            if not hasattr(self, 'invalid_action_counts'):
                self.invalid_action_counts = {-1: 0, 0: 0, 1: 0}
            
            self.invalid_action_counts[original_action] = self.invalid_action_counts.get(original_action, 0) + 1
        
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
        if done:
            self._on_episode_end(info)
            # Reset episode step counter when episode ends
            self._episode_steps = 0
        
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
        
        # Prepare episode data row
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
        
        # Add refinement configuration data if available
        if self.current_episode_refinement:
            initial_elements = self.current_episode_refinement.get('initial_elements', 0)
            
            # Calculate element growth ratio
            element_growth_ratio = final_element_count / max(1, initial_elements)
            
            # Add refinement data to row
            new_row.update({
                'refinement_mode': self.current_episode_refinement.get('mode', 'none'),
                'refinement_level': self.current_episode_refinement.get('level', 0),
                'refinement_probability': self.current_episode_refinement.get('probability', 0.5),
                'initial_elements': initial_elements,
                'initial_resource_usage': self.current_episode_refinement.get('resource_usage', 0),
                'element_growth_ratio': element_growth_ratio
            })
            
            # Update refinement statistics
            level = self.current_episode_refinement.get('level', 0)
            mode = self.current_episode_refinement.get('mode', 'none')
            config_key = f"{mode}_level{level}"
            
            self.refinement_stats['config'].append(config_key)
            self.refinement_stats['mode'].append(mode)
            self.refinement_stats['level'].append(level)
            self.refinement_stats['initial_elements'].append(initial_elements)
            self.refinement_stats['final_elements'].append(final_element_count)
            self.refinement_stats['element_growth'].append(element_growth_ratio)
            self.refinement_stats['reward'].append(self.current_episode_reward)
            self.refinement_stats['refine_pct'].append(refine_pct)
            self.refinement_stats['coarsen_pct'].append(coarsen_pct)
            self.refinement_stats['termination'].append(termination_reason)
        
        # Update episode dataframe
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
            
            # Log refinement configuration if available
            if self.current_episode_refinement:
                mode = self.current_episode_refinement.get('mode', 'none')
                level = self.current_episode_refinement.get('level', 0)
                self.logger.record(f"refinement/mode_{mode}", 1)
                self.logger.record(f"refinement/level_{level}", 1)
                self.logger.record(f"refinement/element_growth", element_growth_ratio)
            
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
            
            if self.current_episode_refinement:
                mode = self.current_episode_refinement.get('mode', 'none')
                level = self.current_episode_refinement.get('level', 0)
                print(f"  Initial refinement: {mode} (level {level})")
                print(f"  Initial elements: {initial_elements}")
                print(f"  Element growth ratio: {element_growth_ratio:.2f}")
        
        # Reset episode-specific tracking
        self.current_episode_start_step = self.num_timesteps
        self.current_episode_actions = {action: 0 for action in self.action_mapping.values()}
        self.current_episode_reward = 0
        self.current_episode_refinement = None
    
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
        
        # Calculate coarsening success rate by refinement configuration
        if self.coarsening_attempts:
            coarsening_summary = "Coarsening success rates by configuration:\n"
            for config, attempts in self.coarsening_attempts.items():
                successes = self.coarsening_successes.get(config, 0)
                success_rate = (successes / attempts) * 100 if attempts > 0 else 0
                mode, level = config
                coarsening_summary += f"  {mode} (level {level}): {successes}/{attempts} ({success_rate:.1f}%)\n"
        
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
            
            # Print coarsening success rates
            if self.coarsening_attempts:
                print(f"\n{coarsening_summary}")
        
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
            
            # Log coarsening success rates
            for config, attempts in self.coarsening_attempts.items():
                successes = self.coarsening_successes.get(config, 0)
                success_rate = successes / max(1, attempts)
                mode, level = config
                self.logger.record(f"coarsening/{mode}_level{level}_success_rate", success_rate)
            
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
        
        # Save refinement statistics if available
        if self.refinement_stats:
            refinement_df = pd.DataFrame(self.refinement_stats)
            refinement_path = os.path.join(self.refinement_dir, f"refinement_stats_{self.num_timesteps}.csv")
            refinement_df.to_csv(refinement_path, index=False)
    
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
        
        # New refinement-specific visualizations
        if self.refinement_stats:
            # 8. Refinement configuration performance
            self._plot_refinement_performance(timestamp)
            
            # 9. Element growth by refinement level
            self._plot_element_growth(timestamp)
            
            # 10. Coarsening success rates
            self._plot_coarsening_success(timestamp)
            
            # 11. Refinement dashboard
            self._plot_refinement_dashboard(timestamp)
    
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

        # Add visualization for pre-termination element counts if data exists
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
    
    def _plot_refinement_performance(self, timestamp: int) -> None:
        """Plot performance metrics by refinement configuration."""
        if not self.episode_df.empty and 'refinement_mode' in self.episode_df.columns:
            # Filter out rows with missing refinement data
            df = self.episode_df.dropna(subset=['refinement_mode', 'refinement_level'])
            
            if len(df) < 5:  # Need enough data to make meaningful plots
                return
                
            plt.figure(figsize=(14, 10))
            
            # 1. Reward by refinement level
            plt.subplot(2, 2, 1)
            if len(df['refinement_level'].unique()) > 1:
                sns.boxplot(x='refinement_level', y='total_reward', data=df)
                plt.title('Reward Distribution by Refinement Level')
                plt.xlabel('Initial Refinement Level')
                plt.ylabel('Total Episode Reward')
                plt.grid(True)
            else:
                plt.text(0.5, 0.5, 'Only one refinement level used', 
                         horizontalalignment='center', verticalalignment='center')
                plt.title('Reward by Refinement Level (Insufficient Data)')
            
            # 2. Reward by refinement mode
            plt.subplot(2, 2, 2)
            if len(df['refinement_mode'].unique()) > 1:
                sns.boxplot(x='refinement_mode', y='total_reward', data=df)
                plt.title('Reward Distribution by Refinement Mode')
                plt.xlabel('Refinement Mode')
                plt.ylabel('Total Episode Reward')
                plt.xticks(rotation=45)
                plt.grid(True)
            else:
                plt.text(0.5, 0.5, 'Only one refinement mode used', 
                         horizontalalignment='center', verticalalignment='center')
                plt.title('Reward by Refinement Mode (Insufficient Data)')
            
            # 3. Action distribution by refinement level
            plt.subplot(2, 2, 3)
            
            # Group by refinement level
            if len(df['refinement_level'].unique()) > 1:
                level_groups = df.groupby('refinement_level')
                
                refine_by_level = level_groups['refine_pct'].mean() * 100
                coarsen_by_level = level_groups['coarsen_pct'].mean() * 100
                no_change_by_level = level_groups['no_change_pct'].mean() * 100
                
                # Create bar positions
                levels = sorted(df['refinement_level'].unique())
                x = np.arange(len(levels))
                width = 0.25
                
                # Create bars
                plt.bar(x - width, refine_by_level, width, label='Refine')
                plt.bar(x, no_change_by_level, width, label='No Change')
                plt.bar(x + width, coarsen_by_level, width, label='Coarsen')
                
                plt.xlabel('Initial Refinement Level')
                plt.ylabel('Action Percentage (%)')
                plt.xticks(x, levels)
                plt.title('Action Distribution by Refinement Level')
                plt.legend()
                plt.grid(True, axis='y')
            else:
                plt.text(0.5, 0.5, 'Only one refinement level used', 
                         horizontalalignment='center', verticalalignment='center')
                plt.title('Actions by Refinement Level (Insufficient Data)')
            
            # 4. Element growth ratio by refinement level
            plt.subplot(2, 2, 4)
            if 'element_growth_ratio' in df.columns and len(df['refinement_level'].unique()) > 1:
                sns.boxplot(x='refinement_level', y='element_growth_ratio', data=df)
                plt.axhline(y=1.0, color='r', linestyle='--', label='No Growth')
                plt.title('Element Growth Ratio by Refinement Level')
                plt.xlabel('Initial Refinement Level')
                plt.ylabel('Final Elements / Initial Elements')
                plt.legend()
                plt.grid(True)
            else:
                plt.text(0.5, 0.5, 'Insufficient element growth data', 
                         horizontalalignment='center', verticalalignment='center')
                plt.title('Element Growth (Insufficient Data)')
            
            plt.tight_layout()
            plt.savefig(os.path.join(self.refinement_dir, f"refinement_performance_{timestamp}.png"))
            plt.close()

    def _plot_element_growth(self, timestamp: int) -> None:
        """Plot initial vs final element count and element growth patterns."""
        if not self.episode_df.empty and 'initial_elements' in self.episode_df.columns:
            plt.figure(figsize=(14, 6))
            
            # 1. Initial vs final element count scatter plot
            plt.subplot(1, 2, 1)
            
            # Create scatter plot with refinement level as color
            if 'refinement_level' in self.episode_df.columns:
                scatter = sns.scatterplot(
                    x='initial_elements', 
                    y='final_element_count',
                    hue='refinement_level',
                    style='refinement_mode',
                    data=self.episode_df
                )
            else:
                scatter = sns.scatterplot(
                    x='initial_elements', 
                    y='final_element_count',
                    data=self.episode_df
                )
            
            # Add diagonal line (y=x)
            max_value = max(
                self.episode_df['initial_elements'].max(),
                self.episode_df['final_element_count'].max()
            )
            plt.plot([0, max_value], [0, max_value], 'k--', alpha=0.5, label='No Change Line')
            
            plt.xlabel('Initial Element Count')
            plt.ylabel('Final Element Count')
            plt.title('Initial vs Final Element Count')
            plt.grid(True)
            
            # Move legend outside plot if it's large
            if 'refinement_level' in self.episode_df.columns and len(self.episode_df['refinement_level'].unique()) > 3:
                plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
            
            # 2. Element growth ratio by initial element count
            plt.subplot(1, 2, 2)
            if 'element_growth_ratio' in self.episode_df.columns:
                sns.scatterplot(
                    x='initial_elements',
                    y='element_growth_ratio',
                    hue='refinement_level',
                    data=self.episode_df
                )
                
                plt.axhline(y=1.0, color='r', linestyle='--', label='No Growth')
                plt.xlabel('Initial Element Count')
                plt.ylabel('Element Growth Ratio')
                plt.title('Element Growth vs Initial Count')
                plt.grid(True)
            
            plt.tight_layout()
            plt.savefig(os.path.join(self.refinement_dir, f"element_growth_{timestamp}.png"))
            plt.close()
            
            # Additional plot: Element growth histogram by refinement level
            if 'element_growth_ratio' in self.episode_df.columns and 'refinement_level' in self.episode_df.columns:
                plt.figure(figsize=(12, 6))
                
                # Get unique refinement levels
                levels = sorted(self.episode_df['refinement_level'].unique())
                
                # Create a facet grid of histograms
                if len(levels) > 1:
                    # Create subplots for each level
                    fig, axes = plt.subplots(1, len(levels), figsize=(15, 5), sharey=True)
                    
                    for i, level in enumerate(levels):
                        level_data = self.episode_df[self.episode_df['refinement_level'] == level]
                        if len(level_data) > 0:
                            sns.histplot(level_data['element_growth_ratio'], ax=axes[i], bins=15, kde=True)
                            axes[i].axvline(x=1.0, color='r', linestyle='--')
                            axes[i].set_title(f'Level {level}')
                            axes[i].set_xlabel('Element Growth Ratio')
                            
                            if i == 0:
                                axes[i].set_ylabel('Count')
                    
                    plt.suptitle('Element Growth Ratio Distribution by Refinement Level')
                    plt.tight_layout()
                else:
                    # Just one level, create a single histogram
                    sns.histplot(self.episode_df['element_growth_ratio'], bins=15, kde=True)
                    plt.axvline(x=1.0, color='r', linestyle='--', label='No Growth')
                    plt.xlabel('Element Growth Ratio')
                    plt.ylabel('Count')
                    plt.title(f'Element Growth Ratio Distribution (Level {levels[0]})')
                    plt.legend()
                    plt.grid(True)
                
                plt.savefig(os.path.join(self.refinement_dir, f"element_growth_hist_{timestamp}.png"))
                plt.close()
    
    def _plot_coarsening_success(self, timestamp: int) -> None:
        """Plot coarsening success rates by refinement configuration."""
        if self.coarsening_attempts:
            plt.figure(figsize=(12, 6))
            
            # Extract data
            configs = []
            attempts = []
            successes = []
            success_rates = []
            
            for config, attempt_count in self.coarsening_attempts.items():
                mode, level = config
                success_count = self.coarsening_successes.get(config, 0)
                success_rate = (success_count / attempt_count) * 100 if attempt_count > 0 else 0
                
                configs.append(f"{mode}\nLevel {level}")
                attempts.append(attempt_count)
                successes.append(success_count)
                success_rates.append(success_rate)
            
            # Sort by success rate
            sorted_indices = np.argsort(success_rates)[::-1]  # Descending
            configs = [configs[i] for i in sorted_indices]
            attempts = [attempts[i] for i in sorted_indices]
            successes = [successes[i] for i in sorted_indices]
            success_rates = [success_rates[i] for i in sorted_indices]
            
            # Create plot
            x = np.arange(len(configs))
            width = 0.35
            
            fig, ax1 = plt.subplots(figsize=(12, 6))
            
            # Plot the attempt and success counts
            p1 = ax1.bar(x - width/2, attempts, width, label='Attempts', color='skyblue')
            p2 = ax1.bar(x - width/2, successes, width, label='Successes', color='green')
            
            ax1.set_xlabel('Refinement Configuration')
            ax1.set_ylabel('Count')
            ax1.set_title('Coarsening Success by Refinement Configuration')
            ax1.set_xticks(x)
            ax1.set_xticklabels(configs)
            ax1.legend(loc='upper left')
            
            # Create second axis for success rate
            ax2 = ax1.twinx()
            p3 = ax2.plot(x, success_rates, 'ro-', label='Success Rate')
            ax2.set_ylabel('Success Rate (%)')
            ax2.set_ylim(0, 100)
            
            # Add success rate values above line
            for i, rate in enumerate(success_rates):
                ax2.annotate(f"{rate:.1f}%", 
                             (x[i], rate + 2),
                             textcoords="offset points",
                             xytext=(0, 5),
                             ha='center')
            
            # Combine legends
            lines, labels = ax1.get_legend_handles_labels()
            lines2, labels2 = ax2.get_legend_handles_labels()
            ax2.legend(lines + lines2, labels + labels2, loc='upper right')
            
            plt.tight_layout()
            plt.savefig(os.path.join(self.refinement_dir, f"coarsening_success_{timestamp}.png"))
            plt.close()
    
    def _plot_refinement_dashboard(self, timestamp: int) -> None:
        """Create a comprehensive dashboard of refinement-related metrics."""
        if not self.episode_df.empty and 'refinement_mode' in self.episode_df.columns:
            # Create multi-panel dashboard
            fig = plt.figure(figsize=(16, 12))
            gs = fig.add_gridspec(3, 2)
            
            # 1. Average reward by refinement configuration
            ax1 = fig.add_subplot(gs[0, 0])
            
            if not self.refinement_stats or len(self.refinement_stats['config']) == 0:
                ax1.text(0.5, 0.5, 'No refinement data available', 
                         horizontalalignment='center', verticalalignment='center')
                ax1.set_title('Refinement Performance (No Data)')
            else:
                # Create dataframe from refinement stats
                refinement_df = pd.DataFrame(self.refinement_stats)
                
                # Group by configuration and calculate mean reward
                config_rewards = refinement_df.groupby('config')['reward'].mean().sort_values(ascending=False)
                
                # Plot horizontal bar chart
                config_rewards.plot(kind='barh', ax=ax1)
                ax1.set_xlabel('Average Reward')
                ax1.set_ylabel('Refinement Configuration')
                ax1.set_title('Average Reward by Refinement Configuration')
                ax1.grid(True, axis='x')
            
            # 2. Termination reason distribution by refinement level
            ax2 = fig.add_subplot(gs[0, 1])
            
            if 'refinement_level' not in self.episode_df.columns or 'termination_reason' not in self.episode_df.columns:
                ax2.text(0.5, 0.5, 'Termination data by refinement level not available', 
                         horizontalalignment='center', verticalalignment='center')
                ax2.set_title('Termination by Refinement Level (No Data)')
            else:
                # Get termination counts by level
                term_by_level = pd.crosstab(
                    self.episode_df['refinement_level'], 
                    self.episode_df['termination_reason'],
                    normalize='index'
                ) * 100
                
                # Plot stacked bar chart
                term_by_level.plot(kind='bar', stacked=True, ax=ax2)
                ax2.set_xlabel('Refinement Level')
                ax2.set_ylabel('Percentage')
                ax2.set_title('Termination Reasons by Refinement Level')
                ax2.legend(loc='upper left', bbox_to_anchor=(1, 1))
            
            # 3. Coarsening success rates visualization
            ax3 = fig.add_subplot(gs[1, 0])
            
            if not self.coarsening_attempts:
                ax3.text(0.5, 0.5, 'No coarsening attempt data available', 
                         horizontalalignment='center', verticalalignment='center')
                ax3.set_title('Coarsening Success (No Data)')
            else:
                # Extract data for plotting
                labels = []
                success_rates = []
                
                for config, attempts in self.coarsening_attempts.items():
                    mode, level = config
                    label = f"{mode} Lvl{level}"
                    success = self.coarsening_successes.get(config, 0)
                    rate = (success / attempts) * 100 if attempts > 0 else 0
                    
                    labels.append(label)
                    success_rates.append(rate)
                
                # Sort by success rate
                sorted_indices = np.argsort(success_rates)
                labels = [labels[i] for i in sorted_indices]
                success_rates = [success_rates[i] for i in sorted_indices]
                
                # Plot horizontal bar chart
                y_pos = np.arange(len(labels))
                ax3.barh(y_pos, success_rates, align='center')
                ax3.set_yticks(y_pos)
                ax3.set_yticklabels(labels)
                ax3.set_xlabel('Success Rate (%)')
                ax3.set_xlim(0, 100)
                ax3.set_title('Coarsening Success Rate by Configuration')
                ax3.grid(True, axis='x')
                
                # Add value labels to bars
                for i, v in enumerate(success_rates):
                    ax3.text(v + 1, i, f"{v:.1f}%", va='center')
            
            # 4. Element growth comparison
            ax4 = fig.add_subplot(gs[1, 1])
            
            if 'element_growth_ratio' not in self.episode_df.columns or 'refinement_level' not in self.episode_df.columns:
                ax4.text(0.5, 0.5, 'Element growth data by level not available', 
                         horizontalalignment='center', verticalalignment='center')
                ax4.set_title('Element Growth by Refinement Level (No Data)')
            else:
                # Group by level and calculate mean growth
                growth_by_level = self.episode_df.groupby('refinement_level')['element_growth_ratio'].mean()
                
                # Plot growth as bar chart
                x = np.arange(len(growth_by_level))
                ax4.bar(x, growth_by_level.values)
                ax4.set_xticks(x)
                ax4.set_xticklabels(growth_by_level.index)
                ax4.axhline(y=1.0, color='r', linestyle='--', label='No Growth')
                ax4.set_xlabel('Refinement Level')
                ax4.set_ylabel('Average Element Growth Ratio')
                ax4.set_title('Element Growth by Refinement Level')
                ax4.legend()
                ax4.grid(True, axis='y')
                
                # Add value labels
                for i, v in enumerate(growth_by_level.values):
                    ax4.text(i, v + 0.05, f"{v:.2f}", ha='center')
            
            # 5. Action distribution by refinement mode
            ax5 = fig.add_subplot(gs[2, 0])
            
            if 'refinement_mode' not in self.episode_df.columns:
                ax5.text(0.5, 0.5, 'Action data by refinement mode not available', 
                         horizontalalignment='center', verticalalignment='center')
                ax5.set_title('Actions by Refinement Mode (No Data)')
            else:
                # Group by mode
                modes = self.episode_df['refinement_mode'].unique()
                
                if len(modes) > 1:
                    # Calculate mean action percentages by mode
                    refine_by_mode = self.episode_df.groupby('refinement_mode')['refine_pct'].mean() * 100
                    coarsen_by_mode = self.episode_df.groupby('refinement_mode')['coarsen_pct'].mean() * 100
                    no_change_by_mode = self.episode_df.groupby('refinement_mode')['no_change_pct'].mean() * 100
                    
                    # Set positions and width for bars
                    x = np.arange(len(modes))
                    width = 0.25
                    
                    # Create bars
                    ax5.bar(x - width, refine_by_mode, width, label='Refine')
                    ax5.bar(x, no_change_by_mode, width, label='No Change')
                    ax5.bar(x + width, coarsen_by_mode, width, label='Coarsen')
                    
                    ax5.set_xticks(x)
                    ax5.set_xticklabels(modes)
                    ax5.set_xlabel('Refinement Mode')
                    ax5.set_ylabel('Action Percentage (%)')
                    ax5.set_title('Action Distribution by Refinement Mode')
                    ax5.legend()
                    ax5.grid(True, axis='y')
                else:
                    ax5.text(0.5, 0.5, 'Only one refinement mode used', 
                             horizontalalignment='center', verticalalignment='center')
                    ax5.set_title('Actions by Mode (Only one mode)')
            
            # 6. Refinement summary statistics
            ax6 = fig.add_subplot(gs[2, 1])
            
            # Create text box with refinement statistics
            summary_text = ["# Refinement Mode Statistics"]
            
            if 'refinement_mode' in self.episode_df.columns:
                # Count episodes by mode
                mode_counts = self.episode_df['refinement_mode'].value_counts()
                total_episodes = len(self.episode_df)
                
                summary_text.append("\n## Episodes by Mode")
                for mode, count in mode_counts.items():
                    summary_text.append(f"- {mode}: {count} ({count/total_episodes*100:.1f}%)")
                
                # Calculate average reward by mode
                reward_by_mode = self.episode_df.groupby('refinement_mode')['total_reward'].mean()
                
                summary_text.append("\n## Avg. Reward by Mode")
                for mode, reward in reward_by_mode.items():
                    summary_text.append(f"- {mode}: {reward:.2f}")
                
                # Calculate coarsening success rate by mode if available
                if self.coarsening_attempts:
                    summary_text.append("\n## Coarsening Success by Mode")
                    
                    # Group configurations by mode
                    mode_success = {}
                    mode_attempts = {}
                    
                    for config, attempts in self.coarsening_attempts.items():
                        mode, level = config
                        
                        if mode not in mode_attempts:
                            mode_attempts[mode] = 0
                            mode_success[mode] = 0
                        
                        mode_attempts[mode] += attempts
                        mode_success[mode] += self.coarsening_successes.get(config, 0)
                    
                    # Calculate rates
                    for mode in mode_attempts:
                        success_rate = (mode_success[mode] / mode_attempts[mode]) * 100 if mode_attempts[mode] > 0 else 0
                        summary_text.append(f"- {mode}: {mode_success[mode]}/{mode_attempts[mode]} ({success_rate:.1f}%)")
            else:
                summary_text.append("\nNo refinement mode data available")
            
            # Create text box
            ax6.axis('off')
            ax6.text(0, 1, '\n'.join(summary_text), fontsize=10, va='top', 
                     bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))
            
            # Adjust layout and save
            plt.tight_layout()
            plt.savefig(os.path.join(self.refinement_dir, f"refinement_dashboard_{timestamp}.png"))
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
        
        # Create refinement-specific final report
        self._create_refinement_report()
        
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
            
            # Add refinement metadata if available
            if len(self.refinement_stats) > 0:
                # Calculate summary statistics for each refinement configuration
                refinement_summaries = {}
                
                if 'config' in self.refinement_stats and 'reward' in self.refinement_stats:
                    # Create a DataFrame for easier analysis
                    refinement_df = pd.DataFrame({
                        'config': self.refinement_stats['config'],
                        'mode': self.refinement_stats['mode'],
                        'level': self.refinement_stats['level'],
                        'reward': self.refinement_stats['reward']
                    })
                    
                    # Group by config and calculate statistics
                    config_stats = refinement_df.groupby(['mode', 'level']).agg({
                        'reward': ['mean', 'min', 'max', 'count']
                    }).reset_index()
                    
                    # Convert to nested dictionary for JSON
                    for _, row in config_stats.iterrows():
                        config_key = f"{row['mode']}_level{row['level']}"
                        refinement_summaries[config_key] = {
                            'mode': row['mode'],
                            'level': row['level'],
                            'episodes': int(row[('reward', 'count')]),
                            'reward_mean': float(row[('reward', 'mean')]),
                            'reward_min': float(row[('reward', 'min')]),
                            'reward_max': float(row[('reward', 'max')])
                        }
                
                # Add coarsening success rates
                if self.coarsening_attempts:
                    if 'coarsening_stats' not in metadata:
                        metadata['coarsening_stats'] = {}
                    
                    for config, attempts in self.coarsening_attempts.items():
                        mode, level = config
                        config_key = f"{mode}_level{level}"
                        successes = self.coarsening_successes.get(config, 0)
                        
                        if config_key in refinement_summaries:
                            refinement_summaries[config_key]['coarsening_attempts'] = attempts
                            refinement_summaries[config_key]['coarsening_successes'] = successes
                            refinement_summaries[config_key]['coarsening_success_rate'] = (successes / attempts) if attempts > 0 else 0
                
                metadata['refinement_summaries'] = refinement_summaries
            
            # Save to file
            metadata_path = os.path.join(self.log_dir, "training_metadata.json")
            with open(metadata_path, 'w') as f:
                json.dump(metadata, f, indent=2)
                
            if self.verbose > 0:
                print(f"Analysis metadata saved to: {metadata_path}")
                
        except Exception as e:
            print(f"Error saving analysis metadata: {e}")
    
    def _create_refinement_report(self) -> None:
        """Create a simplified but robust report for refinement analysis."""
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_pdf import PdfPages
        import traceback
        
        # Skip if no refinement data
        if not self.refinement_stats or len(self.refinement_stats.get('config', [])) == 0:
            print("No refinement data available, skipping refinement report")
            return
            
        # Create DataFrame for easier analysis
        try:
            refinement_df = pd.DataFrame(self.refinement_stats)
        except Exception as e:
            print(f"Error creating refinement DataFrame: {e}")
            traceback.print_exc()
            return
        
        # Path for the report
        report_path = os.path.join(self.log_dir, "refinement_analysis.pdf")
        print(f"Generating refinement report at {report_path}...")
        
        try:
            with PdfPages(report_path) as pdf:
                pages_added = 0
                
                # ======= 1. Title Page =======
                try:
                    plt.figure(figsize=(10, 12))
                    plt.axis('off')
                    
                    # Prepare title page text
                    title_text = [
                        "# Adaptive Mesh Refinement Initialization Analysis",
                        f"Date: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}",
                        f"Total Episodes: {self.episodes_completed}",
                        f"Total Timesteps: {self.num_timesteps}",
                        "\n## Refinement Configurations Used:"
                    ]
                    
                    # List all configurations
                    config_counts = refinement_df['config'].value_counts()
                    for config, count in config_counts.items():
                        pct = count / len(refinement_df) * 100
                        title_text.append(f"- {config}: {count} episodes ({pct:.1f}%)")
                    
                    # Add text to figure
                    plt.text(0.05, 0.95, '\n'.join(title_text), transform=plt.gca().transAxes, 
                            fontsize=14, verticalalignment='top', family='monospace')
                    
                    pdf.savefig()
                    plt.close()
                    pages_added += 1
                    print("Added refinement title page to report")
                except Exception as e:
                    print(f"Error creating refinement title page: {e}")
                    traceback.print_exc()
                    plt.close()
                
                # ======= 2. Reward by Refinement Config =======
                try:
                    if 'config' in refinement_df.columns and 'reward' in refinement_df.columns:
                        plt.figure(figsize=(10, 6))
                        
                        # Group by config and calculate mean rewards
                        mean_rewards = refinement_df.groupby('config')['reward'].mean().sort_values(ascending=False)
                        
                        # Plot horizontal bar chart
                        plt.barh(range(len(mean_rewards)), mean_rewards.values)
                        plt.yticks(range(len(mean_rewards)), mean_rewards.index)
                        plt.xlabel('Average Reward')
                        plt.title('Average Reward by Refinement Configuration')
                        plt.grid(axis='x')
                        
                        # Add value labels
                        for i, v in enumerate(mean_rewards.values):
                            plt.text(v + 10, i, f"{v:.1f}", va='center')
                        
                        plt.tight_layout()
                        pdf.savefig()
                        plt.close()
                        pages_added += 1
                        print("Added reward by config page to report")
                except Exception as e:
                    print(f"Error creating rewards by config page: {e}")
                    traceback.print_exc()
                    plt.close()
                
                # ======= 3. Element Growth by Refinement Level =======
                try:
                    if 'level' in refinement_df.columns and 'element_growth' in refinement_df.columns:
                        plt.figure(figsize=(10, 6))
                        
                        # Group by level
                        growth_by_level = refinement_df.groupby('level')['element_growth'].mean()
                        
                        # Create bar chart
                        plt.bar(growth_by_level.index.astype(str), growth_by_level.values)
                        plt.axhline(y=1.0, color='r', linestyle='--', label='No Growth')
                        plt.xlabel('Refinement Level')
                        plt.ylabel('Average Element Growth Ratio')
                        plt.title('Element Growth by Refinement Level')
                        plt.legend()
                        plt.grid(axis='y')
                        
                        # Add value labels
                        for i, v in enumerate(growth_by_level.values):
                            plt.text(i, v + 0.05, f"{v:.2f}", ha='center')
                        
                        plt.tight_layout()
                        pdf.savefig()
                        plt.close()
                        pages_added += 1
                        print("Added element growth page to report")
                except Exception as e:
                    print(f"Error creating element growth page: {e}")
                    traceback.print_exc()
                    plt.close()
                
                # ======= 4. Coarsening Success Rates =======
                try:
                    if self.coarsening_attempts:
                        plt.figure(figsize=(10, 6))
                        
                        # Extract data
                        configs = []
                        success_rates = []
                        
                        for config, attempts in self.coarsening_attempts.items():
                            if attempts >= 5:  # Only include configs with enough data
                                mode, level = config
                                label = f"{mode}\nLvl {level}"
                                success = self.coarsening_successes.get(config, 0)
                                rate = (success / attempts) * 100
                                
                                configs.append(label)
                                success_rates.append(rate)
                        
                        if configs:  # Only proceed if we have data
                            # Sort by success rate for better visualization
                            sorted_indices = np.argsort(success_rates)[::-1]  # Descending
                            configs = [configs[i] for i in sorted_indices]
                            success_rates = [success_rates[i] for i in sorted_indices]
                            
                            # Create horizontal bar chart
                            y_pos = np.arange(len(configs))
                            plt.barh(y_pos, success_rates)
                            plt.yticks(y_pos, configs)
                            plt.xlabel('Success Rate (%)')
                            plt.title('Coarsening Success Rate by Configuration')
                            plt.grid(axis='x')
                            
                            # Add labels
                            for i, v in enumerate(success_rates):
                                plt.text(v + 1, i, f"{v:.1f}%", va='center')
                            
                            plt.tight_layout()
                            pdf.savefig()
                            plt.close()
                            pages_added += 1
                            print("Added coarsening success page to report")
                except Exception as e:
                    print(f"Error creating coarsening success page: {e}")
                    traceback.print_exc()
                    plt.close()
                
                # ======= 5. Action Distribution by Refinement Level =======
                try:
                    if 'level' in refinement_df.columns and 'refine_pct' in refinement_df.columns:
                        plt.figure(figsize=(10, 6))
                        
                        # Group by level
                        level_groups = refinement_df.groupby('level')
                        
                        levels = sorted(refinement_df['level'].unique())
                        refine_pct = [level_groups['refine_pct'].mean()[level] * 100 for level in levels]
                        coarsen_pct = [level_groups['coarsen_pct'].mean()[level] * 100 for level in levels]
                        no_change_pct = [100 - r - c for r, c in zip(refine_pct, coarsen_pct)]
                        
                        # Create a stacked bar chart
                        plt.bar(levels, refine_pct, label='Refine')
                        plt.bar(levels, no_change_pct, bottom=refine_pct, label='No Change')
                        plt.bar(levels, coarsen_pct, bottom=[r+n for r, n in zip(refine_pct, no_change_pct)], label='Coarsen')
                        
                        plt.xlabel('Refinement Level')
                        plt.ylabel('Percentage (%)')
                        plt.title('Action Distribution by Refinement Level')
                        plt.legend()
                        plt.grid(axis='y')
                        
                        plt.tight_layout()
                        pdf.savefig()
                        plt.close()
                        pages_added += 1
                        print("Added actions by level page to report")
                except Exception as e:
                    print(f"Error creating actions by level page: {e}")
                    traceback.print_exc()
                    plt.close()
                    
            print(f"Refinement report generated with {pages_added} pages and saved to: {report_path}")
            
            # Save path to a text file for easier programmatic access
            with open(os.path.join(self.refinement_dir, "refinement_report_path.txt"), "w") as f:
                f.write(report_path)
                
        except Exception as e:
            print(f"Error generating refinement report: {e}")
            traceback.print_exc()
        
        # Make sure all figures are closed
        plt.close('all')




    # def _create_refinement_report(self) -> None:
    #     """Create a dedicated report for refinement analysis results."""
    #     import matplotlib.pyplot as plt
    #     from matplotlib.backends.backend_pdf import PdfPages
        
    #     # Skip if no refinement data
    #     if not self.refinement_stats or len(self.refinement_stats.get('config', [])) == 0:
    #         if self.verbose > 0:
    #             print("No refinement data available, skipping refinement report")
    #         return
            
    #     # Create DataFrame for easier analysis
    #     refinement_df = pd.DataFrame(self.refinement_stats)
        
    #     # Path for the report
    #     report_path = os.path.join(self.log_dir, "refinement_analysis.pdf")
        
    #     with PdfPages(report_path) as pdf:
    #         # 1. Title Page
    #         plt.figure(figsize=(10, 12))
    #         plt.axis('off')
            
    #         # Prepare title page text
    #         title_text = [
    #             "# Adaptive Mesh Refinement Initialization Analysis",
    #             f"Date: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}",
    #             f"Total Episodes: {self.episodes_completed}",
    #             f"Total Timesteps: {self.num_timesteps}",
    #             "\n## Refinement Configurations Used:"
    #         ]
            
    #         # List all configurations
    #         config_counts = refinement_df['config'].value_counts()
    #         for config, count in config_counts.items():
    #             pct = count / len(refinement_df) * 100
    #             title_text.append(f"- {config}: {count} episodes ({pct:.1f}%)")
            
    #         # Add text to figure
    #         plt.text(0.05, 0.95, '\n'.join(title_text), transform=plt.gca().transAxes, 
    #                 fontsize=14, verticalalignment='top', family='monospace')
            
    #         pdf.savefig()
    #         plt.close()
            
    #         # Additional pages with detailed analysis
    #         # ... (rest of the report generation code) ...
            
    #         if self.verbose > 0:
    #             print(f"Refinement analysis report generated and saved to: {report_path}")
        
    #     # Save path to a text file for easier programmatic access
    #     with open(os.path.join(self.refinement_dir, "refinement_report_path.txt"), "w") as f:
    #         f.write(report_path)
    


    def _create_final_report(self) -> None:
        """Create a simplified but robust final report with training statistics."""
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_pdf import PdfPages
        import traceback
        
        report_path = os.path.join(self.log_dir, "training_report.pdf")
        
        print(f"Generating final report at {report_path}...")
        
        try:
            with PdfPages(report_path) as pdf:
                # Track which pages were successfully added
                pages_added = 0
                
                # ======= 1. Summary Page with metadata =======
                try:
                    plt.figure(figsize=(10, 12))
                    plt.axis('off')
                    
                    # Get environment parameters with fallbacks
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
                            try:
                                budget = self.model.env.envs[0].unwrapped.element_budget
                                gamma_c = self.model.env.envs[0].unwrapped.gamma_c
                                max_steps = self.model.env.envs[0].unwrapped.max_episode_steps
                            except:
                                budget = "Unknown"
                                gamma_c = "Unknown"
                                max_steps = "Unknown"
                    
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
                    pages_added += 1
                    print(f"Added summary page to report")
                except Exception as e:
                    print(f"Error creating summary page: {e}")
                    traceback.print_exc()
                    plt.close()
                    
                # ======= 2. Reward Trends =======
                try:
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
                        pages_added += 1
                        print(f"Added rewards trend page to report")
                except Exception as e:
                    print(f"Error creating reward trends page: {e}")
                    traceback.print_exc()
                    plt.close()
                    
                # ======= 3. Action Distribution =======
                try:
                    plt.figure(figsize=(10, 6))
                    
                    # Create a simple bar chart of action counts
                    actions = list(self.action_names.values())
                    counts = [self.action_counts.get(a, 0) for a in self.action_names.keys()]
                    
                    plt.bar(actions, counts)
                    plt.xlabel('Action Type')
                    plt.ylabel('Count')
                    plt.title('Action Distribution')
                    plt.grid(axis='y')
                    
                    # Add percentages on top of bars
                    total = sum(counts)
                    for i, count in enumerate(counts):
                        if total > 0:
                            pct = count / total * 100
                            plt.text(i, count + (total * 0.01), f"{pct:.1f}%", ha='center')
                    
                    pdf.savefig()
                    plt.close()
                    pages_added += 1
                    print(f"Added action distribution page to report")
                except Exception as e:
                    print(f"Error creating action distribution page: {e}")
                    traceback.print_exc()
                    plt.close()
                    
                # ======= 4. Resource Usage =======
                try:
                    if self.resource_usage_history:
                        plt.figure(figsize=(10, 6))
                        
                        # Use a simple line plot with downsampling if needed
                        sample_step = max(1, len(self.resource_usage_history) // 1000)  # Limit to ~1000 points
                        x_vals = np.arange(0, len(self.resource_usage_history), sample_step)
                        y_vals = [self.resource_usage_history[i] for i in x_vals]
                        
                        plt.plot(x_vals, y_vals)
                        plt.axhline(y=1.0, color='r', linestyle='--', label='Budget limit')
                        
                        plt.xlabel('Timestep')
                        plt.ylabel('Resource Usage')
                        plt.title('Resource Usage Over Time')
                        plt.legend()
                        plt.grid(True)
                        
                        pdf.savefig()
                        plt.close()
                        pages_added += 1
                        print(f"Added resource usage page to report")
                except Exception as e:
                    print(f"Error creating resource usage page: {e}")
                    traceback.print_exc()
                    plt.close()
                    
                # ======= 5. Termination Reasons =======
                try:
                    if self.termination_reasons:
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
                        
                        pdf.savefig()
                        plt.close()
                        pages_added += 1
                        print(f"Added termination reasons page to report")
                except Exception as e:
                    print(f"Error creating termination reasons page: {e}")
                    traceback.print_exc()
                    plt.close()
                    
                # ======= 6. Simple Refinement Summary (if available) =======
                try:
                    if hasattr(self, 'refinement_stats') and self.refinement_stats and 'config' in self.refinement_stats:
                        plt.figure(figsize=(10, 6))
                        plt.axis('off')
                        
                        refinement_summary = [
                            "# Refinement Configuration Summary",
                            f"Total Episodes: {self.episodes_completed}",
                            "\n## Configurations Used:"
                        ]
                        
                        # Count episodes by configuration
                        config_counts = {}
                        for config in self.refinement_stats['config']:
                            if config not in config_counts:
                                config_counts[config] = 0
                            config_counts[config] += 1
                        
                        # Add to summary
                        for config, count in config_counts.items():
                            pct = count / len(self.refinement_stats['config']) * 100
                            refinement_summary.append(f"- {config}: {count} episodes ({pct:.1f}%)")
                        
                        # Add coarsening success rates if available
                        if self.coarsening_attempts:
                            refinement_summary.append("\n## Coarsening Success Rates:")
                            
                            for config, attempts in self.coarsening_attempts.items():
                                mode, level = config
                                successes = self.coarsening_successes.get(config, 0)
                                if attempts > 0:
                                    rate = successes / attempts * 100
                                    refinement_summary.append(f"- {mode} Level {level}: {successes}/{attempts} ({rate:.1f}%)")
                        
                        # Add text to figure
                        plt.text(0.05, 0.95, '\n'.join(refinement_summary), transform=plt.gca().transAxes, 
                                fontsize=12, verticalalignment='top', family='monospace',
                                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
                        
                        pdf.savefig()
                        plt.close()
                        pages_added += 1
                        print(f"Added refinement summary page to report")
                        
                except Exception as e:
                    print(f"Error creating refinement summary page: {e}")
                    traceback.print_exc()
                    plt.close()
                    
            print(f"Final report generated with {pages_added} pages and saved to: {report_path}")
            
        except Exception as e:
            print(f"Error generating final report: {e}")
            traceback.print_exc()
        
        # Make sure all figures are closed
        plt.close('all')
        
        # Always save the Excel data, even if PDF generation fails
        try:
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
                    
                # Add refinement summary sheet if available
                if hasattr(self, 'refinement_stats') and len(self.refinement_stats) > 0:
                    refinement_df = pd.DataFrame(self.refinement_stats)
                    refinement_df.to_excel(writer, sheet_name='Refinement Data', index=False)
                    
                    # Add coarsening success sheet if available
                    if self.coarsening_attempts:
                        coarsen_data = []
                        for config, attempts in self.coarsening_attempts.items():
                            mode, level = config
                            successes = self.coarsening_successes.get(config, 0)
                            success_rate = (successes / attempts) * 100 if attempts > 0 else 0
                            
                            coarsen_data.append({
                                'Mode': mode,
                                'Level': level,
                                'Attempts': attempts,
                                'Successes': successes,
                                'Success Rate (%)': success_rate
                            })
                        
                        if coarsen_data:
                            coarsen_df = pd.DataFrame(coarsen_data)
                            coarsen_df.to_excel(writer, sheet_name='Coarsening Success', index=False)
                
                # Metrics sample (simplified)
                if not self.metrics_df.empty:
                    # Sample metrics to avoid excessive file size
                    sample_size = min(5000, len(self.metrics_df))
                    sample_interval = max(1, len(self.metrics_df) // sample_size)
                    sampled_metrics = self.metrics_df.iloc[::sample_interval].copy()
                    sampled_metrics.to_excel(writer, sheet_name='Metrics Sample', index=False)
            
            print(f"Raw data saved to: {excel_path}")
        except Exception as e:
            print(f"Error saving Excel data: {e}")
            traceback.print_exc()
                
        # Save path to a text file for easier programmatic access
        try:
            with open(os.path.join(self.log_dir, "report_path.txt"), "w") as f:
                f.write(report_path)
        except Exception as e:
            print(f"Error saving report path: {e}")

    # def _create_final_report(self) -> None:
    #     """Create a comprehensive final report with training statistics."""
    #     import matplotlib.pyplot as plt
    #     from matplotlib.backends.backend_pdf import PdfPages
        
    #     report_path = os.path.join(self.log_dir, "training_report.pdf")
        
    #     with PdfPages(report_path) as pdf:
    #         # 1. Summary Page with metadata
    #         plt.figure(figsize=(10, 12))
    #         plt.axis('off')
            
    #         # Prepare metadata and summary text
    #         # Get environment parameters
    #         try:
    #             budget = self.model.env.unwrapped.element_budget
    #             gamma_c = self.model.env.unwrapped.gamma_c
    #             max_steps = self.model.env.unwrapped.max_episode_steps
    #         except (AttributeError, KeyError):
    #             try:
    #                 budget = self.model.env.get_wrapper_attr('element_budget')
    #                 gamma_c = self.model.env.get_wrapper_attr('gamma_c')
    #                 max_steps = self.model.env.get_wrapper_attr('max_episode_steps')
    #             except (AttributeError, KeyError):
    #                 budget = self.model.env.envs[0].unwrapped.element_budget
    #                 gamma_c = self.model.env.envs[0].unwrapped.gamma_c
    #                 max_steps = self.model.env.envs[0].unwrapped.max_episode_steps
            
    #         # Create metadata section
    #         metadata_text = [
    #             "# Experiment Configuration",
    #             f"Element Budget: {budget}",
    #             f"Gamma_C: {gamma_c}",
    #             f"Max Episode Steps: {max_steps}",
    #         ]
            
    #         if hasattr(self.model, 'ent_coef'):
    #             metadata_text.append(f"Entropy Coefficient: {self.model.ent_coef}")
            
    #         if hasattr(self.model, 'learning_rate'):
    #             metadata_text.append(f"Learning Rate: {self.model.learning_rate}")
                
    #         # Create summary section
    #         summary_text = [
    #             "# Adaptive Mesh Refinement RL Training Summary",
    #             f"Date: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}",
    #             f"Total Steps: {self.num_timesteps}",
    #             f"Episodes Completed: {self.episodes_completed}",
    #             "\n## Termination Statistics"
    #         ]
            
    #         # Add termination stats
    #         if self.termination_reasons:
    #             total_episodes = sum(self.termination_reasons.values())
    #             for reason, count in self.termination_reasons.items():
    #                 summary_text.append(f"- {reason}: {count} ({count/total_episodes*100:.1f}%)")
            
    #         # Add action stats
    #         total_actions = sum(self.action_counts.values())
    #         if total_actions > 0:
    #             summary_text.append("\n## Action Distribution")
    #             for action, name in self.action_names.items():
    #                 count = self.action_counts.get(action, 0)
    #                 summary_text.append(f"- {name}: {count} ({count/total_actions*100:.1f}%)")
                
    #         # Add reward stats
    #         if self.episode_rewards:
    #             summary_text.append("\n## Reward Statistics")
    #             summary_text.append(f"- Mean Reward: {np.mean(self.episode_rewards):.2f}")
    #             summary_text.append(f"- Min Reward: {np.min(self.episode_rewards):.2f}")
    #             summary_text.append(f"- Max Reward: {np.max(self.episode_rewards):.2f}")
                
    #             # Last 20% of episodes
    #             last_n = max(5, int(len(self.episode_rewards) * 0.2))
    #             last_rewards = self.episode_rewards[-last_n:]
    #             summary_text.append(f"- Mean Reward (last {last_n} episodes): {np.mean(last_rewards):.2f}")
            
    #         # Add resource usage stats
    #         if self.resource_usage_history:
    #             summary_text.append("\n## Resource Usage")
    #             summary_text.append(f"- Mean Resource Usage: {np.mean(self.resource_usage_history):.2f}")
    #             summary_text.append(f"- Max Resource Usage: {np.max(self.resource_usage_history):.2f}")
                
    #             # Resource usage at termination
    #             if not self.episode_df.empty:
    #                 budget_exceeded = (self.episode_df['final_resource_usage'] > 1).sum()
    #                 summary_text.append(f"- Episodes ending with budget exceeded: {budget_exceeded} ({budget_exceeded/len(self.episode_df)*100:.1f}%)")
            
    #         # Add metadata at the top
    #         plt.text(0.05, 0.95, '\n'.join(metadata_text), transform=plt.gca().transAxes, 
    #                  fontsize=12, verticalalignment='top', family='monospace',
    #                  bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
            
    #         # Add summary text below metadata
    #         plt.text(0.05, 0.7, '\n'.join(summary_text), transform=plt.gca().transAxes, 
    #                  fontsize=12, verticalalignment='top', family='monospace',
    #                  bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
            
    #         # Add page to PDF
    #         pdf.savefig()
    #         plt.close()
            
    #         # 2. Reward Trends
    #         if self.episode_rewards:
    #             plt.figure(figsize=(10, 6))
    #             plt.plot(range(1, len(self.episode_rewards) + 1), self.episode_rewards, 'b-', alpha=0.3)
                
    #             # Add smoothed line
    #             window = min(25, len(self.episode_rewards) // 4)
    #             if window > 0:
    #                 smoothed = pd.Series(self.episode_rewards).rolling(window=window, min_periods=1).mean()
    #                 plt.plot(range(1, len(self.episode_rewards) + 1), smoothed, 'b-', label=f'{window}-episode moving avg')
                
    #             plt.xlabel('Episode')
    #             plt.ylabel('Total Reward')
    #             plt.title('Episode Rewards Over Time')
    #             plt.legend()
    #             plt.grid(True)
    #             pdf.savefig()
    #             plt.close()
                
    #         # Additional report pages
    #         # ... (rest of report generation code) ...
        
    #     if self.verbose > 0:
    #         print(f"Final report generated and saved to: {report_path}")
        
    #     # Also save raw data as Excel with multiple sheets
    #     excel_path = os.path.join(self.log_dir, "training_data.xlsx")
    #     with pd.ExcelWriter(excel_path) as writer:
    #         # Episode data
    #         if not self.episode_df.empty:
    #             self.episode_df.to_excel(writer, sheet_name='Episodes', index=False)
            
    #         # Create action summary sheet
    #         action_summary = pd.DataFrame({
    #             'Action': list(self.action_names.values()),
    #             'Count': [self.action_counts.get(a, 0) for a in self.action_names.keys()],
    #             'Percentage': [self.action_counts.get(a, 0) / max(1, sum(self.action_counts.values())) * 100 
    #                           for a in self.action_names.keys()],
    #             'Avg Reward': [np.mean(self.rewards_by_action.get(a, [0])) for a in self.action_names.keys()]
    #         })
    #         action_summary.to_excel(writer, sheet_name='Action Summary', index=False)
            
    #         # Termination summary
    #         if self.termination_reasons:
    #             term_summary = pd.DataFrame({
    #                 'Reason': list(self.termination_reasons.keys()),
    #                 'Count': list(self.termination_reasons.values()),
    #                 'Percentage': [count / max(1, sum(self.termination_reasons.values())) * 100 
    #                               for count in self.termination_reasons.values()]
    #             })
    #             term_summary.to_excel(writer, sheet_name='Termination Summary', index=False)
            
    #         # Add refinement summary sheet
    #         if len(self.refinement_stats) > 0:
    #             refinement_df = pd.DataFrame(self.refinement_stats)
                
    #             # Create pivot table for refinement analysis
    #             if not refinement_df.empty and 'mode' in refinement_df.columns and 'level' in refinement_df.columns:
    #                 pivot_df = pd.pivot_table(
    #                     refinement_df,
    #                     values=['reward', 'element_growth', 'refine_pct', 'coarsen_pct'],
    #                     index=['mode', 'level'],
    #                     aggfunc={
    #                         'reward': ['mean', 'count', 'std'],
    #                         'element_growth': ['mean', 'max'],
    #                         'refine_pct': 'mean',
    #                         'coarsen_pct': 'mean'
    #                     }
    #                 ).reset_index()
                    
    #                 # Flatten multi-level column names
    #                 pivot_df.columns = ['_'.join(col).strip('_') for col in pivot_df.columns.values]
                    
    #                 # Save to Excel
    #                 pivot_df.to_excel(writer, sheet_name='Refinement Summary', index=False)
    #             else:
    #                 # Just save the raw data if we can't create a proper summary
    #                 refinement_df.to_excel(writer, sheet_name='Refinement Data', index=False)
                
    #             # Add coarsening success sheet
    #             if self.coarsening_attempts:
    #                 coarsen_data = []
                    
    #                 for config, attempts in self.coarsening_attempts.items():
    #                     mode, level = config
    #                     successes = self.coarsening_successes.get(config, 0)
    #                     success_rate = (successes / attempts) * 100 if attempts > 0 else 0
                        
    #                     coarsen_data.append({
    #                         'Mode': mode,
    #                         'Level': level,
    #                         'Attempts': attempts,
    #                         'Successes': successes,
    #                         'Success Rate (%)': success_rate
    #                     })
                    
    #                 coarsen_df = pd.DataFrame(coarsen_data)
    #                 coarsen_df.to_excel(writer, sheet_name='Coarsening Success', index=False)
            
    #         # Aggregate metrics sampled at intervals
    #         if not self.metrics_df.empty:
    #             # Sample metrics to avoid excessive file size
    #             sample_size = min(10000, len(self.metrics_df))
    #             sample_interval = max(1, len(self.metrics_df) // sample_size)
    #             sampled_metrics = self.metrics_df.iloc[::sample_interval].copy()
    #             sampled_metrics.to_excel(writer, sheet_name='Metrics Sample', index=False)
        
    #     if self.verbose > 0:
    #         print(f"Raw data saved to: {excel_path}")
            
    #     # Save path to a text file for easier programmatic access
    #     with open(os.path.join(self.log_dir, "report_path.txt"), "w") as f:
    #         f.write(report_path)