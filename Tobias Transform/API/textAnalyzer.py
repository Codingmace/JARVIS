import requests
from variables import rapidApiKey

class AnalyzeText():
    def __init__(self):
        self.url = url
        
    def contentExtract(self):
        baseUrl = "https://text-analyzer.p.rapidapi.com/analyze-text/text"

        querystring = {"url": self.url}

        headers = {
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "text-analyzer.p.rapidapi.com"
            }

        response = requests.request("GET", baseUrl, headers=headers, params=querystring)
        return response


    def namedExtract(self):
        baseUrl = "https://text-analyzer.p.rapidapi.com/analyze-text/ner"

        querystring = {"url": self.url}

        headers = {
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "text-analyzer.p.rapidapi.com"
            }

        response = requests.request("GET", baseUrl, headers=headers, params=querystring)
        return response


    def partOfSpeech(self):
        baseUrl = "https://text-analyzer.p.rapidapi.com/analyze-text/pos"

        querystring = {"url": self.url}

        headers = {
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "text-analyzer.p.rapidapi.com"
            }

        response = requests.request("GET", baseUrl, headers=headers, params=querystring)
        return response

    
