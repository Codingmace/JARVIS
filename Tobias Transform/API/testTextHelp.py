import requests
from variables import rapidApiKey

class TestText():
    def __init__(self):
        self.url = url
        
    def fetchText(self):
        baseUrl = "https://test1972.p.rapidapi.com/analyze-text/text"

        querystring = {"url": self.url}

        headers = {
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "test1972.p.rapidapi.com"
            }

        response = requests.request("GET", baseUrl, headers=headers, params=querystring)
        return response

    def pos(self):
        baseUrl = "https://test1972.p.rapidapi.com/analyze-text/pos"

        querystring = {"url": self.url}

        headers = {
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "test1972.p.rapidapi.com"
            }

        response = requests.request("GET", baseUrl, headers=headers, params=querystring)
        return response


    def namedEntity(self):
        baseUrl = "https://test1972.p.rapidapi.com/analyze-text/ner"

        querystring = {"url": self.url}

        headers = {
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "test1972.p.rapidapi.com"
            }

        response = requests.request("GET", baseUrl, headers=headers, params=querystring)
        return response

