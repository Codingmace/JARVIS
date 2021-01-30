import requests

def detectThreat(ipAddress, rapidApiKey):
#    ipAddress = "45.16.197.205"
    url = "https://ip-geolocation-and-threat-detection.p.rapidapi.com/" + ipAddress

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "ip-geolocation-and-threat-detection.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    return response.text



