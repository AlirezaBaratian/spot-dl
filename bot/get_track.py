import requests
from typing import Dict
import os

access_token: str = os.environ.get("SPOTIFY_ACCESS_TOKEN")

def get_info(str: id) -> None:
    url: str = f"https://api.spotify.com/v1/tracks/{id}"
    headers: Dict = {
        "Authorization": f"Bearer kos{access_token}"
    }

    r = requests.get(url=url, headers=headers)

    print(f"HTTP {r.status_code} {r.text}")

def get_id(url: str) -> str:
    url_list: list = url.split("://")[1].split("/")
    id: str = url_list[2].split("?")[0]
    return id

url = "https://open.spotify.com/track/1ko2lVN0vKGUl9zrU0qSlT?si=c63a572d06724c5d"
id = get_id(url)
get_info(id)