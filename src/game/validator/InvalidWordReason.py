from enum import Enum


class InvalidWordReason(Enum):
    INVALID_LENGTH = 'Invalid word length.'
    NOT_ALPHA = 'Word must only contain letters.'
