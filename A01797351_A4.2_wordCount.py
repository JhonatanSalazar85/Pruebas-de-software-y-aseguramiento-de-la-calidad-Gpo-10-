"""
Module to count frequency of distinct words in a file.
Executes from command line and outputs to file and screen.
"""

import sys
import time


def get_data(file_path):
    """
    Reads a file and returns a list of lines.
    Handles file not found errors.
    """
    lines = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                lines.append(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Error: Could not decode file '{file_path}'. Check encoding.")
        sys.exit(1)

    return lines


def count_words(lines):
    """
    Counts word frequencies using basic algorithms.
    Returns a dictionary with word counts and a list of errors/invalid data.
    """
    word_frequencies = {}
    invalid_entries = 0

    for line_num, line in enumerate(lines, 1):
        if not line:
            continue

        # Split line by spaces to get words
        words = line.split()

        for word in words:
            # Basic validation: ensure it's not just symbols or empty
            # You can adjust this rule based on what "invalid data" means for you
            if not word.strip():
                print(f"Warning: Empty or invalid data at line {line_num}")
                invalid_entries += 1
                continue

            # Count frequency
            if word in word_frequencies:
                word_frequencies[word] += 1
            else:
                word_frequencies[word] = 1

    return word_frequencies


def main():
    """Main execution function."""
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        sys.exit(1)

    start_time = time.time()
    file_path = sys.argv[1]

    lines = get_data(file_path)
    frequencies = count_words(lines)

    if not frequencies:
        print("No valid words found in the file.")
        sys.exit(1)

    # Prepare results
    results = []
    # formatting columns for better readability
    header = f"{'Word':<20} | {'Count':<10}"
    results.append(header)
    results.append("-" * 35)

    for word, count in frequencies.items():
        results.append(f"{word:<20} | {count:<10}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    time_msg = f"Time Elapsed: {elapsed_time:.6f} seconds"

    # Print to screen
    print("\nWord Count Results:")
    for line in results:
        print(line)
    print(time_msg)

    # Save to file
    with open("WordCountResults.txt", "w", encoding='utf-8') as out_file:
        out_file.write("Word Count Results:\n")
        for line in results:
            out_file.write(line + "\n")
        out_file.write(time_msg + "\n")


if __name__ == "__main__":
    main()