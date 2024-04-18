# Predefined patterns and responses, define more here
general_responses = {
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

# can be used for buildings and services information
# TODO: add factual information 
buildings = {
    "Computer Science Building": {
        "regex": r"cs|computer.*science",
        "location": "next to the Pollak Library, South Side of the library and the north side closes at midnight",
        "hours": "Monday to Thursday 7:00 AM to 10:00 PM, Friday 7:00 AM to 5:00 PM, Saturday and Sunday 9:00 AM to 5:00 PM"
    },
    "Pollak Library": {
        "regex": r"library|pollak",
        "location": "next to the quad",
        "hours": "Monday to Thursday 7:00 AM to 10:00 PM, Friday 7:00 AM to 5:00 PM, Saturday and Sunday 9:00 AM to 5:00 PM"
    },
    "Pantry": {
        "regex": r"pantry",
        "location": "TSU",
        "hours": "Monday to Thursday 10:00 AM to 5:00 PM, Friday 10:00 AM to 3:00 PM"
    },
    "Financial aid office": {
        "regex": r"financial.*aid",
        "location": "GH-123",
        "hours": "Monday to Thursday 8:00 AM to 5:00 PM, Friday 8:00 AM to 3:00 PM"
    },
}
