import requests

def auth(client_id, client_secret):
    url = "https://accounts.spotify.com/api/token"
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }
    r = requests.post(url, data=data)
    print(f"HTTP {r.status_code} {r.text}")
    return r.json()["access_token"]

def test():
    url = "https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb"

    r= requests.get(url, headers=headers)
    print(f"HTTP {r.status_code} {r.text}")

def get_album(id):
    url = f"https://api.spotify.com/v1/albums/{id}"

    r = requests.get(url, headers=headers)
    print(f"HTTP {r.status_code} {r.text}")

def search(term, type):
    url = f"https://api.spotify.com/v1/search?q={term}&type={type}"
    
    r = requests.get(url, headers=headers)

    print(f"HTTP {r.status_code} {r.text}")

def top(type):
    url = f"https://api.spotify.com/v1/me/top/{type}"
    r = requests.get(url, headers=headers)
    print(f"HTTP {r.status_code} {r.text}")

client_id = "929351d861394e70b4c2dd1e9cd524cb"
client_secret = "98ac1d6f78414a95af0ace7636575460"

# auth(client_id, client_secret)
access_token = "BQBHErXr70QlANfy2uNHZ9s2I648S6ngRoGFdbzOYoiA4VAccVeaixqQMwJU7gasLCKrheSNnRjROnwfxkKShP1j6q7mCgrCK3sFMaJw_JGEbfNGMJ4"
headers = {"Authorization": f"Bearer {access_token}"}
# test()
# get_album("5XNU2QTDaLGS6Gc6ihiaXD")
# search("Shayea", "artist")
top("artists")