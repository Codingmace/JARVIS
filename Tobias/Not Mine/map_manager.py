import os

class Maps(object):
    def __init__(self):
        self.chrome = 'C:\\"Program Files (x86)"\Google\Chrome\Application\chrome.exe --allow-outdated-plugins'
        self.url = 'google.com/maps/place/'
        self.command = None

    def showLocations(self, query):
        query = str(query.replace(' ', '+'))
        self.command = 'C:\\"Program Files (x86)"\Google\Chrome\Application\chrome.exe --allow-outdated-plugins https://www.google.com/maps/place/{}'.format(query)
        os.system('cmd /c start {}'.format(self.command))
