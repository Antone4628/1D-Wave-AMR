#!/usr/bin/env python3
"""
Robust Model Transfer Command Generator with Resume Capability
Handles connection timeouts and can resume interrupted transfers.

Usage:
1. Update CONFIGURATION section for your specific sweep
2. Run: python3 generate_robust_model_transfer.py
3. Execute: bash robust_transfer_commands.sh
"""

import itertools
import os

# ====================================================================
# CONFIGURATION - Update these for each parameter sweep
# ====================================================================

# HPC Configuration
HPC_USERNAME = "antonechacartegu"
HPC_HOSTNAME = "borah-login.boisestate.edu"
HPC_PROJECT_ROOT = "projects/drl-amr/1D-Wave-AMR"

# Parameter Sweep Identifier
SWEEP_NAME = "full_param_sweep_data_20250601_105453"

# Local Configuration  
LOCAL_BASE_PATH = "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred"
LOCAL_SWEEP_DIR = "full_sweep_data_20250601"

# Parameter Space Definition
GAMMA_C_VALUES = [25.0, 50.0, 100.0]
STEP_DOMAIN_VALUES = [0.025, 0.05, 0.1]
RL_ITERATIONS_VALUES = [10, 25, 40]
ELEMENT_BUDGET_VALUES = [25, 30, 40]

# File to transfer
TARGET_FILE = "final_model.zip"

# Transfer Configuration
BATCH_SIZE = 10          # Transfer in smaller batches
RETRY_ATTEMPTS = 3       # Retry failed transfers
DELAY_BETWEEN_BATCHES = 2 # Seconds to wait between batches

# ====================================================================
# SCRIPT LOGIC
# ====================================================================

def generate_parameter_combinations():
    """Generate all parameter combinations."""
    return list(itertools.product(
        GAMMA_C_VALUES,
        STEP_DOMAIN_VALUES, 
        RL_ITERATIONS_VALUES,
        ELEMENT_BUDGET_VALUES
    ))

def format_directory_name(gamma_c, step_domain, rl_iterations, element_budget):
    """Format the directory name based on parameters."""
    return f"gamma_{gamma_c}_step_{step_domain}_rl_{rl_iterations}_budget_{element_budget}"

def format_filename(gamma_c, step_domain, rl_iterations, element_budget):
    """Format the local filename with parameters."""
    return f"gamma_{gamma_c}_step_{step_domain}_rl_{rl_iterations}_budget_{element_budget}_{TARGET_FILE}"

def generate_scp_command(gamma_c, step_domain, rl_iterations, element_budget):
    """Generate a single scp command with retry logic."""
    
    # Source path on HPC
    dir_name = format_directory_name(gamma_c, step_domain, rl_iterations, element_budget)
    hpc_path = f"{HPC_USERNAME}@{HPC_HOSTNAME}:{HPC_PROJECT_ROOT}/results/{SWEEP_NAME}/{dir_name}/{TARGET_FILE}"
    
    # Destination path on local machine
    local_filename = format_filename(gamma_c, step_domain, rl_iterations, element_budget)
    local_path = f"{LOCAL_BASE_PATH}/{LOCAL_SWEEP_DIR}/{local_filename}"
    
    return hpc_path, local_path, local_filename

def generate_robust_script():
    """Generate robust transfer script with resume capability."""
    
    combinations = generate_parameter_combinations()
    total_combinations = len(combinations)
    
    print(f"Generating robust transfer script for {total_combinations} parameter combinations...")
    print(f"Features: Resume capability, batch processing, retry logic")
    print()
    
    script_lines = [
        "#!/bin/bash",
        "# Robust Model Transfer Script with Resume Capability",
        f"# Generated for parameter sweep: {SWEEP_NAME}",
        f"# Total combinations: {total_combinations}",
        "",
        "# Configuration",
        f"LOCAL_DIR='{LOCAL_BASE_PATH}/{LOCAL_SWEEP_DIR}'",
        f"RETRY_ATTEMPTS={RETRY_ATTEMPTS}",
        f"BATCH_SIZE={BATCH_SIZE}",
        f"DELAY_BETWEEN_BATCHES={DELAY_BETWEEN_BATCHES}",
        "",
        "# Create destination directory",
        "mkdir -p \"$LOCAL_DIR\"",
        "",
        "# Function to check if file already exists and has reasonable size",
        "file_exists_and_valid() {",
        "    local file=\"$1\"",
        "    if [[ -f \"$file\" && $(stat -f%z \"$file\" 2>/dev/null || stat -c%s \"$file\" 2>/dev/null) -gt 1000 ]]; then",
        "        return 0  # File exists and is > 1KB",
        "    else",
        "        return 1  # File missing or too small",
        "    fi",
        "}",
        "",
        "# Function to transfer with retry",
        "transfer_with_retry() {",
        "    local source=\"$1\"",
        "    local dest=\"$2\"",
        "    local filename=\"$3\"",
        "    local attempt=1",
        "",
        "    while [[ $attempt -le $RETRY_ATTEMPTS ]]; do",
        "        echo \"  Attempt $attempt/$RETRY_ATTEMPTS: $filename\"",
        "        if scp \"$source\" \"$dest\"; then",
        "            echo \"  ✅ Success: $filename\"",
        "            return 0",
        "        else",
        "            echo \"  ❌ Failed attempt $attempt for $filename\"",
        "            ((attempt++))",
        "            if [[ $attempt -le $RETRY_ATTEMPTS ]]; then",
        "                echo \"  Waiting 5 seconds before retry...\"",
        "                sleep 5",
        "            fi",
        "        fi",
        "    done",
        "    echo \"  💥 All attempts failed for $filename\"",
        "    echo \"$filename\" >> failed_transfers.txt",
        "    return 1",
        "}",
        "",
        "# Main transfer logic",
        "echo 'Starting robust model transfer...'",
        "echo 'Checking for existing files and resuming transfer...'",
        "",
        "transferred=0",
        "skipped=0",
        "failed=0",
        "batch_count=0",
        "",
        "# Remove old failed transfers log",
        "rm -f failed_transfers.txt",
        ""
    ]
    
    # Add transfer commands in batches
    for i, (gamma_c, step_domain, rl_iterations, element_budget) in enumerate(combinations, 1):
        
        hpc_path, local_path, local_filename = generate_scp_command(gamma_c, step_domain, rl_iterations, element_budget)
        
        # Start new batch if needed
        if (i - 1) % BATCH_SIZE == 0:
            script_lines.extend([
                f"# === BATCH {(i-1)//BATCH_SIZE + 1} ===",
                f"echo 'Starting batch {(i-1)//BATCH_SIZE + 1} (files {i}-{min(i+BATCH_SIZE-1, total_combinations)})...'",
                ""
            ])
        
        script_lines.extend([
            f"# Transfer {i}/{total_combinations}: {local_filename}",
            f"if file_exists_and_valid \"$LOCAL_DIR/{local_filename}\"; then",
            f"    echo 'Skipping {i}/{total_combinations}: {local_filename} (already exists)'",
            f"    ((skipped++))",
            f"else",
            f"    echo 'Transferring {i}/{total_combinations}: {local_filename}'",
            f"    if transfer_with_retry '{hpc_path}' '$LOCAL_DIR/{local_filename}' '{local_filename}'; then",
            f"        ((transferred++))",
            f"    else",
            f"        ((failed++))",
            f"    fi",
            f"fi",
            ""
        ])
        
        # Add batch delay
        if i % BATCH_SIZE == 0 and i < total_combinations:
            script_lines.extend([
                f"echo 'Completed batch {i//BATCH_SIZE}. Waiting {DELAY_BETWEEN_BATCHES} seconds...'",
                f"sleep {DELAY_BETWEEN_BATCHES}",
                ""
            ])
    
    # Add summary
    script_lines.extend([
        "# Final summary",
        "echo '=================================='",
        "echo 'Transfer Summary:'",
        "echo \"  Transferred: $transferred\"",
        "echo \"  Skipped (already existed): $skipped\"", 
        "echo \"  Failed: $failed\"",
        f"echo \"  Total: {total_combinations}\"",
        "echo '=================================='",
        "",
        "if [[ -f failed_transfers.txt ]]; then",
        "    echo 'Failed transfers saved to: failed_transfers.txt'",
        "    echo 'You can retry these manually or re-run this script'",
        "fi",
        "",
        "echo 'Files in destination:'",
        "ls -1 \"$LOCAL_DIR\" | wc -l",
        "echo \"Location: $LOCAL_DIR\""
    ])
    
    # Write to file
    output_file = "robust_transfer_commands.sh"
    with open(output_file, 'w') as f:
        f.write('\n'.join(script_lines))
    
    # Make executable
    os.chmod(output_file, 0o755)
    
    print(f"✅ Generated {output_file}")
    print(f"✅ Features: Resume capability, {BATCH_SIZE}-file batches, {RETRY_ATTEMPTS}x retry")
    print()
    print("Key improvements:")
    print("- ✅ Skips files that already exist (resumes from where you left off)")
    print("- ✅ Transfers in small batches to avoid connection timeouts")
    print("- ✅ Retries failed transfers automatically")
    print("- ✅ Tracks progress and failures")
    print()
    print("Usage:")
    print(f"  bash {output_file}")

if __name__ == "__main__":
    generate_robust_script()