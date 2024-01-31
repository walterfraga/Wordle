class WordleEvaluator:

    def __init__(self):
        pass

    def evaluate(self, chosen_word, guess_word):
        hints = []
        index = 0
        for letter in guess_word:
            if letter.upper() in chosen_word.upper():
                if chosen_word[index] == letter:
                    hints.append(dict(letter=letter, hint='Correct Place'))
                else:
                    hints.append(dict(letter=letter, hint='In word'))
            else:
                hints.append(dict(letter=letter, hint='Not in Word'))
            index = index + 1
        return hints
