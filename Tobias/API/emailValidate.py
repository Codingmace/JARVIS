import requests
from variables import rapidApiKey

class ValidateEmail():
    def __init__(self):
        self.email = "masnathan@mail.com"
        
    def validEmail(self):
        url = "https://email-validator8.p.rapidapi.com/api/v2.0/email"

        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "email-validator8.p.rapidapi.com"
            }

        response = requests.request("POST", url, data=self.email, headers=headers)
        return response
