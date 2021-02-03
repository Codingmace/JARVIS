import requests
from variables import rapidApiKey

class SummarizeURL():
    def __init__(self):
        self.url = url
        
    def summarize(self):
        baseUrl = "https://summarization3.p.rapidapi.com/summary/v1/"

        querystring = {"url": self.url}

        headers = {
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "summarization3.p.rapidapi.com"
            }

        response = requests.request("GET", baseUrl, headers=headers, params=querystring)
        return response

