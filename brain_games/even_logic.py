import random, prompt


def even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello', name, '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count <= 2:
        number = random.randint(1, 1000)
        print('Question:', number)
        user_answer = prompt.string('Your answer: ')
        real_answer = 'yes' if number % 2 == 0 else 'no'
        if user_answer == real_answer:
            print('Correct!')
            count += 1
        else:
            result = f'"{user_answer}" is wrong answer ;(. Correct answer was "{real_answer}".'
            print(result)
            print("Let's try again,", name, '!')
    print('Congratulations,', name, '!!')
