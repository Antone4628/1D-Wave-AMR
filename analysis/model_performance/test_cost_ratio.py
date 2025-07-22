#!/usr/bin/env python3
"""
Test script to validate cost ratio implementation
"""

import sys
import os

# Add project root to path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(PROJECT_ROOT)

from single_model_runner import run_single_model

def test_cost_ratio():
    """Test cost ratio calculation with a single model"""
    
    # Use the first model from session3_100k_uniform
    models_dir = os.path.join(PROJECT_ROOT, 'analysis', 'data', 'models', 'session3_100k_uniform')
    model_dirs = sorted([d for d in os.listdir(models_dir) if d.startswith('gamma_')])
    
    if not model_dirs:
        print("ERROR: No models found in session3_100k_uniform")
        return False
    
    # Test with first model
    model_dir = model_dirs[0]
    model_path = os.path.join(models_dir, model_dir, 'final_model.zip')
    
    print(f"Testing with model: {model_dir}")
    print(f"Model path: {model_path}")
    
    # Test parameters
    initial_refinement = 4
    element_budget = 50
    max_level = 4
    
    print(f"\nTest parameters:")
    print(f"  initial_refinement: {initial_refinement}")
    print(f"  element_budget: {element_budget}")
    print(f"  max_level: {max_level}")
    
    # Run evaluation
    try:
        results = run_single_model(
            model_path=model_path,
            time_final=1.0,
            element_budget=element_budget,
            max_level=max_level,
            nop=4,
            courant_max=0.1,
            icase=1,
            plot_mode=None,
            include_exact=False,
            verbose=False,
            output_dir=None,
            initial_refinement=initial_refinement
        )
        
        # Print results
        print(f"\n=== COST RATIO TEST RESULTS ===")
        print(f"Initial elements: {results['simulation_metrics']['initial_elements']}")
        print(f"Total timesteps: {results['simulation_metrics']['total_timesteps']}")
        print(f"Calculated timesteps: {results['simulation_metrics']['number_of_timesteps']}")
        print(f"Total cost: {results['total_cost']}")
        print(f"No-AMR baseline cost: {results['simulation_metrics']['no_amr_baseline_cost']}")
        print(f"Cost ratio: {results['simulation_metrics']['cost_ratio']:.4f}")
        
        # Validation checks
        cost_ratio = results['simulation_metrics']['cost_ratio']
        if cost_ratio > 1.0:
            print(f"❌ VALIDATION FAILED: Cost ratio {cost_ratio:.4f} > 1.0")
            return False
        elif cost_ratio < 0.1:
            print(f"⚠️  WARNING: Cost ratio {cost_ratio:.4f} seems very low")
        else:
            print(f"✅ VALIDATION PASSED: Cost ratio {cost_ratio:.4f} is reasonable")
        
        print(f"Final L2 error: {results['final_l2_error']:.6e}")
        print(f"Grid-normalized L2 error: {results['grid_normalized_l2_error']:.6e}")
        
        return True
        
    except Exception as e:
        print(f"❌ ERROR during evaluation: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_cost_ratio()
    if success:
        print(f"\n🎉 Cost ratio implementation test PASSED!")
    else:
        print(f"\n💥 Cost ratio implementation test FAILED!")
        sys.exit(1)