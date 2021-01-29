import requests

def reverseImage(url, rapidApiKey):
    baseUrl = "https://google-reverse-image-search.p.rapidapi.com/imgSearch"

    querystring = {"url":url}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "google-reverse-image-search.p.rapidapi.com"
        }

    response = requests.request("GET", baseUrl, headers=headers, params=querystring)

    print(response.text)
