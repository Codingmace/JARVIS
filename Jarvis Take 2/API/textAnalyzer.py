import requests

def contentExtract(url):
    baseUrl = "https://text-analyzer.p.rapidapi.com/analyze-text/text"

    querystring = {"url":url}

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "text-analyzer.p.rapidapi.com"
        }

    response = requests.request("GET", baseUrl, headers=headers, params=querystring)

    print(response.text)


def namedExtract(url):
    baseUrl = "https://text-analyzer.p.rapidapi.com/analyze-text/ner"

    querystring = {"url":url}

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "text-analyzer.p.rapidapi.com"
        }

    response = requests.request("GET", baseUrl, headers=headers, params=querystring)

    print(response.text)


def partOfSpeech(url):
    baseUrl = "https://text-analyzer.p.rapidapi.com/analyze-text/pos"

    querystring = {"url":url}

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "text-analyzer.p.rapidapi.com"
        }

    response = requests.request("GET", baseUrl, headers=headers, params=querystring)

    print(response.text)

    
