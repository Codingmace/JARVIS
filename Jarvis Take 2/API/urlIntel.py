import requests

def urlIntel(targetUrl):
    url = "https://url-intelligence.p.rapidapi.com/rip"

    querystring = {"target":targetUrl}

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "url-intelligence.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
