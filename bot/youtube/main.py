import requests
api_key = "AIzaSyAvlvxQ7YfqxZYww4Wkbi7gXEhYdODx3Ls"
url = "https://www.googleapis.com/youtube/v3/search"
id = "9fvETktnaRw"
params = {
    'key': api_key,
    'part': 'snippet',
    'q': ' Rick Astley Never Gonna Give You Up',
    'maxResults': 5
}

r = requests.get(url, params=params)

print(f"HTTP {r.status_code} {r.text}")