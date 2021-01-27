import requests

url = "https://ocrly-image-to-text.p.rapidapi.com/"

querystring = {"imageurl":"https://i.pinimg.com/originals/42/1b/e6/421be6184e75937bb223c764ecbc2f2e.jpg","filename":"sample.jpg"}

headers = {
    'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
    'x-rapidapi-host': "ocrly-image-to-text.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
