class WordleValidator:

    def __init__(self):
        pass

    def validate(self, word):
        reasons = []
        if not len(word) == 5:
            reasons.append('Must be 5 length')
        if not word.isalpha():
            reasons.append('Not alpha character')
        if not len(reasons) == 0:
            return reasons
        return None
