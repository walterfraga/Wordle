import tkinter as tk


class WordleRow:
    def validate_input(self, text):
        if len(text) > 1:
            return False
        return True

    def toggle_state(self, event, entry):
        current_column_position = -1
        for child in self.root.grid_slaves():
            if event.widget == child:
                current_column_position = child.grid_info()['column']

        entered_word = ''
        for child in self.root.grid_slaves():
            if isinstance(child, tk.Entry):
                entered_word += child.get()
            child_column_position = child.grid_info()['column']
            if child_column_position == current_column_position + 1:
                if str(event.char).isalnum():
                    child.config(state='normal')
                    child.focus_set()
                elif event.keysym != 'Tab':
                    child.config(state='disabled')

        if len(entered_word) == 5 and (event.keysym == 'KP_Enter' or event.keysym == 'Return'):
            print(entered_word)

        return

    def __init__(self, root, row, num_entries):
        self.root = root
        self.entries = []

        validation = root.register(self.validate_input)
        for col in range(num_entries):
            root.columnconfigure(row, weight=1)
            entry = tk.Entry(root, width=5, validate="key", validatecommand=(validation, "%P"))
            entry.grid(row=row, column=col, pady='5')
            entry.bind("<KeyPress>", lambda event: self.toggle_state(event, entry))
            self.entries.append(entry)
            if col != 0:
                entry.config(state='disabled')

    def get_values(self):
        return [entry.get() for entry in self.entries]


class WordleApplication:
    def __init__(self, root):
        label = tk.Label(root, text='Wordle')
        label.grid(row=0, columnspan=5)
        root.columnconfigure(0, weight=1)

        self.wordle_row1 = WordleRow(root, 1, 5)
        # self.wordle_row2 = WordleRow(root, 2, 5)
        # self.wordle_row3 = WordleRow(root, 3, 5)
        # self.wordle_row4 = WordleRow(root, 4, 5)
        # self.wordle_row5 = WordleRow(root, 5, 5)
        # self.wordle_row6 = WordleRow(root, 6, 5)


if __name__ == "__main__":
    tk_root = tk.Tk()
    tk_root.title('Wordle')
    tk_root.geometry('250x250')
    tk_root['bg'] = '#AC99F2'
    wordle_application = WordleApplication(tk_root)
    tk_root.mainloop()
