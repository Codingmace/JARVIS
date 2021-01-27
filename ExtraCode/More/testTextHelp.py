import requests


def fetchText():
    url = "https://test1972.p.rapidapi.com/analyze-text/text"

    querystring = {"url":"https://en.wikipedia.org/wiki/Hendrik_Spilman"}

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "test1972.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

def pos():
    url = "https://test1972.p.rapidapi.com/analyze-text/pos"

    querystring = {"url":"https://en.wikipedia.org/wiki/Hendrik_Spilman"}

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "test1972.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


def namedEntity():
    url = "https://test1972.p.rapidapi.com/analyze-text/ner"

    querystring = {"url":"https://en.wikipedia.org/wiki/Hendrik_Spilman"}

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "test1972.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

