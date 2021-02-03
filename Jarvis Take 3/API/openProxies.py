import requests

def openProxy(rapidApiKey):
    url = "https://open-proxies.p.rapidapi.com/daily"

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "open-proxies.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    return response.text
