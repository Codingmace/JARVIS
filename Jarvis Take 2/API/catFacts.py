import requests

def catFact(rapidApiKey):
    url = "https://brianiswu-cat-facts-v1.p.rapidapi.com/facts"

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "brianiswu-cat-facts-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    return response
