""" COST MONEY"""
import requests

def categoryPrediction(text, rapidApiKey):
    url = "https://category-prediction-for-news-articles-amp-blogs.p.rapidapi.com/predict/v1"

    querystring = {"text": text }

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "category-prediction-for-news-articles-amp-blogs.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text
