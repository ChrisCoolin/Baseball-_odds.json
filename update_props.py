import requests
import json

# Example endpoint: replace with your actual odds API or data source
API_URL = "https://api.example.com/mlb/player-props/fanduel"

def fetch_props():
    response = requests.get(API_URL)
    response.raise_for_status()
    data = response.json()

    # Transform data to desired structure (example)
    props = []
    for item in data['props']:
        prop = {
            "player": item['playerName'],
            "team": item['teamAbbreviation'],
            "prop": item['marketName'],
            "predicted_odds": item['odds'],
            "book": "FanDuel",
            "game_time": item['startTime']
        }
        props.append(prop)

    return props

def save_props(props, filename="props.json"):
    with open(filename, "w") as f:
        json.dump(props, f, indent=2)

if __name__ == "__main__":
    props = fetch_props()
    save_props(props)
    print(f"Saved {len(props)} props to props.json")