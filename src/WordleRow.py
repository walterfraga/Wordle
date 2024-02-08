import tkinter as tk

from game.evaluator.Hint import Hint

WORDLE_GREEN = "#0ED644"

WORDLE_YELLOW = "#CCD851"


class WordleRow:
    # Ensured one entry in text
    def validate_one_entry(self, text):
        return not len(text) > 1

    def get_letter(self, entry):
        for grid_entry in self.wordle_ui.root.grid_slaves():
            if grid_entry == entry:
                return grid_entry.get()

    def key_press_event(self, event):
        current_column_position = self.get_current_position(event)
        word = ''
        # travers in reverse
        for entry in self.entries:
            word += self.get_letter(entry)
            child_column_position = entry.grid_info()['column']
            if child_column_position == current_column_position + 1:
                if str(event.char).isalnum():
                    entry.config(state='normal')
                    entry.focus_set()
                elif event.keysym != 'Tab':
                    entry.config(state='disabled')
            if child_column_position != 0 and child_column_position == current_column_position and event.keysym == 'BackSpace':
                entry.delete(0, 'end')
                entry.config(state='disabled')
                self.entries[child_column_position-1].delete(0, 'end')
                self.entries[child_column_position-1].focus_set()

        if len(word) == 5 and (event.keysym == 'KP_Enter' or event.keysym == 'Return'):
            self.wordle_ui.callback(word)
        return

    def set_hints(self, hints):
        index = 0
        for hint in hints:
            if hint['hint'].value == Hint.WITHIN_WORD.value:
                self.entries[index].config(disabledbackground=WORDLE_YELLOW)
                self.entries[index].config(disabledforeground="white")
            if hint['hint'].value == Hint.CORRECT_PLACE.value:
                self.entries[index].config(disabledbackground=WORDLE_GREEN)
                self.entries[index].config(disabledforeground="white")
            index = index + 1

    def get_current_position(self, event):
        current_column_position = -1
        for entry in self.entries:
            if entry == event.widget:
                current_column_position = entry.grid_info()['column']
                break
        return current_column_position

    def disable_rows(self, background_color=None):
        for entry in self.entries:
            if background_color is None:
                entry.config(state='disabled')
            else:
                entry.config(state='disabled', disabledbackground=background_color)

    def __init__(self, wordle_ui, row, columns):
        self.wordle_ui = wordle_ui
        self.entries = self.initialize_entry_columns(wordle_ui, columns, row)

    def initialize_entry_columns(self, wordle_ui, columns, row):
        entries = []
        validation = wordle_ui.root.register(self.validate_one_entry)
        for column in range(columns):
            wordle_ui.root.columnconfigure(row, weight=1)
            entry = tk.Entry(wordle_ui.root, width=5, validate="key", validatecommand=(validation, "%P"))
            entry.grid(row=row, column=column, pady='5')
            entry.bind("<KeyPress>", lambda event: self.key_press_event(event))
            entry.config(state='disabled')
            entries.append(entry)
        return entries

    def start(self):
        for child in self.entries:
            child.delete(0, 'end')
        self.entries[0].config(state='normal')
        self.entries[0].focus_set()

