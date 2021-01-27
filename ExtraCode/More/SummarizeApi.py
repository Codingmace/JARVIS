import requests

url = "https://summarization3.p.rapidapi.com/summary/v1/"

querystring = {"url":"https://jproco.medium.com/the-four-people-who-will-tell-you-how-to-build-a-successful-product-237d4185cfe"}

headers = {
    'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
    'x-rapidapi-host': "summarization3.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
