import requests
from variables import rapidApiKey

class UrbanDictionary():
    def __init__(self):
        self.word = word
        
    def defineWord(self):
        url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

        querystring = {"term" : self.word}

        headers = {
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        return response
