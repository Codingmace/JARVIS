""" COST MONEY"""
import requests
from variables import rapidApiKey

class PredictCategory():
    def __init__(self):
        self.text = text
        
    def categoryPrediction(self):
        url = "https://category-prediction-for-news-articles-amp-blogs.p.rapidapi.com/predict/v1"

        querystring = {"text": self.text }

        headers = {
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "category-prediction-for-news-articles-amp-blogs.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        return response
