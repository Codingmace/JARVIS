""" COST MONEY"""
import requests

def categoryPrediction(text):
    url = "https://category-prediction-for-news-articles-amp-blogs.p.rapidapi.com/predict/v1"

    querystring = {"text": text }

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "category-prediction-for-news-articles-amp-blogs.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
