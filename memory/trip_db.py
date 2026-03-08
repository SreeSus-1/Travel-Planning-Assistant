from tinydb import TinyDB
from datetime import datetime

db = TinyDB("trip_memory.json")

def save_trip(destination, budget, interests, days, itinerary, cost, culture, notes=""):
    db.insert({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "destination": destination,
        "budget": budget,
        "interests": interests,
        "days": days,
        "itinerary": itinerary,
        "cost": cost,
        "culture": culture,
        "notes": notes
    })

def get_all_trips():
    return db.all()