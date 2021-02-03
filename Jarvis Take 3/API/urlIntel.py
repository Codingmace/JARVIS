import requests

def urlIntel(targetUrl, rapidApiKey):
    url = "https://url-intelligence.p.rapidapi.com/rip"

    querystring = {"target":targetUrl}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "url-intelligence.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text
