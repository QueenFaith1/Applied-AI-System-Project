import json

def parse_mood_with_claude(user_description: str) -> dict:
    """
    Parse user mood description into a music profile.
    Uses keyword matching to simulate AI natural language understanding.
    """
    
    description = user_description.lower()
    
    # Energy detection
    if any(word in description for word in ["celebrate", "promotion", "excited", "hype", "party", "upbeat"]):
        energy = 0.85
        mood = "happy"
        genre = "pop"
    elif any(word in description for word in ["study", "focus", "work", "concentrate", "calm"]):
        energy = 0.35
        mood = "focused"
        genre = "lofi"
    elif any(word in description for word in ["sad", "nostalgic", "emotional", "deep", "melancholy"]):
        energy = 0.4
        mood = "nostalgic"
        genre = "folk"
    elif any(word in description for word in ["workout", "gym", "run", "intense", "power"]):
        energy = 0.9
        mood = "intense"
        genre = "rock"
    elif any(word in description for word in ["chill", "relax", "sleep", "peaceful", "quiet"]):
        energy = 0.25
        mood = "chill"
        genre = "ambient"
    else:
        energy = 0.65
        mood = "happy"
        genre = "pop"
    
    profile = {"genre": genre, "mood": mood, "energy": energy}
    print(f"✅ AI interpreted your mood as: {profile}")
    return profile