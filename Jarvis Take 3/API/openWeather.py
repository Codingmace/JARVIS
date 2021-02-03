import requests
from variables import rapidApiKey

def currentWeather():
    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    querystring = {"q":"London,uk","lat":"0","lon":"0","callback":"test","id":"2172797","lang":"en","units":"\"metric\" or \"imperial\"","mode":"JSON"}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response

def forecast():
    url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"

    querystring = {"q":"san francisco,us","lat":"35","lon":"139","cnt":"10","units":"metric or imperial","mode":"JSON","lang":"en"}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response


def searchWeatherData():
    url = "https://community-open-weather-map.p.rapidapi.com/find"

    querystring = {"q":"london","cnt":"1","mode":"JSON","lon":"0","type":"link, accurate","lat":"0","units":"imperial, metric"}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response

def historicalWeather(rapidApiKey):
    url = "https://community-open-weather-map.p.rapidapi.com/onecall/timemachine"

    querystring = {"lat":"37.774929","lon":"-122.419418","dt":"1590094153 "}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text


def climateForecast30(city):
    url = "https://community-open-weather-map.p.rapidapi.com/climate/month"

    querystring = {"q": city}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response


def forecast5d3h():
    url = "https://community-open-weather-map.p.rapidapi.com/forecast"

    querystring = {"q":"san francisco,us","lat":"0","lon":"0","lang":"en","cnt":"10","zip":"75035"}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response


