import random
from . import common_logic

def even():
    condition = 'Answer "yes" if the number is even, otherwise answer "no".'

    def get_number():
        number = random.randint(1, 1000)
        return number

    def get_answer(number):
        real_answer = 'yes' if int(number) % 2 == 0 else 'no'
        return real_answer

    common_logic.logic(condition, get_number, get_answer)
