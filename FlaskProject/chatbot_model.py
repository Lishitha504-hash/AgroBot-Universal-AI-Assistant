import random

# Agriculture chatbot responses in Telugu
responses = {
    "greeting": [
        "నమస్కారం! నేను మీ వ్యవసాయ సహాయకుడిని. 🌱 ఈరోజు నేను మీకు ఎలా సహాయపడగలను?",
        "హాయ్! వ్యవసాయం మరియు పంటల గురించి ఏదైనా అడగండి. 🚜"
    ],
    "fertilizer": [
        "మెరుగైన దిగుబడి కోసం, సేంద్రీయ కంపోస్ట్ మరియు యూరియా వంటి నత్రజని అధికంగా ఉండే ఎరువును ఉపయోగించండి.",
        "వేరు పెరుగుదల కోసం ఫాస్ఫరస్ మరియు పొటాషియం ఆధారిత ఎరువులను ఉపయోగించడాన్ని పరిగణించండి."
    ],
    "pest": [
        "వేప నూనె స్ప్రే చాలా తెగుళ్ళకు ప్రభావవంతంగా ఉంటుంది.",
        "తెగుళ్ల జనాభాను నియంత్రించడానికి లేడీబగ్స్ వంటి సహజ వేటాడే జంతువులను పరిచయం చేయండి."
    ],
    "weather": [
        "విత్తనాలు వేసే ముందు దయచేసి స్థానిక వాతావరణ అంచనాను తనిఖీ చేయండి.",
        "భారీ వర్షాలు పడే అవకాశం ఉంటే మొక్కలకు నీరు పెట్టడం మానుకోండి."
    ],
    "default": [
        "నాకు దాని గురించి తెలియదు. దయచేసి వేరే విధంగా అడగగలరా?",
        "క్షమించండి, నాకు అర్థం కాలేదు. మీరు వేరే ప్రశ్న అడగగలరా?"
    ]
}


def get_response(user_input):
    # Convert input to lowercase for consistent matching
    user_input = user_input.lower()

    # Matching based on Telugu keywords (script and Romanized)
    if "నమస్కారం" in user_input or "హాయ్" in user_input or "namaskaram" in user_input or "hi" in user_input or "hai" in user_input:
        return random.choice(responses["greeting"])
    elif "ఎరువు" in user_input or "eruvu" in user_input or "fertilizer" in user_input:
        return random.choice(responses["fertilizer"])
    elif "తెగులు" in user_input or "tegulu" in user_input or "pest" in user_input:
        return random.choice(responses["pest"])
    elif "వాతావరణం" in user_input or "vatavaranam" in user_input or "weather" in user_input:
        return random.choice(responses["weather"])
    else:
        return random.choice(responses["default"])