from src.game.services.WordsService import WordsService
from src.game.evaluator.Hint import Hint
from src.game.model.Guess import Guess
from src.game.evaluator.WordleEvaluator import WordleEvaluator
from src.game.WordleGame import WordleGame
from src.game.validator.WordleValidaor import WordleValidator

YELLOW = '\033[93m{}\033[00m'

GREEN = '\033[92m{}\033[00m'


class WordleText:
    def __init__(self):
        pass

    def play(self):
        word_length = 5
        number_of_guesses = 7
        word_service = WordsService(word_length)

        validator = WordleValidator(word_length, word_service.get_all_words())
        evaluator = WordleEvaluator()
        wordle_game = WordleGame(number_of_guesses, word_service.get_random_word(), validator, evaluator)

        print('Wordle')
        print('You have 6 chances. Try to guess the word\n')
        while range(wordle_game.guesses):
            input_word = input('Attempt (' + str((number_of_guesses+1) - wordle_game.guesses) + ') . Guess my word?\n')
            wordle_guess_result = wordle_game.is_chosen_word(input_word)
            if wordle_guess_result.guess == Guess.INVALID:
                for invalid_reason in wordle_guess_result.invalid_reasons:
                    print(invalid_reason.value)
            if wordle_guess_result.guess == Guess.INCORRECT:
                self.display_hints(wordle_guess_result)
                remaining_letter = ''
                for letter in wordle_game.get_remaining_letters():
                    remaining_letter += letter
                print('remaining letter are: ' + remaining_letter)

            if wordle_guess_result.guess == Guess.CORRECT:
                print("Yeah you guessed my word")
                exit(0)
        print('You were unable to guess my word.\n It was: ' + wordle_game.chosen_word)

    def format_colour(self, colour, text):
        return colour.format(text)

    def display_hints(self, wordle_guess_result):
        displayed_hint = ''
        for hint in wordle_guess_result.hints:
            if hint['hint'] == Hint.NOT_IN_WORD:
                displayed_hint += hint['letter']
            if hint['hint'] == Hint.WITHIN_WORD:
                displayed_hint += self.format_colour(YELLOW, hint['letter'])
            if hint['hint'] == Hint.CORRECT_PLACE:
                displayed_hint += self.format_colour(GREEN, hint['letter'])
        print(displayed_hint)


if __name__ == "__main__":
    wordle_text = WordleText()
    wordle_text.play()
