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

def reversed_replace_with_number(match):
    word = match.group(0)
    return digit_words.get(word[::-1], "")

pattern = '|'.join(re.escape(word) for word in digit_words.keys())

def replace_first_and_last_digit_words(s): 
    # if no matches   
    match = list(re.finditer(pattern, s))
    if not match:
        return s  # No replacement needed

    # replace first occurence only if there were no numbers before it; in case there ere numbers,
    # we need to skip this step
    if not re.search('\d+', s[:match[0].start()]):
      s = re.sub(pattern, replace_with_number,s, count=1)

    # need to reverse string and replace the most rightmost occurence
    string_reversed = s[::-1]
    pattern_reversed = pattern[::-1]

    # Replace the first (leftmost) occurrence in the reversed string
    replaced_reversed = re.sub(pattern_reversed, reversed_replace_with_number, string_reversed, count=1)

    return replaced_reversed[::-1]
    

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
