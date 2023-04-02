import random
from .. import common_logic


def calculation():
    condition = 'What is the result of the expression?'

    def get_expression():
        first_number = random.randint(1, 1000)
        second_number = random.randint(1, 1000)
        operant = random.choice(['+', '-', '*'])
        result = f'{first_number}{operant}{second_number}'
        return result

    def get_answer(expression):
        real_answer = str(eval(expression))
        return real_answer

    common_logic.logic(condition, get_expression, get_answer)
