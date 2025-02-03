# Activity 4.2 - Code Execution Guide 

Follow these steps to execute the code and validate the solutions:

## Setup
1. Install **pylint** and **flake8** in your development environment:
   ```sh
   pip install pylint flake8
   ```

## Running Code Quality Checks
Run the linter to check code quality:
   ```sh
   ./check_code_quality.sh
   ```
- Results will be stored in the **`linter_results/`** folder.

## Executing All Exercises
Run all scripts to generate results:
   ```sh
   ./run_all_scripts.sh
   ```
- Outputs will be saved in the **`script_results/`** folder.

## Running a Single Test
To execute only one test:
   ```sh
   python script_name file_to_read output_folder
   ```
Replace:
- **`script_name`** → The script you want to run.
- **`file_to_read`** → The input data file.
- **`output_folder`** → Folder where results will be stored.