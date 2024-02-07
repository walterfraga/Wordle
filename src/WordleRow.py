import tkinter as tk





class WordleRow:
    # Ensured one entry in text
    def validate_one_entry(self, text):
        return not len(text) > 1

    def get_letter(self, entry):
        for child in self.root.grid_slaves():
            if child == entry:
                return child.get()

    def key_press_event(self, event, entry):
        current_column_position = self.get_current_position(event)
        word = ''
        # travers in reverse
        for entry in self.entries:
            word += self.get_letter(entry)
            print(word)
            child_column_position = entry.grid_info()['column']
            if child_column_position == current_column_position + 1:
                if str(event.char).isalnum():
                    entry.config(state='normal')
                    entry.focus_set()
                elif event.keysym != 'Tab':
                    entry.config(state='disabled')

        if len(word) == 5 and (event.keysym == 'KP_Enter' or event.keysym == 'Return'):
            self.entered_word = word
        return

    def get_current_position(self, event):
        current_column_position = -1
        for child in self.entries:
            if event.widget == child:
                current_column_position = child.grid_info()['column']
                break
        return current_column_position

    def __init__(self, root, row, num_entries):
        self.root = root
        self.entered_word = ''
        self.entries = []

        validation = root.register(self.validate_one_entry)
        for col in range(num_entries):
            root.columnconfigure(row, weight=1)
            entry = tk.Entry(root, width=5, validate="key", validatecommand=(validation, "%P"))
            entry.grid(row=row, column=col, pady='5')
            entry.bind("<KeyPress>", lambda event: self.key_press_event(event, entry))
            self.entries.append(entry)
            if col != 0:
                entry.config(state='disabled')

    def get_values(self):
        return [entry.get() for entry in self.entries]
