from src.game.model.Guess import Guess
from src.game.model.WordleGuessResult import WordleGuessResult


class WordleGame:

    def __init__(self, guesses, words_service, validator, evaluator):
        self.chosen_word = words_service.get_random_word()
        self.guesses = guesses
        self.validator = validator
        self.evaluator = evaluator
        self.entered_letters = set()

    def is_chosen_word(self, guess_word):
        invalid_reason = self.validator.validate(guess_word)
        if invalid_reason is not None:
            return WordleGuessResult(Guess.INVALID, invalid_reason)
        for letter in guess_word:
            self.entered_letters.add(letter)
        if self.guesses == 0:
            return WordleGuessResult(Guess.EXPIRED)
        if self.chosen_word == guess_word:
            return WordleGuessResult(Guess.CORRECT)
        else:
            self.guesses = self.guesses - 1
            hints = self.evaluator.evaluate(self.chosen_word, guess_word)
            return WordleGuessResult(Guess.INCORRECT, None, hints)

    def get_remaining_letters(self):
        remaining_letters = []
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            if letter not in self.entered_letters:
                remaining_letters.append(letter)
            else:
                remaining_letters.append(' ')
        return remaining_letters
