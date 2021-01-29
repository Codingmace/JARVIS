import requests

def currentWeather():
    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    querystring = {"q":"London,uk","lat":"0","lon":"0","callback":"test","id":"2172797","lang":"en","units":"\"metric\" or \"imperial\"","mode":"JSON"}

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

def forecast():
    url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"

    querystring = {"q":"san francisco,us","lat":"35","lon":"139","cnt":"10","units":"metric or imperial","mode":"JSON","lang":"en"}

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


def searchWeatherData():
    url = "https://community-open-weather-map.p.rapidapi.com/find"

    querystring = {"q":"london","cnt":"1","mode":"JSOM","lon":"0","type":"link, accurate","lat":"0","units":"imperial, metric"}

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

def historicalWeather():
    url = "https://community-open-weather-map.p.rapidapi.com/onecall/timemachine"

    querystring = {"lat":"37.774929","lon":"-122.419418","dt":"1590094153 "}

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


def climateForecast30():
    url = "https://community-open-weather-map.p.rapidapi.com/climate/month"

    querystring = {"q":"San Francisco"}

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


def forecast5d3h():
    url = "https://community-open-weather-map.p.rapidapi.com/forecast"

    querystring = {"q":"san francisco,us","lat":"0","lon":"0","lang":"en","cnt":"10","zip":"75035"}

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


Need stuff here
