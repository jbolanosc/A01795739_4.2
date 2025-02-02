import sys
import time
import os


def read_numbers_from_file(filename):
    """
    Reads numbers from a file, handling invalid data.
    Returns a list of valid numbers and prints errors for invalid data.
    """
    numbers = []
    directory = os.path.join(os.getcwd(), "Data")
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, filename)
    try:
        with open(filepath, 'r') as file:
            for line in file:
                try:
                    number = int(line.strip())
                    numbers.append(number)
                except ValueError:
                    print(f"Invalid data found and ignored: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)
    return numbers


def convert_to_binary(number):
    """Converts a number to binary using basic algorithm."""
    if number == 0:
        return "0"
    binary = ""
    n = number
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary


def convert_to_hexadecimal(number):
    """Converts a number to hexadecimal using basic algorithm."""
    hex_chars = "0123456789ABCDEF"
    if number == 0:
        return "0"
    hexadecimal = ""
    n = number
    while n > 0:
        remainder = n % 16
        hexadecimal = hex_chars[remainder] + hexadecimal
        n //= 16
    return hexadecimal


def write_results_to_file(results):
    """Writes the word count results to a file inside Script
        Results folder."""
    directory = os.path.join(os.getcwd(), "ScriptResults")
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, "convertNumbersResults.txt")
    with open(filepath, 'w') as file:
        for number, binary, hexadecimal in results:
            file.write(f"""{number}: Binary={binary},
                       Hexadecimal={hexadecimal}\n""")
    print(f"Results saved to {filepath}")


def main():
    """Main function to convert numbers from a given file."""
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        sys.exit(1)
    filename = sys.argv[1]
    start_time = time.time()
    numbers = read_numbers_from_file(filename)
    if not numbers:
        print("No valid numbers found in the file.")
        sys.exit(1)
    results = []
    for number in numbers:
        binary = convert_to_binary(number)
        hexadecimal = convert_to_hexadecimal(number)
        results.append((number, binary, hexadecimal))
        print(f"{number}: Binary={binary}, Hexadecimal={hexadecimal}")
    write_results_to_file(results)
    elapsed_time = time.time() - start_time
    print(f"Elapsed Time (seconds): {elapsed_time}")
    with open("convertNumbers.txt", 'a') as file:
        file.write(f"Elapsed Time (seconds): {elapsed_time}\n")


if __name__ == "__main__":
    main()
