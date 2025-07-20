
#!/usr/bin/env python3
"""Debug script to verify path calculations."""

import os

print("=== Path Debug Information ===")
print(f"__file__ = {__file__}")
print(f"os.path.dirname(__file__) = {os.path.dirname(__file__)}")
print(f"os.path.abspath(__file__) = {os.path.abspath(__file__)}")
print(f"os.path.abspath(os.path.dirname(__file__)) = {os.path.abspath(os.path.dirname(__file__))}")

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
print(f"PROJECT_ROOT = {PROJECT_ROOT}")

# Check for expected files
expected_files = [
    'batch_animation_runner.py',
    'test_batch_animations.py', 
    'analysis/model_performance/single_model_runner_batch.py',
    'analysis/data/model_performance/session3_100k_uniform/aggregate_results/lowest_cost_models_cleaned.csv'
]

for file_path in expected_files:
    full_path = os.path.join(PROJECT_ROOT, file_path)
    exists = os.path.exists(full_path)
    print(f"{'✅' if exists else '❌'} {file_path}: {full_path}")

print(f"\nCurrent working directory: {os.getcwd()}")