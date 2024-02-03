import random


class WordPicker:
    def pick_word(self):
        word_file = open("../src/game/resources/words.txt", "r")
        words = word_file.readlines()
        return random.choice(words)
