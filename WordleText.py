from game.evaluator.Hint import Hint
from game.model.Guess import Guess
from game.evaluator.WordleEvaluator import WordleEvaluator
from game.WordleGame import WordleGame
from game.validator.WordleValidaor import WordleValidator

YELLOW = '\033[93m{}\033[00m'

GREEN = '\033[92m{}\033[00m'


class WordleText():
    def __init__(self):
        pass

    def play(self):
        validator = WordleValidator()
        evaluator = WordleEvaluator()
        wordle_game = WordleGame(6, validator, evaluator)

        print('Wordle')
        print('You have 6 chances. Try to guess my word\n')
        while range(wordle_game.guesses):
            input_word = input('Attempt (' + str(7 - wordle_game.guesses) + ') . Gues my word?\n')
            wordle_guess_result = wordle_game.is_chosen_word(input_word)
            if wordle_guess_result.guess == Guess.INVALID:
                for invalid_reason in wordle_guess_result.invalid_reasons:
                    print(invalid_reason.value)
            if wordle_guess_result.guess == Guess.INCORRECT:
                self.display_hints(wordle_guess_result)

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
