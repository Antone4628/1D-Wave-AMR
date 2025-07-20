#!/usr/bin/env python3
"""
Test Batch Animation System

Quick verification script to test the batch animation system with a small subset
of jobs before running the full 96-animation batch.

Usage:
    python test_batch_animations.py session3_100k_uniform [--local] [--count N]
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

# Get absolute path to project root
# PROJECT_ROOT = os.path.abspath(os.path.join(
#     os.path.dirname(__file__), 
#     '..',
#     '..'
# ))
# sys.path.append(PROJECT_ROOT)

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

class BatchAnimationTester:
    """Test the batch animation system with a small subset."""
    
    def __init__(self, sweep_name, local_run=False, test_count=2):
        """
        Initialize the tester.
        
        Args:
            sweep_name (str): Parameter sweep name
            local_run (bool): Run locally instead of SLURM
            test_count (int): Number of jobs to test per mode
        """
        self.sweep_name = sweep_name
        self.local_run = local_run
        self.test_count = test_count
        
        # Set up paths
        self.data_dir = os.path.join(PROJECT_ROOT, 'analysis', 'data', 'model_performance', sweep_name)
        self.batch_output_dir = os.path.join(self.data_dir, 'batch_analysis')
        self.jobs_dir = os.path.join(self.batch_output_dir, 'animation_jobs')
        self.slurm_dir = os.path.join(PROJECT_ROOT, 'slurm_scripts')
        
        # Scripts
        self.batch_runner = os.path.join(PROJECT_ROOT, 'batch_animation_runner.py')
        self.single_runner = os.path.join(PROJECT_ROOT, 'analysis', 'model_performance', 'run_single_animation.py')
    
    def test_job_generation(self):
        """Test job generation with limited count."""
        print(f"🧪 Testing job generation with {self.test_count} jobs per mode...")
        
        cmd = [
            'python', self.batch_runner, self.sweep_name,
            '--test-count', str(self.test_count),
            '--verbose'
        ]
        
        try:
            result = subprocess.run(cmd, cwd=PROJECT_ROOT, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ Job generation test passed")
                print(f"   Generated test job files in: {self.jobs_dir}")
                return True
            else:
                print(f"❌ Job generation test failed")
                print(f"   Error: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"❌ Job generation test failed with exception: {e}")
            return False
    
    def test_single_animation(self, mode='snapshot'):
        """Test single animation execution."""
        print(f"\n🧪 Testing single animation execution ({mode} mode)...")
        
        if self.local_run:
            # Run locally
            cmd = [
                'python', self.single_runner,
                '1', mode, self.sweep_name,
                '--verbose'
            ]
            
            try:
                result = subprocess.run(cmd, cwd=PROJECT_ROOT, capture_output=True, text=True, timeout=600)
                
                if result.returncode == 0:
                    print(f"✅ Single animation test passed")
                    print(f"   Output: {result.stdout.strip()}")
                    return True
                else:
                    print(f"❌ Single animation test failed")
                    print(f"   Error: {result.stderr}")
                    return False
                    
            except subprocess.TimeoutExpired:
                print(f"❌ Single animation test timed out")
                return False
            except Exception as e:
                print(f"❌ Single animation test failed with exception: {e}")
                return False
        else:
            # Submit test SLURM job
            slurm_script = os.path.join(self.slurm_dir, f'batch_animation_{mode}.slurm')
            
            if not os.path.exists(slurm_script):
                print(f"❌ SLURM script not found: {slurm_script}")
                return False
                
            # Submit single job for testing
            cmd = ['sbatch', '--array=1', slurm_script]
            
            try:
                result = subprocess.run(cmd, cwd=PROJECT_ROOT, capture_output=True, text=True)
                
                if result.returncode == 0:
                    job_id = result.stdout.strip().split()[-1]
                    print(f"✅ Test SLURM job submitted: {job_id}")
                    print(f"   Monitor with: squeue -j {job_id}")
                    print(f"   Check logs in: {self.jobs_dir}/slurm_logs/")
                    return True
                else:
                    print(f"❌ SLURM job submission failed")
                    print(f"   Error: {result.stderr}")
                    return False
                    
            except Exception as e:
                print(f"❌ SLURM job submission failed with exception: {e}")
                return False
    
    def verify_test_outputs(self):
        """Verify that test outputs were created."""
        print(f"\n🧪 Verifying test outputs...")
        
        found_outputs = []
        
        # Check for any PNG files in batch_analysis subdirectories
        for root, dirs, files in os.walk(self.batch_output_dir):
            for file in files:
                if file.endswith('.png'):
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, self.batch_output_dir)
                    file_size = os.path.getsize(full_path)
                    found_outputs.append((rel_path, file_size))
        
        if found_outputs:
            print(f"✅ Found {len(found_outputs)} test output files:")
            for rel_path, file_size in sorted(found_outputs):
                print(f"   {rel_path} ({file_size:,} bytes)")
            return True
        else:
            print(f"⚠️  No test output files found in {self.batch_output_dir}")
            return False
    
    def run(self):
        """Run complete test suite."""
        print(f"🚀 Batch Animation System Test")
        print(f"Sweep: {self.sweep_name}")
        print(f"Mode: {'Local execution' if self.local_run else 'SLURM submission'}")
        print(f"Test count: {self.test_count} jobs per mode")
        print(f"=" * 50)
        
        tests_passed = 0
        total_tests = 3
        
        # Test 1: Job generation
        if self.test_job_generation():
            tests_passed += 1
        
        # Test 2: Single animation (only if local_run)
        if self.local_run:
            if self.test_single_animation('snapshot'):
                tests_passed += 1
        else:
            # For SLURM, just test submission
            if self.test_single_animation('snapshot'):
                tests_passed += 1
        
        # Test 3: Output verification (only if local_run)
        if self.local_run:
            if self.verify_test_outputs():
                tests_passed += 1
        else:
            print(f"\n🔍 Output verification skipped for SLURM mode")
            print(f"   Check outputs manually after job completion")
            total_tests = 2  # Adjust total for SLURM mode
        
        print(f"\n📊 Test Results: {tests_passed}/{total_tests} tests passed")
        
        if tests_passed == total_tests:
            print(f"✅ All tests passed! System ready for full batch run.")
            if not self.local_run:
                print(f"\n🔥 Ready to submit full batch:")
                for mode in ['snapshot', 'final']:
                    script_file = f"batch_animation_{mode}.slurm"
                    print(f"   sbatch slurm_scripts/{script_file}")
        else:
            print(f"❌ Some tests failed. Please investigate before running full batch.")
            
        return tests_passed == total_tests


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='Test batch animation system')
    parser.add_argument('sweep_name', help='Parameter sweep name')
    parser.add_argument('--local', action='store_true', help='Run test locally instead of submitting to SLURM')
    parser.add_argument('--count', type=int, default=2, help='Number of jobs to test per mode (default: 2)')
    
    args = parser.parse_args()
    
    try:
        tester = BatchAnimationTester(
            sweep_name=args.sweep_name,
            local_run=args.local,
            test_count=args.count
        )
        success = tester.run()
        sys.exit(0 if success else 1)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()