import random

from Guess import Guess
from WordleGuess import WordleGuess


class WordleGame:

    def __init__(self, guesses, validator, evaluator):
        word_file = open("words.txt", "r")
        words = word_file.readlines()
        self.chosen_word = random.choice(words)
        self.guesses = guesses
        self.validator = validator
        self.evaluator = evaluator

    def is_chosen_word(self, guess_word):
        invalid_reason = self.validator.validate(guess_word)
        if invalid_reason is not None:
            return WordleGuess(Guess.INVALID, invalid_reason)
        if self.guesses == 0:
            return WordleGuess(Guess.EXPIRED)
        if self.chosen_word == guess_word:
            return WordleGuess(Guess.CORRECT)
        else:
            self.guesses = self.guesses - 1
            hints = self.evaluator.evaluate(self.chosen_word, guess_word)
            return WordleGuess(Guess.INCORRECT, None, hints)
