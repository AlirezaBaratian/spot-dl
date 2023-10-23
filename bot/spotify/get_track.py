import requests
from typing import Dict

access_token: str = "BQBa1W6QLISQpcqmIzrduxK0Q5MTJYDmH8zZ0lW3KCc5Gw333mnHjgu9rTINZoQTJDpxrJTK-aPnlN9dke0Mk3Dag1KOq7KwMmzU0lb7EzKUJ-6zBYQ"

def get_info(str: id) -> None:
    url: str = f"https://api.spotify.com/v1/tracks/{id}"
    headers: Dict = {
        "Authorization": f"Bearer {access_token}"
    }

    r = requests.get(url=url, headers=headers)

    print(type(r.json()), r.json()["album"]["images"][0]["url"], r.json()["artists"][0]["name"], r.json()["name"])

def get_id(url: str) -> str:
    url_list: list = url.split("://")[1].split("/")
    id: str = url_list[2].split("?")[0]
    return id

url = "https://open.spotify.com/track/1ko2lVN0vKGUl9zrU0qSlT?si=c63a572d06724c5d"
id = get_id(url)
get_info(id)