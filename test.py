import requests
import json
genshin = requests.get(f"https://gsi.fly.dev/characters/search?name=Ganyu")
genshin = genshin.json()
genshin = genshin['results'][0]["id"]
print(genshin)