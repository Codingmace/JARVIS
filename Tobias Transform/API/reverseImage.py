import requests
from variables import rapidApiKey

class ReverseImageSearch():
    def __init__(self):
        self.url = url
            
    def reverseImage(self):
        baseUrl = "https://google-reverse-image-search.p.rapidapi.com/imgSearch"

        querystring = {"url":self.url}

        headers = {
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "google-reverse-image-search.p.rapidapi.com"
            }

        response = requests.request("GET", baseUrl, headers=headers, params=querystring)
        return response
