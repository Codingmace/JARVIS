import pyttsx3
import speech_recognition as sr  #Implement later Automatic-speech recognition
import webbrowser
import datetime
import os
import sys
import smtplib
#import pyaudio
import platform
import getpass

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Do all diagnostics here


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


def greetings():
    hour = int(datetime.datetime.now().hour)
    response = "Good Evening "+ name
    if hour >= 0 and hour < 12:
        response = "Good Morning "+ name

    elif hour >= 12 and hour < 18:
        response = "Good Afternoon"+name

    speak(response)
    speak('I am Tobias. Please tell me how can I help you Master?')


def dirExist(folderPath):
    folderCheck = os.path.isdir(folderPath)
    if not folderCheck: # Make folder if it doesn't exist
        os.makedirs(folderPath)

### UPDATE THIS USING GLOBAL
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

        f.write(("Name: " + name)+"\n")
        f.write("Platform: " + sys.platform + "\n") # OS On
        f.write("MusicPath: " + musicPath+"\n") # Path for music
        f.write("Voice: " + voice + "\n")

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
        basePath2 = "C:\\Program Files\\"
       # print(basePath)
    else:
        speak("Ummm. I don't know where it is. Could you specify where it is ")
        basePath = input("Enter in the path")


def startUpInitial():
    print("Here is the process that is needed at start up")
    # Load configurations
    # Make sure the folders and files are their

if __name__ == '__main__':
    print("Loading Config")
    machineName = "TOBIAS"
    machineMean = "Totally Obscure Intelligent Assistant System"
# Will add this when have preset settings    
#    setupEval(machineName) # Determine all the general info is in settings.txt
    platform = sys.platform
    name = "Master"
    militaryTime = True
    voiceId = 1 # Female
    musicPath = "./music" # Later verify how much we start with
#    softwareList = getSoftwares(platform) ## Will implement later
    browser= 'chrome'
    chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    webbrowser.register(browser, None, webbrowser.BackgroundBrowser(chrome_path))

    ## LOAD IN THE BASIC CONFIGURATIONS
    basicFile = open("data/basicCommands.txt", "r")
    basicCommands = basicFile.readlines()
    ## LOAD IN THE API CONFIGURATIONS
    ApiFile = open("data/ApiCommands.txt", "r")
    ApiCommands = basicFile.readlines()
    
    print("Loaded config")
#    greetings()


    print("This is a list of the Basic Commands")
    for line in basicCommands:
        print(line)

    print("This is a list of the API Commands")
    for line in ApiCommands:
        print(line)
        
    # import pyaudio # Throwing error on the Laptop
    cont = True
    from basicHelper import *
#    from API import apiHandler
    from API.apiHandler import *
#    from API import *
   # from API.apiHandler import *
    while cont:
       # query = takeCommand().lower()
        query = 'google searc  lamborghini'
        cont = not cont

        """ BASIC HELPER SECTION """
        if 'sleep' in query:
            speak("Going to sleep " +name)
            sleep()

        elif 'shutdown' in query:
            speak("Shutting down")
            shutdown(platform)

        elif 'your name' in query:
            speak("My name is "+ machineName)
            if 'stand for' in query:
                speak("which stands for " + machineMean)

        elif 'screenshot' in query:
            status = screenshot("screenshot")
            speak(status)
            
        elif 'are you there' in query:
            speak(str("Yes " + name + ", " + machineName+ " at your service"))

        elif 'what time is it' in query:
            speak("The time is ")
            speak(getTime(militaryTime))

        elif 'change voice' in query:
            voiceId = changeVoice(voiceId)
            speak(str("Voice changed to " +("female" if voiceId == 0 else "male")))
            
        elif 'wikipedia' in query:
            speak('Searching Wikipedia....')
            results = searchWiki(query)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'diagnostics' in query:
            speak('Running Diagnostics')
            speak(diagnostics())
            
#        """ API HELPER SECTION """
        elif 'define' in query:
            word = query.replace('define', '')
            speak("The definition of " + word)
            speak (wordDefinition(word))

        elif 'google' in query:
            newQuery = query.replace("google", "")
            result = google(newQuery)

        elif 'reverse image search' in query:
            print("LOoking up the image. check if it is URL or local file")
        
                





        else: # check if it is a command to run on terminal
            print("Check here if it is a command or not")

