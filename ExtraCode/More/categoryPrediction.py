""" COST MONEY"""

import requests

url = "https://category-prediction-for-news-articles-amp-blogs.p.rapidapi.com/predict/v1"

querystring = {"text":"While collecting the stories of more than 50 startups that got big before they raised venture capital, it was surprising to learn how many founders claimed to get their business off the ground with just $5,000-$10,000. In a world where companies that have raised more than $5M describe themselves as “seed stage,” a four-figure sum seems insufficient to start a billion-dollar business. But it’s not. So, how do you become humongous with humble financing? There are a few principles that seem common:"}

headers = {
    'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
    'x-rapidapi-host': "category-prediction-for-news-articles-amp-blogs.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
