import requests

def fetchText(url):
    baseUrl = "https://test1972.p.rapidapi.com/analyze-text/text"

    querystring = {"url":url}

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "test1972.p.rapidapi.com"
        }

    response = requests.request("GET", baseUrl, headers=headers, params=querystring)

    print(response.text)

def pos(url):
    baseUrl = "https://test1972.p.rapidapi.com/analyze-text/pos"

    querystring = {"url":url}

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "test1972.p.rapidapi.com"
        }

    response = requests.request("GET", baseUrl, headers=headers, params=querystring)

    print(response.text)


def namedEntity(url):
    baseUrl = "https://test1972.p.rapidapi.com/analyze-text/ner"

    querystring = {"url":url}

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "test1972.p.rapidapi.com"
        }

    response = requests.request("GET", baseUrl, headers=headers, params=querystring)

    print(response.text)

