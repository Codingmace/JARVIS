import requests
from variables import rapidApiKey

def ip2location(ipAddress,apiKey):
    url = "https://ip2location-ip2location-v1.p.rapidapi.com/"

    apiKey = "demo"
    querystring = {"ip": ipAddress,"key": apiKey,"package": "WS9"}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "ip2location-ip2location-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    dataResponse = response.json()

    neededData = ['region_name','city_name','latitude','longitude','zip_code']
    importantData = []

    for data in neededData:
        importantData.append(dataResponse[data])

    print(neededData)
    print(importantData)
    return response

    """
    {
    "country_code":"US"
    "country_name":"United States of America"
    "region_name":"Texas"
    "city_name":"Richardson"
    "latitude":"32.94818"
    "longitude":"-96.72972"
    "zip_code":"75080"
    "time_zone":"-06:00"
    "credits_consumed":5
    }
    """



