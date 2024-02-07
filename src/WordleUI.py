import tkinter as tk

from WordleRow import WordleRow
from game.WordleGame import WordleGame
from game.evaluator.WordleEvaluator import WordleEvaluator
from game.model.Guess import Guess
from game.services.WordsService import WordsService
from game.validator.WordleValidaor import WordleValidator

class WordleUI:

    def init_game(self):
        number_of_guesses = 6
        validator = WordleValidator()
        evaluator = WordleEvaluator()
        word_service = WordsService(5)
        return WordleGame(number_of_guesses, word_service, validator, evaluator)

    def enable_row(self, guesses):
        if guesses == 5:
            self.wordle_row2.start()
        elif guesses == 4:
            self.wordle_row3.start()
        elif guesses == 3:
            self.wordle_row4.start()
        elif guesses == 2:
            self.wordle_row5.start()
        elif guesses == 1:
            self.wordle_row6.start()

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Wordle')
        self.root.geometry('250x250')
        self.root['bg'] = '#AC99F2'

        self.wordle_game = self.init_game()
        label = tk.Label(self.root, text='Wordle')
        label.grid(row=0, columnspan=5)
        self.root.columnconfigure(0, weight=1)

        self.wordle_row1 = WordleRow(self, 1, 5)
        self.wordle_row2 = WordleRow(self, 2, 5)
        self.wordle_row3 = WordleRow(self, 3, 5)
        self.wordle_row4 = WordleRow(self, 4, 5)
        self.wordle_row5 = WordleRow(self, 5, 5)
        self.wordle_row6 = WordleRow(self, 6, 5)

        self.status_label = tk.Label(self.root, text='')
        self.status_label.grid(row=7, columnspan=5)

        self.remaining_letters = tk.Label(self.root, text='')
        self.remaining_letters.grid(row=8, columnspan=5)

        self.callback()
        self.root.mainloop()


    def callback(self, word=None):
        if word is None:
            self.wordle_row1.start()
            return
        wordle_guess_result = self.wordle_game.is_chosen_word(word)
        print(wordle_guess_result.guess)
        if wordle_guess_result.guess.value == Guess.INVALID.value:
            reasons = ''
            for invalid_reason in wordle_guess_result.invalid_reasons:
                reasons += invalid_reason.value
            self.status_label.config(text=reasons)
        if wordle_guess_result.guess.value == Guess.INCORRECT.value:
            self.enable_row(self.wordle_game.guesses)
            # self.display_hints(wordle_guess_result)
            remaining_letter = ''
            for letter in self.wordle_game.get_remaining_letters():
                remaining_letter += letter
            self.remaining_letters.config(text=remaining_letter)

        if wordle_guess_result.guess.value == Guess.CORRECT.value:
            self.status_label.Text = "Yeah you guessed my word"
            exit(0)

        if self.wordle_game.guesses == 0:
            self.status_label.config(text='You were unable to guess my word.\n It was: ' + self.wordle_game.chosen_word)


if __name__ == "__main__":
    wordle_application = WordleUI()
