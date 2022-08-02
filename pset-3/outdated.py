months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    original_date = input('Date: ')

    try:
        if '/' in original_date:
            month, day, year = map(int, original_date.split('/'));
        elif ', ' in original_date:
            month_str, day_str, year = original_date.split(' ');
            month = months.index(month_str) + 1
            day = int(day_str[:-1])

        if month > 12 or day > 31:
            continue

        month = month if month >= 10 else f'0{month}'
        day = day if day >= 10 else f'0{day}'

        print(f'{year}-{month}-{day}')
        break
    except:
        continue