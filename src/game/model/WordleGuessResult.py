class WordleGuessResult:

    def __init__(self, guess, invalid_reasons=None, hints=None):
        self.guess = guess
        self.invalid_reasons = invalid_reasons
        self.hints = hints
