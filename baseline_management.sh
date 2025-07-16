#!/bin/bash

# Complete Baseline Management Script
# Manages baseline evaluation for all 25 configurations with conventional-AMR thresholds

function show_help() {
    echo "Usage: $0 [command]"
    echo
    echo "Commands:"
    echo "  cleanup        - Remove existing baseline CSV files"
    echo "  create-jobs    - Create all 25 baseline evaluation SLURM jobs"
    echo "  submit-jobs    - Submit all baseline evaluation jobs"
    echo "  monitor        - Monitor running baseline jobs"
    echo "  check-results  - Check completion status and validate files"
    echo "  test-single    - Test baseline evaluation with a single configuration"
    echo "  full-pipeline  - Run complete pipeline (cleanup -> create -> submit)"
    echo
    echo "Baseline Configuration:"
    echo "  - 25 configurations: ref3-7 × budgets 50,80,100,150,200"
    echo "  - Each job runs 6 thresholds: 0.3, 0.2, 0.1, 0.01, 0.001, 0.0001"
    echo "  - Expected time: 5-15 minutes per job"
    echo "  - Total expected time: ~2-6 hours for all 25 jobs"
    echo
}

function cleanup_baselines() {
    echo "=== Cleaning up existing baseline files ==="
    
    BASELINE_DIR="analysis/data/model_performance/session3_100k_uniform"
    
    if [ ! -d "$BASELINE_DIR" ]; then
        echo "Baseline directory does not exist: $BASELINE_DIR"
        return 1
    fi
    
    # Count existing files
    existing_count=$(ls "$BASELINE_DIR"/baseline_results_*.csv 2>/dev/null | wc -l)
    
    if [ $existing_count -gt 0 ]; then
        echo "Found $existing_count existing baseline files:"
        ls -la "$BASELINE_DIR"/baseline_results_*.csv
        
        echo
        read -p "Delete all existing baseline files? (y/n): " -n 1 -r
        echo
        
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            echo "Removing existing baseline files..."
            rm -f "$BASELINE_DIR"/baseline_results_*.csv
            echo "✓ Cleanup complete"
        else
            echo "Cleanup cancelled"
            return 1
        fi
    else
        echo "No existing baseline files found"
    fi
    
    echo "Ready for baseline generation!"
}

function create_all_jobs() {
    echo "=== Creating All Baseline Evaluation Jobs ==="
    
    # Ensure we have the creation script
    if [ ! -f "create_batch_baseline_jobs.py" ]; then
        echo "Error: create_batch_baseline_jobs.py not found"
        echo "Please ensure the baseline job creation script is available"
        return 1
    fi
    
    # Create all 25 configurations
    echo "Creating 25 baseline evaluation jobs..."
    
    # Build the configuration string for all 25 combinations
    configs=""
    for ref in 3 4 5 6 7; do
        for budget in 50 80 100 150 200; do
            configs="$configs ${ref},${budget}"
        done
    done
    
    echo "Configurations to create: $configs"
    echo
    
    # Create all jobs in one command
    python create_batch_baseline_jobs.py $configs
    
    # Count created files
    job_count=$(ls slurm_scripts/batch_baseline_evaluation_ref_*_budget_*.slurm 2>/dev/null | wc -l)
    echo
    echo "✓ Created $job_count baseline job files"
    
    if [ $job_count -ne 25 ]; then
        echo "⚠ Warning: Expected 25 jobs, but created $job_count"
    fi
}

function submit_all_jobs() {
    echo "=== Submitting All Baseline Jobs ==="
    
    # Check if job files exist
    job_files=(slurm_scripts/batch_baseline_evaluation_ref_*_budget_*.slurm)
    
    if [ ! -f "${job_files[0]}" ]; then
        echo "No baseline job files found. Run 'create-jobs' first."
        return 1
    fi
    
    job_count=0
    for file in "${job_files[@]}"; do
        if [ -f "$file" ]; then
            echo "Submitting $file"
            sbatch "$file"
            ((job_count++))
            sleep 0.5  # Brief pause between submissions
        fi
    done
    
    echo
    echo "✓ Submitted $job_count baseline jobs"
    echo "Monitor with: squeue -u \$USER | grep baseline"
    echo "Expected completion time: 2-6 hours total"
}

function monitor_jobs() {
    echo "=== Monitoring Baseline Jobs ==="
    echo
    echo "Current job status:"
    squeue -u $USER
    echo
    echo "Baseline evaluation jobs:"
    baseline_jobs=$(squeue -u $USER | grep baseline | wc -l)
    if [ $baseline_jobs -gt 0 ]; then
        squeue -u $USER | grep baseline
        echo
        echo "Running baseline jobs: $baseline_jobs"
    else
        echo "No baseline jobs currently running"
    fi
    echo
    echo "Recent baseline job history:"
    sacct -u $USER --starttime=today --format=JobID,JobName,State,ExitCode,Runtime | grep baseline | head -10
}

function check_results() {
    echo "=== Checking Baseline Results ==="
    
    BASELINE_DIR="analysis/data/model_performance/session3_100k_uniform"
    
    # Expected files
    expected_files=()
    for ref in 3 4 5 6 7; do
        for budget in 50 80 100 150 200; do
            expected_files+=("baseline_results_conventional-amr_ref${ref}_budget${budget}.csv")
        done
    done
    
    echo "Checking for ${#expected_files[@]} expected baseline files:"
    
    found=0
    missing=0
    incomplete=0
    
    for file in "${expected_files[@]}"; do
        filepath="$BASELINE_DIR/$file"
        if [ -f "$filepath" ]; then
            lines=$(wc -l < "$filepath")
            if [ "$lines" -eq 7 ]; then
                echo "✓ $file (7 lines: header + 6 thresholds)"
                ((found++))
            else
                echo "⚠ $file ($lines lines, expected 7)"
                ((incomplete++))
            fi
        else
            echo "✗ $file (missing)"
            ((missing++))
        fi
    done
    
    echo
    echo "Summary:"
    echo "  ✓ Complete: $found"
    echo "  ⚠ Incomplete: $incomplete"
    echo "  ✗ Missing: $missing"
    echo "  Total expected: ${#expected_files[@]}"
    
    if [ $missing -eq 0 ] && [ $incomplete -eq 0 ]; then
        echo
        echo "🎉 All baseline files are complete!"
        echo "Ready for analysis integration"
    else
        echo
        echo "❌ Some files are missing or incomplete"
        echo "Check job status and logs for failed jobs"
    fi
}

function test_single() {
    echo "=== Testing Single Baseline Evaluation ==="
    
    # Use a small configuration for testing
    test_ref=3
    test_budget=50
    
    echo "Testing configuration: ref${test_ref}_budget${test_budget}"
    echo "This will run conventional-AMR with all 6 thresholds"
    echo
    
    read -p "Continue with test? (y/n): " -n 1 -r
    echo
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Running test baseline evaluation..."
        
        python analysis/model_performance/baseline_evaluator.py session3_100k_uniform \
            --mode conventional-amr \
            --initial-refinement $test_ref \
            --element-budget $test_budget \
            --threshold-list "0.3,0.2,0.1,0.01,0.001,0.0001" \
            --verbose
        
        # Check result
        test_file="analysis/data/model_performance/session3_100k_uniform/baseline_results_conventional-amr_ref${test_ref}_budget${test_budget}.csv"
        
        if [ -f "$test_file" ]; then
            lines=$(wc -l < "$test_file")
            echo
            echo "✓ Test completed successfully"
            echo "  Output file: $test_file"
            echo "  Lines: $lines (expected: 7)"
            
            if [ $lines -eq 7 ]; then
                echo "✓ Test result looks good - ready to run full batch"
            else
                echo "⚠ Unexpected line count - check for errors"
            fi
        else
            echo "✗ Test failed - output file not created"
            return 1
        fi
    else
        echo "Test cancelled"
    fi
}

function full_pipeline() {
    echo "=== Running Full Baseline Pipeline ==="
    echo
    
    cleanup_baselines || return 1
    echo
    
    create_all_jobs || return 1
    echo
    
    read -p "Submit all 25 baseline jobs now? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        submit_all_jobs
    else
        echo "Jobs created but not submitted"
        echo "Run: $0 submit-jobs when ready"
    fi
}

# Main script logic
case "$1" in
    cleanup)
        cleanup_baselines
        ;;
    create-jobs)
        create_all_jobs
        ;;
    submit-jobs)
        submit_all_jobs
        ;;
    monitor)
        monitor_jobs
        ;;
    check-results)
        check_results
        ;;
    test-single)
        test_single
        ;;
    full-pipeline)
        full_pipeline
        ;;
    *)
        show_help
        ;;
esac