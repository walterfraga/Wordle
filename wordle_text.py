from Guess import Guess
from WordleGame import WordleGame
from WordleValidaor import WordleValidator


def main():
    validator = WordleValidator()
    wordle_game = WordleGame(6, validator)

    while range(wordle_game.guesses):
        input_word = input('Gues my word?\n')
        wordle_guess = wordle_game.is_chosen_word(input_word)
        if wordle_guess.guess == Guess.INVALID:
            for reason in wordle_guess.reasons:
                print(reason)
        if wordle_guess.guess == Guess.CORRECT:
            print("Yeah you guessed my word")
            exit(0)
    print('You were unable to guess my word.\n It was: ' + wordle_game.chosen_word)


if __name__ == "__main__":
    main()
