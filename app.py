import tkinter as tk
from tkinter import messagebox
from chat import get_response, bot_name
from utils import speak, listen, identify_speaker, train_model, load_model
import os

# Define colors and fonts
BG_COLOR = "#333333"  # Dark grey
TEXT_COLOR = "#E1FFFF"  # Off white
BUTTON_COLOR = "#666666"  # Medium grey
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class ChatApplication:
    def __init__(self):
        self.window = tk.Tk()
        self._setup_main_window()
        self.model= load_model('model.pkl')

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Chat application")
        self.window.resizable(width=False, height=False)
        self.window.config(width=500, height=600, bg=BG_COLOR)

        # Head label
        head_label = tk.Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome to the Chat", font=FONT_BOLD, pady=20)
        head_label.place(relwidth=1)

        # Text widget
        self.text_widget = tk.Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, padx=5, pady=5)
        self.text_widget.place(relwidth=1, rely=0.08, relheight=0.745)
        self.text_widget.configure(cursor="arrow", state=tk.DISABLED)

        # Scroll bar
        scrollbar = tk.Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        # Bottom label
        bottom_label = tk.Label(self.window, bg=BG_COLOR, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # Message entry box
        self.msg_entry = tk.Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self.send_message)

        # Send button
        send_button = tk.Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BUTTON_COLOR, fg=TEXT_COLOR, command=lambda: self.send_message(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.03, relwidth=0.22)

        # Record button
        record_button = tk.Button(bottom_label, text="Record", font=FONT_BOLD, width=20, bg=BUTTON_COLOR, fg=TEXT_COLOR, command=self.record_message)
        record_button.place(relx=0.77, rely=0.05, relheight=0.03, relwidth=0.22)

        # Identify Speaker button
        identify_button = tk.Button(bottom_label, text="Identify Speaker", font=FONT_BOLD, width=20, bg=BUTTON_COLOR, fg=TEXT_COLOR, command=self.identify_speaker)
        identify_button.place(relx=0.77, rely=0.10, relheight=0.03, relwidth=0.22)

    def send_message(self, event=None):
        msg = self.msg_entry.get()
        if msg:
            self._insert_message(msg, 'You')
            response = get_response(msg)
            self._insert_message(response, bot_name)
            self.msg_entry.delete(0, END)

    def record_message(self):
        msg = listen()
        if msg:
            self._insert_message(msg, 'You')
            response = get_response(msg)
            self._insert_message(response, bot_name)

    def identify_speaker(self):
        # Assuming 'last_recorded_audio.wav' is the last recorded audio file
        speaker = identify_speaker('last_recorded_audio.wav', self.model, self.label_names)
        messagebox.showinfo("Identified Speaker", f"The last speaker was: {speaker}")

    def _insert_message(self, msg, sender):
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=tk.NORMAL)
        self.text_widget.insert(tk.END, msg1)
        self.text_widget.configure(state=tk.DISABLED)
        if sender == bot_name:
            speak(msg)
        self.text_widget.see(tk.END)

if __name__ == "__main__":
    app = ChatApplication()
    app.run()
