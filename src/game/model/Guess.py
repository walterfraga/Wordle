from enum import Enum


class Guess(Enum):
    CORRECT = 0
    INCORRECT = 1
    EXPIRED = 3
    INVALID = 4
