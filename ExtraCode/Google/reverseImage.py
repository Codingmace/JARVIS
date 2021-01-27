import requests

url = "https://google-reverse-image-search.p.rapidapi.com/imgSearch"

querystring = {"url":"http://codzz.com/mashape/sample.png"}

headers = {
    'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
    'x-rapidapi-host': "google-reverse-image-search.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
