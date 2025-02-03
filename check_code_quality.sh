#!/bin/bash

# Create the LinterResults directory if it doesn't exist
mkdir -p linter_results

# Loop through all Python files in the current directory
for script in ./python_scripts/*.py; do
    if [[ -f "$script" ]]; then
        # Extract filename without extension
        script_name="${script%.py}"
        
        # Define output file paths
        flake8_report="linter_results/${script_name}_flake8.txt"
        pylint_report="linter_results/${script_name}_pylint.txt"
        combined_report="linter_results/${script_name}_linting.txt"

        echo "=== Running Flake8 on $script ==="
        flake8 "$script" --output-file="$flake8_report"
        echo "Flake8 report saved in $flake8_report"

        echo "=== Running Pylint on $script ==="
        pylint "$script" > "$pylint_report"
        echo "Pylint report saved in $pylint_report"

        echo "=== Combining Reports for $script ==="
        (
            echo "=== FLAKE8 REPORT for $script ==="
            cat "$flake8_report"
            echo "\n=== PYLINT REPORT for $script ==="
            cat "$pylint_report"
        ) > "$combined_report"
        echo "Final combined report saved in $combined_report"
    fi
done

echo "All linting reports are saved in the LinterResults directory."
