import requests
from variables import rapidApiKey

class OCRLY():
    def __init__(self):
        self.imageUrl = imageUrl
        self.filename = filename
        
    def OImage2Text(self):
        url = "https://ocrly-image-to-text.p.rapidapi.com/"

        querystring = {"imageurl": self.imageUrl ,"filename": self.filename}

        headers = {
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "ocrly-image-to-text.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        return response
