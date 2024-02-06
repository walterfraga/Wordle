from tkinter import *
from tkinter import ttk



class WordleUI:
    def __init__(self):
        pass

    def play(self):
        ws = Tk()
        ws.title('Wordle')
        ws.geometry('430x225')
        ws['bg'] = '#AC99F2'

        title_panel = PanedWindow()
        title_panel.pack(fill=BOTH, expand=1)

        title_label = Label(title_panel, text="Wordle")
        title_panel.add(title_label)

        game_panel = PanedWindow()
        game_panel.pack(fill=BOTH, expand=1)

        game_label = Label(game_panel, text="Game")
        game_panel.add(game_label)

        remaining_letters_panel = PanedWindow()
        remaining_letters_panel.pack(fill=BOTH, expand=1)

        remaining_letters_label = Label(remaining_letters_panel, text="remaining letters")
        remaining_letters_panel.add(remaining_letters_label)





        ws.mainloop()

if __name__ == "__main__":
    wordle_ui = WordleUI()
    wordle_ui.play()
