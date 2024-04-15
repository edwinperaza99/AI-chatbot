import tkinter as tk
import tkinter.font as tkFont
from bot import Chatbot


class ChatApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        # define screen settings
        self.title("Chatbot")
        self.geometry("400x500")
        self.configure(bg="gray15")  # Set the background color of the main window

        self.chatbot = Chatbot()  # Create an instance of the Chatbot class

        # Create a text widget to display the chat messages
        self.text_widget = tk.Text(self, state="disabled", bg="gray50", wrap="word")
        self.text_widget.pack(padx=15, pady=15)

        # Define custom font here
        customFont = tkFont.Font(family="Helvetica", size=12, weight="bold")

        # define user messages style
        self.text_widget.tag_configure(
            tagName="right",
            justify="right",
            background="gray40",
            lmargin1=10,
            lmargin2=10,
            spacing3=2,
            foreground="white",
            font=customFont,
        )

        # define bot messages style
        self.text_widget.tag_configure(
            tagName="left",
            justify="left",
            background="gray25",
            lmargin1=10,
            lmargin2=10,
            spacing3=2,
            foreground="white",
            font=customFont,
        )

        # Create an entry widget for user input
        self.entry_widget = tk.Entry(self, width=90)
        self.entry_widget.pack(padx=15, pady=15)
        self.entry_widget.bind("<Return>", self.on_enter_pressed)

    def on_enter_pressed(self, event):
        """
        Handle user input.

        input: event - the event that triggered this function

        output: None
        """
        user_input = self.entry_widget.get()
        self.update_chat_window("You", user_input, "right")
        self.entry_widget.delete(0, tk.END)

        response = self.chatbot.get_response(user_input)
        self.update_chat_window("Bot", response, "left")

    def update_chat_window(self, sender, message, tag):
        """
        Update the chat window with a new message.

        inputs:
            sender - the sender of the message
            message - the message to display
            tag - the tag to apply to the message

        output: None
        """
        self.text_widget.config(state="normal")
        self.text_widget.insert(tk.END, f"{sender}: {message}\n", tag)
        self.text_widget.config(state="disabled")
        self.text_widget.see(tk.END)


def main():
    app = ChatApplication()
    app.mainloop()


if __name__ == "__main__":
    main()
