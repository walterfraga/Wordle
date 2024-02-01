from enum import Enum


class Hint(Enum):
    CORRECT_PLACE = 'Letter in correct place.'
    WITHIN_WORD = 'Letter within word.'
    NOT_IN_WORD = 'Letter not in word'
