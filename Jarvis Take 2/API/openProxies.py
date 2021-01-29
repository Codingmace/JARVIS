import requests

def openProxy(rapidApiKey):
    url = "https://open-proxies.p.rapidapi.com/proxies"

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "open-proxies.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    return response.text
