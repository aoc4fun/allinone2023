##########
# Part 1 #
##########

def sum_calibration_values(document):
    total_sum = 0
    for line in document:
        # Extract the first and last digit from each line
        digits = [char for char in line if char.isdigit()]
        if digits:
            first_digit = digits[0]
            last_digit = digits[-1]
            # Combine them into a two-digit number
            value = int(first_digit + last_digit)
            # Add to the total sum
            total_sum += value
    return total_sum

# Example usage
calibration_document = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet"
]

print(sum_calibration_values(calibration_document))

####################
# Part 1 First Try #
####################


def sum_calibration_values(document):
    # Mapping of words to digits
    word_to_digit = {
        "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    total_sum = 0
    for line in document:
        words_and_digits = ""
        # Replace word digits with actual digits
        for word, digit in word_to_digit.items():
            line = line.replace(word, digit)
        # Extract all digits from the line
        words_and_digits = ''.join([char for char in line if char.isdigit()])
        if words_and_digits:
            first_digit = words_and_digits[0]
            last_digit = words_and_digits[-1]
            # Combine them into a two-digit number
            value = int(first_digit + last_digit)
            # Add to the total sum
            total_sum += value
    return total_sum

# Example usage
calibration_document = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"
]

print(sum_calibration_values(calibration_document))

####################
# Part 2   2nd Try #
####################

# Hum, you are wrong. Take the "eightwothree" word. You should extract 8 2 3 .... With your approch, you forgot the 2. And in this precise case, with your order, you replace two by 2, and have eigh2three, and never replace the first word eight.

import re

def sum_calibration_values(document):
    # Mapping of words to digits
    word_to_digit = {
        "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    total_sum = 0
    for line in document:
        # Split line into words and characters
        elements = re.findall(r'\b\w+\b|\w', line)
        digits = []

        for element in elements:
            if element.isdigit():
                digits.append(element)
            elif element in word_to_digit:
                digits.append(word_to_digit[element])

        if digits:
            first_digit = digits[0]
            last_digit = digits[-1]
            # Combine them into a two-digit number
            value = int(first_digit + last_digit)
            # Add to the total sum
            total_sum += value
    return total_sum

# Example usage
calibration_document = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"
]

print(sum_calibration_values(calibration_document))

####################
# Part 2   3rd Try #
####################
# again, false, your findall return the complete string only.
# elements = re.findall(r'\b\w+\b|\w', two1nine) return two1nine.

import re

def sum_calibration_values(document):
    # Mapping of words to digits
    word_to_digit = {
        "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    # Regular expression pattern to match digit words or single digits
    pattern = r'\b(one|two|three|four|five|six|seven|eight|nine)\b|\d'

    total_sum = 0
    for line in document:
        # Find all digit words and digits
        matches = re.findall(pattern, line)
        digits = []

        for match in matches:
            # Match can be a tuple if it matches a digit word
            digit_word = match[0]
            if digit_word:
                # Convert digit word to digit
                digits.append(word_to_digit[digit_word])
            else:
                # Directly append the digit
                digits.append(match)

        if digits:
            first_digit = digits[0]
            last_digit = digits[-1]
            # Combine them into a two-digit number
            value = int(first_digit + last_digit)
            # Add to the total sum
            total_sum += value
    return total_sum

# Example usage
calibration_document = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"
]

# print(sum_calibration_values(calibration_document))

####################
# Part 2   4th Try #
####################

# digit_word = match[0]
#                  ~~~~~^^^
# IndexError: string index out of range

import re


def sum_calibration_values(document):
    # Mapping of words to digits
    word_to_digit = {
        "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    # Regular expression pattern to match digit words or single digits
    pattern = r'one|two|three|four|five|six|seven|eight|nine|\d'

    total_sum = 0
    for line in document:
        # Find all digit words and digits
        matches = re.findall(pattern, line)
        digits = []

        for match in matches:
            # Check if match is a digit word and convert to digit
            digits.append(word_to_digit.get(match, match))

        if digits:
            first_digit = digits[0]
            last_digit = digits[-1]
            # Combine them into a two-digit number
            value = int(first_digit + last_digit)
            # Add to the total sum
            total_sum += value
    return total_sum


# Example usage
calibration_document = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"
]

print(sum_calibration_values(calibration_document))