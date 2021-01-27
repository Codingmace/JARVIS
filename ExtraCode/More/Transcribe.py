import requests


def transcribeUrl():
    url = "https://transcribe.p.rapidapi.com/api/v1/transcribe_url/"

    payload = "{\r\n    \"url\": \"https://data.cache.id/tests/test_1.wav\"\r\n}"
    headers = {
        'content-type': "application/json",
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "transcribe.p.rapidapi.com"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)


def getTask():
    url = "https://transcribe.p.rapidapi.com/api/v1/tasks/ec230e59-186c-4527-9be1-3e9af0c70191"

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "transcribe.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    print(response.text)

def serviceStatus():
    url = "https://transcribe.p.rapidapi.com/api/v1/"

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "transcribe.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    print(response.text)


def getTasks():
    url = "https://transcribe.p.rapidapi.com/api/v1/tasks/"

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "transcribe.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    print(response.text)

def transcribe():
    url = "https://transcribe.p.rapidapi.com/api/v1/transcribe/"

    payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"\r\n\r\n\r\n-----011000010111000001101001--\r\n\r\n"
    headers = {
        'content-type': "multipart/form-data; boundary=---011000010111000001101001",
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "transcribe.p.rapidapi.com"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

        
