"""
Module: convert_numbers
This script reads a file containing numbers,
converts them to binary and hexadecimal,
and writes the results to an output file while handling errors.

Features:
- Reads a file with numbers.
- Converts numbers to binary and hexadecimal using basic algorithms.
- Handles invalid data gracefully.
- Saves results to 'ConvertionResults.txt'.
- Displays execution time at the end.
"""
import os
import sys
import time


def read_numbers_from_file(filepath):
    """
    Reads numbers from a file, handling invalid data.
    Returns a list of valid numbers.
    """
    numbers = []
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    number = int(line.strip())
                    numbers.append(number)
                except ValueError:
                    print(f"Invalid data found and ignored: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return []
    return numbers


def convert_to_binary(number):
    """Converts a number to binary."""
    if number == 0:
        return "0"
    if number < 0:
        return "-" + bin(abs(number))[2:]  # Keep "-" sign
    return bin(number)[2:]


def convert_to_hexadecimal(number):
    """Converts a number to hexadecimal"""
    hex_chars = "0123456789ABCDEF"
    if number == 0:
        return "0"
    if number < 0:
        return "-" + hex(abs(number))[2:].upper()  # Keep "-" sign
    hexadecimal = ""
    item = abs(number)
    while item > 0:
        remainder = item % 16
        hexadecimal = hex_chars[remainder] + hexadecimal
        item //= 16
    return hexadecimal


def write_results_to_file(results, output_file, elapsed_time, tc_name):
    """Appends results to a file inside the output directory."""
    file_exists = os.path.exists(output_file)
    with open(output_file, 'a', encoding='utf-8') as file:
        if not file_exists:
            file.write("TC\tNumber\tBinary\tHexadecimal\tElapsed Time (s)\n")
        for test, number, binary, hexadecimal in results:
            file.write(f"{test}\t{number}\t{binary}\t{hexadecimal}\n")
        file.write(f"{tc_name}\t-\t-\t-\t{elapsed_time:.6f}\n")
    print(f"Results appended to {output_file}")


def main():
    """Main function to convert numbers from multiple files
    in a certain repository."""
    if len(sys.argv) != 3:
        print("""Usage: python convert_numbers.py
              <input_file> <output_directory>""")
        sys.exit(1)
    input_file = sys.argv[1]
    output_directory = sys.argv[2]
    os.makedirs(output_directory, exist_ok=True)
    output_file = os.path.join(output_directory, "convertNumbersResults.tsv")
    print(f"Processing file: {input_file}")
    start_time = time.time()
    numbers = read_numbers_from_file(input_file)
    if not numbers:
        print(f"No valid numbers found in {input_file}.")
        return
    results = []
    tc_name = os.path.splitext(os.path.basename(input_file))[0]
    for number in numbers:
        binary = convert_to_binary(number)
        hexadecimal = convert_to_hexadecimal(number)
        results.append((tc_name, number, binary, hexadecimal))
        print(f"{number}: Binary={binary}, Hexadecimal={hexadecimal}")
    elapsed_time = time.time() - start_time
    print(f"Elapsed Time for {input_file} (seconds): {elapsed_time:.6f}")
    write_results_to_file(results, output_file, elapsed_time, tc_name)


if __name__ == "__main__":
    main()
