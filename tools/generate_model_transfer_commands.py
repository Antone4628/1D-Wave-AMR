#!/usr/bin/env python3
"""
Reusable Model Transfer Command Generator
Generates scp commands to transfer all final_model.zip files from HPC parameter sweeps.

Usage:
1. Update the CONFIGURATION section below for your specific sweep
2. Run: python3 generate_model_transfer_commands.py
3. Review the generated commands in transfer_commands.sh
4. Execute: bash transfer_commands.sh
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

# Parameter Sweep Identifier (update for each new sweep)
SWEEP_NAME = "full_param_sweep_data_20250601_105453"  # The actual directory name on HPC

# Local Configuration  
LOCAL_BASE_PATH = "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred"
LOCAL_SWEEP_DIR = "full_sweep_data_20250601"  # Will be created inside transferred/

# Parameter Space Definition (update if parameter ranges change)
GAMMA_C_VALUES = [25.0, 50.0, 100.0]
STEP_DOMAIN_VALUES = [0.025, 0.05, 0.1]
RL_ITERATIONS_VALUES = [10, 25, 40]
ELEMENT_BUDGET_VALUES = [25, 30, 40]

# File to transfer from each parameter directory
TARGET_FILE = "final_model.zip"

# ====================================================================
# SCRIPT LOGIC - Generally doesn't need changes
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
    """Generate a single scp command for one parameter combination."""
    
    # Source path on HPC
    dir_name = format_directory_name(gamma_c, step_domain, rl_iterations, element_budget)
    hpc_path = f"{HPC_USERNAME}@{HPC_HOSTNAME}:{HPC_PROJECT_ROOT}/results/{SWEEP_NAME}/{dir_name}/{TARGET_FILE}"
    
    # Destination path on local machine
    local_filename = format_filename(gamma_c, step_domain, rl_iterations, element_budget)
    local_path = f"{LOCAL_BASE_PATH}/{LOCAL_SWEEP_DIR}/{local_filename}"
    
    return f"scp {hpc_path} {local_path}"

def generate_all_commands():
    """Generate all scp commands and save to script file with resume capability."""
    
    combinations = generate_parameter_combinations()
    total_combinations = len(combinations)
    
    print(f"Generating transfer commands for {total_combinations} parameter combinations...")
    print(f"HPC Source: {HPC_USERNAME}@{HPC_HOSTNAME}:{HPC_PROJECT_ROOT}/results/{SWEEP_NAME}/")
    print(f"Local Destination: {LOCAL_BASE_PATH}/{LOCAL_SWEEP_DIR}/")
    print()
    
    # Full local path for the script
    full_local_path = f"{LOCAL_BASE_PATH}/{LOCAL_SWEEP_DIR}"
    
    # Generate script content
    script_lines = [
        "#!/bin/bash",
        "# Auto-generated model transfer commands with resume capability",
        f"# Generated for parameter sweep: {SWEEP_NAME}",
        f"# Total combinations: {total_combinations}",
        "",
        "# Create destination directory",
        f"mkdir -p \"{full_local_path}\"",
        "",
        "# Counters",
        "transferred=0",
        "skipped=0",
        "",
        f"echo 'Starting transfer of {total_combinations} models...'",
        f"echo 'Destination: {full_local_path}'",
        "echo 'Will skip files that already exist and are > 1KB'",
        "echo",
        ""
    ]
    
    # Add transfer commands with resume capability
    for i, (gamma_c, step_domain, rl_iterations, element_budget) in enumerate(combinations, 1):
        
        # Generate paths
        dir_name = format_directory_name(gamma_c, step_domain, rl_iterations, element_budget)
        hpc_path = f"{HPC_USERNAME}@{HPC_HOSTNAME}:{HPC_PROJECT_ROOT}/results/{SWEEP_NAME}/{dir_name}/{TARGET_FILE}"
        local_filename = format_filename(gamma_c, step_domain, rl_iterations, element_budget)
        local_file_path = f"{full_local_path}/{local_filename}"
        
        # Check if file exists and transfer
        script_lines.extend([
            f"# Transfer {i}/{total_combinations}: {local_filename}",
            f"if [[ -f \"{local_file_path}\" && $(stat -f%z \"{local_file_path}\" 2>/dev/null || stat -c%s \"{local_file_path}\" 2>/dev/null) -gt 1000 ]]; then",
            f"    echo 'Skipping {i}/{total_combinations}: {local_filename} (already exists)'",
            f"    ((skipped++))",
            f"else",
            f"    echo 'Transferring {i}/{total_combinations}: {local_filename}'",
            f"    if scp \"{hpc_path}\" \"{local_file_path}\"; then",
            f"        echo '✅ Success: {local_filename}'",
            f"        ((transferred++))",
            f"    else",
            f"        echo '❌ Failed: {local_filename}'",
            f"    fi",
            f"    sleep 0.5  # Small delay to prevent connection issues",
            f"fi",
            ""
        ])
    
    script_lines.extend([
        "echo '=================================='",
        "echo 'Transfer Summary:'",
        "echo \"Transferred: $transferred\"",
        "echo \"Skipped: $skipped\"",
        f"echo \"Total: {total_combinations}\"",
        "echo '=================================='",
        "",
        f"echo 'Files in destination:'",
        f"ls -1 \"{full_local_path}\" | wc -l",
        f"echo 'Location: {full_local_path}'"
    ])
    
    # Write to file
    output_file = "transfer_commands.sh"
    with open(output_file, 'w') as f:
        f.write('\n'.join(script_lines))
    
    # Make executable
    os.chmod(output_file, 0o755)
    
    print(f"✅ Generated {output_file} with {total_combinations} transfer commands")
    print(f"✅ Features: Resume capability, progress tracking, file validation")
    print()
    print("Next steps:")
    print(f"1. Execute the transfer: bash {output_file}")
    print("   (The script will skip files you already have)")
    print()
    print("Note: Script includes 0.5s delays between transfers to prevent timeouts.")

if __name__ == "__main__":
    generate_all_commands()


# #!/usr/bin/env python3
# """
# Reusable Model Transfer Command Generator
# Generates scp commands to transfer all final_model.zip files from HPC parameter sweeps.

# Usage:
# 1. Update the CONFIGURATION section below for your specific sweep
# 2. Run: python3 generate_model_transfer_commands.py
# 3. Review the generated commands in transfer_commands.sh
# 4. Execute: bash transfer_commands.sh
# """

# import itertools
# import os

# # ====================================================================
# # CONFIGURATION - Update these for each parameter sweep
# # ====================================================================

# # HPC Configuration
# HPC_USERNAME = "antonechacartegu"
# HPC_HOSTNAME = "borah-login.boisestate.edu"
# HPC_PROJECT_ROOT = "projects/drl-amr/1D-Wave-AMR"

# # Parameter Sweep Identifier (update for each new sweep)
# SWEEP_NAME = "full_param_sweep_data_20250601_105453"  # The actual directory name on HPC

# # Local Configuration  
# LOCAL_BASE_PATH = "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred"
# LOCAL_SWEEP_DIR = "full_sweep_data_20250601"  # Will be created inside transferred/

# # Parameter Space Definition (update if parameter ranges change)
# GAMMA_C_VALUES = [25.0, 50.0, 100.0]
# STEP_DOMAIN_VALUES = [0.025, 0.05, 0.1]
# RL_ITERATIONS_VALUES = [10, 25, 40]
# ELEMENT_BUDGET_VALUES = [25, 30, 40]

# # File to transfer from each parameter directory
# TARGET_FILE = "final_model.zip"

# # ====================================================================
# # SCRIPT LOGIC - Generally doesn't need changes
# # ====================================================================

# def generate_parameter_combinations():
#     """Generate all parameter combinations."""
#     return list(itertools.product(
#         GAMMA_C_VALUES,
#         STEP_DOMAIN_VALUES, 
#         RL_ITERATIONS_VALUES,
#         ELEMENT_BUDGET_VALUES
#     ))

# def format_directory_name(gamma_c, step_domain, rl_iterations, element_budget):
#     """Format the directory name based on parameters."""
#     return f"gamma_{gamma_c}_step_{step_domain}_rl_{rl_iterations}_budget_{element_budget}"

# def format_filename(gamma_c, step_domain, rl_iterations, element_budget):
#     """Format the local filename with parameters."""
#     return f"gamma_{gamma_c}_step_{step_domain}_rl_{rl_iterations}_budget_{element_budget}_{TARGET_FILE}"

# def generate_scp_command(gamma_c, step_domain, rl_iterations, element_budget):
#     """Generate a single scp command for one parameter combination."""
    
#     # Source path on HPC
#     dir_name = format_directory_name(gamma_c, step_domain, rl_iterations, element_budget)
#     hpc_path = f"{HPC_USERNAME}@{HPC_HOSTNAME}:{HPC_PROJECT_ROOT}/results/{SWEEP_NAME}/{dir_name}/{TARGET_FILE}"
    
#     # Destination path on local machine
#     local_filename = format_filename(gamma_c, step_domain, rl_iterations, element_budget)
#     local_path = f"{LOCAL_BASE_PATH}/{LOCAL_SWEEP_DIR}/{local_filename}"
    
#     return f"scp {hpc_path} {local_path}"

# def generate_all_commands():
#     """Generate all scp commands and save to script file."""
    
#     combinations = generate_parameter_combinations()
#     total_combinations = len(combinations)
    
#     print(f"Generating transfer commands for {total_combinations} parameter combinations...")
#     print(f"HPC Source: {HPC_USERNAME}@{HPC_HOSTNAME}:{HPC_PROJECT_ROOT}/results/{SWEEP_NAME}/")
#     print(f"Local Destination: {LOCAL_BASE_PATH}/{LOCAL_SWEEP_DIR}/")
#     print()
    
#     # Generate script content
#     script_lines = [
#         "#!/bin/bash",
#         "# Auto-generated model transfer commands",
#         f"# Generated for parameter sweep: {SWEEP_NAME}",
#         f"# Total combinations: {total_combinations}",
#         "",
#         "# Create destination directory",
#         f"mkdir -p {LOCAL_BASE_PATH}/{LOCAL_SWEEP_DIR}",
#         "",
#         "# Transfer commands",
#         f"echo 'Starting transfer of {total_combinations} models...'",
#         ""
#     ]
    
#     # Add progress tracking and scp commands
#     for i, (gamma_c, step_domain, rl_iterations, element_budget) in enumerate(combinations, 1):
        
#         # Progress indicator
#         script_lines.append(f"echo 'Transferring {i}/{total_combinations}: gamma_{gamma_c}_step_{step_domain}_rl_{rl_iterations}_budget_{element_budget}'")
        
#         # SCP command
#         scp_command = generate_scp_command(gamma_c, step_domain, rl_iterations, element_budget)
#         script_lines.append(scp_command)
#         script_lines.append("")
    
#     script_lines.extend([
#         f"echo 'Transfer complete! {total_combinations} models transferred to:'",
#         f"echo '{LOCAL_BASE_PATH}/{LOCAL_SWEEP_DIR}/'",
#         f"echo 'Total files: '",
#         f"ls -1 {LOCAL_BASE_PATH}/{LOCAL_SWEEP_DIR}/ | wc -l"
#     ])
    
#     # Write to file
#     output_file = "transfer_commands.sh"
#     with open(output_file, 'w') as f:
#         f.write('\n'.join(script_lines))
    
#     # Make executable
#     os.chmod(output_file, 0o755)
    
#     print(f"✅ Generated {output_file} with {total_combinations} transfer commands")
#     print(f"✅ Script includes progress tracking and error handling")
#     print()
#     print("Next steps:")
#     print(f"1. Review the commands: cat {output_file}")
#     print(f"2. Execute the transfer: bash {output_file}")
#     print()
#     print("Note: The script will create the destination directory automatically.")

# if __name__ == "__main__":
#     generate_all_commands()