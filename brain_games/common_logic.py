import prompt


def logic(condition, get_question, get_answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello', name, '!')
    print(condition)
    count = 0
    while count <= 2:
        question = get_question()
        print('Question:', question)
        user_answer = prompt.string('Your answer:')
        real_answer = get_answer(question)
        if user_answer == real_answer:
            print('Correct!')
            count += 1
        else:
            result = f'"{user_answer}" is wrong answer ;(. Correct answer was "{real_answer}".'
            print(result)
            print("Let's try again,", name, '!')
    print('Congratulations,', name, '!!')
