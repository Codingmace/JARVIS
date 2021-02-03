import requests
from variables import rapidApiKey

class WeatherCom():
    def __init__(self):
        self.language = "en"
        self.longitude = "34.0"
        self.latitude = "-118.27"
        self.units = "e"
        self.geocode = self.longitude + "," + self.latitude
        
    def covid19(self):
        url = "https://weather-com.p.rapidapi.com/v3/wx/disease/tracker/countryList/current"

        querystring = {"language":self.language}

        headers = {
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "weather-com.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        return response

    def forecastDaily(self): 
        url = "https://weather-com.p.rapidapi.com/v3/wx/forecast/daily/3day"
        
        querystring = {"geocode": self.geocode,"units":self.units,"language":self.language}

        headers = {
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "weather-com.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        return response

    def forecastHourly(self):
        url = "https://weather-com.p.rapidapi.com/v3/wx/forecast/hourly/1day"

        querystring = {"geocode":self.geocode,"units":self.units,"language":self.language}

        headers = {
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "weather-com.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        return response

    def historical30d(self):
        url = "https://weather-com.p.rapidapi.com/v3/wx/conditions/historical/dailysummary/30day"

        querystring = {"geocode":self.geocode,"units":self.units,"language":self.language}

        headers = {
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "weather-com.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        return response

