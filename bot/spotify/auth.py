#!/usr/bin/env python

import requests

client_id = "929351d861394e70b4c2dd1e9cd524cb"
client_secret = "98ac1d6f78414a95af0ace7636575460"

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