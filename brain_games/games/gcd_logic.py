import math
import random
from .. import common_logic


def gcd_calculation():
    condition = 'Find the greatest common divisor of given numbers.'

    def get_expression():
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
        result = f'{first_number} {second_number}'
        return result

    def get_answer(expression):
        first, second = expression.split()
        real_answer = str(math.gcd(int(first), int(second)))
        return real_answer

    common_logic.logic(condition, get_expression, get_answer)
