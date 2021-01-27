import requests

def covid19():
    url = "https://weather-com.p.rapidapi.com/v3/wx/disease/tracker/countryList/current"

    querystring = {"language":"en"}

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "weather-com.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

def forecastDaily():
    url = "https://weather-com.p.rapidapi.com/v3/wx/forecast/daily/3day"

    querystring = {"geocode":"34.080911,-118.270406","units":"e","language":"en"}

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "weather-com.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

def forecastHourly():
    url = "https://weather-com.p.rapidapi.com/v3/wx/forecast/hourly/1day"

    querystring = {"geocode":"34.080911,-118.270406","units":"e","language":"en"}

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "weather-com.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

def historical30d():
    url = "https://weather-com.p.rapidapi.com/v3/wx/conditions/historical/dailysummary/30day"

    querystring = {"geocode":"34.080911,-118.270406","units":"e","language":"en"}

    headers = {
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "weather-com.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)    

