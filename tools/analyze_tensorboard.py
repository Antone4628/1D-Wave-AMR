
import os
import re
import glob
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tensorboard.backend.event_processing import event_accumulator
from collections import defaultdict
from typing import Dict, List, Tuple, Any, Optional
from matplotlib.backends.backend_pdf import PdfPages
import datetime
import textwrap
import traceback


def load_tensorboard_data(log_dir: str, scalars_only: bool = True, verbose: bool = True) -> Dict[str, pd.DataFrame]:
    """
    Load TensorBoard data from a log directory.
    
    Args:
        log_dir: Path to TensorBoard log directory
        scalars_only: Whether to only load scalar values
        verbose: Whether to print detailed loading information
        
    Returns:
        Dictionary mapping tag names to pandas DataFrames
    """
    if verbose:
        print(f"Loading TensorBoard data from {log_dir}...")
    
    # Find all event files recursively
    event_files = []
    
    # First check direct path
    direct_files = glob.glob(os.path.join(log_dir, "events.out.tfevents.*"))
    if direct_files:
        event_files.extend(direct_files)
        
    # Then check tensorboard subdirectory
    tb_files = glob.glob(os.path.join(log_dir, "tensorboard", "*.tfevents.*"))
    if tb_files:
        event_files.extend(tb_files)
    
    # Finally try recursive search
    if not event_files:
        event_files = glob.glob(os.path.join(log_dir, "**/events.out.tfevents.*"), recursive=True)
    
    if not event_files:
        print(f"Warning: No TensorBoard event files found in {log_dir} or subdirectories")
        # Try one more approach - look for specific directory patterns
        for subdir in ['tensorboard', 'logs', 'tb_logs', 'runs', 'events']:
            potential_path = os.path.join(log_dir, subdir)
            if os.path.exists(potential_path):
                sub_files = glob.glob(os.path.join(potential_path, "**/events.out.tfevents.*"), recursive=True)
                if sub_files:
                    event_files.extend(sub_files)
                    break
    
    if not event_files:
        raise FileNotFoundError(f"No TensorBoard event files found in {log_dir} or its subdirectories")
    
    if verbose:
        print(f"Found {len(event_files)} event files")
    
    dfs = {}
    skipped_tags = set()
    
    for event_file in event_files:
        if verbose:
            print(f"  Processing: {os.path.basename(event_file)}")
        
        try:
            # Load event file with extended size guidance
            ea = event_accumulator.EventAccumulator(
                event_file,
                size_guidance={
                    event_accumulator.SCALARS: 0,  # Load all scalar events
                    event_accumulator.HISTOGRAMS: 0,
                    event_accumulator.IMAGES: 0,
                    event_accumulator.AUDIO: 0,
                    event_accumulator.TENSORS: 0,
                }
            )
            ea.Reload()
            
            # Get available tags
            tags = ea.Tags()['scalars'] if scalars_only else ea.Tags()
            
            if verbose:
                print(f"    Found {len(tags)} tags in this file")
                
            # Load data for each tag
            for tag in tags:
                try:
                    # Clean up tag name for use as column name
                    clean_tag = tag.replace('/', '_').replace(' ', '_')
                    
                    # Extract data
                    if tag in ea.Tags()['scalars']:
                        events = ea.Scalars(tag)
                        if not events:
                            if verbose:
                                print(f"    Warning: No data for tag {tag}")
                            continue
                            
                        data = [(e.wall_time, e.step, e.value) for e in events]
                        df = pd.DataFrame(data, columns=['wall_time', 'step', 'value'])
                        df['tag'] = tag
                        df['clean_tag'] = clean_tag
                        
                        # Validate data
                        if df['value'].isnull().all():
                            if verbose:
                                print(f"    Warning: All values are null for tag {tag}")
                            continue
                            
                        # Add to collection
                        if clean_tag not in dfs:
                            dfs[clean_tag] = df
                        else:
                            dfs[clean_tag] = pd.concat([dfs[clean_tag], df])
                    else:
                        skipped_tags.add(tag)
                except Exception as e:
                    print(f"    Error processing tag {tag}: {e}")
                    continue
                    
        except Exception as e:
            print(f"  Error processing file {event_file}: {e}")
            continue
    
    # Sort each dataframe by step
    for tag in dfs:
        dfs[tag] = dfs[tag].sort_values('step')
        
        # Remove duplicates (can happen with multiple event files)
        dfs[tag] = dfs[tag].drop_duplicates(subset=['step'])
    
    if verbose:
        print(f"  Successfully loaded {len(dfs)} metrics")
        if skipped_tags:
            print(f"  Skipped {len(skipped_tags)} non-scalar tags")
    
    return dfs


def list_available_tags(log_dir: str, verbose: bool = True):
    """Print all available tags in the log directory."""
    try:
        dfs = load_tensorboard_data(log_dir, verbose=verbose)
        
        if not dfs:
            print(f"\nNo metric tags found in {log_dir}")
            return []
            
        tags = sorted(dfs.keys())
        
        print(f"\nAvailable tags in {log_dir}:")
        for tag in tags:
            # Also print data range to help diagnose issues
            if tag in dfs and not dfs[tag].empty:
                min_step = dfs[tag]['step'].min()
                max_step = dfs[tag]['step'].max()
                n_points = len(dfs[tag])
                print(f"  - {tag} ({n_points} points, steps {min_step} to {max_step})")
            else:
                print(f"  - {tag} (empty)")
                
        print("\n")
        return tags
        
    except Exception as e:
        print(f"Error listing tags: {e}")
        return []


def extract_experiment_name(log_dir: str) -> str:
    """Extract experiment name from log directory path."""
    name = os.path.basename(log_dir)
    # Check for common patterns
    gamma_match = re.search(r'gamma_c_(\d+\.?\d*)', log_dir)
    if gamma_match:
        return f"γ={gamma_match.group(1)}"
        
    # Try to extract other common parameter patterns
    param_matches = {
        'gamma': re.search(r'gamma[_-](\d+\.?\d*)', log_dir),
        'lr': re.search(r'lr[_-](\d+\.?\d*)', log_dir),
        'batch': re.search(r'batch[_-](\d+)', log_dir),
        'budget': re.search(r'budget[_-](\d+)', log_dir)
    }
    
    for param, match in param_matches.items():
        if match:
            return f"{param}={match.group(1)}"
    
    return name


def smooth_data(data: pd.DataFrame, window: int = 10) -> pd.DataFrame:
    """Apply smoothing to data."""
    if data.empty or len(data) <= 1:
        return data
        
    if len(data) <= window:
        window = max(2, len(data) // 2)
    
    smoothed = data.copy()
    smoothed['value'] = data['value'].rolling(window=window, min_periods=1).mean()
    return smoothed


def compare_runs(log_dirs: List[str], tags: List[str], output_dir: str, 
                 smooth_window: int = 10, figsize: Tuple[int, int] = (12, 8),
                 pdf: Optional[PdfPages] = None) -> List[plt.Figure]:
    """
    Compare metrics across multiple runs.
    
    Args:
        log_dirs: List of log directories to compare
        tags: List of tags to plot
        output_dir: Directory to save plots
        smooth_window: Window size for smoothing
        figsize: Figure size
        pdf: Optional PdfPages object to add figures to
        
    Returns:
        List of created figures
    """
    os.makedirs(output_dir, exist_ok=True)
    figures = []
    
    # Process each tag
    for tag in tags:
        print(f"Comparing runs for tag: {tag}")
        
        fig = plt.figure(figsize=figsize)
        figures.append(fig)
        
        # Plot data from each run
        run_data = []
        has_data = False
        
        for log_dir in log_dirs:
            try:
                # Load data
                dfs = load_tensorboard_data(log_dir, verbose=False)
                
                # Find matching tag (case-insensitive)
                matching_tags = [t for t in dfs.keys() if tag.lower() in t.lower()]
                if not matching_tags:
                    print(f"  Warning: Tag '{tag}' not found in {log_dir}")
                    continue
                    
                for match_tag in matching_tags:
                    data = dfs[match_tag]
                    
                    # Skip if no data
                    if data.empty:
                        continue
                        
                    # Apply smoothing
                    smoothed = smooth_data(data, window=smooth_window)
                    
                    # Extract experiment name
                    name = extract_experiment_name(log_dir)
                    tag_display = match_tag.replace('_', '/').split('/')[-1]
                    
                    # Plot
                    plt.plot(smoothed['step'], smoothed['value'], label=f"{name}")
                    has_data = True
                    
                    # Save for correlation analysis
                    run_data.append({
                        'name': name,
                        'tag': match_tag,
                        'data': smoothed
                    })
                
            except Exception as e:
                print(f"  Error processing {log_dir} for tag {tag}: {e}")
                traceback.print_exc()
        
        if not has_data:
            print(f"  No data to plot for tag {tag}")
            plt.close()
            figures.pop()  # Remove the empty figure
            continue
        
        # Normalize tag name for display
        display_tag = tag.replace('_', ' ').title()
        
        # Finalize plot
        plt.xlabel('Training Steps')
        plt.ylabel(display_tag)
        plt.title(f'Comparison of {display_tag} Across Runs')
        plt.legend()
        plt.grid(True)
        
        # Save plot to PDF if provided
        if pdf is not None:
            pdf.savefig(fig)
            
        # Save plot to file
        output_file = os.path.join(output_dir, f"comparison_{tag.replace('/', '_')}.png")
        plt.savefig(output_file)
        print(f"  Saved comparison to {output_file}")
    
    return figures


def analyze_correlations(log_dir: str, tags: List[str], output_dir: str,
                         figsize: Tuple[int, int] = (12, 10),
                         pdf: Optional[PdfPages] = None) -> List[plt.Figure]:
    """
    Analyze correlations between different metrics.
    
    Args:
        log_dir: Log directory to analyze
        tags: List of tags to include in correlation analysis
        output_dir: Directory to save plots
        figsize: Figure size
        pdf: Optional PdfPages object to add figures to
        
    Returns:
        List of created figures
    """
    os.makedirs(output_dir, exist_ok=True)
    figures = []
    
    try:
        # Load data with minimal verbose output
        dfs = load_tensorboard_data(log_dir, verbose=False)
        
        if not dfs:
            print(f"No data found in {log_dir} for correlation analysis")
            return figures
            
        # Prepare data for correlation analysis
        correlation_data = {}
        common_steps = None
        
        # Find all available data for requested tags (case-insensitive matching)
        for tag in tags:
            matching_tags = [t for t in dfs.keys() if tag.lower() in t.lower()]
            if not matching_tags:
                print(f"  Warning: Tag '{tag}' not found in {log_dir}")
                continue
            
            for match in matching_tags:
                data = dfs[match]
                
                # Skip empty data
                if data.empty:
                    continue
                    
                # Store tag data
                correlation_data[match] = data
                
                # Track common steps
                if common_steps is None:
                    common_steps = set(data['step'])
                else:
                    common_steps = common_steps.intersection(set(data['step']))
        
        if not correlation_data or not common_steps:
            print(f"Insufficient data for correlation analysis in {log_dir}")
            return figures
            
        if len(common_steps) < 2:
            print(f"Not enough common steps for correlation analysis in {log_dir}")
            return figures
        
        # Filter data to common steps
        filtered_data = {}
        for tag, data in correlation_data.items():
            filtered_data[tag] = data[data['step'].isin(common_steps)]
        
        # Create correlation dataframe
        corr_df = pd.DataFrame({'step': sorted(common_steps)})
        for tag, data in filtered_data.items():
            # Use a more readable display name
            display_tag = tag.replace('_', '/').split('/')[-1]
            merged = pd.merge(corr_df, data[['step', 'value']], on='step')
            corr_df[display_tag] = merged['value']
        
        # Drop step column for correlation
        corr_df_no_step = corr_df.drop('step', axis=1)
        
        # Need at least 2 metrics for correlation
        if corr_df_no_step.shape[1] < 2:
            print(f"Not enough metrics for correlation analysis in {log_dir}")
            return figures
            
        # Calculate correlation matrix
        corr_matrix = corr_df_no_step.corr()
        
        # Plot correlation heatmap
        heatmap_fig = plt.figure(figsize=figsize)
        figures.append(heatmap_fig)
        
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, 
                   center=0, linewidths=0.5, fmt='.2f')
        plt.title(f'Correlation Matrix of Metrics - {extract_experiment_name(log_dir)}')
        plt.tight_layout()
        
        # Save to PDF if provided
        if pdf is not None:
            pdf.savefig(heatmap_fig)
            
        # Save plot to file
        output_file = os.path.join(output_dir, f"correlation_matrix_{extract_experiment_name(log_dir)}.png")
        plt.savefig(output_file)
        print(f"Saved correlation analysis to {output_file}")
        
        # Also create scatter plots for highly correlated pairs
        high_correlations = []
        for i in range(len(corr_matrix.columns)):
            for j in range(i+1, len(corr_matrix.columns)):
                if abs(corr_matrix.iloc[i, j]) > 0.5:  # Threshold for "high" correlation
                    tag1 = corr_matrix.columns[i]
                    tag2 = corr_matrix.columns[j]
                    corr_value = corr_matrix.iloc[i, j]
                    high_correlations.append((tag1, tag2, corr_value))
        
        # Plot scatter plots for highly correlated pairs
        for tag1, tag2, corr_value in high_correlations:
            scatter_fig = plt.figure(figsize=(8, 6))
            figures.append(scatter_fig)
            
            plt.scatter(corr_df[tag1], corr_df[tag2], alpha=0.5)
            
            # Add regression line
            sns.regplot(x=tag1, y=tag2, data=corr_df, scatter=False, color='red')
            
            plt.xlabel(tag1)
            plt.ylabel(tag2)
            plt.title(f'Correlation: {corr_value:.2f}')
            plt.grid(True)
            
            # Save to PDF if provided
            if pdf is not None:
                pdf.savefig(scatter_fig)
                
            # Save plot to file
            output_file = os.path.join(output_dir, f"correlation_{tag1}_{tag2}.png")
            plt.savefig(output_file)
            plt.close()
    
    except Exception as e:
        print(f"Error during correlation analysis: {e}")
        traceback.print_exc()
        
    return figures


def create_multi_panel_dashboard(log_dirs: List[str], output_dir: str,
                                smooth_window: int = 10, figsize: Tuple[int, int] = (16, 12),
                                pdf: Optional[PdfPages] = None) -> List[plt.Figure]:
    """
    Create a multi-panel dashboard with key metrics.
    
    Args:
        log_dirs: List of log directories to include
        output_dir: Directory to save the dashboard
        smooth_window: Window size for smoothing
        figsize: Figure size
        pdf: Optional PdfPages object to add figures to
        
    Returns:
        List of created figures
    """
    os.makedirs(output_dir, exist_ok=True)
    figures = []
    
    # Define key metrics to include in dashboard (with alternative names)
    key_metrics = [
        {'primary': 'rollout_ep_rew_mean', 'alternatives': ['rollout/ep_rew_mean', 'train/reward']},
        {'primary': 'train_entropy_loss', 'alternatives': ['train/entropy_loss', 'entropy_loss']},
        {'primary': 'train_learning_rate', 'alternatives': ['train/learning_rate', 'learning_rate']},
        {'primary': 'train_value_loss', 'alternatives': ['train/value_loss', 'value_loss']},
        {'primary': 'actions_refine_proportion', 'alternatives': ['actions/refine', 'actions/refine_proportion']},
        {'primary': 'actions_coarsen_proportion', 'alternatives': ['actions/coarsen', 'actions/coarsen_proportion']},
        {'primary': 'actions_no_change_proportion', 'alternatives': ['actions/no_change', 'actions/no_change_proportion']},
        {'primary': 'resources_usage', 'alternatives': ['resources/usage', 'resource_usage']},
    ]
    
    # Set up figure and axes
    dashboard_fig, axes = plt.subplots(3, 2, figsize=figsize)
    figures.append(dashboard_fig)
    axes = axes.flatten()
    
    # Process each run
    run_data = {}
    for log_dir in log_dirs:
        try:
            # Load data
            dfs = load_tensorboard_data(log_dir, verbose=False)
            
            if not dfs:
                print(f"No data found in {log_dir} for dashboard")
                continue
                
            # Extract experiment name
            name = extract_experiment_name(log_dir)
            
            # Store data for this run
            run_data[name] = {}
            
            # Find data for each key metric by trying various name patterns
            for metric_info in key_metrics:
                primary = metric_info['primary']
                alternatives = metric_info['alternatives']
                
                # Try all possible names
                all_options = [primary] + alternatives
                found = False
                
                for option in all_options:
                    # Try exact match
                    if option in dfs and not dfs[option].empty:
                        data = dfs[option]
                        smoothed = smooth_data(data, window=smooth_window)
                        run_data[name][primary] = smoothed
                        found = True
                        break
                        
                    # Try case-insensitive matching
                    matching_tags = [t for t in dfs.keys() if option.lower() in t.lower()]
                    for match in matching_tags:
                        if not dfs[match].empty:
                            data = dfs[match]
                            smoothed = smooth_data(data, window=smooth_window)
                            run_data[name][primary] = smoothed
                            found = True
                            break
                    
                    if found:
                        break
                
                if not found:
                    print(f"  Warning: No data found for {primary} in {log_dir}")
        except Exception as e:
            print(f"Error processing {log_dir} for dashboard: {e}")
            continue
    
    # Plot key metrics (up to 6 panels)
    for i, metric_info in enumerate(key_metrics[:6]):  # Plot first 6 metrics (3x2 grid)
        if i >= len(axes):
            break
            
        ax = axes[i]
        metric = metric_info['primary']
        
        # Get display name
        display_name = metric.replace('_', ' ').title()
        
        # Plot each run
        has_data = False
        for name, data in run_data.items():
            if metric in data and not data[metric].empty:
                ax.plot(data[metric]['step'], data[metric]['value'], label=name)
                has_data = True
        
        # Set labels and title
        ax.set_xlabel('Steps')
        ax.set_ylabel(display_name)
        ax.set_title(display_name)
        ax.grid(True)
        
        # Only add legend to first plot to avoid clutter
        if i == 0 and has_data:
            ax.legend()
            
        # If no data, show message
        if not has_data:
            ax.text(0.5, 0.5, f"No data available for {display_name}", 
                    ha='center', va='center', transform=ax.transAxes)
    
    # Adjust layout and save
    dashboard_fig.tight_layout()
    
    # Save to PDF if provided
    if pdf is not None:
        pdf.savefig(dashboard_fig)
        
    # Save to file
    output_file = os.path.join(output_dir, f"dashboard_metrics.png")
    plt.savefig(output_file)
    print(f"Saved dashboard to {output_file}")
    
    # Create action distribution trend chart
    try:
        action_fig = plt.figure(figsize=(12, 8))
        figures.append(action_fig)
        
        # Extract refine/coarsen/no-change proportions for each run
        action_keys = {
            'Refine': 'actions_refine_proportion',
            'Coarsen': 'actions_coarsen_proportion',
            'No Change': 'actions_no_change_proportion'
        }
        
        has_action_data = False
        
        for name, data in run_data.items():
            for action_label, action_key in action_keys.items():
                if action_key in data and not data[action_key].empty:
                    plt.plot(data[action_key]['step'], data[action_key]['value'], 
                            label=f"{name} - {action_label}", 
                            linestyle='-' if action_label == 'Refine' else 
                                      ('--' if action_label == 'Coarsen' else ':'))
                    has_action_data = True
        
        if has_action_data:
            plt.xlabel('Training Steps')
            plt.ylabel('Action Proportion')
            plt.title('Action Distribution Over Time')
            plt.legend()
            plt.grid(True)
            
            # Save to PDF if provided
            if pdf is not None:
                pdf.savefig(action_fig)
                
            # Save plot to file
            output_file = os.path.join(output_dir, f"action_distribution_trend.png")
            plt.savefig(output_file)
            print(f"Saved action distribution trend to {output_file}")
        else:
            plt.close()
            figures.remove(action_fig)
            print("No action distribution data available")
        
    except Exception as e:
        print(f"Error creating action distribution chart: {e}")
        if action_fig in figures:
            figures.remove(action_fig)
    
    return figures


def create_comprehensive_report(log_dirs: List[str], tags: List[str], output_dir: str, 
                              smooth_window: int = 10, figsize: Tuple[int, int] = (12, 8),
                              verbose: bool = False):
    """
    Create a comprehensive PDF report with all analyses.
    
    Args:
        log_dirs: List of log directories to analyze
        tags: List of tags to include in analysis
        output_dir: Directory to save the report
        smooth_window: Window size for smoothing
        figsize: Default figure size
        verbose: Print verbose output during processing
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Define report path
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = os.path.join(output_dir, f"tensorboard_analysis_report_{timestamp}.pdf")
    
    # Initialize found tags
    all_found_tags = set()
    
    # Get available tags from all directories
    print("Scanning log directories for available metrics...")
    for log_dir in log_dirs:
        try:
            found_tags = list_available_tags(log_dir, verbose=verbose)
            all_found_tags.update(found_tags)
        except Exception as e:
            print(f"Error scanning {log_dir}: {e}")
    
    # If no tags specified, use all found tags
    if not tags and all_found_tags:
        print("No tags specified, using all found tags")
        tags = sorted(list(all_found_tags))
        
    # If still no tags, use common defaults
    if not tags:
        print("No tags found, using default tags")
        tags = [
            "rollout/ep_rew_mean", "train/entropy_loss", "train/value_loss",
            "resources/usage", "actions/refine"
        ]
    
    print(f"Creating comprehensive report at {report_path}...")
    
    with PdfPages(report_path) as pdf:
        # 1. Cover Page
        fig = plt.figure(figsize=(12, 15))
        plt.axis('off')
        
        title_text = "TensorBoard Analysis Report"
        subtitle_text = f"Generated on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}"
        
        experiments_text = "Experiments included:\n" + "\n".join([f"- {extract_experiment_name(log_dir)}" for log_dir in log_dirs])
        
        plt.text(0.5, 0.8, title_text, fontsize=24, ha='center', weight='bold')
        plt.text(0.5, 0.75, subtitle_text, fontsize=16, ha='center')
        plt.text(0.5, 0.6, experiments_text, fontsize=14, ha='center')
        
        # Add info about the analyzed metrics
        plt.text(0.5, 0.4, "Analyzed Metrics:", fontsize=16, ha='center', weight='bold')
        metrics_text = "\n".join([f"- {tag}" for tag in tags])
        plt.text(0.5, 0.35, metrics_text, fontsize=12, ha='center')
        
        pdf.savefig(fig)
        plt.close()
        
        # 2. Extract and summarize key statistics
        try:
            summary_fig = plt.figure(figsize=(12, 15))
            plt.axis('off')
            
            summary_title = "Training Summary Statistics"
            plt.text(0.5, 0.95, summary_title, fontsize=20, ha='center', weight='bold')
            
            y_position = 0.9
            for log_dir in log_dirs:
                try:
                    dfs = load_tensorboard_data(log_dir, verbose=False)
                    
                    if not dfs:
                        print(f"No data found in {log_dir} for summary")
                        continue
                        
                    exp_name = extract_experiment_name(log_dir)
                    
                    plt.text(0.5, y_position, f"Experiment: {exp_name}", fontsize=16, ha='center', weight='bold')
                    y_position -= 0.03
                    
                    # Try to extract key statistics
                    stats_text = []
                    
                    # Episode rewards
                    try:
                        # Try different possible names for rewards
                        reward_tags = ['rollout_ep_rew_mean', 'rollout/ep_rew_mean', 'train_reward', 'train/reward', 'reward']
                        reward_tag = None
                        
                        for tag in reward_tags:
                            if tag in dfs and not dfs[tag].empty:
                                reward_tag = tag
                                break
                                
                        if not reward_tag:
                            # Try pattern matching
                            for key in dfs.keys():
                                if 'reward' in key.lower() or 'rew' in key.lower():
                                    reward_tag = key
                                    break
                        
                        if reward_tag and not dfs[reward_tag].empty:
                            rewards = dfs[reward_tag]['value']
                            stats_text.append(f"Mean Reward: {rewards.mean():.2f}")
                            stats_text.append(f"Min Reward: {rewards.min():.2f}")
                            stats_text.append(f"Max Reward: {rewards.max():.2f}")
                            
                            # Last 20% of rewards
                            last_n = max(1, int(len(rewards) * 0.2))
                            last_rewards = rewards.tail(last_n)
                            stats_text.append(f"Final 20% Mean Reward: {last_rewards.mean():.2f}")
                    except Exception as e:
                        print(f"Error extracting reward stats from {log_dir}: {e}")
                    
                    # Episode lengths
                    try:
                        length_tags = ['rollout_ep_len_mean', 'rollout/ep_len_mean', 'episode_length']
                        length_tag = None
                        
                        for tag in length_tags:
                            if tag in dfs and not dfs[tag].empty:
                                length_tag = tag
                                break
                                
                        if not length_tag:
                            # Try pattern matching
                            for key in dfs.keys():
                                if 'length' in key.lower() or 'len' in key.lower():
                                    length_tag = key
                                    break
                                    
                        if length_tag and not dfs[length_tag].empty:
                            lengths = dfs[length_tag]['value']
                            stats_text.append(f"Mean Episode Length: {lengths.mean():.1f}")
                    except Exception as e:
                        print(f"Error extracting length stats from {log_dir}: {e}")
                    
                    # Action distributions
                    try:
                        action_patterns = {
                            'Refine': ['actions_refine_proportion', 'actions/refine', 'refine'],
                            'Coarsen': ['actions_coarsen_proportion', 'actions/coarsen', 'coarsen'],
                            'No Change': ['actions_no_change_proportion', 'actions/no_change', 'no_change']
                        }
                        
                        action_stats = []
                        
                        for action, patterns in action_patterns.items():
                            for pattern in patterns:
                                found = False
                                # Exact match
                                if pattern in dfs and not dfs[pattern].empty:
                                    # Get the last value as the final proportion
                                    final_value = dfs[pattern]['value'].iloc[-1]
                                    action_stats.append(f"{action}: {final_value:.1%}")
                                    found = True
                                    break
                                
                                # Pattern match
                                if not found:
                                    for key in dfs.keys():
                                        if pattern in key.lower():
                                            if not dfs[key].empty:
                                                final_value = dfs[key]['value'].iloc[-1]
                                                action_stats.append(f"{action}: {final_value:.1%}")
                                                found = True
                                                break
                                
                                if found:
                                    break
                        
                        if action_stats:
                            stats_text.append("Final Action Distribution:")
                            stats_text.extend(action_stats)
                    except Exception as e:
                        print(f"Error extracting action stats from {log_dir}: {e}")
                    
                    # Add all stats to the figure
                    wrapped_text = "\n".join(stats_text)
                    plt.text(0.5, y_position, wrapped_text, fontsize=12, ha='center')
                    
                    y_position -= 0.15  # Move down for next experiment
                    
                    if y_position < 0.2:  # Start a new page if we're running out of space
                        pdf.savefig(summary_fig)
                        plt.close()
                        
                        summary_fig = plt.figure(figsize=(12, 15))
                        plt.axis('off')
                        plt.text(0.5, 0.95, "Training Summary Statistics (continued)", 
                                 fontsize=20, ha='center', weight='bold')
                        y_position = 0.9
                except Exception as e:
                    print(f"Error processing {log_dir} for summary: {e}")
                    continue
            
            pdf.savefig(summary_fig)
            plt.close()
        except Exception as e:
            print(f"Error creating summary page: {e}")
            traceback.print_exc()
        
        # 3. Run comparison plots for each selected metric
        print("Creating comparison plots...")
        compare_runs(log_dirs, tags, output_dir, smooth_window, figsize, pdf)
        
        # 4. Run correlation analyses for each experiment
        print("Creating correlation analyses...")
        for log_dir in log_dirs:
            analyze_correlations(log_dir, tags, output_dir, (12, 10), pdf)
        
        # 5. Create dashboard visualizations
        print("Creating dashboard visualizations...")
        create_multi_panel_dashboard(log_dirs, output_dir, smooth_window, (16, 12), pdf)
        
        # 6. Add a conclusion/notes page
        notes_fig = plt.figure(figsize=(12, 15))
        plt.axis('off')
        
        plt.text(0.5, 0.9, "Analysis Notes", fontsize=20, ha='center', weight='bold')
        
        notes_text = [
            "Key Observations:",
            "",
            "1. The charts above show the training progress across multiple metrics.",
            "",
            "2. Correlations between metrics can reveal relationships between action choices,",
            "   resource usage, and rewards.",
            "",
            "3. The dashboard provides a comprehensive view of the most important metrics.",
            "",
            "4. For detailed analysis, examine specific metrics that show significant changes",
            "   during training.",
            "",
            f"This report was generated automatically on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "using the TensorBoard Analysis Tool."
        ]
        
        plt.text(0.5, 0.7, "\n".join(notes_text), fontsize=12, ha='center')
        
        pdf.savefig(notes_fig)
        plt.close()
    
    print(f"Comprehensive report saved to {report_path}")
    return report_path


def extract_config_from_log_dir(log_dir: str) -> dict:
    """
    Try to extract configuration information from the log directory.
    
    Args:
        log_dir: Path to log directory
        
    Returns:
        Dictionary with configuration information or empty dict if not found
    """
    config = {}
    
    # Look for config.yaml or similar files
    config_patterns = ['config.yaml', 'config.yml', 'params.yaml', 'params.yml']
    for pattern in config_patterns:
        config_path = os.path.join(log_dir, pattern)
        if os.path.exists(config_path):
            try:
                import yaml
                with open(config_path, 'r') as f:
                    config = yaml.safe_load(f)
                print(f"Loaded configuration from {config_path}")
                break
            except Exception as e:
                print(f"Error loading config from {config_path}: {e}")
    
    # Also look for metadata.json
    metadata_path = os.path.join(log_dir, "training_metadata.json")
    if os.path.exists(metadata_path):
        try:
            import json
            with open(metadata_path, 'r') as f:
                metadata = json.load(f)
            
            # Merge with config
            config.update(metadata)
            print(f"Loaded metadata from {metadata_path}")
        except Exception as e:
            print(f"Error loading metadata from {metadata_path}: {e}")
    
    return config


def main():
    """Main function for processing command line arguments."""
    parser = argparse.ArgumentParser(description="Analyze TensorBoard logs for AMR-RL experiments")
    parser.add_argument("--log-dirs", nargs="+", required=True, help="Directories containing TensorBoard logs")
    parser.add_argument("--output-dir", default="tensorboard_analysis", help="Directory to save analysis outputs")
    parser.add_argument("--tags", nargs="+", default=[], help="Tags to analyze")
    parser.add_argument("--smooth", type=int, default=20, help="Window size for smoothing")
    parser.add_argument("--compare", action="store_true", help="Compare multiple runs")
    parser.add_argument("--correlations", action="store_true", help="Analyze correlations between metrics")
    parser.add_argument("--dashboard", action="store_true", help="Create multi-panel dashboard")
    parser.add_argument("--list-tags", action="store_true", help="List all available tags in the log directories")
    parser.add_argument("--report", action="store_true", help="Create comprehensive PDF report with all analyses")
    parser.add_argument("--verbose", action="store_true", help="Print detailed information during analysis")

    args = parser.parse_args()
    
    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)

    # List tags if requested
    if args.list_tags:
        for log_dir in args.log_dirs:
            list_available_tags(log_dir, verbose=args.verbose)
        return
    
    # Create comprehensive report if requested
    if args.report:
        create_comprehensive_report(args.log_dirs, args.tags, args.output_dir, args.smooth, verbose=args.verbose)
        return
    
    # Process comparison if requested
    if args.compare or len(args.log_dirs) > 1:
        compare_runs(args.log_dirs, args.tags, args.output_dir, args.smooth)
    
    # Process correlations if requested
    if args.correlations:
        for log_dir in args.log_dirs:
            analyze_correlations(log_dir, args.tags, args.output_dir)
    
    # Create dashboard if requested
    if args.dashboard:
        create_multi_panel_dashboard(args.log_dirs, args.output_dir, args.smooth)
    
    # If no analysis specified, do all
    if not (args.compare or args.correlations or args.dashboard or args.report or args.list_tags):
        print("No specific analysis requested, performing all analyses.")
        
        # Create comprehensive report by default
        create_comprehensive_report(args.log_dirs, args.tags, args.output_dir, args.smooth, verbose=args.verbose)


if __name__ == "__main__":
    main()


# #!/usr/bin/env python
# """
# TensorBoard Log Analysis Script

# This script extracts and visualizes data from TensorBoard logs, allowing for
# comparison across multiple experiments. It's designed specifically for analyzing
# DG-AMR reinforcement learning results.

# Features:
# - Extracts metrics from TensorBoard event files
# - Creates customized visualizations with matplotlib/seaborn
# - Supports comparison of multiple runs on the same plot
# - Performs correlation analysis between key metrics
# - Supports smoothing and multi-panel plots
# """

# import os
# import re
# import glob
# import argparse
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from tensorboard.backend.event_processing import event_accumulator
# from collections import defaultdict
# from typing import Dict, List, Tuple, Any, Optional


# def load_tensorboard_data(log_dir: str, scalars_only: bool = True) -> Dict[str, pd.DataFrame]:
#     """
#     Load TensorBoard data from a log directory.
    
#     Args:
#         log_dir: Path to TensorBoard log directory
#         scalars_only: Whether to only load scalar values
        
#     Returns:
#         Dictionary mapping tag names to pandas DataFrames
#     """
#     print(f"Loading TensorBoard data from {log_dir}...")
    
#     # Find all event files
#     event_files = glob.glob(os.path.join(log_dir, "events.out.tfevents.*"))
#     if not event_files:
#         # Try looking in subdirectories (for SB3 logs)
#         event_files = glob.glob(os.path.join(log_dir, "**/events.out.tfevents.*"), recursive=True)
        
#     if not event_files:
#         raise FileNotFoundError(f"No TensorBoard event files found in {log_dir}")
    
#     dfs = {}
#     for event_file in event_files:
#         print(f"  Processing: {os.path.basename(event_file)}")
        
#         # Load event file
#         ea = event_accumulator.EventAccumulator(
#             event_file,
#             size_guidance={
#                 event_accumulator.SCALARS: 0,  # Load all scalar events
#                 event_accumulator.HISTOGRAMS: 0,
#                 event_accumulator.IMAGES: 0,
#                 event_accumulator.AUDIO: 0,
#                 event_accumulator.TENSORS: 0,
#             }
#         )
#         ea.Reload()
        
#         # Get available tags
#         tags = ea.Tags()['scalars'] if scalars_only else ea.Tags()
        
#         # Load data for each tag
#         for tag in tags:
#             # Clean up tag name for use as column name
#             clean_tag = tag.replace('/', '_').replace(' ', '_')
            
#             # Extract data
#             if tag in ea.Tags()['scalars']:
#                 events = ea.Scalars(tag)
#                 data = [(e.wall_time, e.step, e.value) for e in events]
#                 df = pd.DataFrame(data, columns=['wall_time', 'step', 'value'])
#                 df['tag'] = tag
#                 df['clean_tag'] = clean_tag
                
#                 # Add to collection
#                 if clean_tag not in dfs:
#                     dfs[clean_tag] = df
#                 else:
#                     dfs[clean_tag] = pd.concat([dfs[clean_tag], df])
    
#     # Sort each dataframe by step
#     for tag in dfs:
#         dfs[tag] = dfs[tag].sort_values('step')
    
#     print(f"  Loaded {len(dfs)} metrics")
#     return dfs

# def list_available_tags(log_dir):
#     """Print all available tags in the log directory."""
#     dfs = load_tensorboard_data(log_dir)
#     print("\nAvailable tags in", log_dir)
#     for tag in sorted(dfs.keys()):
#         print(f"  - {tag}")
#     print("\n")


# def extract_experiment_name(log_dir: str) -> str:
#     """Extract experiment name from log directory path."""
#     name = os.path.basename(log_dir)
#     # Check for common patterns
#     gamma_match = re.search(r'gamma_c_(\d+\.\d+)', log_dir)
#     if gamma_match:
#         return f"γ={gamma_match.group(1)}"
#     return name


# def smooth_data(data: pd.DataFrame, window: int = 10) -> pd.DataFrame:
#     """Apply smoothing to data."""
#     if len(data) <= window:
#         return data
    
#     smoothed = data.copy()
#     smoothed['value'] = data['value'].rolling(window=window, min_periods=1).mean()
#     return smoothed


# def compare_runs(log_dirs: List[str], tags: List[str], output_dir: str, 
#                  smooth_window: int = 10, figsize: Tuple[int, int] = (12, 8)):
#     """
#     Compare metrics across multiple runs.
    
#     Args:
#         log_dirs: List of log directories to compare
#         tags: List of tags to plot
#         output_dir: Directory to save plots
#         smooth_window: Window size for smoothing
#         figsize: Figure size
#     """
#     os.makedirs(output_dir, exist_ok=True)
    
#     # Process each tag
#     for tag in tags:
#         print(f"Comparing runs for tag: {tag}")
        
#         plt.figure(figsize=figsize)
        
#         # Plot data from each run
#         run_data = []
#         for log_dir in log_dirs:
#             try:
#                 # Load data
#                 dfs = load_tensorboard_data(log_dir)
                
#                 # Find matching tag
#                 matching_tags = [t for t in dfs.keys() if tag.lower() in t.lower()]
#                 if not matching_tags:
#                     print(f"  Warning: Tag '{tag}' not found in {log_dir}")
#                     continue
                
#                 best_match = matching_tags[0]
#                 data = dfs[best_match]
                
#                 # Apply smoothing
#                 smoothed = smooth_data(data, window=smooth_window)
                
#                 # Extract experiment name
#                 name = extract_experiment_name(log_dir)
                
#                 # Plot
#                 plt.plot(smoothed['step'], smoothed['value'], label=name)
                
#                 # Save for correlation analysis
#                 run_data.append({
#                     'name': name,
#                     'data': smoothed
#                 })
                
#             except Exception as e:
#                 print(f"  Error processing {log_dir} for tag {tag}: {e}")
        
#         if not run_data:
#             print(f"  No data to plot for tag {tag}")
#             plt.close()
#             continue
        
#         # Finalize plot
#         plt.xlabel('Training Steps')
#         plt.ylabel(tag.replace('_', ' ').title())
#         plt.title(f'Comparison of {tag.replace("_", " ").title()} Across Runs')
#         plt.legend()
#         plt.grid(True)
        
#         # Save plot
#         output_file = os.path.join(output_dir, f"comparison_{tag.replace('/', '_')}.png")
#         plt.savefig(output_file)
#         plt.close()
        
#         print(f"  Saved comparison to {output_file}")


# def analyze_correlations(log_dir: str, tags: List[str], output_dir: str,
#                          figsize: Tuple[int, int] = (12, 10)):
#     """
#     Analyze correlations between different metrics.
    
#     Args:
#         log_dir: Log directory to analyze
#         tags: List of tags to include in correlation analysis
#         output_dir: Directory to save plots
#         figsize: Figure size
#     """
#     os.makedirs(output_dir, exist_ok=True)
    
#     try:
#         # Load data
#         dfs = load_tensorboard_data(log_dir)
        
#         # Prepare data for correlation analysis
#         correlation_data = {}
#         common_steps = None
        
#         for tag in tags:
#             # Find matching tags
#             matching_tags = [t for t in dfs.keys() if tag.lower() in t.lower()]
#             if not matching_tags:
#                 print(f"  Warning: Tag '{tag}' not found in {log_dir}")
#                 continue
            
#             best_match = matching_tags[0]
#             data = dfs[best_match]
            
#             # Store tag data
#             correlation_data[tag] = data
            
#             # Track common steps
#             if common_steps is None:
#                 common_steps = set(data['step'])
#             else:
#                 common_steps = common_steps.intersection(set(data['step']))
        
#         if not correlation_data or not common_steps:
#             print(f"Insufficient data for correlation analysis in {log_dir}")
#             return
        
#         # Filter data to common steps
#         filtered_data = {}
#         for tag, data in correlation_data.items():
#             filtered_data[tag] = data[data['step'].isin(common_steps)]
        
#         # Create correlation dataframe
#         corr_df = pd.DataFrame({'step': sorted(common_steps)})
#         for tag, data in filtered_data.items():
#             merged = pd.merge(corr_df, data[['step', 'value']], on='step')
#             corr_df[tag] = merged['value']
        
#         # Calculate correlation matrix
#         corr_matrix = corr_df.drop('step', axis=1).corr()
        
#         # Plot correlation heatmap
#         plt.figure(figsize=figsize)
#         sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, 
#                    center=0, linewidths=0.5, fmt='.2f')
#         plt.title(f'Correlation Matrix of Metrics - {extract_experiment_name(log_dir)}')
#         plt.tight_layout()
        
#         # Save plot
#         output_file = os.path.join(output_dir, f"correlation_matrix_{extract_experiment_name(log_dir)}.png")
#         plt.savefig(output_file)
#         plt.close()
        
#         print(f"Saved correlation analysis to {output_file}")
        
#         # Also create scatter plots for highly correlated pairs
#         high_correlations = []
#         for i in range(len(corr_matrix.columns)):
#             for j in range(i+1, len(corr_matrix.columns)):
#                 if abs(corr_matrix.iloc[i, j]) > 0.5:  # Threshold for "high" correlation
#                     tag1 = corr_matrix.columns[i]
#                     tag2 = corr_matrix.columns[j]
#                     corr_value = corr_matrix.iloc[i, j]
#                     high_correlations.append((tag1, tag2, corr_value))
        
#         # Plot scatter plots for highly correlated pairs
#         for tag1, tag2, corr_value in high_correlations:
#             plt.figure(figsize=(8, 6))
#             plt.scatter(corr_df[tag1], corr_df[tag2], alpha=0.5)
            
#             # Add regression line
#             sns.regplot(x=tag1, y=tag2, data=corr_df, scatter=False, color='red')
            
#             plt.xlabel(tag1.replace('_', ' ').title())
#             plt.ylabel(tag2.replace('_', ' ').title())
#             plt.title(f'Correlation: {corr_value:.2f}')
#             plt.grid(True)
            
#             # Save plot
#             output_file = os.path.join(output_dir, f"correlation_{tag1}_{tag2}.png")
#             plt.savefig(output_file)
#             plt.close()
    
#     except Exception as e:
#         print(f"Error during correlation analysis: {e}")


# def create_multi_panel_dashboard(log_dirs: List[str], output_dir: str,
#                                 smooth_window: int = 10, figsize: Tuple[int, int] = (16, 12)):
#     """
#     Create a multi-panel dashboard with key metrics.
    
#     Args:
#         log_dirs: List of log directories to include
#         output_dir: Directory to save the dashboard
#         smooth_window: Window size for smoothing
#         figsize: Figure size
#     """
#     os.makedirs(output_dir, exist_ok=True)
    
#     # Define key metrics to include in dashboard
#     key_metrics = [
#         'rollout/ep_rew_mean',           # Episode reward
#         'train/entropy_loss',            # Entropy loss
#         'train/learning_rate',           # Learning rate
#         'train/value_loss',              # Value loss
#         'actions_refine_proportion',     # Refine proportion
#         'actions_coarsen_proportion',    # Coarsen proportion
#         'actions_no_change_proportion',  # No-change proportion
#         'resources_usage',               # Resource usage
#         'termination_budget_exceeded',   # Budget exceeded termination
#         'termination_maximum_episode_steps_reached'  # Max steps termination
#     ]
    
#     # Set up figure and axes
#     fig, axes = plt.subplots(3, 2, figsize=figsize)
#     axes = axes.flatten()
    
#     # Process each run
#     run_data = {}
#     for log_dir in log_dirs:
#         try:
#             # Load data
#             dfs = load_tensorboard_data(log_dir)
            
#             # Extract experiment name
#             name = extract_experiment_name(log_dir)
            
#             # Store data for this run
#             run_data[name] = {}
            
#             # Find data for each key metric
#             for metric in key_metrics:
#                 matching_tags = [t for t in dfs.keys() if metric.lower() in t.lower()]
#                 if not matching_tags:
#                     continue
                
#                 best_match = matching_tags[0]
#                 data = dfs[best_match]
                
#                 # Apply smoothing
#                 smoothed = smooth_data(data, window=smooth_window)
                
#                 # Store for plotting
#                 run_data[name][metric] = smoothed
#         except Exception as e:
#             print(f"Error processing {log_dir}: {e}")
    
#     # Plot key metrics
#     for i, metric in enumerate(key_metrics[:6]):  # Plot first 6 metrics (3x2 grid)
#         ax = axes[i]
        
#         # Plot each run
#         for name, data in run_data.items():
#             if metric in data:
#                 ax.plot(data[metric]['step'], data[metric]['value'], label=name)
        
#         # Set labels and title
#         ax.set_xlabel('Steps')
#         ax.set_ylabel(metric.split('/')[-1].replace('_', ' ').title())
#         ax.set_title(metric.split('/')[-1].replace('_', ' ').title())
#         ax.grid(True)
        
#         # Only add legend to first plot to avoid clutter
#         if i == 0:
#             ax.legend()
    
#     # Adjust layout and save
#     fig.tight_layout()
#     output_file = os.path.join(output_dir, f"dashboard_metrics.png")
#     plt.savefig(output_file)
#     plt.close()
    
#     print(f"Saved dashboard to {output_file}")
    
#     # Create action distribution trend chart
#     try:
#         plt.figure(figsize=(12, 8))
        
#         # Extract refine/coarsen/no-change proportions for each run
#         for name, data in run_data.items():
#             refine_key = next((k for k in data.keys() if 'refine_proportion' in k.lower()), None)
#             coarsen_key = next((k for k in data.keys() if 'coarsen_proportion' in k.lower()), None)
#             no_change_key = next((k for k in data.keys() if 'no_change_proportion' in k.lower()), None)
            
#             # Plot trends if data available
#             if refine_key and data[refine_key] is not None:
#                 plt.plot(data[refine_key]['step'], data[refine_key]['value'], 
#                         label=f"{name} - Refine")
            
#             if coarsen_key and data[coarsen_key] is not None:
#                 plt.plot(data[coarsen_key]['step'], data[coarsen_key]['value'], 
#                         label=f"{name} - Coarsen", linestyle='--')
            
#             if no_change_key and data[no_change_key] is not None:
#                 plt.plot(data[no_change_key]['step'], data[no_change_key]['value'], 
#                         label=f"{name} - No Change", linestyle=':')
        
#         plt.xlabel('Training Steps')
#         plt.ylabel('Action Proportion')
#         plt.title('Action Distribution Over Time')
#         plt.legend()
#         plt.grid(True)
        
#         # Save plot
#         output_file = os.path.join(output_dir, f"action_distribution_trend.png")
#         plt.savefig(output_file)
#         plt.close()
        
#         print(f"Saved action distribution trend to {output_file}")
        
#     except Exception as e:
#         print(f"Error creating action distribution chart: {e}")


# def main():
#     """Main function for processing command line arguments."""
#     parser = argparse.ArgumentParser(description="Analyze TensorBoard logs for AMR-RL experiments")
#     parser.add_argument("--log-dirs", nargs="+", required=True, help="Directories containing TensorBoard logs")
#     parser.add_argument("--output-dir", default="tensorboard_analysis", help="Directory to save analysis outputs")
#     parser.add_argument("--tags", nargs="+", default=[
#         "rollout/ep_rew_mean", "train/entropy_loss", "train/value_loss",
#         "resources/usage", "actions/refine"
#     ], help="Tags to analyze")
#     parser.add_argument("--smooth", type=int, default=20, help="Window size for smoothing")
#     parser.add_argument("--compare", action="store_true", help="Compare multiple runs")
#     parser.add_argument("--correlations", action="store_true", help="Analyze correlations between metrics")
#     parser.add_argument("--dashboard", action="store_true", help="Create multi-panel dashboard")
#     parser.add_argument("--list-tags", action="store_true", help="List all available tags in the log directories")


    
#     args = parser.parse_args()
    
#     # Create output directory
#     os.makedirs(args.output_dir, exist_ok=True)
    
#     # Process comparison if requested
#     if args.compare or len(args.log_dirs) > 1:
#         compare_runs(args.log_dirs, args.tags, args.output_dir, args.smooth)
    
#     # Process correlations if requested
#     if args.correlations:
#         for log_dir in args.log_dirs:
#             analyze_correlations(log_dir, args.tags, args.output_dir)
    
#     # Create dashboard if requested
#     if args.dashboard:
#         create_multi_panel_dashboard(args.log_dirs, args.output_dir, args.smooth)
    
#     # If no analysis specified, do all
#     if not (args.compare or args.correlations or args.dashboard):
#         print("No specific analysis requested, performing all analyses.")
#         compare_runs(args.log_dirs, args.tags, args.output_dir, args.smooth)
#         for log_dir in args.log_dirs:
#             analyze_correlations(log_dir, args.tags, args.output_dir)
#         create_multi_panel_dashboard(args.log_dirs, args.output_dir, args.smooth)

    
#     if args.list_tags:
#         for log_dir in args.log_dirs:
#             list_available_tags(log_dir)
#         return


# if __name__ == "__main__":
#     main()