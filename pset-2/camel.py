message = input('camelCase: ')

for letter in message:
    if letter == letter.upper():
        message = message.replace(letter, f'_{letter.lower()}')

print(message)