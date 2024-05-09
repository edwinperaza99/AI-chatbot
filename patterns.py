# variables for buildings and services that have the same consistent hours
LIBRARY_HOURS = "Monday to Thursday 7:00 AM to midnight. Friday 7:00 AM to 5:00. Weekends 9:00 AM to 5:00 PM. The north side of the library closes at midnight on weekdays. Times may vary during holidays and breaks"
PARKING_HOURS = "Monday to Thursday 7:00 AM to 10:00 PM, Friday 7:00 AM to 5:00 PM. Parking is enforced 24/7 for special zones including no overnight parking areas, disabled stalls, loading zones and fire lanes "
# hours for main buildings such as engineering, humanities, etc.
BUILDING_HOURS = "Monday to Thursday 7:00 AM to 10:00 PM, Friday 7:00 AM to 5:00 PM, Saturday and Sunday 9:00 AM to 5:00 PM"

DEFAULT_CONTACT = "There is no number listed for this service, but you can try calling the main campus number: (657) 278-2011"
DINNING_CONTACT = "Call Campus Dining or OC Choice Express at (657) 278-4124 or csufcampusdining@fullerton.edu"
PARKING_CONTACT = "Call Parking and Transportation Services at (657) 278-3082 or email csufcampusparking@fullerton.edu"

# Predefined patterns and responses, define more here
general_responses = {
    r"hi|hello|hey|howdy": [
        "Hello! How can I help you today?",
        "Hi there! What can I do for you?",
        "Hey! Looking for assistance?",
    ],
    r"how are you|how is it going": [
        "I'm a bot, so I'm always doing great!",
        "Doing well, thanks for asking!",
    ],
    r"thank you|thanks": ["You're welcome!", "No problem!"],
    r"help|what can you do": [
        "I can help with general location, hours, and services information."
    ],
    r"what are you|who are you": [
        "I am a chatbot that can assist with general location, hours, and services information."
    ],
    r"bye|exit": ["Goodbye! Have a great day!", "See you later!"],
}

# can be used for buildings and services information
buildings = {
    "Titan Shops": {
        "regex": r"titan.*shops|bookstore|store",
        "location": "located in Commons 2 Dock",
        "hours": "Mon - Thurs: 7:30 AM - 7:00 PM. Fri: 7:30 AM - 5:00 PM. Closed on weekends",
        "contact": "657.278.3418 or titanshops@fullerton.edu.",
    },
    "Becker Amphitheater": {
        "regex": r"becker|amphitheater",
        "location": "located in front of Titan Shops and the TSU",
        "hours": "24/7",
        "contact": DEFAULT_CONTACT,
    },
    "Greenhouse Complex": {
        "regex": r"greenhouse|horticulture",
        "location": "located just west of McCarthy Hall",
        "hours": "Mon - Fri: 8:30am to 4:30pm",
        "contact": "Call Edward Read at (657) 278-2766 or e-mail at: eread@fullerton.edu",
    },
    "Children's Center": {
        "regex": r"children.*center",
        "location": "located just across the Titan Stadium at Children's Wy",
        "hours": "7:45AM - 5:45PM, Monday through Thursday, and 7:45AM - 5:15PM on Friday. We are closed on all University holidays and require specialized scheduling during Spring Break, Fall Recess, Winter Recess, and the Summer",
        "contact": "Call (657) 278-2961.",
    },
    "Carl's Jr": {
        "regex": r"carl.*jr",
        "location": "located on the east side of campus",
        "hours": "Monday - Thursday: 8:00 AM - 7:00 PM. Friday: 8:00 AM - 1:00 PM. Hours may vary during summer and holidays",
        "contact": DINNING_CONTACT,
    },
    "Togo's": {
        "regex": r"togo",
        "location": "located on the first floor of the TSU",
        "hours": "Monday - Thursday: 10:00 AM - 7:00 PM. Friday: 10:00 AM - 2:00 PM. Hours may vary during summer and holidays",
        "contact": DINNING_CONTACT,
    },
    "Pieology": {
        "regex": r"pieology|pizza",
        "location": "located on the first floor of the TSU",
        "hours": "Monday - Thursday: 10:00 AM - 7:00 PM. Friday: 10:00 AM - 2:00 PM. Hours may vary during summer and holidays",
        "contact": DINNING_CONTACT,
    },
    "Starbucks": {
        "regex": r"starbucks|coffee",
        "location": "available at three locations on campus: in the TSU, Pollak Library, and Mihaylo Hall",
        "hours": "different by location, but the Pollak Library location tends to be open the latest. Their hours are: Monday - Thursday: 8:00 AM - 7:00 PM. Friday: 8:00 AM - 1:00 PM",
        "contact": DINNING_CONTACT,
    },
    "Panda Express": {
        "regex": r"panda.*express",
        "location": "located on the first floor of the TSU",
        "hours": "Monday - Thursday: 9:00 AM - 7:00 PM. Friday: 9:00 AM - 2:00 PM. Hours may vary during summer and holidays",
        "contact": DINNING_CONTACT,
    },
    "Juice It Up": {
        "regex": r"juice.*it.*up",
        "location": "located on the first floor of the TSU",
        "hours": "Monday - Thursday: 8:00 AM - 6:30 PM. Friday: 8:30 AM - 1:30 PM. Hours may vary during summer and holidays",
        "contact": DINNING_CONTACT,
    },
    "Hibachi San": {
        "regex": r"hibachi.*san",
        "location": "located on the first floor of the TSU",
        "hours": "Monday - Thursday: 9:00 AM - 7:00 PM. Friday: 9:00 AM - 2:00 PM. Hours may vary during summer and holidays",
        "contact": DINNING_CONTACT,
    },
    "Baja Fresh": {
        "regex": r"baja.*fresh",
        "location": "located on the first floor of the TSU",
        "hours": "Monday - Thursday: 10:00 AM - 5:00 PM. Hours may vary during summer and holidays",
        "contact": DINNING_CONTACT,
    },
    "Fresh Kitchen": {
        "regex": r"fresh.*kitchen",
        "location": "located on the first floor of the TSU",
        "hours": "not available at the moment, please call for more information",
        "contact": DINNING_CONTACT,
    },
    "Avanti Markets": {
        "regex": r"avanti.*markets",
        "location": "located in the first floor of College Park",
        "hours": "Monday - Thursday: 7:00 AM - 9:00 PM. Friday: 7:00 AM - 5:00 PM. Hours may vary during summer and holidays",
        "contact": DINNING_CONTACT,
    },
    "Gastronome": {
        "regex": r"gastronome",
        "location": "located at the Resident Dining Hall",
        "hours": "different throughout the year, call for more information",
        "contact": DINNING_CONTACT,
    },
    "Late Night Cafe": {
        "regex": r"late.*night|cafe",
        "location": "located at the Resident Dining Hall",
        "hours": "different throughout the year, call for more information",
        "contact": DINNING_CONTACT,
    },
    "College Park": {
        "regex": r"college.*park\b|\bcp\b",
        "location": "located across our main campus",
        "hours": "7:00 AM - 10:00 PM. Closed on weekends",
        "contact": "For more information, please contact (714) 868-2542.",
    },
    "Clayes Performing Arts Center": {
        "regex": r"clayes|performing.*arts|\bcpac\b",
        "location": "located between the TSU and Pollak Library, right in front of Titan Shops",
        "hours": "Tuesday-Friday: 12 pm to 4 pm. Closed on major holidays, Winter, Spring and Summer Breaks",
        "contact": "(657) 278-3371",
    },
    "Computer Science Building": {
        "regex": r"\bcs\b|computer.*science",
        "location": "located on the east side of the campus next to Parking Lot E",
        "hours": BUILDING_HOURS,
        "contact": "call (657) 278-3700 or CSDept@fullerton.edu",
    },
    "Dan Black Hall": {
        "regex": r"dan.*black|\bdb\b",
        "location": "located on the south side of campus next to McCarthy Hall",
        "hours": BUILDING_HOURS,
        "contact": DEFAULT_CONTACT,
    },
    "Engineering Building": {
        "regex": r"engineering|\beng\b",
        "location": "located on the east side of campus next to the Computer Science Building",
        "hours": BUILDING_HOURS,
        "contact": "call (657) 278-3012",
    },
    "Education Classroom": {
        "regex": r"education|\bec\b|ed.*classroom",
        "location": "located next to the Pollak Library and the Humanities Building",
        "hours": BUILDING_HOURS,
        "contact": "call (657) 278-3411",
    },
    "Eastside Parking Structure": {
        "regex": r"eastside",
        "location": "located to the southeast of College of Engineering and Computer Science",
        "hours": PARKING_HOURS,
        "contact": PARKING_CONTACT,
    },
    "Golleher Alumni House": {
        "regex": r"golleher|alumni",
        "location": "located off State College Boulevard and Student Union Way",
        "hours": "Monday to Friday 8:00 AM to 5:00 PM, closed on weekends",
        "contact": "call (657) 278-2586",
    },
    "Goodwin Field": {
        "regex": r"goodwin|field",
        "location": "located off West Campus Drive and Yorba Linda Boulevard, near the Arboretum in the back of campus",
        "hours": "different throughout the year, call for more information",
        "contact": "call (657) 278-2777",
    },
    "Humanities Building": {
        "regex": r"humanities|\bhum\b",
        "location": "located next to the quad and the Pollak Library",
        "hours": BUILDING_HOURS,
        "contact": "call (657) 278-3528  ",
    },
    "Kinesiology and Health Science Building": {
        "regex": r"kinesiology|\bkhs\b",
        "location": "located off Gymnasium Drive near the Intramural fields towards Yorba Linda Boulevard",
        "hours": BUILDING_HOURS,
        "contact": "call (657) 278-3316",
    },
    "Langsdorf Hall": {
        "regex": r"langsdorf|\blh\b",
        "location": "located southeast of campus next to Gordon Hall",
        "hours": BUILDING_HOURS,
        "contact": DEFAULT_CONTACT,
    },
    "McCarthy Hall": {
        "regex": r"mccarthy|\bmh\b",
        "location": "located between Gordon Hall and Greenhouses, right in front of Dan Black Hall",
        "hours": BUILDING_HOURS,
        "contact": "Call: (657) 278-3583",
    },
    "Parking and Transportation Services": {
        "regex": r"park.*tra|transportation",
        "location": "located south of the campus near Student Health and Counseling Center",
        "hours": "Monday to Friday 8 AM to 5PM",
        "contact": "Call: 657-278-3082",
    },
    "Residence Halls": {
        "regex": r"residence|res.*hall|\bdorm\b|dormitory|housing",
        "location": "located east of the campus next to The Gastronome",
        "hours": "Monday to Friday 8AM to 5PM",
        "contact": "Call: 657-278-2168",
    },
    "Pollak Library": {
        "regex": r"library|pollak",
        "location": "located at the center of the CSUF campus",
        "hours": LIBRARY_HOURS,
        "contact": "Call: 657-278-3284 or Visit the Research Center during desk hours",
    },
    "Circulation Desk": {
        "regex": r"circulation|circ|checkout.*book|reserve.*book|borrow.*book|return.*book",
        "location": "located at the first floor of the south side of the Pollak Library",
        "hours": LIBRARY_HOURS,
        "contact": "Call: (657) 278-2721",
    },
    "Titan Card": {
        "regex": r"titan.*card|id.*card|student.*id|\btcard\b",
        "location": "located at the first floor of the south side of the Pollak Library",
        "hours": "Monday to Thursday 8:00 AM to 6:00 PM, Friday 8:00 AM to 5:00 PM, closed on weekends",
        "contact": "Call (657) 278-3555",
    },
    "Ruby Gerontology Center": {
        "regex": r"ruby|gerontology|\brgc\b",
        "location": "located near the Arboretum off Gymnasium drive towards Yorba Linda Boulevard",
        "hours": BUILDING_HOURS,
        "contact": DEFAULT_CONTACT,
    },
    "Student Health and Counseling Center": {
        "regex": r"student.*health|counseling",
        "location": "located to the north of McCarthy Hall",
        "hours": "Mon - Fri: 8 a.m. - 5 p.m.",
        "contact": "Call (657) 278-2800",
    },
    "Mihaylo Hall": {
        "regex": r"mihaylo|\bmh\b",
        "location": "located on the corner of Nutwood and Folino Drive on the south side of campus",
        "hours": BUILDING_HOURS,
        "contact": "Call 657-278-4652",
    },
    "Student Housing": {
        "regex": r"student.*housing",
        "location": "located on the east of engineering and computer science building and north of eastside parking structure",
        "hours": BUILDING_HOURS,
        "contact": "Call (657) 278-4652 or email mcbe@fullerton.edu",
    },
    "Student Recreation Center": {
        "regex": r"student.*recreation|\bsrc\b",
        "location": "located off Gymnasium and West Campus Drive across from the tennis courts",
        "hours": "Monday to Thursday 6:00 AM to 12:00 AM, Friday 6:00 AM to 10:00 PM, Saturday and Sunday 8:00 AM to 10:00 PM. Times vary over summer",
        "contact": "Call (657) 278-7529 or email titancreation@fullerton.edu",
    },
    "Titan Stadium": {
        "regex": r"titan.*stadium",
        "location": "located off West Campus Drive and Yorba Linda Boulevard in the back of campus",
        "hours": BUILDING_HOURS,
        "contact": "Call (657) 278-2777",
    },
    "Titan House": {
        "regex": r"titan.*house|\bth\b",
        "location": "located off Gymnasium Drive next to the intramural fields",
        "hours": BUILDING_HOURS,
        "contact": DEFAULT_CONTACT,
    },
    "Titan Student Union": {
        "regex": r"titan.*student.*union|\btsu\b",
        "location": "located near the middle of the campus off State College Boulevard",
        "hours": "Monday to Friday 7:00 AM to 10:00 PM, Saturday and Sunday 12:00 PM to 8:00 PM",
        "contact": "Call (657) 278-2468",
    },
    # direction for services inside buildings below main building
    "Pantry": {
        "regex": r"pantry",
        "location": "located inside the TSU",
        "hours": "Monday to Thursday 10:00 AM to 5:00 PM, Friday 10:00 AM to 3:00 PM",
        "contact": "Call (657) 278-2468",
    },
    "Gordon Hall": {
        "regex": r"university hall|\buh\b|\bgh\b|gordon",
        "location": "located next to the quad towards the 57 freeway",
        "hours": BUILDING_HOURS,
        "contact": "Call (657) 278-3606",
    },
    "University Police": {
        "regex": r"university.*police|security|emergency",
        "location": "located west side of the campus near Student Recreation Center",
        "hours": "24/7",
        "contact": "Their non emergency number is (657) 278-2515. For emergencies call 911.",
    },
    "Visual Arts": {
        "regex": r"visual|arts|\bva\b",
        "location": "located adjacent to Nutwood Parking Structure at the corner of Arts Drive and State College Boulevard",
        "hours": BUILDING_HOURS,
        "contact": "Call (657) 278-3471 or email artdept@fullerton.edu",
    },
    "Nutwood Parking Structure": {
        "regex": r"nutwood|\bnps\b",
        "location": "located on the corner of Nutwood and State College Boulevard",
        "hours": PARKING_HOURS,
        "contact": PARKING_CONTACT,
    },
    "State College Parking Structure": {
        "regex": r"state.*college",
        "location": "located to the West of Student Recreation Center",
        "hours": PARKING_HOURS,
        "contact": PARKING_CONTACT,
    },
}

specific_responses = {
    r"register for classes|class registration| how do I register for class": [
        "You can register for classes in the student portal.",
        "To register for classes, you can contact our administration office.",
        "Registration for classes is available online.",
    ],
    r"how do I sign up for classes| signups": [
        "Signing up for classes is easy! You can do it online through our student portal.",
        "To sign up for classes, log in to your student account and navigate to the registration section.",
    ],
    r"when is class registration": [
        "Class registration starts around April 4th, 2024 for Fall 2024.",
    ],
    r"where can I buy scantrons|scantrons|scantron|where can I get scantrons|how to get scantrons|how do I get scantrons|where can I find scantrons": [
        "You can find scantrons at the following locations: Titan Shops/Bookstore, The Brief convenience store (2nd floor of Langsford Hall), The Yum convenience store (1st floor of Titan Student Union), Scantron vending machine 1st floor of College Park, Scantron vending machine 2nd floor of Pollak Library North"
    ],
    r"where can I find microwave|microwave|microwaves|where can I use the microwave|is there a microwave?": [
        "You can find microwaves in Titan Student Union.",
        "Microwaves are available in Titan Student Union",
    ],
    r"where can I find IT help|Where can I seek IT help": [
        "You can get help in Student Genius Center located in the Pollak Library North, first floor.",
        "The Student Genius Center located in the first floor of Pollak Library North is available to assist you with IT support.",
    ],
    r"where can I borrow laptop|borrow laptop|laptop|laptops": [
        "You can loan out a laptop for the semester in Student Genius Center located in the Pollak Library North, first floor.",
        "Students can loan out laptops for the semester in Student Genius Center located in the Pollak Library North, first floor.",
    ],
    r"where can I find tutoring|tutoring|tutor|tutors": [
        "You can find tutoring services in the Learning Center located in the Pollak Library North, first floor.",
        "Tutoring services are available in the Learning Center located in the Pollak Library North, first floor.",
    ],
    r"where can I park|parking structure|where can I find parking|where can I park my car": [
        "You can park in the Eastside Parking Structure, State College Parking Structure, and Nutwood Parking Structure.",
        "Parking is available in the Eastside Parking Structure, State College Parking Structure, and Nutwood Parking Structure.",
    ],
    r"where can I find food|food|where can I eat|where can I find dining": [
        "You can find food in the Gastronome, Titan Student Union, and College Park.",
        "Dining options are available in the Gastronome, Titan Student Union, and College Park.",
    ],
    r"how do I add money to my Titan Card|add money to Titan Card|add money to my student card": [
        "You can add money to your Titan Card online or in person at the Titan Card office.",
        "To add money to your Titan Card, visit the Titan Card office or add funds online.",
    ],
}
