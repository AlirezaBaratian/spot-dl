import requests

access_token = "BQAt7feu-cYR16DbHUl8sIvu7-2DU76kuTzLmr4-DulVCNo0jdMgVpc5CmBBQBnKmyFhC_8W5y7sEh2AeyA0TnLF5AsJ122ync3nMeAyQlIKTIJrnZE"
url = "https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb"
headers = {"Authorization": f"Bearer {access_token}"}

res = requests.get(url, headers=headers)
print(f"HTTP {res.status_code} {res.text}")