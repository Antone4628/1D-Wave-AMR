#!/usr/bin/env python3
"""
Test script for enhanced callback updates.

Tests:
1. Parameter-based file naming
2. Structured data export (JSON/CSV)
3. Analysis metrics generation
4. PDF generation with parameter naming
5. Integration with existing training pipeline

Run this before deploying to a full parameter sweep.
"""

import os
import sys
import tempfile
import yaml
import json
import pandas as pd
from pathlib import Path

# Add project root and callbacks to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "numerical" / "callbacks"))

def create_test_config(test_dir: str) -> str:
    """Create a test configuration file."""
    config = {
        'environment': {
            'gamma_c': 25.0,
            'step_domain_fraction': 0.05,
            'rl_iterations_per_timestep': 10,
            'element_budget': 30,
            'max_episode_steps': 50,  # Short episodes for quick testing
            'max_consecutive_no_action': 30,
            'min_rl_iterations': 10,
            'max_rl_iterations': 10,
            'initial_refinement': {
                'mode': 'random',
                'probability': 0.7,
                'fixed_level': 2,
                'max_initial_level': 4
            }
        },
        'training': {
            'algorithm': 'A2C',
            'total_timesteps': 1000,  # Very short for testing
            'learning_rate': 0.0003,
            'n_steps': 5,
            'ent_coef': 0.01,
            'callback': 'enhanced'
        },
        'solver': {
            'initial_elements': [-1, -0.4, 0, 0.4, 1],
            'max_level': 8,
            'nop': 4,
            'courant_max': 0.1,
            'icase': 1,
            'balance': False,
            'verbose': False
        }
    }
    
    config_path = os.path.join(test_dir, "config.yaml")
    with open(config_path, 'w') as f:
        yaml.dump(config, f, default_flow_style=False)
    
    return config_path

def test_parameter_extraction():
    """Test parameter extraction and filename generation."""
    print("🧪 Testing parameter extraction and filename generation...")
    
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test config
        config_path = create_test_config(temp_dir)
        
        # Import the enhanced callback
        from enhanced_callback_data import EnhancedMonitorCallback
        
        # Create callback instance
        callback = EnhancedMonitorCallback(
            total_timesteps=1000,
            log_dir=temp_dir,
            verbose=1
        )
        
        # Test parameter extraction
        params = callback._extract_parameters_from_config()
        print(f"   ✓ Extracted parameters: {params}")
        
        # Test filename generation
        pdf_filename = callback._generate_parameter_based_filename("training_report", "pdf")
        json_filename = callback._generate_parameter_based_filename("training_metrics", "json")
        csv_filename = callback._generate_parameter_based_filename("training_summary", "csv")
        
        print(f"   ✓ PDF filename: {pdf_filename}")
        print(f"   ✓ JSON filename: {json_filename}")
        print(f"   ✓ CSV filename: {csv_filename}")
        
        # Verify filename format
        expected_pattern = "gamma_25.0_step_0.05_rl_10_budget_30_1k"
        assert expected_pattern in pdf_filename, f"PDF filename doesn't contain expected pattern: {pdf_filename}"
        assert expected_pattern in json_filename, f"JSON filename doesn't contain expected pattern: {json_filename}"
        assert expected_pattern in csv_filename, f"CSV filename doesn't contain expected pattern: {csv_filename}"
        
        print("   ✅ Parameter extraction and naming tests passed!")

def test_mock_training_run():
    """Test callback with mock training data."""
    print("🧪 Testing callback with mock training data...")
    
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test config
        config_path = create_test_config(temp_dir)
        
        # Import the enhanced callback
        from enhanced_callback_data import EnhancedMonitorCallback
        
        # Create callback instance
        callback = EnhancedMonitorCallback(
            total_timesteps=1000,
            log_dir=temp_dir,
            verbose=1
        )
        
        # Mock training start
        callback.training_start_time = 1234567890.0
        
        # Simulate some training data
        import numpy as np
        
        # Mock episode data
        callback.episode_rewards = list(np.random.normal(-500, 200, 20))  # 20 episodes
        callback.episodes_completed = 20
        callback.termination_reasons = {
            'Maximum episode steps reached': 15,
            'Budget exceeded': 5
        }
        
        # Mock action data
        for i in range(100):
            action = np.random.choice([-1, 0, 1])
            callback.action_history.append((i*10, action))
            callback.action_counts[action] += 1
        
        # Mock resource data
        for i in range(100):
            resource = min(1.0, max(0.0, np.random.normal(0.6, 0.2)))
            callback.resource_history.append((i*10, resource))
        
        # Mock do-nothing counter data
        for i in range(100):
            counter = max(0, int(np.random.normal(5, 3)))
            callback.do_nothing_history.append((i*10, counter))
        
        callback.max_do_nothing_per_episode = [max(0, int(np.random.normal(7, 4))) for _ in range(20)]
        
        # Mock training end
        callback.training_end_time = 1234567890.0 + 300  # 5 minutes later
        
        # Test structured data creation
        metrics = callback._create_analysis_metrics()
        print(f"   ✓ Generated {len(metrics)} analysis metrics")
        
        # Test structured data saving
        callback._save_structured_data()
        
        # Verify files were created
        files = os.listdir(temp_dir)
        json_files = [f for f in files if f.endswith('.json')]
        csv_files = [f for f in files if f.endswith('.csv')]
        
        assert len(json_files) == 1, f"Expected 1 JSON file, got {len(json_files)}"
        assert len(csv_files) == 1, f"Expected 1 CSV file, got {len(csv_files)}"
        
        print(f"   ✓ Created JSON file: {json_files[0]}")
        print(f"   ✓ Created CSV file: {csv_files[0]}")
        
        # Test JSON content
        json_path = os.path.join(temp_dir, json_files[0])
        with open(json_path, 'r') as f:
            json_data = json.load(f)
        
        required_keys = [
            'gamma_c', 'step_domain_fraction', 'rl_iterations_per_timestep', 'element_budget',
            'final_episode_reward_mean', 'convergence_score', 'budget_exceeded_percentage'
        ]
        
        for key in required_keys:
            assert key in json_data, f"Missing required key in JSON: {key}"
        
        print(f"   ✓ JSON contains all required keys: {required_keys}")
        
        # Test CSV content
        csv_path = os.path.join(temp_dir, csv_files[0])
        df = pd.read_csv(csv_path)
        
        assert len(df) == 1, f"Expected 1 row in CSV, got {len(df)}"
        assert 'gamma_c' in df.columns, "Missing gamma_c column in CSV"
        assert 'final_episode_reward_mean' in df.columns, "Missing final_episode_reward_mean column in CSV"
        
        print(f"   ✓ CSV has correct structure: {len(df.columns)} columns, {len(df)} rows")
        
        # Test PDF generation
        callback._create_final_report()
        
        pdf_files = [f for f in os.listdir(temp_dir) if f.endswith('.pdf')]
        assert len(pdf_files) == 1, f"Expected 1 PDF file, got {len(pdf_files)}"
        
        print(f"   ✓ Created PDF file: {pdf_files[0]}")
        
        print("   ✅ Mock training run tests passed!")

def test_integration_compatibility():
    """Test compatibility with existing training pipeline."""
    print("🧪 Testing integration compatibility...")
    
    try:
        # Test import compatibility
        from enhanced_callback_data import EnhancedMonitorCallback
        print("   ✓ Enhanced callback imports successfully")
        
        # Test that all expected methods exist
        required_methods = [
            '_on_training_start', '_on_step', '_on_episode_end', 'on_training_end',
            '_extract_parameters_from_config', '_generate_parameter_based_filename',
            '_create_analysis_metrics', '_save_structured_data'
        ]
        
        for method in required_methods:
            assert hasattr(EnhancedMonitorCallback, method), f"Missing method: {method}"
        
        print(f"   ✓ All required methods present: {required_methods}")
        
        # Test callback initialization
        with tempfile.TemporaryDirectory() as temp_dir:
            callback = EnhancedMonitorCallback(
                total_timesteps=1000,
                log_dir=temp_dir,
                verbose=0
            )
            
            # Test that new attributes are initialized
            assert hasattr(callback, 'action_history'), "Missing action_history attribute"
            assert hasattr(callback, 'resource_history'), "Missing resource_history attribute"
            assert hasattr(callback, 'do_nothing_history'), "Missing do_nothing_history attribute"
            
            print("   ✓ Callback initializes with all required attributes")
        
        print("   ✅ Integration compatibility tests passed!")
        
    except Exception as e:
        print(f"   ❌ Integration compatibility test failed: {e}")
        raise

def create_minimal_training_test():
    """Create a minimal training test script."""
    print("🧪 Creating minimal training test script...")
    
    test_script = """#!/usr/bin/env python3
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
"""
    
    script_path = "test_minimal_training.py"
    with open(script_path, 'w') as f:
        f.write(test_script)
    
    print(f"   ✓ Created minimal training test script: tests/{script_path}")
    print("   ℹ  Run this script to test the enhanced callback with actual training")
    
    return script_path

def main():
    """Run all tests."""
    print("🎯 Testing Enhanced Callback Updates")
    print("=" * 50)
    
    try:
        # Test 1: Parameter extraction and naming
        test_parameter_extraction()
        print()
        
        # Test 2: Mock training run
        test_mock_training_run()
        print()
        
        # Test 3: Integration compatibility
        test_integration_compatibility()
        print()
        
        # Test 4: Create minimal training test
        script_path = create_minimal_training_test()
        print()
        
        print("🎉 All tests passed!")
        print()
        print("📋 Next steps:")
        print(f"1. Run the minimal training test: cd tests && python {script_path}")
        print("2. If successful, deploy enhanced callback to HPC")
        print("3. Test with a small parameter sweep (2-3 jobs)")
        print("4. If successful, run full parameter sweep with extended training")
        
    except Exception as e:
        print(f"❌ Tests failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()