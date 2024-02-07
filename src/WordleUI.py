import tkinter as tk

from WordleRow import WordleRow


class WordleUI:
    def __init__(self):
        root = tk.Tk()
        root.title('Wordle')
        root.geometry('250x250')
        root['bg'] = '#AC99F2'

        label = tk.Label(root, text='Wordle')
        label.grid(row=0, columnspan=5)
        root.columnconfigure(0, weight=1)

        self.wordle_row1 = WordleRow(root, 1, 5)
        #self.wordle_row2 = WordleRow(root, 2, 5)
        #self.wordle_row3 = WordleRow(root, 3, 5)
        #self.wordle_row4 = WordleRow(root, 4, 5)
        #self.wordle_row5 = WordleRow(root, 5, 5)
        #self.wordle_row6 = WordleRow(root, 6, 5)
        root.mainloop()


if __name__ == "__main__":
    wordle_application = WordleUI()
