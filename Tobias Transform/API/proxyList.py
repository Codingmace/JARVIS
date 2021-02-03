import requests
from variables import rapidApiKey

class ProxyList():
    def __init__(self):
        self.key = rapidApiKey

    def openProxy(self):
        url = "https://open-proxies.p.rapidapi.com/daily"
        headers = {
            'x-rapidapi-key': self.key,
            'x-rapidapi-host': "open-proxies.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers)

        return response
