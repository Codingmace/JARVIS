import requests

def catFact(rapidApiKey):
    url = "https://brianiswu-cat-facts-v1.p.rapidapi.com/facts"

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "brianiswu-cat-facts-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    print("Take in the response and return only one random fact. Store all of them to a file")
    return response.text
