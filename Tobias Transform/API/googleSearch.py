import requests
from variables import rapidApiKey

class GoogleSearch():
    def __init__(self):
        self.term = term
        self.number = number
        self.payload = payload
        
        
    def search(self):
        url = "https://google-search3.p.rapidapi.com/api/v1/search/q=" + self.term + "&num="+ self.number
        headers = {
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "google-search3.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers)
        return response


    def images(self):
        url = "https://google-search3.p.rapidapi.com/api/v1/images/q=" + self.term
        headers = {
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "google-search3.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers)
        return response
        

    def crawl(self):
        url = "https://google-search3.p.rapidapi.com/api/v1/crawl/q=" + self.term + "&num=" + self.number
        headers = {
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "google-search3.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers)
        return response


    def news(self):
        url = "https://google-search3.p.rapidapi.com/api/v1/news/q=" + self.term
        headers = {
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "google-search3.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers)
        return response
        


    def SERP(self):
        # THIs is a post request and very tricky

        url = "https://google-search3.p.rapidapi.com/api/v1/serp/"

        payload = "{\r\n    \"query\": \"q=google+search+api&num=100\",\r\n    \"website\": \"https://rapidapi.com\"\r\n}"
        headers = {
            'content-type': "application/json",
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "google-search3.p.rapidapi.com"
            }

        response = requests.request("POST", url, data=self.payload, headers=headers)
        print(response.text)


