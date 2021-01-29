import requests

public_IP = requests.get("https://www.wikipedia.org").headers["X-Client-IP"]
print(public_IP)
