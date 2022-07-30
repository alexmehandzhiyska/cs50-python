from ast import Match
import re

def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    condition_1 = starts_with_2_letters(s)
    condition_2 = has_max_6_chars(s)
    condition_3 = has_middle_numbers(s)
    condition_4 = first_digit_is_0(s)
    condition_5 = has_special_chars(s)

    return condition_1 and condition_2 and not condition_3 and condition_4 != '0' and not condition_5

def starts_with_2_letters(s):
    match = re.match(r'\w{2,}', s)
    return bool(match)

def has_max_6_chars(s):
    return len(s) <= 6

def has_special_chars(s):
    match = re.match(r'[\. !?;,]', s)
    return bool(match)

def has_middle_numbers(s):
    match = re.match(r'.+\d+\D+', s)
    return bool(match)

def first_digit_is_0(s):
    match = re.findall(r'\d', s)
    if (match):
        return match[0]
    return 1

main()