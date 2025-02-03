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
import os
import sys
import time


def read_words_from_file(filepath):
    """
    Reads words from a file, handling invalid data.
    Returns a list of words.
    """
    words = []
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                words.extend(line.strip().split())
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return []
    return words


def count_word_frequencies(words):
    """Counts the frequency of each distinct word in the list."""
    word_count = {}
    for word in words:
        word = word.lower().strip(".,!?()[]{}:;\"'")  # Sanitize
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count


def write_results_to_file(results, output_file, elapsed_time, tc_name):
    """Appends results to a file inside the output directory."""
    file_exists = os.path.exists(output_file)
    with open(output_file, 'a', encoding='utf-8') as file:
        if not file_exists:
            file.write("TC\tWord\tCount\n")
        for word, count in results.items():
            file.write(f"{tc_name}\t{word}\t{count}\n")
        file.write(f"{tc_name}\t-\tElapsed Time: {elapsed_time} seconds\n")
    print(f"Results appended to {output_file}")


def main():
    """Main function to count words from multiple files in P1 directory."""
    if len(sys.argv) != 3:
        print("Usage: python word_count.py <input_file> <output_directory>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_directory = sys.argv[2]
    os.makedirs(output_directory, exist_ok=True)
    output_file = os.path.join(output_directory, "wordCountResults.tsv")
    print(f"Processing file: {input_file}")
    start_time = time.time()
    words = read_words_from_file(input_file)
    if not words:
        print(f"No words found in {input_file}.")
        return
    tc_name = os.path.splitext(os.path.basename(input_file))[0]
    word_frequencies = count_word_frequencies(words)
    elapsed_time = time.time() - start_time
    print(f"Elapsed Time for {input_file} (seconds): {elapsed_time}")
    write_results_to_file(word_frequencies, output_file, elapsed_time, tc_name)


if __name__ == "__main__":
    main()
