import random

TIPS = [
    "Check tire pressure monthly to improve fuel efficiency.",
    "Avoid sudden braking to extend brake life.",
    "Change engine oil every 10,000 km or as per manufacturer’s advice.",
    "Keep your fuel tank at least half full to protect the fuel pump.",
    "Replace air filters every 15,000 km for better mileage."
]

def get_tip() -> str:
    return random.choice(TIPS)
