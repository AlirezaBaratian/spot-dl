#!/usr/bin/env python

import requests, os
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

client_id: str = os.environ.get("SPOTIFY_CLIENT_ID")
client_secret: str = os.environ.get("SPOTIFY_CLIENT_SECRET")

def auth(client_id, client_secret):
    url = "https://accounts.spotify.com/api/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }

    r = requests.post(url, headers=headers, data=data)

    if r.status_code == 200:
        return r.json()["access_token"]
    else:
        print(f"HTTP {r.status_code} {r.text}")

access_token = auth(client_id, client_secret)
print(access_token)