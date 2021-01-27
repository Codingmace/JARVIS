import requests

termSearch = "programming"
url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

querystring = {"term":termSearch}

headers = {
    'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
