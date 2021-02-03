import requests

def fetchText(url,rapidApiKey):
    baseUrl = "https://test1972.p.rapidapi.com/analyze-text/text"

    querystring = {"url":url}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "test1972.p.rapidapi.com"
        }

    response = requests.request("GET", baseUrl, headers=headers, params=querystring)
    return response.text

def pos(url, rapidApiKey):
    baseUrl = "https://test1972.p.rapidapi.com/analyze-text/pos"

    querystring = {"url":url}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "test1972.p.rapidapi.com"
        }

    response = requests.request("GET", baseUrl, headers=headers, params=querystring)
    return response.text


def namedEntity(url, rapidApiKey):
    baseUrl = "https://test1972.p.rapidapi.com/analyze-text/ner"

    querystring = {"url":url}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "test1972.p.rapidapi.com"
        }

    response = requests.request("GET", baseUrl, headers=headers, params=querystring)
    return response.text

