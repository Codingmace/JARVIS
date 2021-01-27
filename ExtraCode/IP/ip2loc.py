import requests

def ip2location(ipAddress):
    url = "https://ip2location-ip2location-v1.p.rapidapi.com/"

    apiKey = "demo"
    querystring = {"ip":ipAddress,"key":apiKey,"package":"WS9"}

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
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



