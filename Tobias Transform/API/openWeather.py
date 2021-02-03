import requests
from variables import rapidApiKey

class OpenWeather():
    def __init__(self):
        self.location = "London, uk"
        self.country = "uk"
        self.longitude = "10"
        self.latitude = "20"
        self.callback = "test"
        self.id = "2172797"
        self.language = "en"
        self.units = "imperial" # or metric
        self.mode = "JSON"
        self.count = "10" # Forcast
        self.type = "link, accurate"
        self.dt = "1590094153"
        self.city = "McKinney"
        self.zipcode = "75002"
        
    def currentWeather(self):
        url = "https://community-open-weather-map.p.rapidapi.com/weather"

        querystring = {"q":self.location,"lat":self.latitude,"lon":self.longitude,"callback":self.callback,"id":self.id,"lang":self.language,"units":self.units,"mode":self.mode}

        headers = {
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        return response

    def forecast(self):
        url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"

        querystring = {"q":self.location,"lat":self.latitude,"lon":self.longitude,"cnt":self.count,"units":self.units,"mode":self.mode,"lang":self.language}

        headers = {
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        return response


    def searchWeatherData(self):
        url = "https://community-open-weather-map.p.rapidapi.com/find"

        querystring = {"q":self.location,"cnt":self.count,"mode":self.mode,"lon":self.longitude,"type":self.type,"lat":self.latitude,"units":self.units}

        headers = {
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        return response

    def historicalWeather(self):
        url = "https://community-open-weather-map.p.rapidapi.com/onecall/timemachine"

        querystring = {"lat":self.latitude,"lon":self.longitude,"dt":self.dt}

        headers = {
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        return response


    def climateForecast30(self):
        url = "https://community-open-weather-map.p.rapidapi.com/climate/month"

        querystring = {"q": self.city}

        headers = {
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        return response


    def forecast5d3h(self):
        url = "https://community-open-weather-map.p.rapidapi.com/forecast"

        querystring = {"q":self.location,"lat":self.latitude,"lon":self.longitude,"lang":self.language,"cnt":self.count,"zip":self.zipcode}

        headers = {
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        return response

