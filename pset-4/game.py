import random

def prompt(prompt_message):
    while True:
        try:
            result = int(input(prompt_message))

            while result < 1:
                result = int(input(prompt_message))

            return result
        except:
            pass

n = prompt('Level: ')
    
rand_num = random.randint(1, n)

while True:
    guess = prompt('Guess: ')

    if guess < rand_num:
        print('Too small!')
    elif guess > rand_num:
        print('Too large!')
    else:
        print('Just right!')
        break