import requests


def image(base64ImageData):

    url = "https://bform-pose-estimation.p.rapidapi.com/image"

    payload = "{\r\n    \"imageBase64\": "+base64ImageData + "}"
    headers = {
        'content-type': "application/json",
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "bform-pose-estimation.p.rapidapi.com"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

def video():

    url = "https://bform-pose-estimation.p.rapidapi.com/video"

    payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"video\"\r\n\r\n\r\n-----011000010111000001101001--\r\n\r\n"
    headers = {
        'content-type': "multipart/form-data; boundary=---011000010111000001101001",
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "bform-pose-estimation.p.rapidapi.com"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
