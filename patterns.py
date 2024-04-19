# TODO: add factual information 
# variables for buildings and services that have the same consistent hours
LIBRARY_HOURS = "Opens at 7:00 AM Monday to Friday, 9:00 AM on weekends. The south side closes at 10:00 PM Monday to Friday and the north side closes at midnight. Both sides close at 5:00 PM Friday to Sunday. Times may vary during holidays and breaks"
PARKING_HOURS = "Monday to Thursday 7:00 AM to 10:00 PM, Friday 7:00 AM to 5:00 PM, Saturday and Sunday 9:00 AM to 5:00 PM"
# hours for main buildings such as engineering, humanities, etc.
BUILDING_HOURS = "Monday to Thursday 7:00 AM to 10:00 PM, Friday 7:00 AM to 5:00 PM, Saturday and Sunday 9:00 AM to 5:00 PM"

DEFAULT_CONTACT = "There is no number listed for this service, but you can try calling the main campus number: (657) 278-2011 ."
DINNING_CONTACT = "Contact Campus Dining or OC Choice Express at (657) 278-4124 or  csufcampusdining@fullerton.edu"


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
    r"thank you|thanks": ["You're welcome!", "No problem!"],
    r"help|what can you do": ["I can help with general location, hours, and services information."],
    r"what are you|who are you": ["I am a chatbot that can assist with general location, hours, and services information."],
    r"bye|exit": ["Goodbye! Have a great day!", "See you later!"],
}

# can be used for buildings and services information
# TODO: add factual information 
buildings = {
    "Titan Shops": {
        "regex": r"titan.*shops|bookstore|store",
        "location": "Commons 2 Dock",
        "hours": "Mon - Thurs: 7:30 AM - 7:00 PM. Fri: 7:30 AM - 5:00 PM. Closed on weekends.",
        "contact": "657.278.3418 or titanshops@fullerton.edu."
    },
    "Becker Amphitheater": {
        "regex": r"becker|amphitheater",
        "location": "In front of Titan Shops and the TSU.",
        "hours": "24/7",
        "contact": DEFAULT_CONTACT
    },
    "Greenhouse Complex": {
        "regex": r"greenhouse|horticulture",
        "location": "The BGC is located just west of McCarthy Hall.",
        "hours": "Mon - Fri: 8:30am to 4:30pm.",
        "contact": "Call Edward Read at (657) 278-2766 or e-mail at: eread@fullerton.edu"
    },
    "Children's Center": {
        "regex": r"children.*center",
        "location": "tbd",
        "hours": "Open from 7:45AM - 5:45PM, Monday through Thursday, and 7:45AM - 5:15PM on Friday. We are closed on all University holidays and require specialized scheduling during Spring Break, Fall Recess, Winter Recess, and the Summer.",
        "contact": "Call (657) 278-2961."
    },
    "Carl's Jr": { 
        "regex": r"carl.*jr",
        "location": "located on the east side of campus.",
        "hours": "Monday - Thursday: 8:00 AM - 7:00 PM. Friday: 8:00 AM - 1:00 PM. Hours may vary during summer and holidays.",
        "contact": DINNING_CONTACT
    },
    "Togo's": {
        "regex": r"togo",
        "location": "located on the first floor of the TSU.",
        "hours": "Monday - Thursday: 10:00 AM - 7:00 PM. Friday: 10:00 AM - 2:00 PM. Hours may vary during summer and holidays.",
        "contact": DINNING_CONTACT
    },
    "Pieology": {
        "regex": r"pieology|pizza",
        "location": "located on the first floor of the TSU.",
        "hours": "Monday - Thursday: 10:00 AM - 7:00 PM. Friday: 10:00 AM - 2:00 PM. Hours may vary during summer and holidays.",
        "contact": DINNING_CONTACT
    },
    "Starbucks": {
        "regex": r"starbucks|coffee",
        "location": "There are three locations on campus: in the TSU, Pollak Library, and Mihaylo Hall.",
        "hours": "Hours vary by location, but the Pollak Library location tends to be open the latest. Their hours are: Monday - Thursday: 8:00 AM - 7:00 PM. Friday: 8:00 AM - 1:00 PM",
        "contact": DINNING_CONTACT
    },
    "Panda Express": {
        "regex": r"panda.*express",
        "location": "located on the first floor of the TSU.",
        "hours": "Monday - Thursday: 9:00 AM - 7:00 PM. Friday: 9:00 AM - 2:00 PM. Hours may vary during summer and holidays.",
        "contact": DINNING_CONTACT
    },
    "Juice It Up": {
        "regex": r"juice.*it.*up",
        "location": "located on the first floor of the TSU.",
        "hours": "Monday - Thursday: 8:00 AM - 6:30 PM. Friday: 8:30 AM - 1:30 PM. Hours may vary during summer and holidays.",
        "contact": DINNING_CONTACT
    },
    "Hibachi San": {
        "regex": r"hibachi.*san",
        "location": "located on the first floor of the TSU.",
        "hours": "Monday - Thursday: 9:00 AM - 7:00 PM. Friday: 9:00 AM - 2:00 PM. Hours may vary during summer and holidays.",
        "contact": DINNING_CONTACT
    },
    "Baja Fresh": {
        "regex": r"baja.*fresh",
        "location": "located on the first floor of the TSU.",
        "hours": "Monday - Thursday: 10:00 AM - 5:00 PM. Hours may vary during summer and holidays.",
        "contact": DINNING_CONTACT
    },
    "Fresh Kitchen": {
        "regex": r"fresh.*kitchen",
        "location": "located on the first floor of the TSU.",
        "hours": "Currently closed",
        "contact": DINNING_CONTACT
    },
    "Avanti Markets": {
        "regex": r"avanti.*markets",
        "location": "located in the first floor of College Park.",
        "hours": "Monday - Thursday: 7:00 AM - 9:00 PM. Friday: 7:00 AM - 5:00 PM. Hours may vary during summer and holidays.",
        "contact": DINNING_CONTACT
    },
    "Gastronome": {
        "regex": r"gastronome",
        "location": "Located at the Resident Dining Hall",
        "hours": "Please visit The Titan Eats website for updated hours of operation.",
        "contact": DINNING_CONTACT
    },
    "Late Night Cafe": {
        "regex": r"late.*night|cafe",
        "location": "Located at the Resident Dining Hall",
        "hours": "Please visit The Titan Eats website for updated hours of operation.",
        "contact": DINNING_CONTACT
    },
    "College Park": {
        "regex": r"college.*park|cp",
        "location": "located across our main campus.",
        "hours": "7:00 AM - 10:00 PM. Closed on weekends.",
        "contact": "For more information, please contact (714) 868-2542."
    },
    "Clayes Performing Arts Center": {
        "regex": r"clayes|performing.*arts|cpac",
        "location": "tbd",
        "hours": "Tuesday-Friday: 12 pm to 4 pm. Closed on major holidays, Winter, Spring and Summer Breaks",
        "contact": "(657) 278-3371"
    },
    "Computer Science Building": {
        "regex": r"cs|computer.*science",
        "location": "located on the east side of the campus next to Parking Lot E.",
        "hours": BUILDING_HOURS,
        "contact": "call (657) 278-3700 or CSDept@fullerton.edu"
    },
    "Dan Black Hall": {
        "regex": r"dan.*black|db|hall",
        "location": "located on the south side of campus next to McCarthy Hall.",
        "hours": BUILDING_HOURS,
        "contact": DEFAULT_CONTACT
    },
    "Engineering Building": {
        "regex": r"engineering|eng",
        "location": "located on the east side of campus next to the Computer Science Building.",
        "hours": BUILDING_HOURS,
        "contact": "call (657) 278-3012"
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
        "location": "located at the center of the CSUF campus",
        "hours": LIBRARY_HOURS,
        "contact": "Call: 657-278-3284 or Visit the Research Center during desk hours"
    },
    "Circulation Desk": {
        "regex": r"circulation|circ|checkout.*book|reserve.*book|borrow.*book|return.*book",
        "location": "located at the first floor of the south side of the Pollak Library",
        "hours": LIBRARY_HOURS,
        "contact": "Call Gregory Witmer at (657) 278-2721"
    },
    "Titan Card": {
        "regex": r"titan.*card|id",
        "location": "located at the first floor of the south side of the Pollak Library",
        "hours": "Monday to Thursday 8:00 AM to 6:00 PM, Friday 8:00 AM to 5:00 PM, closed on weekends",
        "contact": "Call (657) 278-3555"
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