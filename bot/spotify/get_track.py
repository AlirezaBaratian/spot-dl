import requests

access_token: str = "BQD5dND7YK0EvtkuLwucnNlaKwfhZgMlXJGNGsTynG5KqqzoGmkZgoSCHMJ1-I00I9Y0-ENLqFfJLtEnxiR9QN2PWueI3sVkiklTcWPhFjj99sf-PiY"

def get_info() -> None:
    url: str = "https://api.spotify.com/v1/tracks/7aUuoq4oMfLxaLa5GVUDHi"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    r = requests.get(url=url, headers=headers)

    print(f"HTTP {r.status_code} {r.text}")

get_info()