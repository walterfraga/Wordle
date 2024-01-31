import random


class WordleGame:

    def __init__(self, guesses):
        word_file = open("words.txt", "r")
        words = word_file.readlines()
        self.chosen_word = random.choice(words)
        self.guesses = guesses

    def is_chosen_word(self, guess_word):
        if self.guesses == 0:
            return 3
        if self.chosen_word == guess_word:
            return 0
        else:
            self.guesses = self.guesses - 1
            return 1
