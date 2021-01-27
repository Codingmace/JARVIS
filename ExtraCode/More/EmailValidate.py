#UNPOPULAR
import requests

url = "https://email-address-validation.p.rapidapi.com/validate"

querystring = {"address":"email@example.com"}

headers = {
    'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
    'x-rapidapi-host': "email-address-validation.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
