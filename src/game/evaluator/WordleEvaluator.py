from src.game.evaluator.Hint import Hint


class WordleEvaluator:

    def __init__(self):
        pass

    def evaluate(self, chosen_word, guess_word):
        hints = []
        index = 0
        if guess_word is None or len(guess_word) == 0:
            return None

        for letter in guess_word:
            if letter.upper() in chosen_word.upper():
                if chosen_word[index].upper() == letter.upper():
                    hints.append(dict(letter=letter, hint=Hint.CORRECT_PLACE))
                else:
                    hints.append(dict(letter=letter, hint=Hint.WITHIN_WORD))
            else:
                hints.append(dict(letter=letter, hint=Hint.NOT_IN_WORD))
            index = index + 1
        return hints
