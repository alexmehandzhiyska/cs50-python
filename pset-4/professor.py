import random

def get_level():
    while True:
        try:
            n = int(input())

            if n >= 1 and n <= 3:
                return n
        except:
            pass

def generate_integer(level):
    min = pow(10, level - 1)
    max = pow(10, level) - 1

    if min == 1:
        min = 0

    return random.randint(min, max)

def generate_question(level):
    x = generate_integer(level)
    y = generate_integer(level)

    question = f'{x} + {y} = '
    answer = x + y
    return [question, answer]

def main():
    level = get_level()
    questions_count = 0

    question, answer = generate_question(level)
    incorrect_tries = 0
    incorrect_questions = 0

    while True:
        if questions_count == 10:
            print(f'Score: {11 - incorrect_questions}')
            break
        try:
            result = int(input(question))
            questions_count += 1

            if result == answer:
                question, answer = generate_question(level)
            else:
                incorrect_tries += 1
                print('EEE')

            if incorrect_tries == 3:
                incorrect_questions += 1
                print(f'{question}{answer}')
                question, answer = generate_question(level)
        except:
            print('EEE')            

if __name__ == "__main__":
    main()