import re
import random


class Chatbot:
    def __init__(self):
        # Predefined patterns and responses, define more here
        self.responses = {
            r"hi|hello|hey": [
                "Hello! How can I help you today?",
                "Hi there! What can I do for you?",
                "Hey! Looking for assistance?",
            ],
            r"how are you|how is it going": [
                "I'm a bot, so I'm always doing great!",
                "Doing well, thanks for asking!",
            ],
            r"bye|exit": ["Goodbye! Have a great day!", "See you later!"],
        }

    def get_response(self, user_input):
        """
        Get a response from the chatbot based on the user input.

        input: user_input - the input from the user

        output: response - the chatbot's response
        """
        # Check for patterns in the user input
        for pattern, responses in self.responses.items():
            # Use re.IGNORECASE to make the pattern case-insensitive
            if re.search(pattern, user_input, re.IGNORECASE):
                return random.choice(responses)  # Return a random response
        # default response if no patterns are found
        return "Sorry, I don't understand that."


if __name__ == "__main__":
    print("\nERROR: bot.py is the wrong file! Run program from app.py\n")
