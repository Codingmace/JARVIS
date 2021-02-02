import requests
from variables import rapidApiKey

class PlateRecognition():
    def __init__(self):
        self.imageUrl = imageUrl
        self.payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"image\"\r\n\r\n\r\n-----011000010111000001101001--\r\n\r\n"
        
    def recognizeByUrl(self):
        url = "https://number-plate-recognition.p.rapidapi.com/recognition"

        payload = "image_url=" + self.imageUrl
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "number-plate-recognition.p.rapidapi.com"
            }

        response = requests.request("POST", url, data=payload, headers=headers)
        return response

    # Binary Image? Maybe?
    def recognizeByImage(self):
    # Binary Imagex
        url = "https://number-plate-recognition.p.rapidapi.com/recognition"

        payload = self.payload
        headers = {
            'content-type': "multipart/form-data; boundary=---011000010111000001101001",
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "number-plate-recognition.p.rapidapi.com"
            }

        response = requests.request("POST", url, data=payload, headers=headers)
        return response

