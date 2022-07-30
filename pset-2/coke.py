change = 50
coins = [25, 10, 5]

while change > 0:
    cents = int(input('Insert Coin: '))

    if cents in coins:
        change -= cents
    print(f'Amount due: {abs(change)}')