#!/bin/bash
echo "Submitting TEST parameter sweep..."
echo "2 combinations, 2000 timesteps each (~10 minutes total)"
echo ""

JOB_ID=$(sbatch slurm_scripts/test_param_sweep.slurm | cut -d' ' -f4)
echo "Test job submitted with ID: $JOB_ID"
echo ""
echo "Monitor with:"
echo "  squeue -u $USER"
echo "  watch -n 10 'squeue -u $USER'"
echo ""
echo "Check results in: results/test_param_sweep_2025-08-11_144339/"
