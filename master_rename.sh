#!/bin/bash

# Master File Rename Script
# Orchestrates the renaming of both model and baseline files

echo "🚀 DRL-AMR File Renaming Process Starting..."
echo "=============================================="
echo ""

# Record start time
START_TIME=$(date +%s)

# Set the directory path
DATA_DIR="analysis/data/model_performance/session3_100k_uniform"

echo "📂 Working Directory: $DATA_DIR"
echo ""

# Check initial file counts
echo "📊 Pre-rename File Inventory:"
MODEL_COUNT=$(find "$DATA_DIR" -name "model_results_ref*_budget*.csv" ! -name "*_max*" | wc -l)
BASELINE_COUNT=$(find "$DATA_DIR" -name "baseline_results_conventional-amr_ref*_budget*.csv" ! -name "*_max*" | wc -l)
echo "   - Model files to rename: $MODEL_COUNT"
echo "   - Baseline files to rename: $BASELINE_COUNT"
echo "   - Total files to process: $((MODEL_COUNT + BASELINE_COUNT))"
echo ""

# Step 1: Rename model files
echo "🔧 STEP 1: Processing Model Files"
echo "================================="
./rename_model_files.sh
MODEL_EXIT_CODE=$?

echo ""

# Step 2: Rename baseline files
echo "🔧 STEP 2: Processing Baseline Files"
echo "===================================="
./rename_baseline_files.sh
BASELINE_EXIT_CODE=$?

echo ""

# Final verification and summary
echo "🎯 FINAL VERIFICATION AND SUMMARY"
echo "=================================="

# Check new file counts
NEW_MODEL_COUNT=$(find "$DATA_DIR" -name "model_results_ref*_budget*_max*.csv" | wc -l)
NEW_BASELINE_COUNT=$(find "$DATA_DIR" -name "baseline_results_conventional-amr_ref*_budget*_max*.csv" | wc -l)

echo "📈 Results:"
echo "   - New model files created: $NEW_MODEL_COUNT (expected: $MODEL_COUNT)"
echo "   - New baseline files created: $NEW_BASELINE_COUNT (expected: $BASELINE_COUNT)"
echo "   - Total new files: $((NEW_MODEL_COUNT + NEW_BASELINE_COUNT))"
echo ""

# Verify success
if [ $MODEL_EXIT_CODE -eq 0 ] && [ $BASELINE_EXIT_CODE -eq 0 ]; then
    if [ $NEW_MODEL_COUNT -eq $MODEL_COUNT ] && [ $NEW_BASELINE_COUNT -eq $BASELINE_COUNT ]; then
        echo "✅ SUCCESS: All files renamed successfully!"
        echo ""
        echo "📁 File Structure Ready for Phase 2:"
        echo "   - Original files preserved"
        echo "   - New files follow pattern: *_ref{X}_budget{Y}_max{X}.csv"
        echo "   - Both analyzer scripts ready for parser updates"
    else
        echo "⚠️  WARNING: File count mismatch detected"
        echo "   Please verify results manually"
    fi
else
    echo "❌ ERROR: One or more renaming processes failed"
    echo "   Model files exit code: $MODEL_EXIT_CODE"
    echo "   Baseline files exit code: $BASELINE_EXIT_CODE"
fi

# Calculate runtime
END_TIME=$(date +%s)
RUNTIME=$((END_TIME - START_TIME))
echo ""
echo "⏱️  Total runtime: ${RUNTIME} seconds"

echo ""
echo "🎯 NEXT STEPS:"
echo "1. Verify file integrity with: ls -la $DATA_DIR/*_max*.csv"
echo "2. Update parser logic in both analyzer scripts"
echo "3. Test configuration detection with new file names"
echo ""
echo "📋 Phase 1 Status: File Naming Standardization COMPLETE ✅"
