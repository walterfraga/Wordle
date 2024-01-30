


def main():
    wordle_game = WordleGame(6)

    for index in range(6):
        input_word = input('Gues my word?\n')
        if input_word == chosen_word:
            print("Yeah you guessed my word")
            exit(0)
    print('You were unable to guess my word\n. It was: ' + chosen_word)


if __name__ == "__main__":
    main()
