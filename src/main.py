import requests

resp = requests.get("https://google.com")

print(resp.content)
