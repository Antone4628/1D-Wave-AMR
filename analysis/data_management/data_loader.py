#!/usr/bin/env python3
"""
Data Loader for AMR Parameter Analysis
Loads and validates JSON training metrics from parameter sweeps.
"""

import json
import pandas as pd
from pathlib import Path
import numpy as np
import re
import os
from typing import Dict, List, Tuple, Optional
import sys

# Add utilities to path
# sys.path.append(str(Path(__file__).parent.parent / "utilities"))
# from utilities.config import RAW_DATA_DIR, PROCESSED_DATA_DIR, PARAMETER_SPACE

# Get absolute path to project root using established pattern
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 
    '..',  # Go up to analysis/
    '..'   # Go up to main project root (1D_wave_AMR/)
))
sys.path.append(PROJECT_ROOT)
from analysis.utilities.config import RAW_DATA_DIR, PROCESSED_DATA_DIR, PARAMETER_SPACE

class ParameterSweepLoader:
    """Load and process parameter sweep data"""
    
    def __init__(self, sweep_name: str):
        self.sweep_name = sweep_name
        self.raw_data_path = Path(RAW_DATA_DIR) / sweep_name
        self.processed_data_path = Path(PROCESSED_DATA_DIR) / sweep_name
        
        # Ensure processed directory exists
        self.processed_data_path.mkdir(parents=True, exist_ok=True)
        
        self.parameter_combinations = []
        self.metrics_data = {}
        
    def discover_parameter_combinations(self) -> List[Dict]:
        """Discover all parameter combinations from directory structure"""
        
        if not self.raw_data_path.exists():
            raise FileNotFoundError(f"Raw data path not found: {self.raw_data_path}")
        
        # Find all parameter directories
        param_dirs = list(self.raw_data_path.glob("gamma_*_step_*_rl_*_budget_*"))
        
        combinations = []
        for param_dir in param_dirs:
            # Parse parameters from directory name
            params = self._parse_parameters_from_dirname(param_dir.name)
            if params:
                params['directory'] = param_dir
                combinations.append(params)
        
        self.parameter_combinations = sorted(combinations, key=lambda x: (
            x['gamma_c'], x['step_domain_fraction'], 
            x['rl_iterations_per_timestep'], x['element_budget']
        ))
        
        print(f"Discovered {len(self.parameter_combinations)} parameter combinations")
        return self.parameter_combinations
    
    def _parse_parameters_from_dirname(self, dirname: str) -> Optional[Dict]:
        """Parse parameters from directory name like gamma_25.0_step_0.025_rl_10_budget_25"""
        
        pattern = r"gamma_([0-9.]+)_step_([0-9.]+)_rl_([0-9]+)_budget_([0-9]+)"
        match = re.match(pattern, dirname)
        
        if match:
            return {
                'gamma_c': float(match.group(1)),
                'step_domain_fraction': float(match.group(2)),
                'rl_iterations_per_timestep': int(match.group(3)),
                'element_budget': int(match.group(4)),
                'dirname': dirname
            }
        return None
    
    def load_json_metrics(self, validate=True) -> Dict:
        """Load all JSON training metrics"""
        
        if not self.parameter_combinations:
            self.discover_parameter_combinations()
        
        metrics_data = {}
        failed_loads = []
        
        for params in self.parameter_combinations:
            param_dir = params['directory']
            
            # Find JSON files in this directory
            json_files = list(param_dir.glob("*_training_metrics.json"))
            
            if not json_files:
                failed_loads.append(f"No JSON file in {param_dir.name}")
                continue
            
            if len(json_files) > 1:
                print(f"⚠️ Multiple JSON files in {param_dir.name}, using first: {json_files[0].name}")
            
            json_file = json_files[0]
            
            try:
                with open(json_file, 'r') as f:
                    metrics = json.load(f)
                
                # Add parameter info to metrics
                param_key = self._get_parameter_key(params)
                metrics['parameters'] = params.copy()
                metrics['parameters'].pop('directory', None)  # Remove path object
                
                metrics_data[param_key] = metrics
                
            except Exception as e:
                failed_loads.append(f"Failed to load {json_file}: {e}")
        
        print(f"✅ Loaded {len(metrics_data)} parameter combinations")
        if failed_loads:
            print(f"⚠️ Failed loads: {len(failed_loads)}")
            for failure in failed_loads:
                print(f"  - {failure}")
        
        self.metrics_data = metrics_data
        
        if validate:
            self._validate_metrics_data()
        
        return metrics_data
    
    def _get_parameter_key(self, params: Dict) -> str:
        """Generate unique key for parameter combination"""
        return f"g{params['gamma_c']}_s{params['step_domain_fraction']}_r{params['rl_iterations_per_timestep']}_b{params['element_budget']}"
    
    def _validate_metrics_data(self):
        """Validate loaded metrics data"""
        
        if not self.metrics_data:
            print("⚠️ No metrics data to validate")
            return
        
        # Check consistency of metrics across all combinations
        all_keys = set()
        for combo_data in self.metrics_data.values():
            all_keys.update(combo_data.keys())
        
        # Remove 'parameters' from analysis
        metric_keys = all_keys - {'parameters'}
        
        print(f"📊 Validation Results:")
        print(f"Total parameter combinations: {len(self.metrics_data)}")
        print(f"Unique metrics per combination: {len(metric_keys)}")
        
        # Check for missing metrics
        missing_metrics = {}
        for param_key, combo_data in self.metrics_data.items():
            missing = metric_keys - set(combo_data.keys())
            if missing:
                missing_metrics[param_key] = missing
        
        if missing_metrics:
            print(f"⚠️ Combinations with missing metrics: {len(missing_metrics)}")
            for param_key, missing in list(missing_metrics.items())[:3]:  # Show first 3
                print(f"  - {param_key}: missing {len(missing)} metrics")
        else:
            print("✅ All combinations have consistent metrics")
        
        # Sample some key metrics
        sample_metrics = ['final_episode_reward_mean', 'convergence_score', 
                         'episodes_completed', 'training_duration_hours']
        available_sample = [m for m in sample_metrics if m in metric_keys]
        
        if available_sample:
            print(f"\\n📈 Sample metrics overview:")
            for metric in available_sample[:4]:
                values = [combo_data.get(metric) for combo_data in self.metrics_data.values()]
                values = [v for v in values if v is not None]
                if values:
                    print(f"  - {metric}: {np.mean(values):.3f} ± {np.std(values):.3f} (n={len(values)})")
    
    def to_dataframe(self) -> pd.DataFrame:
        """Convert metrics data to pandas DataFrame for analysis"""
        
        if not self.metrics_data:
            self.load_json_metrics()
        
        rows = []
        for param_key, combo_data in self.metrics_data.items():
            row = combo_data['parameters'].copy()
            
            # Add all metrics except parameters
            for key, value in combo_data.items():
                if key != 'parameters':
                    row[key] = value
            
            row['parameter_key'] = param_key
            rows.append(row)
        
        df = pd.DataFrame(rows)
        
        # Ensure parameter columns are first
        param_cols = ['parameter_key', 'gamma_c', 'step_domain_fraction', 
                     'rl_iterations_per_timestep', 'element_budget']
        other_cols = [col for col in df.columns if col not in param_cols]
        df = df[param_cols + other_cols]
        
        print(f"📊 DataFrame created: {df.shape[0]} rows × {df.shape[1]} columns")
        return df
    
    def save_processed_data(self, df: pd.DataFrame = None):
        """Save processed data for quick loading"""
        
        if df is None:
            df = self.to_dataframe()
        
        # Save as both CSV and pickle for different use cases
        csv_path = self.processed_data_path / "combined_metrics.csv"
        pickle_path = self.processed_data_path / "combined_metrics.pkl"
        
        df.to_csv(csv_path, index=False)
        df.to_pickle(pickle_path)
        
        print(f"💾 Saved processed data:")
        print(f"  - CSV: {csv_path}")
        print(f"  - Pickle: {pickle_path}")
        
        return csv_path, pickle_path

def quick_load_sweep(sweep_name: str) -> pd.DataFrame:
    """Quick load processed sweep data if available"""
    
    processed_path = Path(PROCESSED_DATA_DIR) / sweep_name / "combined_metrics.pkl"
    
    if processed_path.exists():
        print(f"Loading processed data from {processed_path}")
        return pd.read_pickle(processed_path)
    else:
        print(f"Processed data not found, loading from raw JSON files...")
        loader = ParameterSweepLoader(sweep_name)
        df = loader.to_dataframe()
        loader.save_processed_data(df)
        return df

if __name__ == "__main__":
    import sys
    
    # Use command line argument or default
    if len(sys.argv) > 1:
        sweep_name = sys.argv[1]
    else:
        sweep_name = "full_param_sweep_data_20250601_105453"
    
    print(f"Loading parameter sweep: {sweep_name}")
    
    # Initialize loader
    loader = ParameterSweepLoader(sweep_name)
    
    # Load and process data
    df = loader.to_dataframe()
    
    # Save processed data
    loader.save_processed_data(df)
    
    print(f"\n📋 Data summary:")
    print(f"Shape: {df.shape}")
    print(f"Parameters: {df[['gamma_c', 'step_domain_fraction', 'rl_iterations_per_timestep', 'element_budget']].nunique()}")