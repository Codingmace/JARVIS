import requests

def summarize(url):
    baseUrl = "https://summarization3.p.rapidapi.com/summary/v1/"

    querystring = {"url":url}

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "summarization3.p.rapidapi.com"
        }

    response = requests.request("GET", baseUrl, headers=headers, params=querystring)

    print(response.text)
