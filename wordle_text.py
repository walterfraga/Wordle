from game.model.Guess import Guess
from game.evaluator.WordleEvaluator import WordleEvaluator
from game.WordleGame import WordleGame
from game.validator.WordleValidaor import WordleValidator


def main():
    validator = WordleValidator()
    evaluator = WordleEvaluator()
    wordle_game = WordleGame(6, validator, evaluator)

    while range(wordle_game.guesses):
        input_word = input('Gues my word?\n')
        wordle_guess = wordle_game.is_chosen_word(input_word)
        if wordle_guess.guess == Guess.INVALID:
            for invalid_reason in wordle_guess.invalid_reasons:
                print(invalid_reason)
        if wordle_guess.guess == Guess.INCORRECT:
            for hint in wordle_guess.hints:
                print(hint['letter'] + ' ' + hint['hint'])

        if wordle_guess.guess == Guess.CORRECT:
            print("Yeah you guessed my word")
            exit(0)
    print('You were unable to guess my word.\n It was: ' + wordle_game.chosen_word)


if __name__ == "__main__":
    main()
