import requests
from variables import rapidApiKey

class URLThreatDetect():
    def __init__(self):
        self.ipAddress = "45.16.197.205" # Test IP
        
    def detectThreat(self):
        url = "https://ip-geolocation-and-threat-detection.p.rapidapi.com/" + self.ipAddress

        headers = {
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "ip-geolocation-and-threat-detection.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers)
        return response



