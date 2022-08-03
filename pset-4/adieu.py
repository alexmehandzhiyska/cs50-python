import inflect

p = inflect.engine()

names_list = []

while True:
    try:
        name = input('Name: ')
        names_list.append(name)
    except:
        print(f'Adieu, adieu, to {p.join(names_list)}')
        break