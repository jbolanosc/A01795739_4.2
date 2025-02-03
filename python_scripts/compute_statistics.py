"""
Module: compute_statistics
This script reads a file containing numbers, calculates descriptive statistics
(mean, median, mode, variance, and standard deviation), and writes the results
to an output file while handling errors.
"""
import os
import sys
import time


def read_file_information(filepath):
    """
    Reads numbers from a file, handling invalid data.
    Returns a list of valid numbers.
    """
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
        return []
    return numbers


def compute_mean(numbers):
    """Computes the mean (average)"""
    return sum(numbers) / len(numbers) if numbers else 0


def compute_median(numbers):
    """Computes the median"""
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    mid = length // 2
    if length % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return sorted_numbers[mid]


def compute_mode(numbers):
    """Computes the mode"""
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    return modes[0] if len(modes) == 1 else "#N/A"


def compute_variance(numbers, mean):
    """Computes population variance."""
    if not numbers:
        return None
    diff_squared = [(x - mean) ** 2 for x in numbers]
    return sum(diff_squared) / len(numbers)


def compute_standard_deviation(variance):
    """Computes standard deviation"""
    return variance ** 0.5


def compute_statistics(numbers):
    """
    Computes mean, median, mode, variance, and standard deviation.
    """
    if not numbers:
        return {
            "COUNT": 0, "MEAN": None, "MEDIAN": None,
            "MODE": None, "SD": None, "VARIANCE": None
        }
    mean = compute_mean(numbers)
    return {
        "COUNT": len(numbers),
        "MEAN": mean,
        "MEDIAN": compute_median(numbers),
        "MODE": compute_mode(numbers),
        "SD": compute_standard_deviation(
            compute_variance(numbers, mean)
        ),
        "VARIANCE": compute_variance(numbers, mean)
    }


def write_results_to_file(results, output_file, elapsed_time, tc_name):
    """Appends statistics results to a TSV file manually."""
    file_exists = os.path.exists(output_file)
    with open(output_file, 'a', encoding='utf-8') as file:
        if not file_exists:
            file.write(
                "TC\tCOUNT\tMEAN\tMEDIAN\tMODE\tSD\tVARIANCE\t"
                "Elapsed Time (s)\n"
            )
        file.write(
            f"{tc_name}\t{results['COUNT']}\t{results['MEAN']}\t"
            f"{results['MEDIAN']}\t{results['MODE']}\t"
            f"{results['SD']}\t{results['VARIANCE']}\t"
            f"{elapsed_time:.6f}\n"
        )
    print(f"Results appended to {output_file}")


def main():
    """Main function to compute statistics for multiple files if needed."""
    if len(sys.argv) != 3:
        print(
            "Usage: python compute_statistics.py "
            "<input_file> <output_directory>"
        )
        sys.exit(1)
    input_file = sys.argv[1]
    output_directory = sys.argv[2]
    os.makedirs(output_directory, exist_ok=True)
    output_file = os.path.join(
        output_directory, "computeStatisticsResults.tsv"
    )
    print(f"Processing file: {input_file}")
    start_time = time.time()
    numbers = read_file_information(input_file)
    stats = compute_statistics(numbers)
    elapsed_time = time.time() - start_time
    tc_name = os.path.splitext(os.path.basename(input_file))[0]
    stats["TC"] = tc_name
    print(
        f"Elapsed Time for {input_file} (seconds): "
        f"{elapsed_time:.6f}"
    )
    write_results_to_file(stats, output_file, elapsed_time, tc_name)


if __name__ == "__main__":
    main()
