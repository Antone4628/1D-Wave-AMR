#!/bin/bash
# Auto-generated model transfer commands with resume capability
# Generated for parameter sweep: full_param_sweep_data_20250601_105453
# Total combinations: 81

# Create destination directory
mkdir -p "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601"

# Counters
transferred=0
skipped=0

echo 'Starting transfer of 81 models...'
echo 'Destination: /Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601'
echo 'Will skip files that already exist and are > 1KB'
echo

# Transfer 1/81: gamma_25.0_step_0.025_rl_10_budget_25_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_10_budget_25_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_10_budget_25_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_10_budget_25_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 1/81: gamma_25.0_step_0.025_rl_10_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 1/81: gamma_25.0_step_0.025_rl_10_budget_25_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.025_rl_10_budget_25/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_10_budget_25_final_model.zip"; then
        echo '✅ Success: gamma_25.0_step_0.025_rl_10_budget_25_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_25.0_step_0.025_rl_10_budget_25_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 2/81: gamma_25.0_step_0.025_rl_10_budget_30_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_10_budget_30_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_10_budget_30_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_10_budget_30_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 2/81: gamma_25.0_step_0.025_rl_10_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 2/81: gamma_25.0_step_0.025_rl_10_budget_30_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.025_rl_10_budget_30/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_10_budget_30_final_model.zip"; then
        echo '✅ Success: gamma_25.0_step_0.025_rl_10_budget_30_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_25.0_step_0.025_rl_10_budget_30_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 3/81: gamma_25.0_step_0.025_rl_10_budget_40_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_10_budget_40_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_10_budget_40_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_10_budget_40_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 3/81: gamma_25.0_step_0.025_rl_10_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 3/81: gamma_25.0_step_0.025_rl_10_budget_40_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.025_rl_10_budget_40/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_10_budget_40_final_model.zip"; then
        echo '✅ Success: gamma_25.0_step_0.025_rl_10_budget_40_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_25.0_step_0.025_rl_10_budget_40_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 4/81: gamma_25.0_step_0.025_rl_25_budget_25_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_25_budget_25_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_25_budget_25_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_25_budget_25_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 4/81: gamma_25.0_step_0.025_rl_25_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 4/81: gamma_25.0_step_0.025_rl_25_budget_25_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.025_rl_25_budget_25/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_25_budget_25_final_model.zip"; then
        echo '✅ Success: gamma_25.0_step_0.025_rl_25_budget_25_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_25.0_step_0.025_rl_25_budget_25_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 5/81: gamma_25.0_step_0.025_rl_25_budget_30_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_25_budget_30_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_25_budget_30_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_25_budget_30_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 5/81: gamma_25.0_step_0.025_rl_25_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 5/81: gamma_25.0_step_0.025_rl_25_budget_30_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.025_rl_25_budget_30/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_25_budget_30_final_model.zip"; then
        echo '✅ Success: gamma_25.0_step_0.025_rl_25_budget_30_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_25.0_step_0.025_rl_25_budget_30_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 6/81: gamma_25.0_step_0.025_rl_25_budget_40_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_25_budget_40_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_25_budget_40_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_25_budget_40_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 6/81: gamma_25.0_step_0.025_rl_25_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 6/81: gamma_25.0_step_0.025_rl_25_budget_40_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.025_rl_25_budget_40/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_25_budget_40_final_model.zip"; then
        echo '✅ Success: gamma_25.0_step_0.025_rl_25_budget_40_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_25.0_step_0.025_rl_25_budget_40_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 7/81: gamma_25.0_step_0.025_rl_40_budget_25_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_40_budget_25_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_40_budget_25_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_40_budget_25_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 7/81: gamma_25.0_step_0.025_rl_40_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 7/81: gamma_25.0_step_0.025_rl_40_budget_25_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.025_rl_40_budget_25/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_40_budget_25_final_model.zip"; then
        echo '✅ Success: gamma_25.0_step_0.025_rl_40_budget_25_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_25.0_step_0.025_rl_40_budget_25_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 8/81: gamma_25.0_step_0.025_rl_40_budget_30_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_40_budget_30_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_40_budget_30_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_40_budget_30_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 8/81: gamma_25.0_step_0.025_rl_40_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 8/81: gamma_25.0_step_0.025_rl_40_budget_30_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.025_rl_40_budget_30/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_40_budget_30_final_model.zip"; then
        echo '✅ Success: gamma_25.0_step_0.025_rl_40_budget_30_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_25.0_step_0.025_rl_40_budget_30_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 9/81: gamma_25.0_step_0.025_rl_40_budget_40_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_40_budget_40_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_40_budget_40_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_40_budget_40_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 9/81: gamma_25.0_step_0.025_rl_40_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 9/81: gamma_25.0_step_0.025_rl_40_budget_40_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.025_rl_40_budget_40/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.025_rl_40_budget_40_final_model.zip"; then
        echo '✅ Success: gamma_25.0_step_0.025_rl_40_budget_40_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_25.0_step_0.025_rl_40_budget_40_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 10/81: gamma_25.0_step_0.05_rl_10_budget_25_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_10_budget_25_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_10_budget_25_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_10_budget_25_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 10/81: gamma_25.0_step_0.05_rl_10_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 10/81: gamma_25.0_step_0.05_rl_10_budget_25_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.05_rl_10_budget_25/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_10_budget_25_final_model.zip"; then
        echo '✅ Success: gamma_25.0_step_0.05_rl_10_budget_25_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_25.0_step_0.05_rl_10_budget_25_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 11/81: gamma_25.0_step_0.05_rl_10_budget_30_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_10_budget_30_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_10_budget_30_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_10_budget_30_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 11/81: gamma_25.0_step_0.05_rl_10_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 11/81: gamma_25.0_step_0.05_rl_10_budget_30_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.05_rl_10_budget_30/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_10_budget_30_final_model.zip"; then
        echo '✅ Success: gamma_25.0_step_0.05_rl_10_budget_30_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_25.0_step_0.05_rl_10_budget_30_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 12/81: gamma_25.0_step_0.05_rl_10_budget_40_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_10_budget_40_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_10_budget_40_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_10_budget_40_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 12/81: gamma_25.0_step_0.05_rl_10_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 12/81: gamma_25.0_step_0.05_rl_10_budget_40_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.05_rl_10_budget_40/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_10_budget_40_final_model.zip"; then
        echo '✅ Success: gamma_25.0_step_0.05_rl_10_budget_40_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_25.0_step_0.05_rl_10_budget_40_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 13/81: gamma_25.0_step_0.05_rl_25_budget_25_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_25_budget_25_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_25_budget_25_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_25_budget_25_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 13/81: gamma_25.0_step_0.05_rl_25_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 13/81: gamma_25.0_step_0.05_rl_25_budget_25_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.05_rl_25_budget_25/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_25_budget_25_final_model.zip"; then
        echo '✅ Success: gamma_25.0_step_0.05_rl_25_budget_25_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_25.0_step_0.05_rl_25_budget_25_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 14/81: gamma_25.0_step_0.05_rl_25_budget_30_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_25_budget_30_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_25_budget_30_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_25_budget_30_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 14/81: gamma_25.0_step_0.05_rl_25_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 14/81: gamma_25.0_step_0.05_rl_25_budget_30_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.05_rl_25_budget_30/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_25_budget_30_final_model.zip"; then
        echo '✅ Success: gamma_25.0_step_0.05_rl_25_budget_30_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_25.0_step_0.05_rl_25_budget_30_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 15/81: gamma_25.0_step_0.05_rl_25_budget_40_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_25_budget_40_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_25_budget_40_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_25_budget_40_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 15/81: gamma_25.0_step_0.05_rl_25_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 15/81: gamma_25.0_step_0.05_rl_25_budget_40_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.05_rl_25_budget_40/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_25_budget_40_final_model.zip"; then
        echo '✅ Success: gamma_25.0_step_0.05_rl_25_budget_40_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_25.0_step_0.05_rl_25_budget_40_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 16/81: gamma_25.0_step_0.05_rl_40_budget_25_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_40_budget_25_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_40_budget_25_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_40_budget_25_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 16/81: gamma_25.0_step_0.05_rl_40_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 16/81: gamma_25.0_step_0.05_rl_40_budget_25_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.05_rl_40_budget_25/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_40_budget_25_final_model.zip"; then
        echo '✅ Success: gamma_25.0_step_0.05_rl_40_budget_25_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_25.0_step_0.05_rl_40_budget_25_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 17/81: gamma_25.0_step_0.05_rl_40_budget_30_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_40_budget_30_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_40_budget_30_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_40_budget_30_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 17/81: gamma_25.0_step_0.05_rl_40_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 17/81: gamma_25.0_step_0.05_rl_40_budget_30_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.05_rl_40_budget_30/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_40_budget_30_final_model.zip"; then
        echo '✅ Success: gamma_25.0_step_0.05_rl_40_budget_30_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_25.0_step_0.05_rl_40_budget_30_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 18/81: gamma_25.0_step_0.05_rl_40_budget_40_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_40_budget_40_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_40_budget_40_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_40_budget_40_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 18/81: gamma_25.0_step_0.05_rl_40_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 18/81: gamma_25.0_step_0.05_rl_40_budget_40_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.05_rl_40_budget_40/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.05_rl_40_budget_40_final_model.zip"; then
        echo '✅ Success: gamma_25.0_step_0.05_rl_40_budget_40_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_25.0_step_0.05_rl_40_budget_40_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 19/81: gamma_25.0_step_0.1_rl_10_budget_25_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_10_budget_25_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_10_budget_25_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_10_budget_25_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 19/81: gamma_25.0_step_0.1_rl_10_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 19/81: gamma_25.0_step_0.1_rl_10_budget_25_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.1_rl_10_budget_25/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_10_budget_25_final_model.zip"; then
        echo '✅ Success: gamma_25.0_step_0.1_rl_10_budget_25_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_25.0_step_0.1_rl_10_budget_25_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 20/81: gamma_25.0_step_0.1_rl_10_budget_30_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_10_budget_30_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_10_budget_30_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_10_budget_30_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 20/81: gamma_25.0_step_0.1_rl_10_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 20/81: gamma_25.0_step_0.1_rl_10_budget_30_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.1_rl_10_budget_30/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_10_budget_30_final_model.zip"; then
        echo '✅ Success: gamma_25.0_step_0.1_rl_10_budget_30_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_25.0_step_0.1_rl_10_budget_30_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 21/81: gamma_25.0_step_0.1_rl_10_budget_40_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_10_budget_40_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_10_budget_40_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_10_budget_40_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 21/81: gamma_25.0_step_0.1_rl_10_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 21/81: gamma_25.0_step_0.1_rl_10_budget_40_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.1_rl_10_budget_40/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_10_budget_40_final_model.zip"; then
        echo '✅ Success: gamma_25.0_step_0.1_rl_10_budget_40_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_25.0_step_0.1_rl_10_budget_40_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 22/81: gamma_25.0_step_0.1_rl_25_budget_25_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_25_budget_25_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_25_budget_25_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_25_budget_25_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 22/81: gamma_25.0_step_0.1_rl_25_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 22/81: gamma_25.0_step_0.1_rl_25_budget_25_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.1_rl_25_budget_25/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_25_budget_25_final_model.zip"; then
        echo '✅ Success: gamma_25.0_step_0.1_rl_25_budget_25_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_25.0_step_0.1_rl_25_budget_25_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 23/81: gamma_25.0_step_0.1_rl_25_budget_30_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_25_budget_30_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_25_budget_30_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_25_budget_30_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 23/81: gamma_25.0_step_0.1_rl_25_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 23/81: gamma_25.0_step_0.1_rl_25_budget_30_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.1_rl_25_budget_30/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_25_budget_30_final_model.zip"; then
        echo '✅ Success: gamma_25.0_step_0.1_rl_25_budget_30_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_25.0_step_0.1_rl_25_budget_30_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 24/81: gamma_25.0_step_0.1_rl_25_budget_40_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_25_budget_40_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_25_budget_40_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_25_budget_40_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 24/81: gamma_25.0_step_0.1_rl_25_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 24/81: gamma_25.0_step_0.1_rl_25_budget_40_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.1_rl_25_budget_40/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_25_budget_40_final_model.zip"; then
        echo '✅ Success: gamma_25.0_step_0.1_rl_25_budget_40_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_25.0_step_0.1_rl_25_budget_40_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 25/81: gamma_25.0_step_0.1_rl_40_budget_25_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_40_budget_25_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_40_budget_25_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_40_budget_25_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 25/81: gamma_25.0_step_0.1_rl_40_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 25/81: gamma_25.0_step_0.1_rl_40_budget_25_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.1_rl_40_budget_25/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_40_budget_25_final_model.zip"; then
        echo '✅ Success: gamma_25.0_step_0.1_rl_40_budget_25_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_25.0_step_0.1_rl_40_budget_25_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 26/81: gamma_25.0_step_0.1_rl_40_budget_30_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_40_budget_30_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_40_budget_30_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_40_budget_30_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 26/81: gamma_25.0_step_0.1_rl_40_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 26/81: gamma_25.0_step_0.1_rl_40_budget_30_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.1_rl_40_budget_30/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_40_budget_30_final_model.zip"; then
        echo '✅ Success: gamma_25.0_step_0.1_rl_40_budget_30_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_25.0_step_0.1_rl_40_budget_30_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 27/81: gamma_25.0_step_0.1_rl_40_budget_40_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_40_budget_40_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_40_budget_40_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_40_budget_40_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 27/81: gamma_25.0_step_0.1_rl_40_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 27/81: gamma_25.0_step_0.1_rl_40_budget_40_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_25.0_step_0.1_rl_40_budget_40/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_25.0_step_0.1_rl_40_budget_40_final_model.zip"; then
        echo '✅ Success: gamma_25.0_step_0.1_rl_40_budget_40_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_25.0_step_0.1_rl_40_budget_40_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 28/81: gamma_50.0_step_0.025_rl_10_budget_25_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_10_budget_25_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_10_budget_25_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_10_budget_25_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 28/81: gamma_50.0_step_0.025_rl_10_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 28/81: gamma_50.0_step_0.025_rl_10_budget_25_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.025_rl_10_budget_25/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_10_budget_25_final_model.zip"; then
        echo '✅ Success: gamma_50.0_step_0.025_rl_10_budget_25_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_50.0_step_0.025_rl_10_budget_25_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 29/81: gamma_50.0_step_0.025_rl_10_budget_30_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_10_budget_30_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_10_budget_30_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_10_budget_30_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 29/81: gamma_50.0_step_0.025_rl_10_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 29/81: gamma_50.0_step_0.025_rl_10_budget_30_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.025_rl_10_budget_30/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_10_budget_30_final_model.zip"; then
        echo '✅ Success: gamma_50.0_step_0.025_rl_10_budget_30_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_50.0_step_0.025_rl_10_budget_30_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 30/81: gamma_50.0_step_0.025_rl_10_budget_40_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_10_budget_40_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_10_budget_40_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_10_budget_40_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 30/81: gamma_50.0_step_0.025_rl_10_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 30/81: gamma_50.0_step_0.025_rl_10_budget_40_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.025_rl_10_budget_40/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_10_budget_40_final_model.zip"; then
        echo '✅ Success: gamma_50.0_step_0.025_rl_10_budget_40_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_50.0_step_0.025_rl_10_budget_40_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 31/81: gamma_50.0_step_0.025_rl_25_budget_25_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_25_budget_25_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_25_budget_25_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_25_budget_25_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 31/81: gamma_50.0_step_0.025_rl_25_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 31/81: gamma_50.0_step_0.025_rl_25_budget_25_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.025_rl_25_budget_25/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_25_budget_25_final_model.zip"; then
        echo '✅ Success: gamma_50.0_step_0.025_rl_25_budget_25_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_50.0_step_0.025_rl_25_budget_25_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 32/81: gamma_50.0_step_0.025_rl_25_budget_30_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_25_budget_30_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_25_budget_30_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_25_budget_30_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 32/81: gamma_50.0_step_0.025_rl_25_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 32/81: gamma_50.0_step_0.025_rl_25_budget_30_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.025_rl_25_budget_30/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_25_budget_30_final_model.zip"; then
        echo '✅ Success: gamma_50.0_step_0.025_rl_25_budget_30_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_50.0_step_0.025_rl_25_budget_30_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 33/81: gamma_50.0_step_0.025_rl_25_budget_40_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_25_budget_40_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_25_budget_40_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_25_budget_40_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 33/81: gamma_50.0_step_0.025_rl_25_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 33/81: gamma_50.0_step_0.025_rl_25_budget_40_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.025_rl_25_budget_40/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_25_budget_40_final_model.zip"; then
        echo '✅ Success: gamma_50.0_step_0.025_rl_25_budget_40_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_50.0_step_0.025_rl_25_budget_40_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 34/81: gamma_50.0_step_0.025_rl_40_budget_25_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_40_budget_25_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_40_budget_25_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_40_budget_25_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 34/81: gamma_50.0_step_0.025_rl_40_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 34/81: gamma_50.0_step_0.025_rl_40_budget_25_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.025_rl_40_budget_25/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_40_budget_25_final_model.zip"; then
        echo '✅ Success: gamma_50.0_step_0.025_rl_40_budget_25_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_50.0_step_0.025_rl_40_budget_25_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 35/81: gamma_50.0_step_0.025_rl_40_budget_30_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_40_budget_30_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_40_budget_30_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_40_budget_30_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 35/81: gamma_50.0_step_0.025_rl_40_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 35/81: gamma_50.0_step_0.025_rl_40_budget_30_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.025_rl_40_budget_30/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_40_budget_30_final_model.zip"; then
        echo '✅ Success: gamma_50.0_step_0.025_rl_40_budget_30_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_50.0_step_0.025_rl_40_budget_30_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 36/81: gamma_50.0_step_0.025_rl_40_budget_40_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_40_budget_40_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_40_budget_40_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_40_budget_40_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 36/81: gamma_50.0_step_0.025_rl_40_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 36/81: gamma_50.0_step_0.025_rl_40_budget_40_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.025_rl_40_budget_40/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.025_rl_40_budget_40_final_model.zip"; then
        echo '✅ Success: gamma_50.0_step_0.025_rl_40_budget_40_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_50.0_step_0.025_rl_40_budget_40_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 37/81: gamma_50.0_step_0.05_rl_10_budget_25_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_10_budget_25_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_10_budget_25_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_10_budget_25_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 37/81: gamma_50.0_step_0.05_rl_10_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 37/81: gamma_50.0_step_0.05_rl_10_budget_25_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.05_rl_10_budget_25/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_10_budget_25_final_model.zip"; then
        echo '✅ Success: gamma_50.0_step_0.05_rl_10_budget_25_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_50.0_step_0.05_rl_10_budget_25_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 38/81: gamma_50.0_step_0.05_rl_10_budget_30_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_10_budget_30_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_10_budget_30_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_10_budget_30_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 38/81: gamma_50.0_step_0.05_rl_10_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 38/81: gamma_50.0_step_0.05_rl_10_budget_30_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.05_rl_10_budget_30/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_10_budget_30_final_model.zip"; then
        echo '✅ Success: gamma_50.0_step_0.05_rl_10_budget_30_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_50.0_step_0.05_rl_10_budget_30_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 39/81: gamma_50.0_step_0.05_rl_10_budget_40_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_10_budget_40_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_10_budget_40_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_10_budget_40_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 39/81: gamma_50.0_step_0.05_rl_10_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 39/81: gamma_50.0_step_0.05_rl_10_budget_40_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.05_rl_10_budget_40/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_10_budget_40_final_model.zip"; then
        echo '✅ Success: gamma_50.0_step_0.05_rl_10_budget_40_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_50.0_step_0.05_rl_10_budget_40_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 40/81: gamma_50.0_step_0.05_rl_25_budget_25_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_25_budget_25_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_25_budget_25_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_25_budget_25_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 40/81: gamma_50.0_step_0.05_rl_25_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 40/81: gamma_50.0_step_0.05_rl_25_budget_25_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.05_rl_25_budget_25/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_25_budget_25_final_model.zip"; then
        echo '✅ Success: gamma_50.0_step_0.05_rl_25_budget_25_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_50.0_step_0.05_rl_25_budget_25_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 41/81: gamma_50.0_step_0.05_rl_25_budget_30_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_25_budget_30_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_25_budget_30_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_25_budget_30_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 41/81: gamma_50.0_step_0.05_rl_25_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 41/81: gamma_50.0_step_0.05_rl_25_budget_30_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.05_rl_25_budget_30/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_25_budget_30_final_model.zip"; then
        echo '✅ Success: gamma_50.0_step_0.05_rl_25_budget_30_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_50.0_step_0.05_rl_25_budget_30_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 42/81: gamma_50.0_step_0.05_rl_25_budget_40_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_25_budget_40_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_25_budget_40_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_25_budget_40_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 42/81: gamma_50.0_step_0.05_rl_25_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 42/81: gamma_50.0_step_0.05_rl_25_budget_40_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.05_rl_25_budget_40/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_25_budget_40_final_model.zip"; then
        echo '✅ Success: gamma_50.0_step_0.05_rl_25_budget_40_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_50.0_step_0.05_rl_25_budget_40_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 43/81: gamma_50.0_step_0.05_rl_40_budget_25_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_40_budget_25_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_40_budget_25_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_40_budget_25_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 43/81: gamma_50.0_step_0.05_rl_40_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 43/81: gamma_50.0_step_0.05_rl_40_budget_25_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.05_rl_40_budget_25/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_40_budget_25_final_model.zip"; then
        echo '✅ Success: gamma_50.0_step_0.05_rl_40_budget_25_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_50.0_step_0.05_rl_40_budget_25_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 44/81: gamma_50.0_step_0.05_rl_40_budget_30_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_40_budget_30_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_40_budget_30_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_40_budget_30_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 44/81: gamma_50.0_step_0.05_rl_40_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 44/81: gamma_50.0_step_0.05_rl_40_budget_30_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.05_rl_40_budget_30/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_40_budget_30_final_model.zip"; then
        echo '✅ Success: gamma_50.0_step_0.05_rl_40_budget_30_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_50.0_step_0.05_rl_40_budget_30_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 45/81: gamma_50.0_step_0.05_rl_40_budget_40_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_40_budget_40_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_40_budget_40_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_40_budget_40_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 45/81: gamma_50.0_step_0.05_rl_40_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 45/81: gamma_50.0_step_0.05_rl_40_budget_40_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.05_rl_40_budget_40/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.05_rl_40_budget_40_final_model.zip"; then
        echo '✅ Success: gamma_50.0_step_0.05_rl_40_budget_40_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_50.0_step_0.05_rl_40_budget_40_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 46/81: gamma_50.0_step_0.1_rl_10_budget_25_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_10_budget_25_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_10_budget_25_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_10_budget_25_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 46/81: gamma_50.0_step_0.1_rl_10_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 46/81: gamma_50.0_step_0.1_rl_10_budget_25_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.1_rl_10_budget_25/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_10_budget_25_final_model.zip"; then
        echo '✅ Success: gamma_50.0_step_0.1_rl_10_budget_25_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_50.0_step_0.1_rl_10_budget_25_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 47/81: gamma_50.0_step_0.1_rl_10_budget_30_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_10_budget_30_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_10_budget_30_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_10_budget_30_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 47/81: gamma_50.0_step_0.1_rl_10_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 47/81: gamma_50.0_step_0.1_rl_10_budget_30_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.1_rl_10_budget_30/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_10_budget_30_final_model.zip"; then
        echo '✅ Success: gamma_50.0_step_0.1_rl_10_budget_30_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_50.0_step_0.1_rl_10_budget_30_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 48/81: gamma_50.0_step_0.1_rl_10_budget_40_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_10_budget_40_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_10_budget_40_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_10_budget_40_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 48/81: gamma_50.0_step_0.1_rl_10_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 48/81: gamma_50.0_step_0.1_rl_10_budget_40_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.1_rl_10_budget_40/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_10_budget_40_final_model.zip"; then
        echo '✅ Success: gamma_50.0_step_0.1_rl_10_budget_40_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_50.0_step_0.1_rl_10_budget_40_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 49/81: gamma_50.0_step_0.1_rl_25_budget_25_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_25_budget_25_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_25_budget_25_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_25_budget_25_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 49/81: gamma_50.0_step_0.1_rl_25_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 49/81: gamma_50.0_step_0.1_rl_25_budget_25_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.1_rl_25_budget_25/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_25_budget_25_final_model.zip"; then
        echo '✅ Success: gamma_50.0_step_0.1_rl_25_budget_25_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_50.0_step_0.1_rl_25_budget_25_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 50/81: gamma_50.0_step_0.1_rl_25_budget_30_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_25_budget_30_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_25_budget_30_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_25_budget_30_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 50/81: gamma_50.0_step_0.1_rl_25_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 50/81: gamma_50.0_step_0.1_rl_25_budget_30_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.1_rl_25_budget_30/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_25_budget_30_final_model.zip"; then
        echo '✅ Success: gamma_50.0_step_0.1_rl_25_budget_30_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_50.0_step_0.1_rl_25_budget_30_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 51/81: gamma_50.0_step_0.1_rl_25_budget_40_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_25_budget_40_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_25_budget_40_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_25_budget_40_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 51/81: gamma_50.0_step_0.1_rl_25_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 51/81: gamma_50.0_step_0.1_rl_25_budget_40_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.1_rl_25_budget_40/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_25_budget_40_final_model.zip"; then
        echo '✅ Success: gamma_50.0_step_0.1_rl_25_budget_40_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_50.0_step_0.1_rl_25_budget_40_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 52/81: gamma_50.0_step_0.1_rl_40_budget_25_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_40_budget_25_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_40_budget_25_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_40_budget_25_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 52/81: gamma_50.0_step_0.1_rl_40_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 52/81: gamma_50.0_step_0.1_rl_40_budget_25_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.1_rl_40_budget_25/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_40_budget_25_final_model.zip"; then
        echo '✅ Success: gamma_50.0_step_0.1_rl_40_budget_25_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_50.0_step_0.1_rl_40_budget_25_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 53/81: gamma_50.0_step_0.1_rl_40_budget_30_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_40_budget_30_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_40_budget_30_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_40_budget_30_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 53/81: gamma_50.0_step_0.1_rl_40_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 53/81: gamma_50.0_step_0.1_rl_40_budget_30_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.1_rl_40_budget_30/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_40_budget_30_final_model.zip"; then
        echo '✅ Success: gamma_50.0_step_0.1_rl_40_budget_30_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_50.0_step_0.1_rl_40_budget_30_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 54/81: gamma_50.0_step_0.1_rl_40_budget_40_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_40_budget_40_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_40_budget_40_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_40_budget_40_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 54/81: gamma_50.0_step_0.1_rl_40_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 54/81: gamma_50.0_step_0.1_rl_40_budget_40_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_50.0_step_0.1_rl_40_budget_40/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_50.0_step_0.1_rl_40_budget_40_final_model.zip"; then
        echo '✅ Success: gamma_50.0_step_0.1_rl_40_budget_40_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_50.0_step_0.1_rl_40_budget_40_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 55/81: gamma_100.0_step_0.025_rl_10_budget_25_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_10_budget_25_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_10_budget_25_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_10_budget_25_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 55/81: gamma_100.0_step_0.025_rl_10_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 55/81: gamma_100.0_step_0.025_rl_10_budget_25_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.025_rl_10_budget_25/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_10_budget_25_final_model.zip"; then
        echo '✅ Success: gamma_100.0_step_0.025_rl_10_budget_25_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_100.0_step_0.025_rl_10_budget_25_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 56/81: gamma_100.0_step_0.025_rl_10_budget_30_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_10_budget_30_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_10_budget_30_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_10_budget_30_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 56/81: gamma_100.0_step_0.025_rl_10_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 56/81: gamma_100.0_step_0.025_rl_10_budget_30_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.025_rl_10_budget_30/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_10_budget_30_final_model.zip"; then
        echo '✅ Success: gamma_100.0_step_0.025_rl_10_budget_30_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_100.0_step_0.025_rl_10_budget_30_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 57/81: gamma_100.0_step_0.025_rl_10_budget_40_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_10_budget_40_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_10_budget_40_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_10_budget_40_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 57/81: gamma_100.0_step_0.025_rl_10_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 57/81: gamma_100.0_step_0.025_rl_10_budget_40_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.025_rl_10_budget_40/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_10_budget_40_final_model.zip"; then
        echo '✅ Success: gamma_100.0_step_0.025_rl_10_budget_40_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_100.0_step_0.025_rl_10_budget_40_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 58/81: gamma_100.0_step_0.025_rl_25_budget_25_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_25_budget_25_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_25_budget_25_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_25_budget_25_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 58/81: gamma_100.0_step_0.025_rl_25_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 58/81: gamma_100.0_step_0.025_rl_25_budget_25_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.025_rl_25_budget_25/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_25_budget_25_final_model.zip"; then
        echo '✅ Success: gamma_100.0_step_0.025_rl_25_budget_25_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_100.0_step_0.025_rl_25_budget_25_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 59/81: gamma_100.0_step_0.025_rl_25_budget_30_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_25_budget_30_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_25_budget_30_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_25_budget_30_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 59/81: gamma_100.0_step_0.025_rl_25_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 59/81: gamma_100.0_step_0.025_rl_25_budget_30_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.025_rl_25_budget_30/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_25_budget_30_final_model.zip"; then
        echo '✅ Success: gamma_100.0_step_0.025_rl_25_budget_30_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_100.0_step_0.025_rl_25_budget_30_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 60/81: gamma_100.0_step_0.025_rl_25_budget_40_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_25_budget_40_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_25_budget_40_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_25_budget_40_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 60/81: gamma_100.0_step_0.025_rl_25_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 60/81: gamma_100.0_step_0.025_rl_25_budget_40_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.025_rl_25_budget_40/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_25_budget_40_final_model.zip"; then
        echo '✅ Success: gamma_100.0_step_0.025_rl_25_budget_40_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_100.0_step_0.025_rl_25_budget_40_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 61/81: gamma_100.0_step_0.025_rl_40_budget_25_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_40_budget_25_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_40_budget_25_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_40_budget_25_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 61/81: gamma_100.0_step_0.025_rl_40_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 61/81: gamma_100.0_step_0.025_rl_40_budget_25_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.025_rl_40_budget_25/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_40_budget_25_final_model.zip"; then
        echo '✅ Success: gamma_100.0_step_0.025_rl_40_budget_25_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_100.0_step_0.025_rl_40_budget_25_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 62/81: gamma_100.0_step_0.025_rl_40_budget_30_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_40_budget_30_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_40_budget_30_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_40_budget_30_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 62/81: gamma_100.0_step_0.025_rl_40_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 62/81: gamma_100.0_step_0.025_rl_40_budget_30_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.025_rl_40_budget_30/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_40_budget_30_final_model.zip"; then
        echo '✅ Success: gamma_100.0_step_0.025_rl_40_budget_30_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_100.0_step_0.025_rl_40_budget_30_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 63/81: gamma_100.0_step_0.025_rl_40_budget_40_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_40_budget_40_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_40_budget_40_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_40_budget_40_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 63/81: gamma_100.0_step_0.025_rl_40_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 63/81: gamma_100.0_step_0.025_rl_40_budget_40_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.025_rl_40_budget_40/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.025_rl_40_budget_40_final_model.zip"; then
        echo '✅ Success: gamma_100.0_step_0.025_rl_40_budget_40_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_100.0_step_0.025_rl_40_budget_40_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 64/81: gamma_100.0_step_0.05_rl_10_budget_25_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_10_budget_25_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_10_budget_25_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_10_budget_25_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 64/81: gamma_100.0_step_0.05_rl_10_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 64/81: gamma_100.0_step_0.05_rl_10_budget_25_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.05_rl_10_budget_25/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_10_budget_25_final_model.zip"; then
        echo '✅ Success: gamma_100.0_step_0.05_rl_10_budget_25_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_100.0_step_0.05_rl_10_budget_25_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 65/81: gamma_100.0_step_0.05_rl_10_budget_30_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_10_budget_30_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_10_budget_30_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_10_budget_30_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 65/81: gamma_100.0_step_0.05_rl_10_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 65/81: gamma_100.0_step_0.05_rl_10_budget_30_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.05_rl_10_budget_30/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_10_budget_30_final_model.zip"; then
        echo '✅ Success: gamma_100.0_step_0.05_rl_10_budget_30_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_100.0_step_0.05_rl_10_budget_30_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 66/81: gamma_100.0_step_0.05_rl_10_budget_40_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_10_budget_40_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_10_budget_40_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_10_budget_40_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 66/81: gamma_100.0_step_0.05_rl_10_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 66/81: gamma_100.0_step_0.05_rl_10_budget_40_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.05_rl_10_budget_40/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_10_budget_40_final_model.zip"; then
        echo '✅ Success: gamma_100.0_step_0.05_rl_10_budget_40_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_100.0_step_0.05_rl_10_budget_40_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 67/81: gamma_100.0_step_0.05_rl_25_budget_25_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_25_budget_25_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_25_budget_25_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_25_budget_25_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 67/81: gamma_100.0_step_0.05_rl_25_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 67/81: gamma_100.0_step_0.05_rl_25_budget_25_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.05_rl_25_budget_25/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_25_budget_25_final_model.zip"; then
        echo '✅ Success: gamma_100.0_step_0.05_rl_25_budget_25_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_100.0_step_0.05_rl_25_budget_25_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 68/81: gamma_100.0_step_0.05_rl_25_budget_30_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_25_budget_30_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_25_budget_30_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_25_budget_30_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 68/81: gamma_100.0_step_0.05_rl_25_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 68/81: gamma_100.0_step_0.05_rl_25_budget_30_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.05_rl_25_budget_30/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_25_budget_30_final_model.zip"; then
        echo '✅ Success: gamma_100.0_step_0.05_rl_25_budget_30_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_100.0_step_0.05_rl_25_budget_30_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 69/81: gamma_100.0_step_0.05_rl_25_budget_40_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_25_budget_40_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_25_budget_40_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_25_budget_40_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 69/81: gamma_100.0_step_0.05_rl_25_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 69/81: gamma_100.0_step_0.05_rl_25_budget_40_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.05_rl_25_budget_40/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_25_budget_40_final_model.zip"; then
        echo '✅ Success: gamma_100.0_step_0.05_rl_25_budget_40_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_100.0_step_0.05_rl_25_budget_40_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 70/81: gamma_100.0_step_0.05_rl_40_budget_25_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_40_budget_25_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_40_budget_25_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_40_budget_25_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 70/81: gamma_100.0_step_0.05_rl_40_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 70/81: gamma_100.0_step_0.05_rl_40_budget_25_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.05_rl_40_budget_25/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_40_budget_25_final_model.zip"; then
        echo '✅ Success: gamma_100.0_step_0.05_rl_40_budget_25_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_100.0_step_0.05_rl_40_budget_25_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 71/81: gamma_100.0_step_0.05_rl_40_budget_30_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_40_budget_30_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_40_budget_30_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_40_budget_30_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 71/81: gamma_100.0_step_0.05_rl_40_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 71/81: gamma_100.0_step_0.05_rl_40_budget_30_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.05_rl_40_budget_30/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_40_budget_30_final_model.zip"; then
        echo '✅ Success: gamma_100.0_step_0.05_rl_40_budget_30_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_100.0_step_0.05_rl_40_budget_30_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 72/81: gamma_100.0_step_0.05_rl_40_budget_40_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_40_budget_40_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_40_budget_40_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_40_budget_40_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 72/81: gamma_100.0_step_0.05_rl_40_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 72/81: gamma_100.0_step_0.05_rl_40_budget_40_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.05_rl_40_budget_40/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.05_rl_40_budget_40_final_model.zip"; then
        echo '✅ Success: gamma_100.0_step_0.05_rl_40_budget_40_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_100.0_step_0.05_rl_40_budget_40_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 73/81: gamma_100.0_step_0.1_rl_10_budget_25_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_10_budget_25_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_10_budget_25_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_10_budget_25_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 73/81: gamma_100.0_step_0.1_rl_10_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 73/81: gamma_100.0_step_0.1_rl_10_budget_25_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.1_rl_10_budget_25/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_10_budget_25_final_model.zip"; then
        echo '✅ Success: gamma_100.0_step_0.1_rl_10_budget_25_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_100.0_step_0.1_rl_10_budget_25_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 74/81: gamma_100.0_step_0.1_rl_10_budget_30_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_10_budget_30_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_10_budget_30_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_10_budget_30_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 74/81: gamma_100.0_step_0.1_rl_10_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 74/81: gamma_100.0_step_0.1_rl_10_budget_30_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.1_rl_10_budget_30/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_10_budget_30_final_model.zip"; then
        echo '✅ Success: gamma_100.0_step_0.1_rl_10_budget_30_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_100.0_step_0.1_rl_10_budget_30_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 75/81: gamma_100.0_step_0.1_rl_10_budget_40_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_10_budget_40_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_10_budget_40_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_10_budget_40_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 75/81: gamma_100.0_step_0.1_rl_10_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 75/81: gamma_100.0_step_0.1_rl_10_budget_40_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.1_rl_10_budget_40/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_10_budget_40_final_model.zip"; then
        echo '✅ Success: gamma_100.0_step_0.1_rl_10_budget_40_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_100.0_step_0.1_rl_10_budget_40_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 76/81: gamma_100.0_step_0.1_rl_25_budget_25_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_25_budget_25_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_25_budget_25_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_25_budget_25_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 76/81: gamma_100.0_step_0.1_rl_25_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 76/81: gamma_100.0_step_0.1_rl_25_budget_25_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.1_rl_25_budget_25/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_25_budget_25_final_model.zip"; then
        echo '✅ Success: gamma_100.0_step_0.1_rl_25_budget_25_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_100.0_step_0.1_rl_25_budget_25_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 77/81: gamma_100.0_step_0.1_rl_25_budget_30_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_25_budget_30_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_25_budget_30_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_25_budget_30_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 77/81: gamma_100.0_step_0.1_rl_25_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 77/81: gamma_100.0_step_0.1_rl_25_budget_30_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.1_rl_25_budget_30/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_25_budget_30_final_model.zip"; then
        echo '✅ Success: gamma_100.0_step_0.1_rl_25_budget_30_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_100.0_step_0.1_rl_25_budget_30_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 78/81: gamma_100.0_step_0.1_rl_25_budget_40_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_25_budget_40_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_25_budget_40_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_25_budget_40_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 78/81: gamma_100.0_step_0.1_rl_25_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 78/81: gamma_100.0_step_0.1_rl_25_budget_40_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.1_rl_25_budget_40/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_25_budget_40_final_model.zip"; then
        echo '✅ Success: gamma_100.0_step_0.1_rl_25_budget_40_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_100.0_step_0.1_rl_25_budget_40_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 79/81: gamma_100.0_step_0.1_rl_40_budget_25_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_40_budget_25_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_40_budget_25_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_40_budget_25_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 79/81: gamma_100.0_step_0.1_rl_40_budget_25_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 79/81: gamma_100.0_step_0.1_rl_40_budget_25_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.1_rl_40_budget_25/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_40_budget_25_final_model.zip"; then
        echo '✅ Success: gamma_100.0_step_0.1_rl_40_budget_25_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_100.0_step_0.1_rl_40_budget_25_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 80/81: gamma_100.0_step_0.1_rl_40_budget_30_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_40_budget_30_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_40_budget_30_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_40_budget_30_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 80/81: gamma_100.0_step_0.1_rl_40_budget_30_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 80/81: gamma_100.0_step_0.1_rl_40_budget_30_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.1_rl_40_budget_30/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_40_budget_30_final_model.zip"; then
        echo '✅ Success: gamma_100.0_step_0.1_rl_40_budget_30_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_100.0_step_0.1_rl_40_budget_30_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

# Transfer 81/81: gamma_100.0_step_0.1_rl_40_budget_40_final_model.zip
if [[ -f "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_40_budget_40_final_model.zip" && $(stat -f%z "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_40_budget_40_final_model.zip" 2>/dev/null || stat -c%s "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_40_budget_40_final_model.zip" 2>/dev/null) -gt 1000 ]]; then
    echo 'Skipping 81/81: gamma_100.0_step_0.1_rl_40_budget_40_final_model.zip (already exists)'
    ((skipped++))
else
    echo 'Transferring 81/81: gamma_100.0_step_0.1_rl_40_budget_40_final_model.zip'
    if scp "antonechacartegu@borah-login.boisestate.edu:projects/drl-amr/1D-Wave-AMR/results/full_param_sweep_data_20250601_105453/gamma_100.0_step_0.1_rl_40_budget_40/final_model.zip" "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601/gamma_100.0_step_0.1_rl_40_budget_40_final_model.zip"; then
        echo '✅ Success: gamma_100.0_step_0.1_rl_40_budget_40_final_model.zip'
        ((transferred++))
    else
        echo '❌ Failed: gamma_100.0_step_0.1_rl_40_budget_40_final_model.zip'
    fi
    sleep 0.5  # Small delay to prevent connection issues
fi

echo '=================================='
echo 'Transfer Summary:'
echo "Transferred: $transferred"
echo "Skipped: $skipped"
echo "Total: 81"
echo '=================================='

echo 'Files in destination:'
ls -1 "/Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601" | wc -l
echo 'Location: /Users/antonechacartegui/desktop/1D_wave_AMR/models/transferred/full_sweep_data_20250601'