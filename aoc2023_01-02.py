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

def replace_with_number(match):
    word = match.group(0)
    return digit_words.get(word, "")

pattern = '|'.join(re.escape(word) for word in digit_words.keys())

def replace_first_and_last_digit_words(s):
    # Find all occurrences of digit words
    matches = list(re.finditer(pattern, s))
    
    print(re.findall(pattern, s))
    
    if not matches:
        return s  # No replacement needed

    # Replace the first occurrence
    first_match = matches[0]
    s = s[:first_match.start()] + replace_with_number(first_match) + s[first_match.end():]

    # Find all occurrences again as the string has changed
    matches = list(re.finditer(pattern, s))
    print(re.findall(pattern, s))

    if len(matches) > 1:
        # Replace the last occurrence if it's different from the first
        last_match = matches[-1]
        s = s[:last_match.start()] + replace_with_number(last_match) + s[last_match.end():]
    
    return s

def main():
    line_number = 0
    total_sum = 0
    for line in sys.stdin:
        line_number += 1
        line = line.strip().lower()
        line_digitized = replace_first_and_last_digit_words(line)
        numbers = keep_numbers(line_digitized)  # Extract numbers from the line
        try:
            if numbers:  # Check if num is not empty
                result = first_and_last(numbers)
                total_sum += int(result)
                print(f"{line_number}. {line} -> {line_digitized} -> {numbers} -> {result}")
            else:
                print(f"Empty line detected at line {line_number}")
        except Exception as e:
            print(f"Error processing line {line_number}: {e}")

    print(f"Total sum: {total_sum}")

if __name__ == "__main__":
    main()
