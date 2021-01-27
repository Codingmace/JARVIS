import requests

url = "https://brianiswu-cat-facts-v1.p.rapidapi.com/facts"

headers = {
    'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
    'x-rapidapi-host': "brianiswu-cat-facts-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
