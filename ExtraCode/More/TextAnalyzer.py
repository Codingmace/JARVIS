import requests

def contentExtract():
    url = "https://text-analyzer.p.rapidapi.com/analyze-text/text"

    querystring = {"url":"https://en.wikipedia.org/wiki/Narendra_Modi"}

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "text-analyzer.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


def namedExtract():
    url = "https://text-analyzer.p.rapidapi.com/analyze-text/ner"

    querystring = {"url":"https://en.wikipedia.org/wiki/Narendra_Modi"}

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "text-analyzer.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


def partOfSpeech():
    url = "https://text-analyzer.p.rapidapi.com/analyze-text/pos"

    querystring = {"url":"https://en.wikipedia.org/wiki/Narendra_Modi"}

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "text-analyzer.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

    
