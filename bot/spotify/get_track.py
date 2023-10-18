import requests
from typing import Dict

access_token: str = "BQAAqDtFygSNs9ISCtm1g55Bd2c8cWFlBDGuNjD_v8dyqcXgFm5q1eYItt0ZE0zU3lpdqEpqGfZU5-U6e81zy8bT1dx6CepB4hRVRZXA1rNj0RxHfbo"

def get_info():
    id: str = "11dFghVXANMlKmJXsNCbNl"
    url: str = f"https://api.spotify.com/v1/tracks/{id}"
    headers: Dict = {
        "Authorization": f"Bearer {access_token}"
    }

    r = requests.get(url=url, headers=headers)

    print(f'HTTP {r.status_code} {r.text}')

get_info()