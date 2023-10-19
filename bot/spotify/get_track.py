import requests
from typing import Dict

access_token: str = "BQBl8FplsABUQRYYUFS8XlC_r-YNKPMp7nB-V3-ugmI4BSmGG6AXa12h_u_IunhKTz3S9EP3BfqoY6BrgRUWT7Kc4tpKROmrRKBo_IEHZ4te0nu-miQ"

def get_info(str: id):
    url: str = f"https://api.spotify.com/v1/tracks/{id}"
    headers: Dict = {
        "Authorization": f"Bearer {access_token}"
    }

    r = requests.get(url=url, headers=headers)

    print(f'HTTP {r.status_code} {r.text}')

def get_id(url: str) -> str:
    url_list: list = url.split("://")[1].split("/")
    type: str = url_list[1]
    id: str = url_list[2]
    return id

url = "https://open.spotify.com/track/1ko2lVN0vKGUl9zrU0qSlT?si=c63a572d06724c5d"
id = get_id(url)
get_info(id)