#!/bin/bash
# Robust Model Transfer Script with Resume Capability
# Generated for parameter sweep: full_param_sweep_data_20250601_105453
# Total combinations: 81

# Configuration
LOCAL_DIR='/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601'
RETRY_ATTEMPTS=3
BATCH_SIZE=10
DELAY_BETWEEN_BATCHES=2

# Create destination directory
mkdir -p "$LOCAL_DIR"

# Function to check if file already exists and has reasonable size
file_exists_and_valid() {
    local file="$1"
    if [[ -f "$file" && $(stat -f%z "$file" 2>/dev/null || stat -c%s "$file" 2>/dev/null) -gt 1000 ]]; then
        return 0  # File exists and is > 1KB
    else
        return 1  # File missing or too small
    fi
}

# Function to transfer with retry
transfer_with_retry() {
    local source="$1"
    local dest="$2"
    local filename="$3"
    local attempt=1

    while [[ $attempt -le $RETRY_ATTEMPTS ]]; do
        echo "  Attempt $attempt/$RETRY_ATTEMPTS: $filename"
        if scp "$source" "$dest"; then
            echo "  ✅ Success: $filename"
            return 0
        else
            echo "  ❌ Failed attempt $attempt for $filename"
            ((attempt++))
            if [[ $attempt -le $RETRY_ATTEMPTS ]]; then
                echo "  Waiting 5 seconds before retry..."
                sleep 5
            fi
        fi
    done
    echo "  💥 All attempts failed for $filename"
    echo "$filename" >> failed_transfers.txt
    return 1
}

# Main transfer logic
echo 'Starting robust model transfer...'
echo 'Checking for existing files and resuming transfer...'

transferred=0
skipped=0
failed=0
batch_count=0

# Remove old failed transfers log
rm -f failed_transfers.txt

# === BATCH 1 ===
echo 'Starting batch 1 (files 1-10)...'

# Transfer 1/81: gamma_25.0_step_0.025_rl_10_budget_25_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_25.0_step_0.025_rl_10_budget_25_final_model.zip"; then
    echo 'Skipping 1/81: gamma_25.0_step_0.025_rl_10_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 1/81: gamma_25.0_step_0.025_rl_10_budget_25_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.025_rl_10_budget_25/final_model.zip' '$LOCAL_DIR/gamma_25.0_step_0.025_rl_10_budget_25_final_model.zip' 'gamma_25.0_step_0.025_rl_10_budget_25_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 2/81: gamma_25.0_step_0.025_rl_10_budget_30_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_25.0_step_0.025_rl_10_budget_30_final_model.zip"; then
    echo 'Skipping 2/81: gamma_25.0_step_0.025_rl_10_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 2/81: gamma_25.0_step_0.025_rl_10_budget_30_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.025_rl_10_budget_30/final_model.zip' '$LOCAL_DIR/gamma_25.0_step_0.025_rl_10_budget_30_final_model.zip' 'gamma_25.0_step_0.025_rl_10_budget_30_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 3/81: gamma_25.0_step_0.025_rl_10_budget_40_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_25.0_step_0.025_rl_10_budget_40_final_model.zip"; then
    echo 'Skipping 3/81: gamma_25.0_step_0.025_rl_10_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 3/81: gamma_25.0_step_0.025_rl_10_budget_40_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.025_rl_10_budget_40/final_model.zip' '$LOCAL_DIR/gamma_25.0_step_0.025_rl_10_budget_40_final_model.zip' 'gamma_25.0_step_0.025_rl_10_budget_40_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 4/81: gamma_25.0_step_0.025_rl_25_budget_25_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_25.0_step_0.025_rl_25_budget_25_final_model.zip"; then
    echo 'Skipping 4/81: gamma_25.0_step_0.025_rl_25_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 4/81: gamma_25.0_step_0.025_rl_25_budget_25_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.025_rl_25_budget_25/final_model.zip' '$LOCAL_DIR/gamma_25.0_step_0.025_rl_25_budget_25_final_model.zip' 'gamma_25.0_step_0.025_rl_25_budget_25_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 5/81: gamma_25.0_step_0.025_rl_25_budget_30_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_25.0_step_0.025_rl_25_budget_30_final_model.zip"; then
    echo 'Skipping 5/81: gamma_25.0_step_0.025_rl_25_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 5/81: gamma_25.0_step_0.025_rl_25_budget_30_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.025_rl_25_budget_30/final_model.zip' '$LOCAL_DIR/gamma_25.0_step_0.025_rl_25_budget_30_final_model.zip' 'gamma_25.0_step_0.025_rl_25_budget_30_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 6/81: gamma_25.0_step_0.025_rl_25_budget_40_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_25.0_step_0.025_rl_25_budget_40_final_model.zip"; then
    echo 'Skipping 6/81: gamma_25.0_step_0.025_rl_25_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 6/81: gamma_25.0_step_0.025_rl_25_budget_40_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.025_rl_25_budget_40/final_model.zip' '$LOCAL_DIR/gamma_25.0_step_0.025_rl_25_budget_40_final_model.zip' 'gamma_25.0_step_0.025_rl_25_budget_40_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 7/81: gamma_25.0_step_0.025_rl_40_budget_25_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_25.0_step_0.025_rl_40_budget_25_final_model.zip"; then
    echo 'Skipping 7/81: gamma_25.0_step_0.025_rl_40_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 7/81: gamma_25.0_step_0.025_rl_40_budget_25_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.025_rl_40_budget_25/final_model.zip' '$LOCAL_DIR/gamma_25.0_step_0.025_rl_40_budget_25_final_model.zip' 'gamma_25.0_step_0.025_rl_40_budget_25_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 8/81: gamma_25.0_step_0.025_rl_40_budget_30_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_25.0_step_0.025_rl_40_budget_30_final_model.zip"; then
    echo 'Skipping 8/81: gamma_25.0_step_0.025_rl_40_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 8/81: gamma_25.0_step_0.025_rl_40_budget_30_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.025_rl_40_budget_30/final_model.zip' '$LOCAL_DIR/gamma_25.0_step_0.025_rl_40_budget_30_final_model.zip' 'gamma_25.0_step_0.025_rl_40_budget_30_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 9/81: gamma_25.0_step_0.025_rl_40_budget_40_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_25.0_step_0.025_rl_40_budget_40_final_model.zip"; then
    echo 'Skipping 9/81: gamma_25.0_step_0.025_rl_40_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 9/81: gamma_25.0_step_0.025_rl_40_budget_40_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.025_rl_40_budget_40/final_model.zip' '$LOCAL_DIR/gamma_25.0_step_0.025_rl_40_budget_40_final_model.zip' 'gamma_25.0_step_0.025_rl_40_budget_40_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 10/81: gamma_25.0_step_0.05_rl_10_budget_25_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_25.0_step_0.05_rl_10_budget_25_final_model.zip"; then
    echo 'Skipping 10/81: gamma_25.0_step_0.05_rl_10_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 10/81: gamma_25.0_step_0.05_rl_10_budget_25_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.05_rl_10_budget_25/final_model.zip' '$LOCAL_DIR/gamma_25.0_step_0.05_rl_10_budget_25_final_model.zip' 'gamma_25.0_step_0.05_rl_10_budget_25_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

echo 'Completed batch 1. Waiting 2 seconds...'
sleep 2

# === BATCH 2 ===
echo 'Starting batch 2 (files 11-20)...'

# Transfer 11/81: gamma_25.0_step_0.05_rl_10_budget_30_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_25.0_step_0.05_rl_10_budget_30_final_model.zip"; then
    echo 'Skipping 11/81: gamma_25.0_step_0.05_rl_10_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 11/81: gamma_25.0_step_0.05_rl_10_budget_30_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.05_rl_10_budget_30/final_model.zip' '$LOCAL_DIR/gamma_25.0_step_0.05_rl_10_budget_30_final_model.zip' 'gamma_25.0_step_0.05_rl_10_budget_30_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 12/81: gamma_25.0_step_0.05_rl_10_budget_40_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_25.0_step_0.05_rl_10_budget_40_final_model.zip"; then
    echo 'Skipping 12/81: gamma_25.0_step_0.05_rl_10_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 12/81: gamma_25.0_step_0.05_rl_10_budget_40_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.05_rl_10_budget_40/final_model.zip' '$LOCAL_DIR/gamma_25.0_step_0.05_rl_10_budget_40_final_model.zip' 'gamma_25.0_step_0.05_rl_10_budget_40_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 13/81: gamma_25.0_step_0.05_rl_25_budget_25_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_25.0_step_0.05_rl_25_budget_25_final_model.zip"; then
    echo 'Skipping 13/81: gamma_25.0_step_0.05_rl_25_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 13/81: gamma_25.0_step_0.05_rl_25_budget_25_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.05_rl_25_budget_25/final_model.zip' '$LOCAL_DIR/gamma_25.0_step_0.05_rl_25_budget_25_final_model.zip' 'gamma_25.0_step_0.05_rl_25_budget_25_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 14/81: gamma_25.0_step_0.05_rl_25_budget_30_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_25.0_step_0.05_rl_25_budget_30_final_model.zip"; then
    echo 'Skipping 14/81: gamma_25.0_step_0.05_rl_25_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 14/81: gamma_25.0_step_0.05_rl_25_budget_30_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.05_rl_25_budget_30/final_model.zip' '$LOCAL_DIR/gamma_25.0_step_0.05_rl_25_budget_30_final_model.zip' 'gamma_25.0_step_0.05_rl_25_budget_30_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 15/81: gamma_25.0_step_0.05_rl_25_budget_40_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_25.0_step_0.05_rl_25_budget_40_final_model.zip"; then
    echo 'Skipping 15/81: gamma_25.0_step_0.05_rl_25_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 15/81: gamma_25.0_step_0.05_rl_25_budget_40_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.05_rl_25_budget_40/final_model.zip' '$LOCAL_DIR/gamma_25.0_step_0.05_rl_25_budget_40_final_model.zip' 'gamma_25.0_step_0.05_rl_25_budget_40_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 16/81: gamma_25.0_step_0.05_rl_40_budget_25_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_25.0_step_0.05_rl_40_budget_25_final_model.zip"; then
    echo 'Skipping 16/81: gamma_25.0_step_0.05_rl_40_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 16/81: gamma_25.0_step_0.05_rl_40_budget_25_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.05_rl_40_budget_25/final_model.zip' '$LOCAL_DIR/gamma_25.0_step_0.05_rl_40_budget_25_final_model.zip' 'gamma_25.0_step_0.05_rl_40_budget_25_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 17/81: gamma_25.0_step_0.05_rl_40_budget_30_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_25.0_step_0.05_rl_40_budget_30_final_model.zip"; then
    echo 'Skipping 17/81: gamma_25.0_step_0.05_rl_40_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 17/81: gamma_25.0_step_0.05_rl_40_budget_30_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.05_rl_40_budget_30/final_model.zip' '$LOCAL_DIR/gamma_25.0_step_0.05_rl_40_budget_30_final_model.zip' 'gamma_25.0_step_0.05_rl_40_budget_30_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 18/81: gamma_25.0_step_0.05_rl_40_budget_40_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_25.0_step_0.05_rl_40_budget_40_final_model.zip"; then
    echo 'Skipping 18/81: gamma_25.0_step_0.05_rl_40_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 18/81: gamma_25.0_step_0.05_rl_40_budget_40_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.05_rl_40_budget_40/final_model.zip' '$LOCAL_DIR/gamma_25.0_step_0.05_rl_40_budget_40_final_model.zip' 'gamma_25.0_step_0.05_rl_40_budget_40_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 19/81: gamma_25.0_step_0.1_rl_10_budget_25_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_25.0_step_0.1_rl_10_budget_25_final_model.zip"; then
    echo 'Skipping 19/81: gamma_25.0_step_0.1_rl_10_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 19/81: gamma_25.0_step_0.1_rl_10_budget_25_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.1_rl_10_budget_25/final_model.zip' '$LOCAL_DIR/gamma_25.0_step_0.1_rl_10_budget_25_final_model.zip' 'gamma_25.0_step_0.1_rl_10_budget_25_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 20/81: gamma_25.0_step_0.1_rl_10_budget_30_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_25.0_step_0.1_rl_10_budget_30_final_model.zip"; then
    echo 'Skipping 20/81: gamma_25.0_step_0.1_rl_10_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 20/81: gamma_25.0_step_0.1_rl_10_budget_30_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.1_rl_10_budget_30/final_model.zip' '$LOCAL_DIR/gamma_25.0_step_0.1_rl_10_budget_30_final_model.zip' 'gamma_25.0_step_0.1_rl_10_budget_30_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

echo 'Completed batch 2. Waiting 2 seconds...'
sleep 2

# === BATCH 3 ===
echo 'Starting batch 3 (files 21-30)...'

# Transfer 21/81: gamma_25.0_step_0.1_rl_10_budget_40_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_25.0_step_0.1_rl_10_budget_40_final_model.zip"; then
    echo 'Skipping 21/81: gamma_25.0_step_0.1_rl_10_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 21/81: gamma_25.0_step_0.1_rl_10_budget_40_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.1_rl_10_budget_40/final_model.zip' '$LOCAL_DIR/gamma_25.0_step_0.1_rl_10_budget_40_final_model.zip' 'gamma_25.0_step_0.1_rl_10_budget_40_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 22/81: gamma_25.0_step_0.1_rl_25_budget_25_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_25.0_step_0.1_rl_25_budget_25_final_model.zip"; then
    echo 'Skipping 22/81: gamma_25.0_step_0.1_rl_25_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 22/81: gamma_25.0_step_0.1_rl_25_budget_25_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.1_rl_25_budget_25/final_model.zip' '$LOCAL_DIR/gamma_25.0_step_0.1_rl_25_budget_25_final_model.zip' 'gamma_25.0_step_0.1_rl_25_budget_25_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 23/81: gamma_25.0_step_0.1_rl_25_budget_30_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_25.0_step_0.1_rl_25_budget_30_final_model.zip"; then
    echo 'Skipping 23/81: gamma_25.0_step_0.1_rl_25_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 23/81: gamma_25.0_step_0.1_rl_25_budget_30_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.1_rl_25_budget_30/final_model.zip' '$LOCAL_DIR/gamma_25.0_step_0.1_rl_25_budget_30_final_model.zip' 'gamma_25.0_step_0.1_rl_25_budget_30_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 24/81: gamma_25.0_step_0.1_rl_25_budget_40_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_25.0_step_0.1_rl_25_budget_40_final_model.zip"; then
    echo 'Skipping 24/81: gamma_25.0_step_0.1_rl_25_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 24/81: gamma_25.0_step_0.1_rl_25_budget_40_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.1_rl_25_budget_40/final_model.zip' '$LOCAL_DIR/gamma_25.0_step_0.1_rl_25_budget_40_final_model.zip' 'gamma_25.0_step_0.1_rl_25_budget_40_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 25/81: gamma_25.0_step_0.1_rl_40_budget_25_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_25.0_step_0.1_rl_40_budget_25_final_model.zip"; then
    echo 'Skipping 25/81: gamma_25.0_step_0.1_rl_40_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 25/81: gamma_25.0_step_0.1_rl_40_budget_25_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.1_rl_40_budget_25/final_model.zip' '$LOCAL_DIR/gamma_25.0_step_0.1_rl_40_budget_25_final_model.zip' 'gamma_25.0_step_0.1_rl_40_budget_25_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 26/81: gamma_25.0_step_0.1_rl_40_budget_30_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_25.0_step_0.1_rl_40_budget_30_final_model.zip"; then
    echo 'Skipping 26/81: gamma_25.0_step_0.1_rl_40_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 26/81: gamma_25.0_step_0.1_rl_40_budget_30_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.1_rl_40_budget_30/final_model.zip' '$LOCAL_DIR/gamma_25.0_step_0.1_rl_40_budget_30_final_model.zip' 'gamma_25.0_step_0.1_rl_40_budget_30_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 27/81: gamma_25.0_step_0.1_rl_40_budget_40_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_25.0_step_0.1_rl_40_budget_40_final_model.zip"; then
    echo 'Skipping 27/81: gamma_25.0_step_0.1_rl_40_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 27/81: gamma_25.0_step_0.1_rl_40_budget_40_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.1_rl_40_budget_40/final_model.zip' '$LOCAL_DIR/gamma_25.0_step_0.1_rl_40_budget_40_final_model.zip' 'gamma_25.0_step_0.1_rl_40_budget_40_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 28/81: gamma_50.0_step_0.025_rl_10_budget_25_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_50.0_step_0.025_rl_10_budget_25_final_model.zip"; then
    echo 'Skipping 28/81: gamma_50.0_step_0.025_rl_10_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 28/81: gamma_50.0_step_0.025_rl_10_budget_25_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.025_rl_10_budget_25/final_model.zip' '$LOCAL_DIR/gamma_50.0_step_0.025_rl_10_budget_25_final_model.zip' 'gamma_50.0_step_0.025_rl_10_budget_25_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 29/81: gamma_50.0_step_0.025_rl_10_budget_30_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_50.0_step_0.025_rl_10_budget_30_final_model.zip"; then
    echo 'Skipping 29/81: gamma_50.0_step_0.025_rl_10_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 29/81: gamma_50.0_step_0.025_rl_10_budget_30_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.025_rl_10_budget_30/final_model.zip' '$LOCAL_DIR/gamma_50.0_step_0.025_rl_10_budget_30_final_model.zip' 'gamma_50.0_step_0.025_rl_10_budget_30_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 30/81: gamma_50.0_step_0.025_rl_10_budget_40_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_50.0_step_0.025_rl_10_budget_40_final_model.zip"; then
    echo 'Skipping 30/81: gamma_50.0_step_0.025_rl_10_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 30/81: gamma_50.0_step_0.025_rl_10_budget_40_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.025_rl_10_budget_40/final_model.zip' '$LOCAL_DIR/gamma_50.0_step_0.025_rl_10_budget_40_final_model.zip' 'gamma_50.0_step_0.025_rl_10_budget_40_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

echo 'Completed batch 3. Waiting 2 seconds...'
sleep 2

# === BATCH 4 ===
echo 'Starting batch 4 (files 31-40)...'

# Transfer 31/81: gamma_50.0_step_0.025_rl_25_budget_25_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_50.0_step_0.025_rl_25_budget_25_final_model.zip"; then
    echo 'Skipping 31/81: gamma_50.0_step_0.025_rl_25_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 31/81: gamma_50.0_step_0.025_rl_25_budget_25_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.025_rl_25_budget_25/final_model.zip' '$LOCAL_DIR/gamma_50.0_step_0.025_rl_25_budget_25_final_model.zip' 'gamma_50.0_step_0.025_rl_25_budget_25_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 32/81: gamma_50.0_step_0.025_rl_25_budget_30_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_50.0_step_0.025_rl_25_budget_30_final_model.zip"; then
    echo 'Skipping 32/81: gamma_50.0_step_0.025_rl_25_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 32/81: gamma_50.0_step_0.025_rl_25_budget_30_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.025_rl_25_budget_30/final_model.zip' '$LOCAL_DIR/gamma_50.0_step_0.025_rl_25_budget_30_final_model.zip' 'gamma_50.0_step_0.025_rl_25_budget_30_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 33/81: gamma_50.0_step_0.025_rl_25_budget_40_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_50.0_step_0.025_rl_25_budget_40_final_model.zip"; then
    echo 'Skipping 33/81: gamma_50.0_step_0.025_rl_25_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 33/81: gamma_50.0_step_0.025_rl_25_budget_40_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.025_rl_25_budget_40/final_model.zip' '$LOCAL_DIR/gamma_50.0_step_0.025_rl_25_budget_40_final_model.zip' 'gamma_50.0_step_0.025_rl_25_budget_40_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 34/81: gamma_50.0_step_0.025_rl_40_budget_25_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_50.0_step_0.025_rl_40_budget_25_final_model.zip"; then
    echo 'Skipping 34/81: gamma_50.0_step_0.025_rl_40_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 34/81: gamma_50.0_step_0.025_rl_40_budget_25_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.025_rl_40_budget_25/final_model.zip' '$LOCAL_DIR/gamma_50.0_step_0.025_rl_40_budget_25_final_model.zip' 'gamma_50.0_step_0.025_rl_40_budget_25_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 35/81: gamma_50.0_step_0.025_rl_40_budget_30_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_50.0_step_0.025_rl_40_budget_30_final_model.zip"; then
    echo 'Skipping 35/81: gamma_50.0_step_0.025_rl_40_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 35/81: gamma_50.0_step_0.025_rl_40_budget_30_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.025_rl_40_budget_30/final_model.zip' '$LOCAL_DIR/gamma_50.0_step_0.025_rl_40_budget_30_final_model.zip' 'gamma_50.0_step_0.025_rl_40_budget_30_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 36/81: gamma_50.0_step_0.025_rl_40_budget_40_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_50.0_step_0.025_rl_40_budget_40_final_model.zip"; then
    echo 'Skipping 36/81: gamma_50.0_step_0.025_rl_40_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 36/81: gamma_50.0_step_0.025_rl_40_budget_40_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.025_rl_40_budget_40/final_model.zip' '$LOCAL_DIR/gamma_50.0_step_0.025_rl_40_budget_40_final_model.zip' 'gamma_50.0_step_0.025_rl_40_budget_40_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 37/81: gamma_50.0_step_0.05_rl_10_budget_25_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_50.0_step_0.05_rl_10_budget_25_final_model.zip"; then
    echo 'Skipping 37/81: gamma_50.0_step_0.05_rl_10_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 37/81: gamma_50.0_step_0.05_rl_10_budget_25_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.05_rl_10_budget_25/final_model.zip' '$LOCAL_DIR/gamma_50.0_step_0.05_rl_10_budget_25_final_model.zip' 'gamma_50.0_step_0.05_rl_10_budget_25_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 38/81: gamma_50.0_step_0.05_rl_10_budget_30_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_50.0_step_0.05_rl_10_budget_30_final_model.zip"; then
    echo 'Skipping 38/81: gamma_50.0_step_0.05_rl_10_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 38/81: gamma_50.0_step_0.05_rl_10_budget_30_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.05_rl_10_budget_30/final_model.zip' '$LOCAL_DIR/gamma_50.0_step_0.05_rl_10_budget_30_final_model.zip' 'gamma_50.0_step_0.05_rl_10_budget_30_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 39/81: gamma_50.0_step_0.05_rl_10_budget_40_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_50.0_step_0.05_rl_10_budget_40_final_model.zip"; then
    echo 'Skipping 39/81: gamma_50.0_step_0.05_rl_10_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 39/81: gamma_50.0_step_0.05_rl_10_budget_40_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.05_rl_10_budget_40/final_model.zip' '$LOCAL_DIR/gamma_50.0_step_0.05_rl_10_budget_40_final_model.zip' 'gamma_50.0_step_0.05_rl_10_budget_40_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 40/81: gamma_50.0_step_0.05_rl_25_budget_25_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_50.0_step_0.05_rl_25_budget_25_final_model.zip"; then
    echo 'Skipping 40/81: gamma_50.0_step_0.05_rl_25_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 40/81: gamma_50.0_step_0.05_rl_25_budget_25_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.05_rl_25_budget_25/final_model.zip' '$LOCAL_DIR/gamma_50.0_step_0.05_rl_25_budget_25_final_model.zip' 'gamma_50.0_step_0.05_rl_25_budget_25_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

echo 'Completed batch 4. Waiting 2 seconds...'
sleep 2

# === BATCH 5 ===
echo 'Starting batch 5 (files 41-50)...'

# Transfer 41/81: gamma_50.0_step_0.05_rl_25_budget_30_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_50.0_step_0.05_rl_25_budget_30_final_model.zip"; then
    echo 'Skipping 41/81: gamma_50.0_step_0.05_rl_25_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 41/81: gamma_50.0_step_0.05_rl_25_budget_30_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.05_rl_25_budget_30/final_model.zip' '$LOCAL_DIR/gamma_50.0_step_0.05_rl_25_budget_30_final_model.zip' 'gamma_50.0_step_0.05_rl_25_budget_30_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 42/81: gamma_50.0_step_0.05_rl_25_budget_40_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_50.0_step_0.05_rl_25_budget_40_final_model.zip"; then
    echo 'Skipping 42/81: gamma_50.0_step_0.05_rl_25_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 42/81: gamma_50.0_step_0.05_rl_25_budget_40_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.05_rl_25_budget_40/final_model.zip' '$LOCAL_DIR/gamma_50.0_step_0.05_rl_25_budget_40_final_model.zip' 'gamma_50.0_step_0.05_rl_25_budget_40_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 43/81: gamma_50.0_step_0.05_rl_40_budget_25_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_50.0_step_0.05_rl_40_budget_25_final_model.zip"; then
    echo 'Skipping 43/81: gamma_50.0_step_0.05_rl_40_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 43/81: gamma_50.0_step_0.05_rl_40_budget_25_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.05_rl_40_budget_25/final_model.zip' '$LOCAL_DIR/gamma_50.0_step_0.05_rl_40_budget_25_final_model.zip' 'gamma_50.0_step_0.05_rl_40_budget_25_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 44/81: gamma_50.0_step_0.05_rl_40_budget_30_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_50.0_step_0.05_rl_40_budget_30_final_model.zip"; then
    echo 'Skipping 44/81: gamma_50.0_step_0.05_rl_40_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 44/81: gamma_50.0_step_0.05_rl_40_budget_30_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.05_rl_40_budget_30/final_model.zip' '$LOCAL_DIR/gamma_50.0_step_0.05_rl_40_budget_30_final_model.zip' 'gamma_50.0_step_0.05_rl_40_budget_30_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 45/81: gamma_50.0_step_0.05_rl_40_budget_40_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_50.0_step_0.05_rl_40_budget_40_final_model.zip"; then
    echo 'Skipping 45/81: gamma_50.0_step_0.05_rl_40_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 45/81: gamma_50.0_step_0.05_rl_40_budget_40_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.05_rl_40_budget_40/final_model.zip' '$LOCAL_DIR/gamma_50.0_step_0.05_rl_40_budget_40_final_model.zip' 'gamma_50.0_step_0.05_rl_40_budget_40_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 46/81: gamma_50.0_step_0.1_rl_10_budget_25_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_50.0_step_0.1_rl_10_budget_25_final_model.zip"; then
    echo 'Skipping 46/81: gamma_50.0_step_0.1_rl_10_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 46/81: gamma_50.0_step_0.1_rl_10_budget_25_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.1_rl_10_budget_25/final_model.zip' '$LOCAL_DIR/gamma_50.0_step_0.1_rl_10_budget_25_final_model.zip' 'gamma_50.0_step_0.1_rl_10_budget_25_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 47/81: gamma_50.0_step_0.1_rl_10_budget_30_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_50.0_step_0.1_rl_10_budget_30_final_model.zip"; then
    echo 'Skipping 47/81: gamma_50.0_step_0.1_rl_10_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 47/81: gamma_50.0_step_0.1_rl_10_budget_30_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.1_rl_10_budget_30/final_model.zip' '$LOCAL_DIR/gamma_50.0_step_0.1_rl_10_budget_30_final_model.zip' 'gamma_50.0_step_0.1_rl_10_budget_30_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 48/81: gamma_50.0_step_0.1_rl_10_budget_40_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_50.0_step_0.1_rl_10_budget_40_final_model.zip"; then
    echo 'Skipping 48/81: gamma_50.0_step_0.1_rl_10_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 48/81: gamma_50.0_step_0.1_rl_10_budget_40_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.1_rl_10_budget_40/final_model.zip' '$LOCAL_DIR/gamma_50.0_step_0.1_rl_10_budget_40_final_model.zip' 'gamma_50.0_step_0.1_rl_10_budget_40_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 49/81: gamma_50.0_step_0.1_rl_25_budget_25_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_50.0_step_0.1_rl_25_budget_25_final_model.zip"; then
    echo 'Skipping 49/81: gamma_50.0_step_0.1_rl_25_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 49/81: gamma_50.0_step_0.1_rl_25_budget_25_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.1_rl_25_budget_25/final_model.zip' '$LOCAL_DIR/gamma_50.0_step_0.1_rl_25_budget_25_final_model.zip' 'gamma_50.0_step_0.1_rl_25_budget_25_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 50/81: gamma_50.0_step_0.1_rl_25_budget_30_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_50.0_step_0.1_rl_25_budget_30_final_model.zip"; then
    echo 'Skipping 50/81: gamma_50.0_step_0.1_rl_25_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 50/81: gamma_50.0_step_0.1_rl_25_budget_30_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.1_rl_25_budget_30/final_model.zip' '$LOCAL_DIR/gamma_50.0_step_0.1_rl_25_budget_30_final_model.zip' 'gamma_50.0_step_0.1_rl_25_budget_30_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

echo 'Completed batch 5. Waiting 2 seconds...'
sleep 2

# === BATCH 6 ===
echo 'Starting batch 6 (files 51-60)...'

# Transfer 51/81: gamma_50.0_step_0.1_rl_25_budget_40_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_50.0_step_0.1_rl_25_budget_40_final_model.zip"; then
    echo 'Skipping 51/81: gamma_50.0_step_0.1_rl_25_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 51/81: gamma_50.0_step_0.1_rl_25_budget_40_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.1_rl_25_budget_40/final_model.zip' '$LOCAL_DIR/gamma_50.0_step_0.1_rl_25_budget_40_final_model.zip' 'gamma_50.0_step_0.1_rl_25_budget_40_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 52/81: gamma_50.0_step_0.1_rl_40_budget_25_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_50.0_step_0.1_rl_40_budget_25_final_model.zip"; then
    echo 'Skipping 52/81: gamma_50.0_step_0.1_rl_40_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 52/81: gamma_50.0_step_0.1_rl_40_budget_25_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.1_rl_40_budget_25/final_model.zip' '$LOCAL_DIR/gamma_50.0_step_0.1_rl_40_budget_25_final_model.zip' 'gamma_50.0_step_0.1_rl_40_budget_25_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 53/81: gamma_50.0_step_0.1_rl_40_budget_30_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_50.0_step_0.1_rl_40_budget_30_final_model.zip"; then
    echo 'Skipping 53/81: gamma_50.0_step_0.1_rl_40_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 53/81: gamma_50.0_step_0.1_rl_40_budget_30_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.1_rl_40_budget_30/final_model.zip' '$LOCAL_DIR/gamma_50.0_step_0.1_rl_40_budget_30_final_model.zip' 'gamma_50.0_step_0.1_rl_40_budget_30_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 54/81: gamma_50.0_step_0.1_rl_40_budget_40_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_50.0_step_0.1_rl_40_budget_40_final_model.zip"; then
    echo 'Skipping 54/81: gamma_50.0_step_0.1_rl_40_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 54/81: gamma_50.0_step_0.1_rl_40_budget_40_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.1_rl_40_budget_40/final_model.zip' '$LOCAL_DIR/gamma_50.0_step_0.1_rl_40_budget_40_final_model.zip' 'gamma_50.0_step_0.1_rl_40_budget_40_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 55/81: gamma_100.0_step_0.025_rl_10_budget_25_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_100.0_step_0.025_rl_10_budget_25_final_model.zip"; then
    echo 'Skipping 55/81: gamma_100.0_step_0.025_rl_10_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 55/81: gamma_100.0_step_0.025_rl_10_budget_25_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.025_rl_10_budget_25/final_model.zip' '$LOCAL_DIR/gamma_100.0_step_0.025_rl_10_budget_25_final_model.zip' 'gamma_100.0_step_0.025_rl_10_budget_25_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 56/81: gamma_100.0_step_0.025_rl_10_budget_30_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_100.0_step_0.025_rl_10_budget_30_final_model.zip"; then
    echo 'Skipping 56/81: gamma_100.0_step_0.025_rl_10_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 56/81: gamma_100.0_step_0.025_rl_10_budget_30_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.025_rl_10_budget_30/final_model.zip' '$LOCAL_DIR/gamma_100.0_step_0.025_rl_10_budget_30_final_model.zip' 'gamma_100.0_step_0.025_rl_10_budget_30_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 57/81: gamma_100.0_step_0.025_rl_10_budget_40_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_100.0_step_0.025_rl_10_budget_40_final_model.zip"; then
    echo 'Skipping 57/81: gamma_100.0_step_0.025_rl_10_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 57/81: gamma_100.0_step_0.025_rl_10_budget_40_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.025_rl_10_budget_40/final_model.zip' '$LOCAL_DIR/gamma_100.0_step_0.025_rl_10_budget_40_final_model.zip' 'gamma_100.0_step_0.025_rl_10_budget_40_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 58/81: gamma_100.0_step_0.025_rl_25_budget_25_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_100.0_step_0.025_rl_25_budget_25_final_model.zip"; then
    echo 'Skipping 58/81: gamma_100.0_step_0.025_rl_25_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 58/81: gamma_100.0_step_0.025_rl_25_budget_25_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.025_rl_25_budget_25/final_model.zip' '$LOCAL_DIR/gamma_100.0_step_0.025_rl_25_budget_25_final_model.zip' 'gamma_100.0_step_0.025_rl_25_budget_25_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 59/81: gamma_100.0_step_0.025_rl_25_budget_30_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_100.0_step_0.025_rl_25_budget_30_final_model.zip"; then
    echo 'Skipping 59/81: gamma_100.0_step_0.025_rl_25_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 59/81: gamma_100.0_step_0.025_rl_25_budget_30_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.025_rl_25_budget_30/final_model.zip' '$LOCAL_DIR/gamma_100.0_step_0.025_rl_25_budget_30_final_model.zip' 'gamma_100.0_step_0.025_rl_25_budget_30_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 60/81: gamma_100.0_step_0.025_rl_25_budget_40_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_100.0_step_0.025_rl_25_budget_40_final_model.zip"; then
    echo 'Skipping 60/81: gamma_100.0_step_0.025_rl_25_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 60/81: gamma_100.0_step_0.025_rl_25_budget_40_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.025_rl_25_budget_40/final_model.zip' '$LOCAL_DIR/gamma_100.0_step_0.025_rl_25_budget_40_final_model.zip' 'gamma_100.0_step_0.025_rl_25_budget_40_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

echo 'Completed batch 6. Waiting 2 seconds...'
sleep 2

# === BATCH 7 ===
echo 'Starting batch 7 (files 61-70)...'

# Transfer 61/81: gamma_100.0_step_0.025_rl_40_budget_25_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_100.0_step_0.025_rl_40_budget_25_final_model.zip"; then
    echo 'Skipping 61/81: gamma_100.0_step_0.025_rl_40_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 61/81: gamma_100.0_step_0.025_rl_40_budget_25_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.025_rl_40_budget_25/final_model.zip' '$LOCAL_DIR/gamma_100.0_step_0.025_rl_40_budget_25_final_model.zip' 'gamma_100.0_step_0.025_rl_40_budget_25_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 62/81: gamma_100.0_step_0.025_rl_40_budget_30_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_100.0_step_0.025_rl_40_budget_30_final_model.zip"; then
    echo 'Skipping 62/81: gamma_100.0_step_0.025_rl_40_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 62/81: gamma_100.0_step_0.025_rl_40_budget_30_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.025_rl_40_budget_30/final_model.zip' '$LOCAL_DIR/gamma_100.0_step_0.025_rl_40_budget_30_final_model.zip' 'gamma_100.0_step_0.025_rl_40_budget_30_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 63/81: gamma_100.0_step_0.025_rl_40_budget_40_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_100.0_step_0.025_rl_40_budget_40_final_model.zip"; then
    echo 'Skipping 63/81: gamma_100.0_step_0.025_rl_40_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 63/81: gamma_100.0_step_0.025_rl_40_budget_40_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.025_rl_40_budget_40/final_model.zip' '$LOCAL_DIR/gamma_100.0_step_0.025_rl_40_budget_40_final_model.zip' 'gamma_100.0_step_0.025_rl_40_budget_40_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 64/81: gamma_100.0_step_0.05_rl_10_budget_25_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_100.0_step_0.05_rl_10_budget_25_final_model.zip"; then
    echo 'Skipping 64/81: gamma_100.0_step_0.05_rl_10_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 64/81: gamma_100.0_step_0.05_rl_10_budget_25_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.05_rl_10_budget_25/final_model.zip' '$LOCAL_DIR/gamma_100.0_step_0.05_rl_10_budget_25_final_model.zip' 'gamma_100.0_step_0.05_rl_10_budget_25_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 65/81: gamma_100.0_step_0.05_rl_10_budget_30_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_100.0_step_0.05_rl_10_budget_30_final_model.zip"; then
    echo 'Skipping 65/81: gamma_100.0_step_0.05_rl_10_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 65/81: gamma_100.0_step_0.05_rl_10_budget_30_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.05_rl_10_budget_30/final_model.zip' '$LOCAL_DIR/gamma_100.0_step_0.05_rl_10_budget_30_final_model.zip' 'gamma_100.0_step_0.05_rl_10_budget_30_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 66/81: gamma_100.0_step_0.05_rl_10_budget_40_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_100.0_step_0.05_rl_10_budget_40_final_model.zip"; then
    echo 'Skipping 66/81: gamma_100.0_step_0.05_rl_10_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 66/81: gamma_100.0_step_0.05_rl_10_budget_40_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.05_rl_10_budget_40/final_model.zip' '$LOCAL_DIR/gamma_100.0_step_0.05_rl_10_budget_40_final_model.zip' 'gamma_100.0_step_0.05_rl_10_budget_40_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 67/81: gamma_100.0_step_0.05_rl_25_budget_25_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_100.0_step_0.05_rl_25_budget_25_final_model.zip"; then
    echo 'Skipping 67/81: gamma_100.0_step_0.05_rl_25_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 67/81: gamma_100.0_step_0.05_rl_25_budget_25_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.05_rl_25_budget_25/final_model.zip' '$LOCAL_DIR/gamma_100.0_step_0.05_rl_25_budget_25_final_model.zip' 'gamma_100.0_step_0.05_rl_25_budget_25_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 68/81: gamma_100.0_step_0.05_rl_25_budget_30_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_100.0_step_0.05_rl_25_budget_30_final_model.zip"; then
    echo 'Skipping 68/81: gamma_100.0_step_0.05_rl_25_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 68/81: gamma_100.0_step_0.05_rl_25_budget_30_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.05_rl_25_budget_30/final_model.zip' '$LOCAL_DIR/gamma_100.0_step_0.05_rl_25_budget_30_final_model.zip' 'gamma_100.0_step_0.05_rl_25_budget_30_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 69/81: gamma_100.0_step_0.05_rl_25_budget_40_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_100.0_step_0.05_rl_25_budget_40_final_model.zip"; then
    echo 'Skipping 69/81: gamma_100.0_step_0.05_rl_25_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 69/81: gamma_100.0_step_0.05_rl_25_budget_40_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.05_rl_25_budget_40/final_model.zip' '$LOCAL_DIR/gamma_100.0_step_0.05_rl_25_budget_40_final_model.zip' 'gamma_100.0_step_0.05_rl_25_budget_40_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 70/81: gamma_100.0_step_0.05_rl_40_budget_25_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_100.0_step_0.05_rl_40_budget_25_final_model.zip"; then
    echo 'Skipping 70/81: gamma_100.0_step_0.05_rl_40_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 70/81: gamma_100.0_step_0.05_rl_40_budget_25_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.05_rl_40_budget_25/final_model.zip' '$LOCAL_DIR/gamma_100.0_step_0.05_rl_40_budget_25_final_model.zip' 'gamma_100.0_step_0.05_rl_40_budget_25_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

echo 'Completed batch 7. Waiting 2 seconds...'
sleep 2

# === BATCH 8 ===
echo 'Starting batch 8 (files 71-80)...'

# Transfer 71/81: gamma_100.0_step_0.05_rl_40_budget_30_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_100.0_step_0.05_rl_40_budget_30_final_model.zip"; then
    echo 'Skipping 71/81: gamma_100.0_step_0.05_rl_40_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 71/81: gamma_100.0_step_0.05_rl_40_budget_30_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.05_rl_40_budget_30/final_model.zip' '$LOCAL_DIR/gamma_100.0_step_0.05_rl_40_budget_30_final_model.zip' 'gamma_100.0_step_0.05_rl_40_budget_30_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 72/81: gamma_100.0_step_0.05_rl_40_budget_40_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_100.0_step_0.05_rl_40_budget_40_final_model.zip"; then
    echo 'Skipping 72/81: gamma_100.0_step_0.05_rl_40_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 72/81: gamma_100.0_step_0.05_rl_40_budget_40_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.05_rl_40_budget_40/final_model.zip' '$LOCAL_DIR/gamma_100.0_step_0.05_rl_40_budget_40_final_model.zip' 'gamma_100.0_step_0.05_rl_40_budget_40_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 73/81: gamma_100.0_step_0.1_rl_10_budget_25_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_100.0_step_0.1_rl_10_budget_25_final_model.zip"; then
    echo 'Skipping 73/81: gamma_100.0_step_0.1_rl_10_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 73/81: gamma_100.0_step_0.1_rl_10_budget_25_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.1_rl_10_budget_25/final_model.zip' '$LOCAL_DIR/gamma_100.0_step_0.1_rl_10_budget_25_final_model.zip' 'gamma_100.0_step_0.1_rl_10_budget_25_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 74/81: gamma_100.0_step_0.1_rl_10_budget_30_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_100.0_step_0.1_rl_10_budget_30_final_model.zip"; then
    echo 'Skipping 74/81: gamma_100.0_step_0.1_rl_10_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 74/81: gamma_100.0_step_0.1_rl_10_budget_30_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.1_rl_10_budget_30/final_model.zip' '$LOCAL_DIR/gamma_100.0_step_0.1_rl_10_budget_30_final_model.zip' 'gamma_100.0_step_0.1_rl_10_budget_30_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 75/81: gamma_100.0_step_0.1_rl_10_budget_40_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_100.0_step_0.1_rl_10_budget_40_final_model.zip"; then
    echo 'Skipping 75/81: gamma_100.0_step_0.1_rl_10_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 75/81: gamma_100.0_step_0.1_rl_10_budget_40_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.1_rl_10_budget_40/final_model.zip' '$LOCAL_DIR/gamma_100.0_step_0.1_rl_10_budget_40_final_model.zip' 'gamma_100.0_step_0.1_rl_10_budget_40_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 76/81: gamma_100.0_step_0.1_rl_25_budget_25_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_100.0_step_0.1_rl_25_budget_25_final_model.zip"; then
    echo 'Skipping 76/81: gamma_100.0_step_0.1_rl_25_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 76/81: gamma_100.0_step_0.1_rl_25_budget_25_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.1_rl_25_budget_25/final_model.zip' '$LOCAL_DIR/gamma_100.0_step_0.1_rl_25_budget_25_final_model.zip' 'gamma_100.0_step_0.1_rl_25_budget_25_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 77/81: gamma_100.0_step_0.1_rl_25_budget_30_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_100.0_step_0.1_rl_25_budget_30_final_model.zip"; then
    echo 'Skipping 77/81: gamma_100.0_step_0.1_rl_25_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 77/81: gamma_100.0_step_0.1_rl_25_budget_30_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.1_rl_25_budget_30/final_model.zip' '$LOCAL_DIR/gamma_100.0_step_0.1_rl_25_budget_30_final_model.zip' 'gamma_100.0_step_0.1_rl_25_budget_30_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 78/81: gamma_100.0_step_0.1_rl_25_budget_40_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_100.0_step_0.1_rl_25_budget_40_final_model.zip"; then
    echo 'Skipping 78/81: gamma_100.0_step_0.1_rl_25_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 78/81: gamma_100.0_step_0.1_rl_25_budget_40_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.1_rl_25_budget_40/final_model.zip' '$LOCAL_DIR/gamma_100.0_step_0.1_rl_25_budget_40_final_model.zip' 'gamma_100.0_step_0.1_rl_25_budget_40_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 79/81: gamma_100.0_step_0.1_rl_40_budget_25_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_100.0_step_0.1_rl_40_budget_25_final_model.zip"; then
    echo 'Skipping 79/81: gamma_100.0_step_0.1_rl_40_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 79/81: gamma_100.0_step_0.1_rl_40_budget_25_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.1_rl_40_budget_25/final_model.zip' '$LOCAL_DIR/gamma_100.0_step_0.1_rl_40_budget_25_final_model.zip' 'gamma_100.0_step_0.1_rl_40_budget_25_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Transfer 80/81: gamma_100.0_step_0.1_rl_40_budget_30_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_100.0_step_0.1_rl_40_budget_30_final_model.zip"; then
    echo 'Skipping 80/81: gamma_100.0_step_0.1_rl_40_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 80/81: gamma_100.0_step_0.1_rl_40_budget_30_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.1_rl_40_budget_30/final_model.zip' '$LOCAL_DIR/gamma_100.0_step_0.1_rl_40_budget_30_final_model.zip' 'gamma_100.0_step_0.1_rl_40_budget_30_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

echo 'Completed batch 8. Waiting 2 seconds...'
sleep 2

# === BATCH 9 ===
echo 'Starting batch 9 (files 81-81)...'

# Transfer 81/81: gamma_100.0_step_0.1_rl_40_budget_40_final_model.zip
if file_exists_and_valid "$LOCAL_DIR/gamma_100.0_step_0.1_rl_40_budget_40_final_model.zip"; then
    echo 'Skipping 81/81: gamma_100.0_step_0.1_rl_40_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 81/81: gamma_100.0_step_0.1_rl_40_budget_40_final_model.zip'
    if transfer_with_retry 'antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.1_rl_40_budget_40/final_model.zip' '$LOCAL_DIR/gamma_100.0_step_0.1_rl_40_budget_40_final_model.zip' 'gamma_100.0_step_0.1_rl_40_budget_40_final_model.zip'; then
        ((transferred++))
    else
        ((failed++))
    fi
fi

# Final summary
echo '=================================='
echo 'Transfer Summary:'
echo "  Transferred: $transferred"
echo "  Skipped (already existed): $skipped"
echo "  Failed: $failed"
echo "  Total: 81"
echo '=================================='

if [[ -f failed_transfers.txt ]]; then
    echo 'Failed transfers saved to: failed_transfers.txt'
    echo 'You can retry these manually or re-run this script'
fi

echo 'Files in destination:'
ls -1 "$LOCAL_DIR" | wc -l
echo "Location: $LOCAL_DIR"