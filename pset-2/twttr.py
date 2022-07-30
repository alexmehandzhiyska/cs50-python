title = input('Input: ')
vowels = ['a', 'e', 'i', 'o', 'u']

for letter in title:
    if letter.lower() in vowels:
        title = title.replace(letter, '')

print(title)