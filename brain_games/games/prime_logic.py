import random
from .. import common_logic


def prime():
    condition = 'Answer "yes" if given number is prime. Otherwise answer "no".'

    def get_number():
        number = random.randint(1, 1000)
        return number

    def is_prime_number(number):
        number = int(number)
        counter = 0
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                counter += 1
                break
        result = 'yes' if counter == 0 else 'no'
        return result

    common_logic.logic(condition, get_number, is_prime_number)
