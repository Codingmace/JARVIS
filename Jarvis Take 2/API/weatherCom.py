import requests

def covid19(rapidApiKey):
    url = "https://weather-com.p.rapidapi.com/v3/wx/disease/tracker/countryList/current"

    querystring = {"language":"en"}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "weather-com.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text

def forecastDaily(rapidApiKey): 
    url = "https://weather-com.p.rapidapi.com/v3/wx/forecast/daily/3day"

    querystring = {"geocode":"34.080911,-118.270406","units":"e","language":"en"}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "weather-com.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text

def forecastHourly(rapidApiKey):
    url = "https://weather-com.p.rapidapi.com/v3/wx/forecast/hourly/1day"

    querystring = {"geocode":"34.080911,-118.270406","units":"e","language":"en"}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "weather-com.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text

def historical30d(rapidApiKey):
    url = "https://weather-com.p.rapidapi.com/v3/wx/conditions/historical/dailysummary/30day"

    querystring = {"geocode":"34.080911,-118.270406","units":"e","language":"en"}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "weather-com.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text

