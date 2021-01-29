import requests

def OImage2Text(imageUrl, filename):
    url = "https://ocrly-image-to-text.p.rapidapi.com/"

    querystring = {"imageurl":imageUrl,"filename":filename}

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "ocrly-image-to-text.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
