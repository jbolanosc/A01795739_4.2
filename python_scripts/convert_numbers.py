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
    Returns a list of valid numbers or marks invalid ones as "#VALUE!".
    """
    numbers = []
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line.lstrip('-').isdigit():
                    numbers.append(int(stripped_line))
                else:
                    numbers.append("#VALUE!")
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return []
    return numbers


def convert_to_binary(number):
    """Converts a number to binary representation."""
    if number == "#VALUE!":
        return "#VALUE!"
    if number >= 0:
        return bin(number)[2:]
    return bin(number & 0x3FF)[2:]  # Keeps 10-bit representation for negatives


def convert_to_hexadecimal(number):
    """Converts a number to hexadecimal representation."""
    if number == "#VALUE!":
        return "#VALUE!"
    if number >= 0:
        return hex(number)[2:].upper()
    # Ensures proper negative representation
    return hex(number & 0xFFFFFFFF)[2:].upper()


def write_results_to_file(results, output_file, elapsed_time, tc_name):
    """Appends results to a TSV file."""
    file_exists = os.path.exists(output_file)
    with open(output_file, 'a', encoding='utf-8') as file:
        if not file_exists:
            file.write("ITEM\tTC4\tBIN\tHEX\n")
        for i, (number, binary, hexadecimal) in enumerate(results, 1):
            file.write(f"{i}\t{number}\t{binary}\t{hexadecimal}\n")
        file.write(f"{tc_name} Elapsed time: {elapsed_time:.6f} seconds\n")
    print(f"Results appended to {output_file}")


def main():
    """Main function to convert numbers from a file."""
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
    results = [(num, convert_to_binary(num),
                convert_to_hexadecimal(num)) for num in numbers]
    elapsed_time = time.time() - start_time
    print(f"Elapsed Time for {input_file} (seconds): {elapsed_time:.6f}")
    tc_name = os.path.splitext(os.path.basename(input_file))[0]
    write_results_to_file(results, output_file, elapsed_time, tc_name)


if __name__ == "__main__":
    main()
