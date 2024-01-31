import random

from game.model.Guess import Guess
from game.model.WordleGuessResult import WordleGuessResult


class WordleGame:

    def __init__(self, guesses, validator, evaluator):
        word_file = open("game/resources/words.txt", "r")
        words = word_file.readlines()
        self.chosen_word = random.choice(words)
        self.guesses = guesses
        self.validator = validator
        self.evaluator = evaluator

    def is_chosen_word(self, guess_word):
        invalid_reason = self.validator.validate(guess_word)
        if invalid_reason is not None:
            return WordleGuessResult(Guess.INVALID, invalid_reason)
        if self.guesses == 0:
            return WordleGuessResult(Guess.EXPIRED)
        if self.chosen_word == guess_word:
            return WordleGuessResult(Guess.CORRECT)
        else:
            self.guesses = self.guesses - 1
            hints = self.evaluator.evaluate(self.chosen_word, guess_word)
            return WordleGuessResult(Guess.INCORRECT, None, hints)
