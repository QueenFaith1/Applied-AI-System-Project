"""
Applied AI Music Recommender
Extends the Music Recommender Simulation with Claude AI natural language processing.
"""

from src.recommender import load_songs, recommend_songs
from src.ai_profile import parse_mood_with_claude
from tabulate import tabulate
import logging

logging.basicConfig(filename='recommender.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

def run_profile(profile_name, user_prefs, songs):
    logging.info(f"Running profile: {profile_name} with prefs: {user_prefs}")
    print(f"\n{'='*60}")
    print(f"🎧 Profile: {profile_name}")
    print(f"{'='*60}")
    
    try:
        recommendations = recommend_songs(user_prefs, songs, k=5)
        table_data = []
        for i, rec in enumerate(recommendations, 1):
            song, score, explanation = rec
            table_data.append([
                f"#{i}",
                song['title'],
                song['artist'],
                f"{score:.2f}/4.00",
                explanation
            ])
        headers = ["Rank", "Title", "Artist", "Score", "Why"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
        logging.info(f"Successfully generated {len(recommendations)} recommendations")
    except Exception as e:
        print(f"⚠️ Error generating recommendations: {e}")
        logging.error(f"Error: {e}")

def main() -> None:
    try:
        songs = load_songs("data/songs.csv")
        print(f"Loaded songs: {len(songs)}")
        logging.info(f"Loaded {len(songs)} songs")
    except FileNotFoundError:
        print("❌ Error: songs.csv not found!")
        logging.error("songs.csv not found")
        return

    print("\n🤖 Using Claude AI to interpret mood descriptions...\n")
    
    mood1 = "I just got a promotion and want to celebrate with upbeat happy music!"
    mood2 = "I need to focus and study, something calm and relaxing"
    mood3 = "I am feeling nostalgic and want something emotional and deep"

    profile1 = parse_mood_with_claude(mood1)
    profile2 = parse_mood_with_claude(mood2)
    profile3 = parse_mood_with_claude(mood3)

    run_profile(f"Celebration: {mood1[:30]}...", profile1, songs)
    run_profile(f"Study: {mood2[:30]}...", profile2, songs)
    run_profile(f"Nostalgic: {mood3[:30]}...", profile3, songs)

if __name__ == "__main__":
    main()