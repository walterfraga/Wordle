import requests


class WordsService:

    def __init__(self, length):
        self.length = length
        pass

    def get_random_word(self):
        random_word_response = requests.get(
            url='https://random-word-api.herokuapp.com/word?length=' + str(self.length))

        random_word = random_word_response.json()

        return random_word[0]


