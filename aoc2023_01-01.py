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

def main():
    line_number = 0
    total_sum = 0
    for line in sys.stdin:
        line_number += 1
        line = line.strip()
        numbers = keep_numbers(line.strip())  # Extract numbers from the line
        try:
            if numbers:  # Check if num is not empty
                result = first_and_last(numbers)
                total_sum += int(result)
                print(f"{line_number}. '{line}' -> Extracted Numbers: '{numbers}' -> First & Last Digits Concatenated: {result}")
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
