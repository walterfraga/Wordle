from enum import Enum


class InvalidWordReason(Enum):
    UNKNOWN_WORD = "Unknown word."
    INVALID_LENGTH = 'Invalid word length.'
    NOT_ALPHA = 'Word must only contain letters.'
