import prompt

def welcome_user():
    name = prompt.string('May I have your name? ')
    result = f'Hello, {name}!'
    print(result)