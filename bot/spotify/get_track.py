import requests

access_token: str = "BQBtg6O9hTifZ396SHepfTbbkgA1wFFkR35YFrZ8PJKyVgSo44OIGEoXh0vuOS8VZTWCGGebTlIoWPPQmIpzUbovJyXWPZAzTvEAx5jci9U7nt6UbQ8"

def get_info() -> None:
    url: str = "https://api.spotify.com/v1/tracks/7aUuoq4oMfLxaLa5GVUDHi"
    headers: Dict = {
        "Authorization": f"Bearer {access_token}"
    }

    r = requests.get(url=url, headers=headers)

    print(f"HTTP {r.status_code} {r.text}")

get_info()