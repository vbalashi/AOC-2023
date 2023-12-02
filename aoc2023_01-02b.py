import re

def process_line(line: str) -> int:
    """
    Converts all digit words to their numeric equivalents,
    extracts the first and last digit, and returns the integer value.
    """
    digit_words = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3',
        'four': '4', 'five': '5', 'six': '6', 'seven': '7',
        'eight': '8', 'nine': '9'
    }
    # Replace digit words with digits
    for word, digit in digit_words.items():
        line = line.replace(word, digit)

    # Extract digits
    digits = re.findall(r'\d', line)
    if not digits:
        return 0  # Return 0 if no digits are found

    # Return concatenated first and last digit as integer
    print(digits[0] + digits[-1])
    return int(digits[0] + digits[-1])

def sum_processed_lines(file_path):
    """
    Processes lines from a file, extracting and summing the values from each line.
    """
    total_sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            total_sum += process_line(line.strip())
    return total_sum

def process_line_corrected(line: str) -> int:
    digit_words = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3',
        'four': '4', 'five': '5', 'six': '6', 'seven': '7',
        'eight': '8', 'nine': '9'
    }
    # Sort digit words by length in descending order to replace longer words first
    sorted_digit_words = sorted(digit_words.items(), key=lambda x: len(x[0]), reverse=True)
    # Replace digit words with digits
    for word, digit in sorted_digit_words:
        line = line.replace(word, digit)

    # Extract digits
    digits = re.findall(r'\d', line)
    if not digits:
        return 0  # Return 0 if no digits are found

    # Return concatenated first and last digit as integer
    return int(digits[0] + digits[-1])



# Example usage
file_path = 'aoc2023_01-01_task.txt'
total_sum = sum_processed_lines(file_path)
print(total_sum)

# Re-test with the adjusted function
corrected_result = process_line_corrected(file_path)
print(corrected_result)
