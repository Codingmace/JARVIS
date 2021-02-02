import requests
from variables import rapidApiKey

class PoseEstimate():
    def __init__(self):
        self.image = base64ImageData
        self.videoData = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"video\"\r\n\r\n\r\n-----011000010111000001101001--\r\n\r\n"


    def image(self):
        url = "https://bform-pose-estimation.p.rapidapi.com/image"

        payload = "{\r\n    \"imageBase64\": "+ self.image + "}"
        headers = {
            'content-type': "application/json",
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "bform-pose-estimation.p.rapidapi.com"
            }

        response = requests.request("POST", url, data=payload, headers=headers)
        return response

    def video(self):
        url = "https://bform-pose-estimation.p.rapidapi.com/video"

        payload = self.videoData
        headers = {
            'content-type': "multipart/form-data; boundary=---011000010111000001101001",
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "bform-pose-estimation.p.rapidapi.com"
            }

        response = requests.request("POST", url, data=payload, headers=headers)
        return response
