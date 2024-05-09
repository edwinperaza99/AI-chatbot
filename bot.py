import re
import random
from patterns import general_responses, buildings, register_class_responses


class Chatbot:
    def __init__(self):
        self.buildings = buildings
        self.general = general_responses
        # Identify keywords for location and hours
        self.location_keywords = r"where|location|locate|direct|get|find"
        self.hours_keywords = r"when|time|hours|close|open"
        self.contact_keywords = r"contact|phone|email|reach"
        self.register = register_class_responses

    def get_response(self, user_input):
        """
        Get a response from the chatbot based on the user input.

        input: user_input - the input from the user

        output: response - the chatbot's response
        """
        response_parts = []

        # Check for general patterns first
        for pattern, responses in self.general.items():
            if re.search(pattern, user_input, re.IGNORECASE):
                response_parts.append(random.choice(responses))

        # Check for building-specific information
        for building, info in self.buildings.items():
            if re.search(info["regex"], user_input, re.IGNORECASE):
                if re.search(self.location_keywords, user_input, re.IGNORECASE):
                    response_parts.append(f"{building} is {info['location']}.")
                if re.search(self.hours_keywords, user_input, re.IGNORECASE):
                    response_parts.append(
                        f"The hours of operation for the {building} are {info['hours']}."
                    )
                if re.search(self.contact_keywords, user_input, re.IGNORECASE):
                    response_parts.append(f"To contact {building}. {info['contact']}")

        # TODO: add another loop to check for specific help such as registering for classes
        for pattern, responses in self.register.items():
            if re.search(pattern, user_input, re.IGNORECASE):
                response_parts.append(random.choice(responses))

        # Compile final response or default if no specific information is found
        if response_parts:
            return "\n".join(response_parts)
        else:
            return "Sorry, I don't understand that. I am a chatbot that can assist with general location, hours, and services information."


if __name__ == "__main__":
    print("\nERROR: bot.py is the wrong file! Run program from app.py\n")
