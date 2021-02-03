import requests
from variables import rapidApiKey

class URLIntel():
    def __init__(self):
        self.targetUrl = targetUrl
        
def urlIntel(rapidApiKey):
    url = "https://url-intelligence.p.rapidapi.com/rip"

    querystring = {"target":self.targetUrl}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "url-intelligence.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response
