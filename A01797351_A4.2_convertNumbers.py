"""
Module to convert numbers to binary and hexadecimal bases.
Executes from command line and outputs to file and screen.
"""

import sys
import time


def get_data(file_path):
    """
    Reads a file and extracts numbers.
    Handles invalid data by printing an error message.
    Returns a list of valid numbers (integers).
    """
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                clean_line = line.strip()
                if not clean_line:
                    continue

                try:
                    
                    number = int(float(clean_line))
                    data.append(number)
                except ValueError:
                    print(f"Error: Invalid data at line {line_num}: '{clean_line}'")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    return data


def to_binary(num):
    """
    Converts a number to binary string using basic algorithms.
    """
    if num == 0:
        return "0"

    is_negative = False
    if num < 0:
        is_negative = True
        num = abs(num)

    binary_digits = []
    while num > 0:
        remainder = num % 2
        binary_digits.append(str(remainder))
        num = num // 2

    # Reverse list and join
    result = "".join(binary_digits[::-1])

    return "-" + result if is_negative else result


def to_hexadecimal(num):
    """
    Converts a number to hexadecimal string using basic algorithms.
    """
    if num == 0:
        return "0"

    is_negative = False
    if num < 0:
        is_negative = True
        num = abs(num)

    hex_map = "0123456789ABCDEF"
    hex_digits = []

    while num > 0:
        remainder = num % 16
        hex_digits.append(hex_map[remainder])
        num = num // 16

    result = "".join(hex_digits[::-1])

    return "-" + result if is_negative else result


def main():
    """Main execution function."""
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    start_time = time.time()
    file_path = sys.argv[1]

    numbers = get_data(file_path)

    if not numbers:
        print("No valid data found in the file.")
        sys.exit(1)

    results = []
    for num in numbers:
        binary = to_binary(num)
        hexadecimal = to_hexadecimal(num)
        results.append(f"NUMBER: {num} | BIN: {binary} | HEX: {hexadecimal}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    time_msg = f"Time Elapsed: {elapsed_time:.6f} seconds"

    # Print to screen
    print("\nConversion Results:")
    for line in results:
        print(line)
    print(time_msg)

    # Print to file
    with open("ConvertionResults.txt", "w", encoding='utf-8') as out_file:
        out_file.write("Conversion Results:\n")
        for line in results:
            out_file.write(line + "\n")
        out_file.write(time_msg + "\n")


if __name__ == "__main__":
    main()