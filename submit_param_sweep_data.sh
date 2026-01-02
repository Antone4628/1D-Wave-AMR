#!/bin/bash
# Master submission script for parameter sweep WITH DATA EXPORT
# Enhanced with CLI parameterization for flexible timesteps
# Generated: 2026-01-02 07:36:10

echo "Starting 81-Parameter Sweep Submission (Enhanced Data Export Version)"
echo "===================================================================="
echo "🎯 Sweep name: session5_mexican_hat_200k"
echo "📊 Timesteps: 200k uniform"
echo "📁 Output directory: results"
echo "📈 Using enhanced_callback_data for structured JSON/CSV export"
echo ""

# Array to store job IDs
declare -a JOB_IDS

# Submit each group

echo "Submitting Group 1: gamma_25.0_step_0.025 (200k)"
JOB_ID_1=$(sbatch slurm_scripts/param_sweep_data/data_group_01.slurm | cut -d' ' -f4)
echo "  Job ID: $JOB_ID_1"
JOB_IDS+=($JOB_ID_1)
sleep 2  # Brief pause between submissions

echo "Submitting Group 2: gamma_25.0_step_0.05 (200k)"
JOB_ID_2=$(sbatch slurm_scripts/param_sweep_data/data_group_02.slurm | cut -d' ' -f4)
echo "  Job ID: $JOB_ID_2"
JOB_IDS+=($JOB_ID_2)
sleep 2  # Brief pause between submissions

echo "Submitting Group 3: gamma_25.0_step_0.1 (200k)"
JOB_ID_3=$(sbatch slurm_scripts/param_sweep_data/data_group_03.slurm | cut -d' ' -f4)
echo "  Job ID: $JOB_ID_3"
JOB_IDS+=($JOB_ID_3)
sleep 2  # Brief pause between submissions

echo "Submitting Group 4: gamma_50.0_step_0.025 (200k)"
JOB_ID_4=$(sbatch slurm_scripts/param_sweep_data/data_group_04.slurm | cut -d' ' -f4)
echo "  Job ID: $JOB_ID_4"
JOB_IDS+=($JOB_ID_4)
sleep 2  # Brief pause between submissions

echo "Submitting Group 5: gamma_50.0_step_0.05 (200k)"
JOB_ID_5=$(sbatch slurm_scripts/param_sweep_data/data_group_05.slurm | cut -d' ' -f4)
echo "  Job ID: $JOB_ID_5"
JOB_IDS+=($JOB_ID_5)
sleep 2  # Brief pause between submissions

echo "Submitting Group 6: gamma_50.0_step_0.1 (200k)"
JOB_ID_6=$(sbatch slurm_scripts/param_sweep_data/data_group_06.slurm | cut -d' ' -f4)
echo "  Job ID: $JOB_ID_6"
JOB_IDS+=($JOB_ID_6)
sleep 2  # Brief pause between submissions

echo "Submitting Group 7: gamma_100.0_step_0.025 (200k)"
JOB_ID_7=$(sbatch slurm_scripts/param_sweep_data/data_group_07.slurm | cut -d' ' -f4)
echo "  Job ID: $JOB_ID_7"
JOB_IDS+=($JOB_ID_7)
sleep 2  # Brief pause between submissions

echo "Submitting Group 8: gamma_100.0_step_0.05 (200k)"
JOB_ID_8=$(sbatch slurm_scripts/param_sweep_data/data_group_08.slurm | cut -d' ' -f4)
echo "  Job ID: $JOB_ID_8"
JOB_IDS+=($JOB_ID_8)
sleep 2  # Brief pause between submissions

echo "Submitting Group 9: gamma_100.0_step_0.1 (200k)"
JOB_ID_9=$(sbatch slurm_scripts/param_sweep_data/data_group_09.slurm | cut -d' ' -f4)
echo "  Job ID: $JOB_ID_9"
JOB_IDS+=($JOB_ID_9)
sleep 2  # Brief pause between submissions

echo ""
echo "All jobs submitted successfully!"
echo "Total jobs: 9"
echo "Total parameter combinations: 81"
echo "Training load: 81 × 200k = 16.0M total timesteps"
echo "Sweep name: session5_mexican_hat_200k"
echo ""
echo "Job IDs:"
echo "  Group  1: $JOB_ID_1 (200k)"
echo "  Group  2: $JOB_ID_2 (200k)"
echo "  Group  3: $JOB_ID_3 (200k)"
echo "  Group  4: $JOB_ID_4 (200k)"
echo "  Group  5: $JOB_ID_5 (200k)"
echo "  Group  6: $JOB_ID_6 (200k)"
echo "  Group  7: $JOB_ID_7 (200k)"
echo "  Group  8: $JOB_ID_8 (200k)"
echo "  Group  9: $JOB_ID_9 (200k)"

echo ""
echo "Monitor jobs with:"
echo "  squeue -u $USER"
echo "  python3 monitor_param_sweep.py"
echo ""
echo "Expected completion time:"
echo "  All groups (200k): ~10 hours each"
echo ""
echo "Results will be saved to:"
echo "  results/session5_mexican_hat_200k/"
echo ""
echo "Data collection:"
echo "  Structured data: JSON + CSV files for immediate analysis"
echo "  PDF reports: Comprehensive training reports as before"
