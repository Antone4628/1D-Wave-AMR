#!/usr/bin/env python3
"""
Debug what commands the script is actually building
"""

from pathlib import Path

# Simulate the script's command construction
hpc_path = "antonechacartegu@borah-login:/bsuhome/antonechacartegu/projects/drl-amr/1D-Wave-AMR/results/session3_100k_uniform"
combo_name = "gamma_50.0_step_0.025_rl_10_budget_25"
local_raw_path = Path("analysis/data/raw/session3_100k_uniform")
local_combo_dir = local_raw_path / combo_name

# Exactly how the script builds the commands
json_source = f"{hpc_path}/{combo_name}/{combo_name}_100k_training_metrics.json"
json_dest = str(local_combo_dir / f"{combo_name}_100k_training_metrics.json")

csv_source = f"{hpc_path}/{combo_name}/{combo_name}_100k_training_summary.csv"
csv_dest = str(local_combo_dir / f"{combo_name}_100k_training_summary.csv")

json_cmd = f"rsync -avz '{json_source}' '{json_dest}'"
csv_cmd = f"rsync -avz '{csv_source}' '{csv_dest}'"

print("=== SCRIPT COMMAND CONSTRUCTION DEBUG ===")
print(f"JSON command that script would run:")
print(f"  {json_cmd}")
print()
print(f"CSV command that script would run:")  
print(f"  {csv_cmd}")
print()
print("=== WORKING MANUAL COMMANDS ===")
print("JSON manual command that worked:")
print("  rsync -avz --progress 'antonechacartegu@borah-login:/bsuhome/antonechacartegu/projects/drl-amr/1D-Wave-AMR/results/session3_100k_uniform/gamma_50.0_step_0.025_rl_10_budget_25/gamma_50.0_step_0.025_rl_10_budget_25_100k_training_metrics.json' ./test_manual_transfer.json")
print()
print("CSV manual command that worked:")
print("  rsync -avz --progress 'antonechacartegu@borah-login:/bsuhome/antonechacartegu/projects/drl-amr/1D-Wave-AMR/results/session3_100k_uniform/gamma_50.0_step_0.025_rl_10_budget_25/gamma_50.0_step_0.025_rl_10_budget_25_100k_training_summary.csv' ./test_csv_transfer.csv")
print()
print("=== COMPARISON ===")
print("Key differences to check:")
print("1. Does the script build the correct paths?")
print("2. Are the destination directories created?")
print("3. Are there quoting/escaping differences?")
print()
print(f"Local destination directory exists? {local_combo_dir.exists()}")
print(f"Local destination directory: {local_combo_dir}")

# Test if we need to create the directory
if not local_combo_dir.exists():
    print("  -> Directory needs to be created")
    local_combo_dir.mkdir(parents=True, exist_ok=True)
    print(f"  -> Created: {local_combo_dir}")
print()
print("=== TEST THESE SCRIPT-EQUIVALENT COMMANDS ===")
print("Run these to test if the script's exact commands work:")
print()
print(f"# Create directory first:")
print(f"mkdir -p '{local_combo_dir}'")
print()
print(f"# JSON transfer (script equivalent):")
print(f"{json_cmd}")
print()
print(f"# CSV transfer (script equivalent):")  
print(f"{csv_cmd}")
print()
print("If these work manually, then the issue is in subprocess execution.")