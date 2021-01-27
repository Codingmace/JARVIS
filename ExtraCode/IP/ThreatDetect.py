import requests

ipAddress = "45.16.197.205"
url = "https://ip-geolocation-and-threat-detection.p.rapidapi.com/" + ipAddress

headers = {
    'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
    'x-rapidapi-host': "ip-geolocation-and-threat-detection.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

## Add the JSON Parsing Here

print(response.text)




