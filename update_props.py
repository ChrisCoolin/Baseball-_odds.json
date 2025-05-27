import requests
import json
from datetime import datetime

# ✅ Replace with your preferred API
API_URL = "https://raw.githubusercontent.com/bigfreechip/MLB-Player-Prop-Data/main/todays_props.json"

def fetch_props():
    response = requests.get(API_URL)
    response.raise_for_status()
    data = response.json()

    props = []
    for item in data:
        props.append({
            "player": item.get("player", "Unknown"),
            "team": item.get("team", "UNK"),
            "prop": item.get("type", "N/A"),
            "predicted_odds": item.get("best_odds", "+100"),
            "book": item.get("book", "Unknown"),
            "game_time": item.get("start_time", datetime.utcnow().isoformat())
        })

    return props

def save_props(props, filename="props.json"):
    with open(filename, "w") as f:
        json.dump(props, f, indent=2)

if __name__ == "__main__":
    props = fetch_props()
    save_props(props)
    print(f"✅ Saved {len(props)} props to props.json")