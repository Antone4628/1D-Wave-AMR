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


def list_available_tags(log_dir):
    """Print all available tags in the log directory."""
    dfs = load_tensorboard_data(log_dir)
    print("\nAvailable tags in", log_dir)
    for tag in sorted(dfs.keys()):
        print(f"  - {tag}")
    print("\n")


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
            figures.pop()  # Remove the empty figure
            continue
        
        # Finalize plot
        plt.xlabel('Training Steps')
        plt.ylabel(tag.replace('_', ' ').title())
        plt.title(f'Comparison of {tag.replace("_", " ").title()} Across Runs')
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
            return figures
        
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
            
            plt.xlabel(tag1.replace('_', ' ').title())
            plt.ylabel(tag2.replace('_', ' ').title())
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
    dashboard_fig, axes = plt.subplots(3, 2, figsize=figsize)
    figures.append(dashboard_fig)
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
        
        # Save to PDF if provided
        if pdf is not None:
            pdf.savefig(action_fig)
            
        # Save plot to file
        output_file = os.path.join(output_dir, f"action_distribution_trend.png")
        plt.savefig(output_file)
        print(f"Saved action distribution trend to {output_file}")
        
    except Exception as e:
        print(f"Error creating action distribution chart: {e}")
        if action_fig in figures:
            figures.remove(action_fig)
    
    return figures


def create_comprehensive_report(log_dirs: List[str], tags: List[str], output_dir: str, 
                              smooth_window: int = 10, figsize: Tuple[int, int] = (12, 8)):
    """
    Create a comprehensive PDF report with all analyses.
    
    Args:
        log_dirs: List of log directories to analyze
        tags: List of tags to include in analysis
        output_dir: Directory to save the report
        smooth_window: Window size for smoothing
        figsize: Default figure size
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Define report path
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = os.path.join(output_dir, f"tensorboard_analysis_report_{timestamp}.pdf")
    
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
                dfs = load_tensorboard_data(log_dir)
                exp_name = extract_experiment_name(log_dir)
                
                plt.text(0.5, y_position, f"Experiment: {exp_name}", fontsize=16, ha='center', weight='bold')
                y_position -= 0.03
                
                # Try to extract key statistics
                stats_text = []
                
                # Episode rewards
                try:
                    reward_tag = next((t for t in dfs.keys() if 'ep_rew_mean' in t.lower()), None)
                    if reward_tag:
                        rewards = dfs[reward_tag]['value']
                        stats_text.append(f"Mean Reward: {rewards.mean():.2f}")
                        stats_text.append(f"Min Reward: {rewards.min():.2f}")
                        stats_text.append(f"Max Reward: {rewards.max():.2f}")
                        
                        # Last 20% of rewards
                        last_n = max(1, int(len(rewards) * 0.2))
                        last_rewards = rewards.tail(last_n)
                        stats_text.append(f"Final 20% Mean Reward: {last_rewards.mean():.2f}")
                except Exception as e:
                    print(f"Error extracting reward stats: {e}")
                
                # Episode lengths
                try:
                    length_tag = next((t for t in dfs.keys() if 'ep_len_mean' in t.lower()), None)
                    if length_tag:
                        lengths = dfs[length_tag]['value']
                        stats_text.append(f"Mean Episode Length: {lengths.mean():.1f}")
                except Exception as e:
                    print(f"Error extracting length stats: {e}")
                
                # Action distributions
                try:
                    action_tags = {
                        'Refine': next((t for t in dfs.keys() if 'refine_proportion' in t.lower()), None),
                        'Coarsen': next((t for t in dfs.keys() if 'coarsen_proportion' in t.lower()), None),
                        'No Change': next((t for t in dfs.keys() if 'no_change_proportion' in t.lower()), None)
                    }
                    
                    action_stats = []
                    for action, tag in action_tags.items():
                        if tag and tag in dfs:
                            # Get the last value as the final proportion
                            final_value = dfs[tag]['value'].iloc[-1]
                            action_stats.append(f"{action}: {final_value:.1%}")
                    
                    if action_stats:
                        stats_text.append("Final Action Distribution:")
                        stats_text.extend(action_stats)
                except Exception as e:
                    print(f"Error extracting action stats: {e}")
                
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
            
            pdf.savefig(summary_fig)
            plt.close()
        except Exception as e:
            print(f"Error creating summary page: {e}")
        
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
    
    return config


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
    parser.add_argument("--list-tags", action="store_true", help="List all available tags in the log directories")
    parser.add_argument("--report", action="store_true", help="Create comprehensive PDF report with all analyses")

    args = parser.parse_args()
    
    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)

    # List tags if requested
    if args.list_tags:
        for log_dir in args.log_dirs:
            list_available_tags(log_dir)
        return
    
    # Create comprehensive report if requested
    if args.report:
        create_comprehensive_report(args.log_dirs, args.tags, args.output_dir, args.smooth)
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
    if not (args.compare or args.correlations or args.dashboard or args.report):
        print("No specific analysis requested, performing all analyses.")
        
        # Create comprehensive report by default
        create_comprehensive_report(args.log_dirs, args.tags, args.output_dir, args.smooth)


if __name__ == "__main__":
    main()