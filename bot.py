import re


class Chatbot:
    def __init__(self):
        # Predefined patterns and responses, define more here
        self.patterns = {
            r"hi|hello": "Hello! How can I help you today?",
            r"how are you": "I'm a bot, so I'm always doing great!",
            r"bye|exit": "Goodbye! Have a great day!",
        }

    def get_response(self, user_input):
        """
        Get a response from the chatbot based on the user input.

        input: user_input - the input from the user

        output: response - the chatbot's response
        """
        # Check for patterns in the user input
        for pattern in self.patterns:
            # Use re.IGNORECASE to make the pattern case-insensitive
            if re.search(pattern, user_input, re.IGNORECASE):
                # Return the response corresponding to the pattern that matches
                return self.patterns[pattern]
        return "Sorry, I don't understand that."


if __name__ == "__main__":
    print("\nERROR: bot.py is the wrong file! Run program from app.py\n")
