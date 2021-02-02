import requests
import os

class Weather(object):
    def __init__(self):
        self.city = None
        self.command = None

    def getWeatherManual(self, city):
        command = 'C:\\"Program Files (x86)"\Google\Chrome\Application\chrome.exe --allow-outdated-plugins https://www.google.com/search?q=weather+in+{}'.format(city)
        os.system('cmd /c {}'.format(command))
