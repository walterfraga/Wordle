from src.game.validator.InvalidWordReason import InvalidWordReason


class WordleValidator:

    def __init__(self):
        pass

    def validate(self, word):
        reasons = []
        if word is not None:
            if not len(word) == 5:
                reasons.append(InvalidWordReason.INVALID_LENGTH)
            if not word.isalpha():
                reasons.append(InvalidWordReason.NOT_ALPHA)
            if not len(reasons) == 0:
                return reasons
        return None
