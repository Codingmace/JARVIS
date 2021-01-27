import requests

url = "https://ip-location5.p.rapidapi.com/get_geo_info"
## Can also do IPv6

payload = "ip=146.160.63.10"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
    'x-rapidapi-host': "ip-location5.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
