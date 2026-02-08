"""
Module to compute descriptive statistics from a file containing numbers.
Executes from command line and outputs to file and screen.
"""

import sys
import time


def get_data(file_path):
    """
    Reads a file and extracts numbers.
    Handles invalid data by printing an error message.
    Returns a list of valid numbers.
    """
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                # Remove whitespace and newlines
                clean_line = line.strip()
                if not clean_line:
                    continue  # Skip empty lines

                try:
                    # Attempt to convert to float
                    number = float(clean_line)
                    data.append(number)
                except ValueError:
                    print(f"Error: Invalid data at line {line_num}: '{clean_line}'")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    return data


def calculate_mean(data):
    """Calculates the arithmetic mean."""
    if not data:
        return 0.0
    return sum(data) / len(data)


def calculate_median(data):
    """Calculates the median."""
    if not data:
        return 0.0
    sorted_data = sorted(data)
    n_items = len(sorted_data)
    mid = n_items // 2

    if n_items % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return sorted_data[mid]


def calculate_mode(data):
    """Calculates the mode."""
    if not data:
        return "N/A"

    frequency = {}
    for num in data:
        frequency[num] = frequency.get(num, 0) + 1

    max_count = max(frequency.values())
    modes = [num for num, count in frequency.items() if count == max_count]

    if len(modes) == 1:
        return modes[0]
    return modes  # Returns a list if multimodal


def calculate_variance(data, mean):
    """Calculates the POPULATION variance (dividing by N, not N-1)."""
    if not data:
        return 0.0
    
    return sum((x - mean) ** 2 for x in data) / len(data)


def calculate_std_dev(variance):
    """Calculates the standard deviation."""
    return variance ** 0.5


def main():
    """Main execution function."""
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        sys.exit(1)

    start_time = time.time()
    file_path = sys.argv[1]

    data = get_data(file_path)

    if not data:
        print("No valid data found in the file.")
        sys.exit(1)

    mean = calculate_mean(data)
    median = calculate_median(data)
    mode = calculate_mode(data)
    variance = calculate_variance(data, mean)
    std_dev = calculate_std_dev(variance)

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Prepare output strings
    results = [
        f"Mean: {mean}",
        f"Median: {median}",
        f"Mode: {mode}",
        f"Standard Deviation: {std_dev}",
        f"Variance: {variance}",
        f"Time Elapsed: {elapsed_time:.6f} seconds"
    ]

    # Print to screen
    print("\nDescriptive Statistics Results:")
    for line in results:
        print(line)

    # Print to file
    with open("StatisticsResults.txt", "w", encoding='utf-8') as out_file:
        out_file.write("Descriptive Statistics Results:\n")
        for line in results:
            out_file.write(line + "\n")


if __name__ == "__main__":
    main()