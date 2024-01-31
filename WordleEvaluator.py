class WordleEvaluator:

    def __init__(self):
        pass

    def evaluate(self, chosen_word, guess_word):
        hint = ''
        for letter in guess_word:
            if letter in chosen_word:
                hint += letter
        return hint
