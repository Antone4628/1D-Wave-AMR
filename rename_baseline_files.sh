#!/bin/bash

# Baseline Files Backup and Rename Script
# Renames all baseline_results_conventional-amr_ref{X}_budget{Y}.csv files to baseline_results_conventional-amr_ref{X}_budget{Y}_max{X}.csv

echo "🔄 Starting baseline files backup and rename process..."

# Set the directory path
DATA_DIR="analysis/data/model_performance/session3_100k_uniform"

# Check if directory exists
if [ ! -d "$DATA_DIR" ]; then
    echo "❌ Error: Directory $DATA_DIR not found!"
    exit 1
fi

# Find all baseline files
BASELINE_FILES=$(find "$DATA_DIR" -name "baseline_results_conventional-amr_ref*_budget*.csv" ! -name "*_max*" | sort)

# Count files
FILE_COUNT=$(echo "$BASELINE_FILES" | wc -l)
echo "📊 Found $FILE_COUNT baseline files to rename"

# Counter for progress
COUNTER=0

# Process each file
for FILE in $BASELINE_FILES; do
    # Extract filename without path
    FILENAME=$(basename "$FILE")
    
    # Extract directory path
    DIR_PATH=$(dirname "$FILE")
    
    # Extract ref and budget numbers using regex
    if [[ $FILENAME =~ baseline_results_conventional-amr_ref([0-9]+)_budget([0-9]+)\.csv ]]; then
        REF_NUM="${BASH_REMATCH[1]}"
        BUDGET_NUM="${BASH_REMATCH[2]}"
        
        # Create new filename with max_level = ref_num
        NEW_FILENAME="baseline_results_conventional-amr_ref${REF_NUM}_budget${BUDGET_NUM}_max${REF_NUM}.csv"
        NEW_FILEPATH="$DIR_PATH/$NEW_FILENAME"
        
        # Increment counter
        ((COUNTER++))
        
        # Copy file with new name
        if cp "$FILE" "$NEW_FILEPATH"; then
            echo "✅ [$COUNTER/$FILE_COUNT] $FILENAME → $NEW_FILENAME"
        else
            echo "❌ [$COUNTER/$FILE_COUNT] Failed to copy $FILENAME"
        fi
    else
        echo "⚠️  Warning: Could not parse filename: $FILENAME"
    fi
done

echo ""
echo "🎉 Baseline file renaming complete!"
echo "📋 Summary:"
echo "   - Original files: $FILE_COUNT (preserved)"
echo "   - New files created: $COUNTER"
echo "   - Location: $DATA_DIR"

# Verify results
echo ""
echo "🔍 Verification - New baseline files created:"
ls -1 "$DATA_DIR"/baseline_results_conventional-amr_ref*_budget*_max*.csv | wc -l
echo "   Files with new naming pattern:"
ls -1 "$DATA_DIR"/baseline_results_conventional-amr_ref*_budget*_max*.csv | head -5
if [ $(ls -1 "$DATA_DIR"/baseline_results_conventional-amr_ref*_budget*_max*.csv | wc -l) -gt 5 ]; then
    echo "   ... (showing first 5, run 'ls $DATA_DIR/baseline_results_conventional-amr_ref*_budget*_max*.csv' to see all)"
fi
