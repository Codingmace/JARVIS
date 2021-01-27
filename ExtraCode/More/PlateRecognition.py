import requests


def recognizeByUrl():
    url = "https://number-plate-recognition.p.rapidapi.com/recognition"

    payload = "image_url=https%3A%2F%2Fcore-api.net%2Fimages%2Fnumber-plate.jpg"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "number-plate-recognition.p.rapidapi.com"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

def recognizeByImage():
# Binary Imagex
    url = "https://number-plate-recognition.p.rapidapi.com/recognition"

    payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"image\"\r\n\r\n\r\n-----011000010111000001101001--\r\n\r\n"
    headers = {
        'content-type': "multipart/form-data; boundary=---011000010111000001101001",
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "number-plate-recognition.p.rapidapi.com"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
