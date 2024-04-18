import re
import random
from responses import responses


class Chatbot:
    def __init__(self):
        self.responses = responses

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
