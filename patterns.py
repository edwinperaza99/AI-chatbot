# TODO: add factual information 
# variables for buildings and services that have the same consistent hours
LIBRARY_HOURS = "Monday to Thursday 7:00 AM to 10:00 PM, Friday 7:00 AM to 5:00 PM, Saturday and Sunday 9:00 AM to 5:00 PM"
TSU_HOURS = "Monday to Thursday 7:00 AM to 10:00 PM, Friday 7:00 AM to 5:00 PM, Saturday and Sunday 9:00 AM to 5:00 PM"
PARKING_HOURS = "Monday to Thursday 7:00 AM to 10:00 PM, Friday 7:00 AM to 5:00 PM, Saturday and Sunday 9:00 AM to 5:00 PM"

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
        "location": "next to the Pollak Library",
        "hours": "Monday to Thursday 7:00 AM to 10:00 PM, Friday 7:00 AM to 5:00 PM, Saturday and Sunday 9:00 AM to 5:00 PM"
    },
    "Engineering Building": {
        "regex": r"engineering|eng",
        "location": "next to the TSU",
        "hours": "Monday to Thursday 7:00 AM to 10:00 PM, Friday 7:00 AM to 5:00 PM, Saturday and Sunday 9:00 AM to 5:00 PM"
    },
    "Titan Shops": {
        "regex": r"titan.*shops|bookstore|store",
        "location": "tbd",
        "hours": "Monday to Thursday 8:00 AM to 5:00 PM, Friday 8:00 AM to 3:00 PM"
    },
    "Becker Amphitheater": {
        "regex": r"becker|amphitheater",
        "location": "tbd",
        "hours": "tbd"
    },
    "Greenhouse Complex": {
        "regex": r"greenhouse|horticulture",
        "location": "tbd",
        "hours": "tbd"
    },
    "Children's Center": {
        "regex": r"children.*center",
        "location": "tbd",
        "hours": "tbd"
    },
    "Carl's Jr": { 
        "regex": r"carl.*jr",
        "location": "tbd",
        "hours": "tbd"
    },
    "Starbucks": {
        "regex": r"starbucks",
        "location": "tbd",
        "hours": "tbd"
    },
    "Gastronome": {
        "regex": r"gastronome",
        "location": "tbd",
        "hours": "tbd"
    },
    "College Park": {
        "regex": r"college.*park",
        "location": "tbd",
        "hours": "tbd"
    },
    "Clayes Performing Arts Center": {
        "regex": r"clayes|performing.*arts",
        "location": "tbd",
        "hours": "tbd"
    },
    "Dan Black Hall": {
        "regex": r"dan.*black|db|hall",
        "location": "tbd",
        "hours": "tbd"
    },
    "Education Classroom": {
        "regex": r"education|ed|classroom",
        "location": "tbd",
        "hours": "tbd"
    },
    "Eastside Parking Structure": { 
        "regex": r"eastside|parking.*structure",
        "location": "tbd",
        "hours": "tbd"
    },
    "Golleher Alumni House": {
        "regex": r"golleher|alumni",
        "location": "tbd",
        "hours": "tbd"
    },
    "Goodwin Field": {
        "regex": r"goodwin|field",
        "location": "tbd",
        "hours": "tbd"
    },
    "Humanities Building": {
        "regex": r"humanities|hum",
        "location": "tbd",
        "hours": "tbd"
    },
    "Kinesiology and Health Science Building": {
        "regex": r"kinesiology|khs",
        "location": "tbd",
        "hours": "tbd"
    },
    "Langsdorf Hall": {
        "regex": r"langsdorf|lh",
        "location": "tbd",
        "hours": "tbd"
    },
    "McCarthy Hall": {
        "regex": r"mccarthy|mh",
        "location": "tbd",
        "hours": "tbd"
    },
    "Parking and Transportation Services": {
        "regex": r"parking|transportation",
        "location": "tbd",
        "hours": "tbd"
    },
    "Residence Halls": {
        "regex": r"residence|halls",
        "location": "tbd",
        "hours": "tbd"
    },
    "Pollak Library": {
        "regex": r"library|pollak",
        "location": "next to the quad",
        "hours": "Monday to Thursday 7:00 AM to 10:00 PM, Friday 7:00 AM to 5:00 PM, Saturday and Sunday 9:00 AM to 5:00 PM"
    },
    "Ruby Gerontology Center": {
        "regex": r"ruby|gerontology",
        "location": "tbd",
        "hours": "tbd"
    },
    "Student Health and Counseling Center": {
        "regex": r"student.*health|counseling",
        "location": "tbd",
        "hours": "tbd"
    },
    "Mihaylo Hall": {
        "regex": r"mihaylo|mh",
        "location": "tbd",
        "hours": "tbd"
    },
    "Student Housing": {
        "regex": r"student.*housing",
        "location": "tbd",
        "hours": "tbd"
    },
    "Student Recreation Center": { 
        "regex": r"student.*recreation|src",
        "location": "tbd",
        "hours": "tbd"
    },
    "Titan Stadium": {
        "regex": r"titan.*stadium",
        "location": "tbd",
        "hours": "tbd"
    },
    "Titan House": {
        "regex": r"titan.*house",
        "location": "tbd",
        "hours": "tbd"
    },
    "Titan Stadium": {
        "regex": r"titan.*stadium",
        "location": "tbd",
        "hours": "tbd"
    },
    "Titan Student Union": {
        "regex": r"titan.*student.*union|tsu",
        "location": "next to the Engineering Building",
        "hours": "Monday to Thursday 7:00 AM to 10:00 PM, Friday 7:00 AM to 5:00 PM, Saturday and Sunday 9:00 AM to 5:00 PM"
    },
    # direction for services inside buildings below main building
    "Pantry": {
        "regex": r"pantry",
        "location": "TSU",
        "hours": "Monday to Thursday 10:00 AM to 5:00 PM, Friday 10:00 AM to 3:00 PM"
    },
    "University Hall": {
        "regex": r"university|uh",
        "location": "tbd",
        "hours": "tbd"
    },
    "University Police": {
        "regex": r"university.*police|up",
        "location": "tbd",
        "hours": "tbd"
    },
    "Visual Arts": {
        "regex": r"visual|arts",
        "location": "tbd",
        "hours": "tbd"
    },
    "Nutwood Parking Structure": {
        "regex": r"nutwood|parking.*structure",
        "location": "tbd",
        "hours": "tbd"
    },
    "State College Parking Structure": {
        "regex": r"state.*college|parking.*structure",
        "location": "tbd",
        "hours": "tbd"
    },

}

# TODO: check for laptops, calculators, scantrons, microwaves etc.