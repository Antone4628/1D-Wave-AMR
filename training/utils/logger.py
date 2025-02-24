"""
Logging utilities for DG AMR training.
"""

import os
import json
import logging
from typing import Dict, Any

class TrainingLogger:
    """Custom logging for training progress and metrics."""
    
    def __init__(self, log_dir: str):
        self.log_dir = log_dir
        os.makedirs(log_dir, exist_ok=True)
        
        # Set up logging
        self.logger = logging.getLogger('dgamr_training')
        self.logger.setLevel(logging.INFO)
        
        # File handler
        fh = logging.FileHandler(os.path.join(log_dir, 'training.log'))
        fh.setLevel(logging.INFO)
        
        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        
        # Formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        
    def log_metrics(self, metrics: Dict[str, Any]):
        """Log training metrics."""
        self.logger.info(f"Training metrics: {metrics}")
        
        # Save metrics to JSON
        metrics_file = os.path.join(self.log_dir, 'metrics.jsonl')
        with open(metrics_file, 'a') as f:
            f.write(json.dumps(metrics) + '\n')
            
    def log_config(self, config: Dict[str, Any]):
        """Log training configuration."""
        self.logger.info(f"Training config: {config}")