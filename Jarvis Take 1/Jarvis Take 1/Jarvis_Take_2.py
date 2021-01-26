import pyttsx3
import wikipedia
import speech_recognition as sr  #Implement later Automatic-speech recognition
import webbrowser
import datetime
import os
import sys
import smtplib
import psutil
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


def screenshot():
    speak("Taking screenshot")
    img = pyautogui.screenshot()
    dirExist('screenshot')
    img.save('screenshots/screenshot ' + datetime.datetime.now().replace(microsecond=0)+ '.png')

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


def greetings():
    hour = int(datetime.datetime.now().hour)
    response = "Good Evening "+ name
    if hour >= 0 and hour < 12:
        response = "Good Morning "+ name

    elif hour >= 12 and hour < 18:
        response = "Good Afternoon"+name

    speak(response)
    speak('I am JARVIS. Please tell me how can I help you SIR?')


def dirExist(folderPath):
    folderCheck = os.path.isdir(folderPath)
    if not folderCheck: # Make folder if it doesn't exist
        os.makedirs(folderPath)


# Evaluting that the settings file has everything
def setupEval(machineName): # MachineName will be when have more than 1 machine and changing the data foler to it
    dirExist("data")
    f1 = open("data/oldSettings.txt")
    f = open("data/settings.txt", "w")
    lines = f1.readlines()
    if(len(lines) < 5): # Restart Setup
        name = "Master" # User's name
        musicPath = "./music" # Later verify how much we start with
        dirExist(musicPath)
        voiceId = 1 # Setting to female
        voice = "female" if voiceId == 1 else "male"

        f.write(("Name: " + name))
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
    musicPath = "./music" # Later verify how much we start with
    softwareList = getSoftwares(platform)
    browser= 'chrome'
    chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    webbrowser.register(browser, None, webbrowser.BackgroundBrowser(chrome_path))

    print("Loaded config")
    greetings()

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
            
        elif 'open google' in query:
            webbrowser.get(browser).open_new_tab("https://google.com")

        elif 'open stackoverflow' in query:
            webbrowser.get(browser).open_new_tab("https://stackoverflow.com")

        elif 'open' in query:
            query.replace("open ", "")
            print("Check if the query is a software")
            print("Check to see if it is a file")
            print("Check if the query is a website")
            print("Throw an error if not above")

        elif 'play' in query:
            if 'music' in query:
                os.startfile(musicPath)
            else:
                query.replace("play ", "")
                print("Find the song")
                print("Play the song or throw an error")
            
        elif 'remember' in query: ## Add to take in the entry name
            print("Many things that can go here but going to start simple")
            query.replace("remember", "")
            print("Split up the command. The key word and action")
            print("For now is will split them")
            rememberMessage = query.replace("remember", "").split(" is ")
            rememberCmd = open('extraCommands.txt', 'a')
            rememberCmd.write(rememberMessage[0])
            rememberCmd.close()
            rememberAction = open('extraActions.txt', 'a')
            rememberAction.write(rememberMessage[1])
            rememberAction.close()

        elif 'list extra' in query:# print out the recently added comamnds
            if 'command' in query:
                remember = open("extraCommands.txt", "r")
                lines = remember.readlines()
                speak(str("I have " + str(len(lines)) + " learned commands"))
            if 'action' in query:
                remember = open("extraActions.txt", "r")
                lines = remember.readlines()
                speak(str("I have " + str(len(lines)) + " learned commands"))


        else: # check if it is a command to run on terminal
            print("Check here if it is a command or not")


