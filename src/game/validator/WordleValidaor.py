from src.game.validator.InvalidWordReason import InvalidWordReason


class WordleValidator:

    def __init__(self, length, list_valid_words=None):
        self.length = length
        self.list_valid_words = list_valid_words

    def validate(self, word):
        reasons = []
        if word is not None:
            if not len(word) == self.length:
                reasons.append(InvalidWordReason.INVALID_LENGTH)
            if not word.isalpha():
                reasons.append(InvalidWordReason.NOT_ALPHA)
            if self.list_valid_words is not None and word not in self.list_valid_words:
                reasons.append(InvalidWordReason.UNKNOWN_WORD)
            if not len(reasons) == 0:
                return reasons
        return None
