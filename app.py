import tkinter as tk
import tkinter.font as tkFont
from bot import Chatbot


class ChatApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chatbot")
        self.geometry("400x500")
        self.configure(bg="grey15")  # Light gray background

        self.chatbot = Chatbot()

        # Text widget
        self.text_widget = tk.Text(self, state="disabled", bg="grey40", wrap="word")
        self.text_widget.pack(padx=15, pady=15, expand=True, fill=tk.BOTH)

        # Custom font
        custom_font = tkFont.Font(family="Helvetica", size=12, weight="bold")

        # User messages style
        self.text_widget.tag_configure(
            "right",
            justify="right",
            background="#64b5f6",  # Light blue background
            lmargin1=10,
            lmargin2=10,
            spacing3=2,
            foreground="black",
            font=custom_font,
        )

        # Bot messages style
        self.text_widget.tag_configure(
            "left",
            justify="left",
            background="#81c784",  # Light green background
            lmargin1=10,
            lmargin2=10,
            spacing3=2,
            foreground="black",
            font=custom_font,
        )

        # Input frame
        input_frame = tk.Frame(self, bg="#f0f0f0")
        input_frame.pack(padx=15, pady=10, fill=tk.X)

        # Entry widget
        self.entry_widget = tk.Entry(
            input_frame, width=35, highlightthickness=0, font=custom_font
        )
        self.entry_widget.grid(row=0, column=0, padx=0, sticky="ew")
        self.entry_widget.bind("<Return>", self.send_message)

        # Set column weights so entry widget takes up all available space
        input_frame.columnconfigure(0, weight=1)
        input_frame.columnconfigure(1, weight=0)
        input_frame.columnconfigure(2, weight=0)

        # Create a spacer label
        spacer_label = tk.Label(input_frame, bg="#f0f0f0")
        spacer_label.grid(row=0, column=1, padx=(0, 8))

        # Send button
        self.send_button = tk.Button(
            input_frame, text="Send", command=self.send_message
        )
        self.send_button.grid(row=0, column=2, padx=0)

        self.minsize(200, 400)
        self.resizable(True, True)

    def send_message(self, event=None):
        user_input = self.entry_widget.get()
        if user_input.strip():
            self.update_chat_window("You", user_input, "right")
            self.entry_widget.delete(0, tk.END)

            response = self.chatbot.get_response(user_input)
            self.update_chat_window("Bot", response, "left")

    def update_chat_window(self, sender, message, tag):
        self.text_widget.config(state="normal")
        self.text_widget.insert(tk.END, f"{sender}: {message}\n", tag)
        self.text_widget.config(state="disabled")
        self.text_widget.see(tk.END)


def main():
    app = ChatApplication()
    app.mainloop()


if __name__ == "__main__":
    main()
