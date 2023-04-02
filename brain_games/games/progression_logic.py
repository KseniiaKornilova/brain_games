import random
from .. import common_logic


def progression():
    condition = 'What number is missing in the progression?'

    def get_progression():
        initial_number = random.randint(-100, 100)
        difference = random.randint(1, 10)
        sequence = [initial_number + i * difference for i in range(10)]
        gap_index = random.randint(0, len(sequence) - 1)
        global gap
        gap = sequence[gap_index]
        sequence[gap_index] = '..'
        sequence = [str(x) for x in sequence]
        progression = ' '.join(sequence)
        return progression

    def get_answer(progression):
        return str(gap)

    common_logic.logic(condition, get_progression, get_answer)
