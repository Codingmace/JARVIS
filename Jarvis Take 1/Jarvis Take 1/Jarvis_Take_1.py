import pyttsx3
import wikipedia
import speech_recognition as sr  #IMplement later Automatic-speech recognition
import webbrowser
import datetime
import os
import sys
import smtplib
import psutil
import pyjokes
import pyaudio
import pyautogui
import platform
import getpass

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Add setting and maybe a tag
def screenshot():
    speak("Taking screenshot")
    img = pyautogui.screenshot()
    img.save('screenshot/screenshot.png')

# Do all diagnostics here
def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)


def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 494
        r.adjust_for_ambient_noise(source, duration=1.5)
        audio = r.listen(source)

    try:
        print('Recognizing..')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        # print(e)

        print('Say that again please...')
        return 'None'
    return query


def weather():
    print("Need to do the weather")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    response = "Good Evening "+ name
    if hour >= 0 and hour < 12:
        response = "Good Morning "+ name

    elif hour >= 12 and hour < 18:
        response = "Good Afternoon"+name

    speak(response)
    
    weather()
    speak('I am JARVIS. Please tell me how can I help you SIR?')


def dirExist(folderPath):
    folderCheck = os.path.isdir(folderPath)
    if not folderCheck: # Make folder if it doesn't exist
        os.makedirs(folderPath)


# Evaluting that the settings file has everything
def setupEval(machineName): # MachineName will be when have more than 1 machine and changing the data foler to it
    dirExist("data")
    f = open("data/settings.txt")
    lines = f.readlines()
    if(len(lines) < 5): # Restart Setup
        name = "Master" # User's name
        musicPath = "./music" # Later verify how much we start with
        dirExist(musicPath)
        voiceId = 1 # Setting to female
        voice = "female" if voiceId == 1 else "male"

        f.write("Name: " + name)
        f.write("Platform: " + sys.platform) # OS On
        f.write("MusicPath: " + musicPath) # Path for music
        f.write("Voice: " + voice)

        # CONTINUE WITH A FRESH STARTUP

    else:
        print("Well seems you already have data. Good for you. Maybe later you could add some manipulation but we are keeping it simple right now")

def getSoftwares(platform):
    softwareList = []
    basePath = ""
    if platform == 'linux' or platform == 'linux2':
        basePath = '/usr/bin/'
    elif platform == "darwin":
        basePath = '/Applications/'
    elif platform == "win32":
        basePath = "C:\\Program Files (x86)\\"
       # print(basePath)
    else:
        speak("Ummm. I don't know where it is. Could you specify where it is ")
        basePath = input("Enter in the path")




if __name__ == '__main__':
    print("Loading Config")
    machineName = "JARVIS"
    setupEval(machineName) # Determine all the general info is in settings.txt
    platform = sys.platform
    name = "Master"
    voiceId = 1 # Female
    print("Loaded config")
    softwareList = getSoftwares(platform)
    """
    Default Chrome Locations
    Linux : /usr/bin/google-chrome
    Mac : open -a /Applications/Google\ Chrome.app
    Windows : C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
        webbrowser.register(
        'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    """
    while True:
        query = takeCommand().lower()
        if 'sleep' in query:
            print("Going to sleep")
            sys.exit()

        elif 'shutdown' in query:
            print("Shutting down")
            if platform == "win32":
                os.system("shutdown /p /f")
            if platform == "linux" or "darwin" or "linux2":
                os.system("poweroff")

        elif 'your name' in query:
            print("My name is " + machineName)
            if 'stand for' in query:
                print("which stands for JUST A VERY INTELLIGENT SYSTEM")

        elif 'screenshot' in query:
            screenshot()

        elif 'music' in query:
            # PLay spotify?
            print("Make a music function")

        elif 'are you there' in query:
            speak(str("Yes " + name + ", " +machineName+ " at your service"))

        elif 'what time is it' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'{name}, the time is {strTime}')

        elif 'change voice' in query:
            if voiceId == 1:
                voiceId = 0
            elif voiceId == 0:
                voiceId = 1
            speak(str("Voice changed to " +("female" if voiceId == 0 else "male")))
            

        elif 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)
            
            
        else: # check if it is a command to run on terminal
            print("Check here if it is a command or not")





        elif 'cpu' in query:
            cpu()


        elif 'open google' in query:
            webbrowser.get('chrome').open_new_tab('https://google.com')

        elif 'open stackoverflow' in query:
            webbrowser.get('chrome').open_new_tab('https://stackoverflow.com')

        elif 'play music' in query:
            os.startfile(musicPath)

        elif 'search' in query:
            speak('What do you want to search for?')
            search = takeCommand()
            url = 'https://google.com/search?q=' + search
            webbrowser.get('chrome').open_new_tab(url)
            speak('Here is What I found for' + search)

        elif 'location' in query:
            speak('What is the location?')
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get('chrome').open_new_tab(url)
            speak('Here is the location ' + location)


        elif 'remember that' in query: ## Add to take in the entry name
            speak("what should i remember",name)
            rememberMessage = takeCommand()
            speak("Ok. I will remember",rememberMessage)
            remember = open('data.txt', 'a')
            remember.write(rememberMessage)
            remember.close()

        elif 'do you remember anything' in query:# print out the recently added comamnds
            remember = open('data.txt', 'r')
            speak("You said me to remember that" + remember.read())


