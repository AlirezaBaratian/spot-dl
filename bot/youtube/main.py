import requests
api_key = "AIzaSyAvlvxQ7YfqxZYww4Wkbi7gXEhYdODx3Ls"
url = "https://www.googleapis.com/youtube/v3/videos"
id = "9fvETktnaRw"
params = {
    "key": api_key,
    "id": id,
    "part": "statistics"
}

r = requests.get(url, params=params)

print(f"HTTP {r.status_code} {r.text}")