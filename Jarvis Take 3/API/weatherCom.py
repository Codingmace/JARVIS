import requests
from variable import rapidApiKey

def covid19(language):
    url = "https://weather-com.p.rapidapi.com/v3/wx/disease/tracker/countryList/current"

    querystring = {"language": language}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "weather-com.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response

def forecastDaily(): 
    url = "https://weather-com.p.rapidapi.com/v3/wx/forecast/daily/3day"

    querystring = {"geocode":"34.080911,-118.270406","units":"e","language":"en"}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "weather-com.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response

def forecastHourly():
    url = "https://weather-com.p.rapidapi.com/v3/wx/forecast/hourly/1day"

    querystring = {"geocode":"34.080911,-118.270406","units":"e","language":"en"}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "weather-com.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response

def historical30d():
    url = "https://weather-com.p.rapidapi.com/v3/wx/conditions/historical/dailysummary/30day"

    querystring = {"geocode":"34.080911,-118.270406","units":"e","language":"en"}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "weather-com.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response

