#!/usr/bin/env python3
'''
Minimal training test to validate enhanced callback in real environment.
Run this for 1-2 minutes to verify everything works before full deployment.
'''

import os
import sys
import yaml
import tempfile
from pathlib import Path

# Add project paths
project_root = Path(__file__).parent.parent  # tests/ -> 1D-Wave-AMR/
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "experiments"))
sys.path.insert(0, str(project_root / "callbacks"))

def main():
    print("🚀 Running minimal training test with enhanced callback...")
    
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"Test directory: {temp_dir}")
        
        # Create minimal config
        config = {
            'environment': {
                'gamma_c': 50.0,
                'step_domain_fraction': 0.1,
                'rl_iterations_per_timestep': 10,
                'element_budget': 25,
                'max_episode_steps': 20,  # Very short episodes
                'max_consecutive_no_action': 30,
                'min_rl_iterations': 10,
                'max_rl_iterations': 10
            },
            'training': {
                'algorithm': 'A2C',
                'total_timesteps': 200,  # Very short training
                'learning_rate': 0.0003,
                'n_steps': 5,
                'ent_coef': 0.01,
                'callback': 'enhanced'
            }
        }
        
        config_path = os.path.join(temp_dir, "config.yaml")
        with open(config_path, 'w') as f:
            yaml.dump(config, f)
        
        print("✓ Created test config")
        
        # Import and run minimal training
        try:
            from run_experiments_mixed_gpu import main as run_training
            
            # Override sys.argv for the training script
            original_argv = sys.argv
            sys.argv = [
                'run_experiments_mixed_gpu.py',
                '--config', config_path,
                '--results-dir', temp_dir,
                '--no-timestamp',
                '--device', 'cpu',  # Force CPU for compatibility
                '--verbose'
            ]
            
            print("🏃 Starting minimal training run...")
            run_training()
            
            # Restore original argv
            sys.argv = original_argv
            
            print("✅ Training completed successfully!")
            
            # Check outputs
            files = os.listdir(temp_dir)
            print(f"Generated files: {files}")
            
            # Verify expected files
            expected_extensions = ['.json', '.csv', '.pdf', '.yaml']
            for ext in expected_extensions:
                matching_files = [f for f in files if f.endswith(ext)]
                if matching_files:
                    print(f"✓ Found {ext} file: {matching_files[0]}")
                else:
                    print(f"⚠ No {ext} file found")
            
        except Exception as e:
            print(f"❌ Training test failed: {e}")
            import traceback
            traceback.print_exc()
            sys.argv = original_argv
            raise

if __name__ == "__main__":
    main()
