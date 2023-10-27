import requests

access_token: str = "BQCi4MGJyaDPHxDMuF594ybarGE-8Oo6aGePc8p6JuvaqFSHFM6WAaXaJi3yNbL1tTFRtfmuZNo4KZlVksyj8o_Lg9ewUlMfG6lY7UBn5ALaJkw-30o"

def get_info() -> None:
    url: str = "https://api.spotify.com/v1/tracks/7aUuoq4oMfLxaLa5GVUDHi"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    r = requests.get(url=url, headers=headers)

    print(f"HTTP {r.status_code} {r.json()["album"]["release_date"]}")

get_info()