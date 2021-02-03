from JARVIS import web_searches, app_manager, calculator, weather, audio_manager, map_manager, time_manager, timetabler
from playsound import playsound
from datetime import datetime

class Handler(object):
    def __init__(self):
        self.a = app_manager.AppManager()
        self.w = web_searches.Web()
        self.c = calculator.Calc()
        self.weather = weather.Weather()
        self.audio = audio_manager.Audio()
        self.m = map_manager.Maps()
        self.t = time_manager.Time()
        self.s = timetabler.Timetabler()
        self.command = None

    def handleOpenCommands(self, query):
        playsound('audio\\opening_app.mp3')
        query = str(query).replace('open ', '').lower()
        keyFound = False
        keys = self.a.keys
        exe = self.a.exe
        for key in keys:
            if str(key) in query:
                command = exe[str(key)]
                keyFound = True
                self.a.open(path=command)
                break
        if keyFound is False:
            try:
                self.a.open(path=query)
            except:
                print('Sorry, the command you typed does not exist')

    def handleURLCommands(self, query):
        query = str(query).split(' ')
        url = str(query[2]).strip()
        browser = str(query[4]).strip()
        keys = self.w.keys
        exe = self.a.exe
        for key in keys:
            if str(key).lower() == str(browser).lower():
                if str(key).lower() == 'chrome':
                    playsound('audio/search_chrome.mp3')
                else:
                    playsound('audio/search_firefox.mp3')
                command = str(exe[str(key)]) + ' ' + str(url)
                self.w.goToUrL(command)

    def handleSearchCommands(self, query):
        query = str(query).split('"')
        search = str(query[1]).replace(' ', '+')
        browser = str(query[2]).replace(' in ', '').strip()
        keys = self.w.keys
        exe = self.a.exe
        for key in keys:
            if str(key).lower() == str(browser).lower():
                if str(key).lower() == 'chrome':
                    playsound('audio/search_chrome.mp3')
                    command = str(exe[str(key)]) + ' https://www.google.com/search?q={}'.format(search)
                    self.w.goToUrL(command)
                elif str(key).lower() == 'firefox':
                    playsound('audio/search_firefox.mp3')
                    command = str(exe[str(key)]) + ' https://www.google.com/search?q={}'.format(search)
                    self.w.goToUrL(command)
                elif str(key).lower() == 'google maps':
                    search = search.replace('+', ' ')
                    self.m.showLocations(search)
                    playsound('audio\\locating.mp3')
                break

    def handleCloseCommands(self, query):
        query = str(query).replace('close ', '').lower()
        keyFound = False
        keys = self.a.keys
        exe = self.a.exe
        for key in keys:
            if str(key) in query:
                command = exe[str(key)]
                keyFound = True
                self.a.close(path=command)
                break
        if keyFound is False:
            try:
                self.a.open(path=query)
            except:
                print('Sorry, the command you typed does not exist')

    def handleMathCommand(self, query):
        answer = None
        if '+' in query:
            query = str(query).lower().replace('what is ', '').split(' + ')
            answer = self.c.add(query[0], query[1])
        elif 'minus' in query:
            query = str(query).lower().replace('what is ', '').split(' minus ')
            answer = self.c.subtract(query[0], query[1])
        elif 'x' in query:
            query = str(query).lower().replace('what is ', '').split(' x ')
            answer = self.c.multiply(query[0], query[1])
        elif '/' in query:
            query = str(query).lower().replace('what is ', '').split(' / ')
            answer = self.c.divide(query[0], query[1])
        elif '^' in query:
            query = str(query).lower().replace('what is ', '').split(' ^ ')
            answer = self.c.computePowers(query[0], query[1])
        else:
            print('Sorry but the query you have typed currently does not exist')

        return answer

    def handleManualWeatherCommands(self, query):
        query = str(query).replace('what is the weather in ', '').lower()
        self.weather.getWeatherManual(query)

    def handleAudioCommands(self, query):
        if str(query).lower() == 'mute':
            print('')
        elif 'set volume to' in str(query).lower():
            value = str(query).replace('set volume to', '').replace('%', '').strip()
            self.audio.changeVolume(value)
        else:
            print('Sorry but the command you typed currently does not exist.')

    def handleMapsCommands(self, query):
        query = str(query).replace('locate ', '')
        self.m.showLocations(query)

    def handleAutoTimeCommands(self):
        time = self.t.returnTimeAuto()
        return str(time)

    def handleManualTimeCommands(self, query):
        query = str(query).lower().replace('what is the time in ', '')
        time = self.t.returnManualTime(query)
        return str(time)

    def handleTimetablerCommands(self, query):
        if 'add' in str(query).lower():
            query = str(query).lower().replace('add "', '').split('" to events with a due date of "')
            self.s.addEvent(str(query[0]), str(query[1]))
            print('Event added')
        elif str(query).lower() == 'clear all events':
            self.s.clearEvents()
            print('Events Cleared')
        elif 'remove' in str(query).lower():
            query = str(query).lower().replace('remove "', '').replace('" from events', '')
            self.s.removeEvent(query)
            print('Event removed')
        elif str(query).lower() == 'get events':
            events = self.s.getEvents()
            print(str(events))
        elif 'check when' in str(query).lower():
            query = str(query).lower().replace('check when "', '').replace('" is due', '')
            self.s.manualCheckEvent(query)



