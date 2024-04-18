# Predefined patterns and responses, define more here
responses = {
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
    r"(where|located).*((cs|computer.*science).*building)": [
        "It is located next to the Pollak Library."
    ],
    r"(library|pollak).*(close|open|time)": [
        "The hours of operation of the Pollak Library are Monday to Thursday 7:00 a.m to 10:00 p.m. on the South Side of the library and the north side closes at midnight. Friday it is open 7:00 a.m. to 5:00 p.m. Saturday and Sunday it is open from 9:00 a.m. to 5:00 p.m."
    ],
}
