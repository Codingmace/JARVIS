import requests

def summarize(url, rapidApiKey):
    baseUrl = "https://summarization3.p.rapidapi.com/summary/v1/"

    querystring = {"url":url}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "summarization3.p.rapidapi.com"
        }

    response = requests.request("GET", baseUrl, headers=headers, params=querystring)
    return response.text
