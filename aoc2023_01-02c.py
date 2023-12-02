import re
import sys

def keep_numbers(s: str):
    # Find all sequences of digits and join them into a single string
    return ''.join(re.findall(r'\d+', s))

def first_and_last(s: str) -> str:
    if len(s) == 0:
        raise ValueError("Input string is empty")
    else:
        return s[0] + s[-1]

def words_to_numbers(s: str) -> str:
    digit_words = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    # Function to replace the leftmost occurrence of each digit word
    def replace_leftmost():
        for word in digit_words.keys():
            match = re.search(re.escape(word), s)
            if match:
                return s[:match.start()] + digit_words[word] + s[match.end():]
        return s

    # Function to replace the rightmost occurrence of each digit word
    def replace_rightmost():
        for word in reversed(digit_words.keys()):
            match = re.search(re.escape(word) + r'(?![\s\S]*' + re.escape(word) + ')', s)
            if match:
                return s[:match.start()] + digit_words[word] + s[match.end():]
        return s

    # Replace the leftmost occurrence first
    s = replace_leftmost()
    # Then replace the rightmost occurrence
    s = replace_rightmost()

    return s


def main():
    line_number = 0
    total_sum = 0
    for line in sys.stdin:
        line_number += 1
        line = line.strip().lower()
        line_digitized = words_to_numbers(line)
        numbers = keep_numbers(line_digitized)  # Extract numbers from the line
        try:
            if numbers:  # Check if num is not empty
                result = first_and_last(numbers)
                total_sum += int(result)
                # print(f"{line_number}. {line} -> {line_digitized} -> {numbers} -> {result}")
                print(result)
            else:
                print(f"Empty line detected at line {line_number}")
        except Exception as e:
            print(f"Error processing line {line_number}: {e}")

    print(f"Total sum: {total_sum}")

if __name__ == "__main__":
    main()



# def main():
#     try:
#         result = first_and_last("example")
#         print(result)  # Output will be 'ee'

#         result = first_and_last("")  # This will raise an exception
#         print(result)
#     except ValueError as e:
#         print(f"Error: {e}")
