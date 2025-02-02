"""
Module: word_count
This script reads a file containing words,
counts the frequency of each unique word,
and writes the results to an output file while handling errors.

Features:
- Reads a file containing words separated by spaces.
- Counts the occurrences of each distinct word.
- Handles invalid data gracefully.
- Saves results to 'WordCountResults.txt'.
- Displays execution time at the end.
"""
import sys
import time
import os


def read_words_from_file(filename):
    """
    Reads words from a file, handling invalid data.
    Returns a list of words and prints errors for invalid data.
    """
    directory = os.path.join(os.getcwd(), "Data")
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, filename)
    words = []
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                words.extend(line.strip().split())
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied for file '{filepath}'.")
        sys.exit(1)
    except IsADirectoryError:
        print(f"Error: Expected a file but found a directory: '{filepath}'")
        sys.exit(1)
    except OSError as os_ex:
        print(f"Error reading file: {os_ex}")
        sys.exit(1)
    return words


def count_word_frequencies(words):
    """Counts the frequency of each distinct word in the list."""
    word_count = {}
    for word in words:
        word = word.lower().strip(".,!?()[]{}:;\"'")  # Basic cleanup
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count


def write_results_to_file(results, elapsed_time):
    """Writes the word count results to a file inside Script
        Results folder."""
    directory = os.path.join(os.getcwd(), "ScriptResults")
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, "WordCountResults.txt")
    with open(filepath, 'w', encoding='utf-8') as file:
        for word, count in sorted(results.items()):
            file.write(f"{word}: {count}\n")
        file.write(f"\nElapsed Time (seconds): {elapsed_time}\n")
    print(f"Results saved to {filepath}")


def main():
    """Main function to count words from a given file."""
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        sys.exit(1)
    filename = sys.argv[1]
    start_time = time.time()
    words = read_words_from_file(filename)
    if not words:
        print("No words found in the file.")
        sys.exit(1)
    word_frequencies = count_word_frequencies(words)
    for word, count in sorted(word_frequencies.items()):
        print(f"{word}: {count}")
    elapsed_time = time.time() - start_time
    elapsed_str = f"Elapsed Time (seconds): {elapsed_time}"
    write_results_to_file(word_frequencies, elapsed_str)
    print(f"Elapsed Time (seconds): {elapsed_time}")


if __name__ == "__main__":
    main()
