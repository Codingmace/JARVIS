import pyttsx3
import speech_recognition as sr  #Implement later Automatic-speech recognition
import webbrowser
import datetime
import os
import sys
import smtplib
import psutil
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
    softwareList = getSoftwares(platform)
    browser= 'chrome'
    chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    webbrowser.register(browser, None, webbrowser.BackgroundBrowser(chrome_path))


    ## LOAD IN THE BASIC CONFIGURATIONS
    basicFile = open("data/basicCommands.txt", "r")
    basicCommands = basicFile.readlines()
    
    print("Loaded config")
    greetings()


    print("This is a list of the Basic Commands")
    for line in basicCommands:
        print(line)


    # import pyaudio # Throwing error on the Laptop
    from basicHelper import * 
    while True:
       # query = takeCommand().lower()
        query = 'a'
        
        if 'sleep' in query:
#            from basicHelper import sleep
            speak("Going to sleep " +name)
            sleep()

        elif 'shutdown' in query:
#            from basicHelper import shutdown
            speak("Shutting down")
            shutdown(platform)

        elif 'your name' in query:
            speak("My name is "+ machineName)
            if 'stand for' in query:
                speak("which stands for " + machineMean)

        elif 'screenshot' in query:
#            from basicHelper import screenshot
            screenshot("screenshot")

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

            
        elif 'open google' in query:
            webbrowser.get(browser).open_new_tab("https://google.com")

##        elif 'open stackoverflow' in query:
##            webbrowser.get(browser).open_new_tab("https://stackoverflow.com")

        elif 'music' in query:
            # Play spotify?
            print("Make a music function")
            
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

