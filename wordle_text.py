from WordleGame import WordleGame


def main():
    wordle_game = WordleGame(6)

    for index in range(wordle_game.guesses):
        input_word = input('Gues my word?\n')
        if wordle_game.is_chosen_word(input_word) == 0:
            print("Yeah you guessed my word")
            exit(0)
    print('You were unable to guess my word.\n It was: ' + wordle_game.chosen_word)


if __name__ == "__main__":
    main()
