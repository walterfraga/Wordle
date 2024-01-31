class WordleEvaluator:

    def __init__(self):
        pass

    def evaluate(self, chosen_word, guess_word):
        hint = ''
        index = 0
        for letter in guess_word:
            if letter in chosen_word:
                if chosen_word[index] == letter:
                    hint += letter + ' - Correct Place\n'
                else:
                    hint += letter + ' - In word\n'
            else:
                hint += letter + ' - Not in Word\n'
            index = index + 1
        return hint
