import requests

def contentExtract(url, rapidApiKey):
    baseUrl = "https://text-analyzer.p.rapidapi.com/analyze-text/text"

    querystring = {"url":url}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "text-analyzer.p.rapidapi.com"
        }

    response = requests.request("GET", baseUrl, headers=headers, params=querystring)
    return response.text


def namedExtract(url, rapidApiKey):
    baseUrl = "https://text-analyzer.p.rapidapi.com/analyze-text/ner"

    querystring = {"url":url}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "text-analyzer.p.rapidapi.com"
        }

    response = requests.request("GET", baseUrl, headers=headers, params=querystring)
    return response.text


def partOfSpeech(url,rapidApiKey):
    baseUrl = "https://text-analyzer.p.rapidapi.com/analyze-text/pos"

    querystring = {"url":url}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "text-analyzer.p.rapidapi.com"
        }

    response = requests.request("GET", baseUrl, headers=headers, params=querystring)
    return response.text

    
