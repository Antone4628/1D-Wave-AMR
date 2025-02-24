"""
Callbacks for DG AMR training monitoring and checkpointing.
"""

import os
import numpy as np
from stable_baselines3.common.callbacks import BaseCallback
from .utils.logger import TrainingLogger


class CheckpointCallback(BaseCallback):
    """Callback for model checkpointing and logging."""
    
    def __init__(
        self,
        save_freq: int,
        save_path: str,
        training_logger: TrainingLogger,  # Changed from logger to training_logger
        name_prefix: str = "model",
        verbose: int = 1,
    ):
        super().__init__(verbose)
        self.save_freq = save_freq
        self.save_path = save_path
        self.training_logger = training_logger  # Store as training_logger instead of logger
        self.name_prefix = name_prefix
        
    def _init_callback(self):
        if self.save_path is not None:
            os.makedirs(self.save_path, exist_ok=True)

    def _on_step(self) -> bool:
        if self.n_calls % self.save_freq == 0:
            model_path = os.path.join(
                self.save_path, 
                f"{self.name_prefix}_{self.n_calls}_steps.zip"
            )
            self.model.save(model_path)
            
            # Log metrics
            self.training_logger.log_metrics({
                "timesteps": self.n_calls,
                "mean_reward": float(np.mean(self.model.ep_info_buffer)),
                "checkpoint_path": model_path
            })
            
            if self.verbose > 1:
                print(f"Saved model checkpoint to {model_path}")
        return True

class MetricsCallback(BaseCallback):
    """Callback for tracking and logging training metrics."""
    
    def __init__(self, training_logger: TrainingLogger, log_freq: int = 100):  # Changed here too
        super().__init__()
        self.training_logger = training_logger  # And here
        self.log_freq = log_freq
        
    def _on_step(self) -> bool:
        if self.n_calls % self.log_freq == 0:
            self.training_logger.log_metrics({  # And here
                "timesteps": self.n_calls,
                "mean_reward": float(np.mean(self.model.ep_info_buffer)),
                "episodes": len(self.model.ep_info_buffer)
            })
        return True
    
