import tkinter as tk
from tkinter import filedialog

class NoteTakingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Note Taking App")
        self.master.geometry("400x300")

        # Create the text box
        self.note_entry = tk.Text(self.master)
        self.note_entry.pack()

        # Create the menu bar
        self.menu_bar = tk.Menu(self.master)

        # Create the file menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New Note", command=self.new_note)
        self.file_menu.add_command(label="Open Note", command=self.open_note)
        self.file_menu.add_command(label="Save Note", command=self.save_note)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_application)

        # Add the file menu to the menu bar
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Create the format menu
        self.format_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.format_menu.add_command(label="Bold", command=self.bold_text)
        self.format_menu.add_command(label="Italic", command=self.italic_text)
        self.format_menu.add_command(label="Underline", command=self.underline_text)
        self.format_menu.add_separator()
        self.format_menu.add_command(label="Bullet Points", command=self.bullet_points)

        # Add the format menu to the menu bar
        self.menu_bar.add_cascade(label="Format", menu=self.format_menu)

        # Set the menu bar for the root window
        self.master.config(menu=self.menu_bar)

    def new_note(self):
        # Clear the text box
        self.note_entry.delete("1.0", tk.END)

    def open_note(self):
        # Open a file dialog to select a file
        file_path = filedialog.askopenfilename()

        # Read the contents of the file and insert them into the text box
        with open(file_path, "r") as f:
            self.note_entry.insert(tk.END, f.read())

    def save_note(self):
        # Open a file dialog to select a file
        file_path = filedialog.asksaveasfilename()

        # Write the contents of the text box to the file
        with open(file_path, "w") as f:
            f.write(self.note_entry.get("1.0", tk.END))

    def exit_application(self):
        # Destroy the root window
        self.master.destroy()

    def bold_text(self):
        # Get the current tags for the selected text
        tags = self.note_entry.tag_names("sel.first")

        # Toggle the "bold" tag for the selected text
        if "bold" in tags:
            self.note_entry.tag_remove("bold", "sel.first", "sel.last")
        else:
            self.note_entry.tag_add("bold", "sel.first", "sel.last")

    def italic_text(self):
        # Get the current tags for the selected text
        tags = self.note_entry.tag_names("sel.first")

        # Toggle the "italic" tag for the selected text
        if "italic" in tags:
            self.note_entry.tag_remove("italic", "sel.first", "sel.last")
        else:
            self.note_entry.tag_add("italic", "sel.first", "sel.last")

    def underline_text(self):
        # Get the current tags for the selected text
        tags = self.note_entry.tag_names("sel.first")

        # Toggle the "underline" tag for the selected text
        if "underline" in tags:
            self.note_entry.tag_remove("underline", "sel.first", "sel.last")
        else:
            self.note_entry.tag_add("underline", "sel.first", "sel.last")

    def bullet_points(self):
        # Insert a bullet point at the beginning of the selected line
        line_start = self.note_entry.index("sel.first linestart")
        self.note_entry.insert(line_start, "• ")

if __name__ == "__main__":
    # Create the root window
    root = tk.Tk()

    # Create the note-taking application
    app = NoteTakingApp(root)

    # Start the event loop
    root.mainloop()
