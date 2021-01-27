import requests

url = "https://veriphone.p.rapidapi.com/verify"

querystring = {"phone":"+4915123577723","default_country":"US"}

headers = {
    'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
    'x-rapidapi-host': "veriphone.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
