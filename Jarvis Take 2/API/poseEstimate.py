import requests

def image(base64ImageData, rapidApiKey):

    url = "https://bform-pose-estimation.p.rapidapi.com/image"

    payload = "{\r\n    \"imageBase64\": "+base64ImageData + "}"
    headers = {
        'content-type': "application/json",
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "bform-pose-estimation.p.rapidapi.com"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text

def video(rapidApiKey):

    url = "https://bform-pose-estimation.p.rapidapi.com/video"

    payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"video\"\r\n\r\n\r\n-----011000010111000001101001--\r\n\r\n"
    headers = {
        'content-type': "multipart/form-data; boundary=---011000010111000001101001",
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "bform-pose-estimation.p.rapidapi.com"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text
