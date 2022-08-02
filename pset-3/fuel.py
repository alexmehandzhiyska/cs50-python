
while True:
    fraction = input('Fraction: ')

    try:
        x, y = map(int, fraction.split('/'))

        if x > y or y == 0:
            continue

        percentage = round((x / y) * 100)

        if percentage <= 1:
            print('E')
        elif percentage >= 99:
            print('F')
        else:
            print(f'{percentage}%')
        break
    except (ValueError, ZeroDivisionError):
        continue