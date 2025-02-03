#!/bin/bash

# Define directories
DATA_DIR="./data/P3"
OUTPUT_DIR="./script_results/P3"
SCRIPT="./python_scripts/word_count.py"

# Check if the data directory exists
if [ ! -d "$DATA_DIR" ]; then
    echo "Error: Data directory $DATA_DIR does not exist."
    exit 1
fi

# Ensure the output directory exists
mkdir -p "$OUTPUT_DIR"

# Process each file in the directory
for FILE in "$DATA_DIR"/*; do
    if [ -f "$FILE" ]; then
        echo "Processing file: $(basename "$FILE")"
        python "$SCRIPT" "$FILE" "$OUTPUT_DIR"
    fi
done

echo "All files processed. Results stored in $OUTPUT_DIR."
