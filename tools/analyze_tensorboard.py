#!/usr/bin/env python
"""
TensorBoard Log Analysis Script

This script extracts and visualizes data from TensorBoard logs, allowing for
comparison across multiple experiments. It's designed specifically for analyzing
DG-AMR reinforcement learning results.

Features:
- Extracts metrics from TensorBoard event files
- Creates customized visualizations with matplotlib/seaborn
- Supports comparison of multiple runs on the same plot
- Performs correlation analysis between key metrics
- Supports smoothing and multi-panel plots
"""

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


def load_tensorboard_data(log_dir: str, scalars_only: bool = True) -> Dict[str, pd.DataFrame]:
    """
    Load TensorBoard data from a log directory.
    
    Args:
        log_dir: Path to TensorBoard log directory
        scalars_only: Whether to only load scalar values
        
    Returns:
        Dictionary mapping tag names to pandas DataFrames
    """
    print(f"Loading TensorBoard data from {log_dir}...")
    
    # Find all event files
    event_files = glob.glob(os.path.join(log_dir, "events.out.tfevents.*"))
    if not event_files:
        # Try looking in subdirectories (for SB3 logs)
        event_files = glob.glob(os.path.join(log_dir, "**/events.out.tfevents.*"), recursive=True)
        
    if not event_files:
        raise FileNotFoundError(f"No TensorBoard event files found in {log_dir}")
    
    dfs = {}
    for event_file in event_files:
        print(f"  Processing: {os.path.basename(event_file)}")
        
        # Load event file
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
        
        # Load data for each tag
        for tag in tags:
            # Clean up tag name for use as column name
            clean_tag = tag.replace('/', '_').replace(' ', '_')
            
            # Extract data
            if tag in ea.Tags()['scalars']:
                events = ea.Scalars(tag)
                data = [(e.wall_time, e.step, e.value) for e in events]
                df = pd.DataFrame(data, columns=['wall_time', 'step', 'value'])
                df['tag'] = tag
                df['clean_tag'] = clean_tag
                
                # Add to collection
                if clean_tag not in dfs:
                    dfs[clean_tag] = df
                else:
                    dfs[clean_tag] = pd.concat([dfs[clean_tag], df])
    
    # Sort each dataframe by step
    for tag in dfs:
        dfs[tag] = dfs[tag].sort_values('step')
    
    print(f"  Loaded {len(dfs)} metrics")
    return dfs


def extract_experiment_name(log_dir: str) -> str:
    """Extract experiment name from log directory path."""
    name = os.path.basename(log_dir)
    # Check for common patterns
    gamma_match = re.search(r'gamma_c_(\d+\.\d+)', log_dir)
    if gamma_match:
        return f"γ={gamma_match.group(1)}"
    return name


def smooth_data(data: pd.DataFrame, window: int = 10) -> pd.DataFrame:
    """Apply smoothing to data."""
    if len(data) <= window:
        return data
    
    smoothed = data.copy()
    smoothed['value'] = data['value'].rolling(window=window, min_periods=1).mean()
    return smoothed


def compare_runs(log_dirs: List[str], tags: List[str], output_dir: str, 
                 smooth_window: int = 10, figsize: Tuple[int, int] = (12, 8)):
    """
    Compare metrics across multiple runs.
    
    Args:
        log_dirs: List of log directories to compare
        tags: List of tags to plot
        output_dir: Directory to save plots
        smooth_window: Window size for smoothing
        figsize: Figure size
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Process each tag
    for tag in tags:
        print(f"Comparing runs for tag: {tag}")
        
        plt.figure(figsize=figsize)
        
        # Plot data from each run
        run_data = []
        for log_dir in log_dirs:
            try:
                # Load data
                dfs = load_tensorboard_data(log_dir)
                
                # Find matching tag
                matching_tags = [t for t in dfs.keys() if tag.lower() in t.lower()]
                if not matching_tags:
                    print(f"  Warning: Tag '{tag}' not found in {log_dir}")
                    continue
                
                best_match = matching_tags[0]
                data = dfs[best_match]
                
                # Apply smoothing
                smoothed = smooth_data(data, window=smooth_window)
                
                # Extract experiment name
                name = extract_experiment_name(log_dir)
                
                # Plot
                plt.plot(smoothed['step'], smoothed['value'], label=name)
                
                # Save for correlation analysis
                run_data.append({
                    'name': name,
                    'data': smoothed
                })
                
            except Exception as e:
                print(f"  Error processing {log_dir} for tag {tag}: {e}")
        
        if not run_data:
            print(f"  No data to plot for tag {tag}")
            plt.close()
            continue
        
        # Finalize plot
        plt.xlabel('Training Steps')
        plt.ylabel(tag.replace('_', ' ').title())
        plt.title(f'Comparison of {tag.replace("_", " ").title()} Across Runs')
        plt.legend()
        plt.grid(True)
        
        # Save plot
        output_file = os.path.join(output_dir, f"comparison_{tag.replace('/', '_')}.png")
        plt.savefig(output_file)
        plt.close()
        
        print(f"  Saved comparison to {output_file}")


def analyze_correlations(log_dir: str, tags: List[str], output_dir: str,
                         figsize: Tuple[int, int] = (12, 10)):
    """
    Analyze correlations between different metrics.
    
    Args:
        log_dir: Log directory to analyze
        tags: List of tags to include in correlation analysis
        output_dir: Directory to save plots
        figsize: Figure size
    """
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        # Load data
        dfs = load_tensorboard_data(log_dir)
        
        # Prepare data for correlation analysis
        correlation_data = {}
        common_steps = None
        
        for tag in tags:
            # Find matching tags
            matching_tags = [t for t in dfs.keys() if tag.lower() in t.lower()]
            if not matching_tags:
                print(f"  Warning: Tag '{tag}' not found in {log_dir}")
                continue
            
            best_match = matching_tags[0]
            data = dfs[best_match]
            
            # Store tag data
            correlation_data[tag] = data
            
            # Track common steps
            if common_steps is None:
                common_steps = set(data['step'])
            else:
                common_steps = common_steps.intersection(set(data['step']))
        
        if not correlation_data or not common_steps:
            print(f"Insufficient data for correlation analysis in {log_dir}")
            return
        
        # Filter data to common steps
        filtered_data = {}
        for tag, data in correlation_data.items():
            filtered_data[tag] = data[data['step'].isin(common_steps)]
        
        # Create correlation dataframe
        corr_df = pd.DataFrame({'step': sorted(common_steps)})
        for tag, data in filtered_data.items():
            merged = pd.merge(corr_df, data[['step', 'value']], on='step')
            corr_df[tag] = merged['value']
        
        # Calculate correlation matrix
        corr_matrix = corr_df.drop('step', axis=1).corr()
        
        # Plot correlation heatmap
        plt.figure(figsize=figsize)
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, 
                   center=0, linewidths=0.5, fmt='.2f')
        plt.title(f'Correlation Matrix of Metrics - {extract_experiment_name(log_dir)}')
        plt.tight_layout()
        
        # Save plot
        output_file = os.path.join(output_dir, f"correlation_matrix_{extract_experiment_name(log_dir)}.png")
        plt.savefig(output_file)
        plt.close()
        
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
            plt.figure(figsize=(8, 6))
            plt.scatter(corr_df[tag1], corr_df[tag2], alpha=0.5)
            
            # Add regression line
            sns.regplot(x=tag1, y=tag2, data=corr_df, scatter=False, color='red')
            
            plt.xlabel(tag1.replace('_', ' ').title())
            plt.ylabel(tag2.replace('_', ' ').title())
            plt.title(f'Correlation: {corr_value:.2f}')
            plt.grid(True)
            
            # Save plot
            output_file = os.path.join(output_dir, f"correlation_{tag1}_{tag2}.png")
            plt.savefig(output_file)
            plt.close()
    
    except Exception as e:
        print(f"Error during correlation analysis: {e}")


def create_multi_panel_dashboard(log_dirs: List[str], output_dir: str,
                                smooth_window: int = 10, figsize: Tuple[int, int] = (16, 12)):
    """
    Create a multi-panel dashboard with key metrics.
    
    Args:
        log_dirs: List of log directories to include
        output_dir: Directory to save the dashboard
        smooth_window: Window size for smoothing
        figsize: Figure size
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Define key metrics to include in dashboard
    key_metrics = [
        'rollout/ep_rew_mean',           # Episode reward
        'train/entropy_loss',            # Entropy loss
        'train/learning_rate',           # Learning rate
        'train/value_loss',              # Value loss
        'actions_refine_proportion',     # Refine proportion
        'actions_coarsen_proportion',    # Coarsen proportion
        'actions_no_change_proportion',  # No-change proportion
        'resources_usage',               # Resource usage
        'termination_budget_exceeded',   # Budget exceeded termination
        'termination_maximum_episode_steps_reached'  # Max steps termination
    ]
    
    # Set up figure and axes
    fig, axes = plt.subplots(3, 2, figsize=figsize)
    axes = axes.flatten()
    
    # Process each run
    run_data = {}
    for log_dir in log_dirs:
        try:
            # Load data
            dfs = load_tensorboard_data(log_dir)
            
            # Extract experiment name
            name = extract_experiment_name(log_dir)
            
            # Store data for this run
            run_data[name] = {}
            
            # Find data for each key metric
            for metric in key_metrics:
                matching_tags = [t for t in dfs.keys() if metric.lower() in t.lower()]
                if not matching_tags:
                    continue
                
                best_match = matching_tags[0]
                data = dfs[best_match]
                
                # Apply smoothing
                smoothed = smooth_data(data, window=smooth_window)
                
                # Store for plotting
                run_data[name][metric] = smoothed
        except Exception as e:
            print(f"Error processing {log_dir}: {e}")
    
    # Plot key metrics
    for i, metric in enumerate(key_metrics[:6]):  # Plot first 6 metrics (3x2 grid)
        ax = axes[i]
        
        # Plot each run
        for name, data in run_data.items():
            if metric in data:
                ax.plot(data[metric]['step'], data[metric]['value'], label=name)
        
        # Set labels and title
        ax.set_xlabel('Steps')
        ax.set_ylabel(metric.split('/')[-1].replace('_', ' ').title())
        ax.set_title(metric.split('/')[-1].replace('_', ' ').title())
        ax.grid(True)
        
        # Only add legend to first plot to avoid clutter
        if i == 0:
            ax.legend()
    
    # Adjust layout and save
    fig.tight_layout()
    output_file = os.path.join(output_dir, f"dashboard_metrics.png")
    plt.savefig(output_file)
    plt.close()
    
    print(f"Saved dashboard to {output_file}")
    
    # Create action distribution trend chart
    try:
        plt.figure(figsize=(12, 8))
        
        # Extract refine/coarsen/no-change proportions for each run
        for name, data in run_data.items():
            refine_key = next((k for k in data.keys() if 'refine_proportion' in k.lower()), None)
            coarsen_key = next((k for k in data.keys() if 'coarsen_proportion' in k.lower()), None)
            no_change_key = next((k for k in data.keys() if 'no_change_proportion' in k.lower()), None)
            
            # Plot trends if data available
            if refine_key and data[refine_key] is not None:
                plt.plot(data[refine_key]['step'], data[refine_key]['value'], 
                        label=f"{name} - Refine")
            
            if coarsen_key and data[coarsen_key] is not None:
                plt.plot(data[coarsen_key]['step'], data[coarsen_key]['value'], 
                        label=f"{name} - Coarsen", linestyle='--')
            
            if no_change_key and data[no_change_key] is not None:
                plt.plot(data[no_change_key]['step'], data[no_change_key]['value'], 
                        label=f"{name} - No Change", linestyle=':')
        
        plt.xlabel('Training Steps')
        plt.ylabel('Action Proportion')
        plt.title('Action Distribution Over Time')
        plt.legend()
        plt.grid(True)
        
        # Save plot
        output_file = os.path.join(output_dir, f"action_distribution_trend.png")
        plt.savefig(output_file)
        plt.close()
        
        print(f"Saved action distribution trend to {output_file}")
        
    except Exception as e:
        print(f"Error creating action distribution chart: {e}")


def main():
    """Main function for processing command line arguments."""
    parser = argparse.ArgumentParser(description="Analyze TensorBoard logs for AMR-RL experiments")
    parser.add_argument("--log-dirs", nargs="+", required=True, help="Directories containing TensorBoard logs")
    parser.add_argument("--output-dir", default="tensorboard_analysis", help="Directory to save analysis outputs")
    parser.add_argument("--tags", nargs="+", default=[
        "rollout/ep_rew_mean", "train/entropy_loss", "train/value_loss",
        "resources/usage", "actions/refine"
    ], help="Tags to analyze")
    parser.add_argument("--smooth", type=int, default=20, help="Window size for smoothing")
    parser.add_argument("--compare", action="store_true", help="Compare multiple runs")
    parser.add_argument("--correlations", action="store_true", help="Analyze correlations between metrics")
    parser.add_argument("--dashboard", action="store_true", help="Create multi-panel dashboard")
    
    args = parser.parse_args()
    
    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)
    
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
    if not (args.compare or args.correlations or args.dashboard):
        print("No specific analysis requested, performing all analyses.")
        compare_runs(args.log_dirs, args.tags, args.output_dir, args.smooth)
        for log_dir in args.log_dirs:
            analyze_correlations(log_dir, args.tags, args.output_dir)
        create_multi_panel_dashboard(args.log_dirs, args.output_dir, args.smooth)


if __name__ == "__main__":
    main()