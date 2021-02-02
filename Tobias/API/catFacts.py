import requests
from variables import rapidApiKey

class CatFacts():
    def __init__(self):
        self.key = rapidApiKey
        
    def catFact(self):
        url = "https://brianiswu-cat-facts-v1.p.rapidapi.com/facts"

        headers = {
            'x-rapidapi-key': key,
            'x-rapidapi-host': "brianiswu-cat-facts-v1.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers)

        return response
