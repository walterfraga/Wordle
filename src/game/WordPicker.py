import random
import os


class WordPicker:
    def pick_word(self):
        working_directory = os.getcwd()
        word_file = open(working_directory + "/src/game/resources/words.txt", "r")
        words = word_file.readlines()
        return random.choice(words)
