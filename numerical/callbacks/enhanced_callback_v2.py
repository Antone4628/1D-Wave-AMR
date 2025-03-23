# Modifications to enhance compatibility between EnhancedMonitorCallback and analyze_tensorboard.py

# In the EnhancedMonitorCallback class, we need to add these features:
# 1. Export event files compatible with TensorBoard analysis script
# 2. Add consistent tag naming to ensure metrics are properly captured
# 3. Add metadata about the configuration to aid in analysis

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


def _create_final_report(self) -> None:
    """Create a comprehensive final report with training statistics and added metadata."""
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_pdf import PdfPages
    import datetime
    
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
        
        # Continue with the rest of the existing report generation...
        
        # Save the path to a text file for easier programmatic access
        with open(os.path.join(self.log_dir, "report_path.txt"), "w") as f:
            f.write(report_path)
        
        if self.verbose > 0:
            print(f"Final report generated and saved to: {report_path}")

# Other important enhancements to ensure consistent metrics are logged:

def on_training_end(self) -> None:
    """Called when training ends."""
    # Save final datasets
    self._save_datasets()
    
    # Generate final visualizations
    self._generate_visualizations()
    
    # Create final comprehensive report
    self._create_final_report()
    
    # Save a metadata file to help the analysis script
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
            "termination_reasons": self.termination_reasons,
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