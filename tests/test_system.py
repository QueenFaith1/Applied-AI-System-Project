from src.ai_profile import parse_mood_with_claude
from src.recommender import load_songs, recommend_songs, score_song

def test_celebration_mood():
    profile = parse_mood_with_claude("I just got a promotion and want to celebrate!")
    assert profile['mood'] == 'happy'
    assert profile['energy'] >= 0.8

def test_study_mood():
    profile = parse_mood_with_claude("I need to focus and study")
    assert profile['mood'] == 'focused'
    assert profile['energy'] <= 0.5

def test_nostalgic_mood():
    profile = parse_mood_with_claude("I am feeling nostalgic and emotional")
    assert profile['mood'] == 'nostalgic'

def test_load_songs():
    songs = load_songs("data/songs.csv")
    assert len(songs) == 15

def test_score_song():
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}
    song = {"genre": "pop", "mood": "happy", "energy": 0.82}
    score, reasons = score_song(user_prefs, song)
    assert score > 3.0

def test_empty_mood():
    profile = parse_mood_with_claude("")
    assert "genre" in profile
    assert "mood" in profile
    assert "energy" in profile