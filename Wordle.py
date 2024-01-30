import random


def main():
    word_file = open("words.txt", "r")
    words = word_file.readlines()
    chosen_word = random.choice(words)
    print(chosen_word)


if __name__ == "__main__":
    main()
