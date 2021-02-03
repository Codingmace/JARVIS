import requests
from variables import rapidApiKey

class VerifyPhoneNumber():
    def __init__(self):
        self.number = number
        self.country = "US"
        
    def verifyPhone(number, rapidApiKey):
        url = "https://veriphone.p.rapidapi.com/verify"

        querystring = {"phone": self.number,"default_country":self.country}

        headers = {
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "veriphone.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        return response
