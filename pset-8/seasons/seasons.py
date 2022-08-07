from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    birthdate_str = input('Date: ')
    is_valid = validate_date(birthdate_str)

    if not is_valid:
        sys.exit('Invalid date!')

    year, month, day = map(int, birthdate_str.split('-'))

    birthdate = date(year, month, day)
    today = date.today()

    dates_diff = today - birthdate
    mins_diff = dates_diff.days * 1440
    mins_diff_words = p.number_to_words(mins_diff, andword='')
    print(f'{mins_diff_words.capitalize()} minutes')
    
def validate_date(date):
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    return bool(re.match(pattern, date))


if __name__ == "__main__":
    main()