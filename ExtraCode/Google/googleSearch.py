import requests


def search():
    url = "https://google-search3.p.rapidapi.com/api/v1/search/q=elon+musk&num=100"

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "google-search3.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    print(response.text)

def images():
    url = "https://google-search3.p.rapidapi.com/api/v1/images/q=tesla"

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "google-search3.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    print(response.text)

def crawl():
    url = "https://google-search3.p.rapidapi.com/api/v1/crawl/q=best+iphone&num=100"

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "google-search3.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    print(response.text)

def news():
    url = "https://google-search3.p.rapidapi.com/api/v1/news/q=president+united+states"

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "google-search3.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    print(response.text)
    


def SERP():
    # THIs is a post request and very tricky

    url = "https://google-search3.p.rapidapi.com/api/v1/serp/"

    payload = "{\r\n    \"query\": \"q=google+search+api&num=100\",\r\n    \"website\": \"https://rapidapi.com\"\r\n}"
    headers = {
        'content-type': "application/json",
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "google-search3.p.rapidapi.com"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)


