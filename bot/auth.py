#!/usr/bin/env python

import requests, os
from dotenv import load_dotenv

load_dotenv()

def auth() -> str:
    client_id: str = os.environ.get("SPOTIFY_CLIENT_ID")
    client_secret: str = os.environ.get("SPOTIFY_CLIENT_SECRET")
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
        
def refresh_token(acees_token: str) -> None:
    env_path: str = ".env"
    with open(env_path, 'r') as env_file:
        lines = env_file.readlines()
    if (lines):
        for i, line in enumerate(lines):
            if line.startswith("SPOTIFY_ACCESS_TOKEN"):
                lines[i] = f"""SPOTIFY_ACCESS_TOKEN="{access_token}"\n"""
                break
    with open(env_path, 'w') as env_file:
        env_file.writelines(lines)

access_token = auth()