import requests
from variables import rapidApiKey

def openProxy():
    url = "https://open-proxies.p.rapidapi.com/daily"

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "open-proxies.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    return response
