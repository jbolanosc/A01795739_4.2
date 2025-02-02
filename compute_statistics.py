"""
Module: compute_statistics
This script reads a file containing numbers, calculates descriptive statistics
(mean, median, mode, variance, and standard deviation), and writes the results
to an output file while handling errors.
"""
import sys
import time
import os


def read_file_information(filename):
    """
    Reads numbers from a file, handling invalid data.
    Returns a list of valid numbers and prints errors for invalid data.
    """
    directory = os.path.join(os.getcwd(), "Data")
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, filename)
    numbers = []
    try:
        with open(filepath, "r", encoding='utf-8') as file:
            for line in file:
                try:
                    number = float(line.strip())
                    numbers.append(number)
                except ValueError:
                    print(f"Invalid data found and ignored: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)
    return numbers


def compute_mean(numbers):
    """Computes the mean (average) of a list of numbers."""
    total = sum(numbers)
    return total / len(numbers) if numbers else 0


def compute_median(numbers):
    """Computes the median of a list of numbers."""
    sorted_numbers = sorted(numbers)
    item = len(sorted_numbers)
    mid = item // 2
    if item % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]


def compute_mode(numbers):
    """Computes the mode of a list of numbers."""
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    return modes if len(modes) > 1 else modes[0]


def compute_variance(numbers, mean):
    """Computes the variance of a list of numbers."""
    if not numbers:
        return 0
    squared_diffs = [(x - mean) ** 2 for x in numbers]
    variance = sum(squared_diffs) / len(numbers)
    return variance


def compute_standard_deviation(variance):
    """Computes the standard deviation based on variance."""
    return variance ** 0.5


def write_results_to_file(results):
    """Writes the word count results to a file inside Script
        Results folder."""
    directory = os.path.join(os.getcwd(), "ScriptResults")
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, "computeStatisticsResults.txt")
    with open(filepath, 'w', encoding='utf-8') as file:
        for key, value in results.items():
            file.write(f"{key}: {value}\n")
    print(f"Results saved to {filepath}")


def main():
    """Main function to compute statistics from a given file."""
    if len(sys.argv) != 2:
        print("Invalid execution command.")
        print("Usage: python computeStatistics.py file.txt")
        sys.exit(1)
    filename = sys.argv[1]
    start_time = time.time()
    numbers = read_file_information(filename)
    if not numbers:
        print("No valid numbers found in the file.")
        sys.exit(1)
    mean = compute_mean(numbers)
    median = compute_median(numbers)
    mode = compute_mode(numbers)
    variance = compute_variance(numbers, mean)
    std_dev = compute_standard_deviation(variance)
    elapsed_time = time.time() - start_time
    results = {
        "Mean": mean,
        "Median": median,
        "Mode": mode,
        "Variance": variance,
        "Standard Deviation": std_dev,
        "Elapsed Time (seconds)": elapsed_time
    }
    for key, value in results.items():
        print(f"{key}: {value}")
    write_results_to_file(results)


if __name__ == "__main__":
    main()
