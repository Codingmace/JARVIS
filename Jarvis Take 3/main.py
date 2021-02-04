import pyttsx3
import speech_recognition as sr  #Implement later Automatic-speech recognition
import webbrowser
import datetime
import os
import sys
import smtplib
import platform
import getpass

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Do all diagnostics here


def takeCommand(query):
    return query

def greetings(machineName, userName):
    hour = int(datetime.datetime.now().hour)
    response = "Good Evening "+ name
    if hour >= 0 and hour < 12:
        response = "Good Morning "+ name

    elif hour >= 12 and hour < 18:
        response = "Good Afternoon"+name

    speak(response)
    speak('I am ' + machineName + '. Please tell me how can I help you ' + userName + '?')


def dirExist(folderPath):
    folderCheck = os.path.isdir(folderPath)
    if not folderCheck: # Make folder if it doesn't exist
        os.makedirs(folderPath)


if __name__ == '__main__':
    print("Loading Config")
    machineName = "TOBIAS"
    machineMean = "Totally Obscure Intelligent Assistant System"
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

    cont = True
    from basicHelper import *
    from API.apiHandler import *
    while cont:
        query = ""
        query = "weather"
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
        elif 'define' in query: # Done
            word = query.replace('define', '')
            print(wordDefinition(word))
            print("Hope that definition works for you") # Could add returning an example

        elif 'google' in query:
            newQuery = query.replace("google", "")
            if "search" in query or "image" in query or "crawl" in query or "news" in query:
                result = google(newQuery)


        elif 'reverse image search' in query:
            newQuery = query.replace("reverse image search", "")
            reverseImageSearch(newQuery)


        elif 'proxy' in query:
            proxies = proxyCheck()
            tempFile = open("1-31-2020.txt", "w")
            tempFile.write(proxies)
            tempFile.flush()
            tempFile.close()
            print(proxies[0]) # Check this works. Wasn't able to test today
            print("Printing out top 2 and saving all of them to a file")

        elif 'cat fact' in query:
            query = query.replace("cat fact","")
            print(randomCatFact(query))
            print("would you like another")

        elif 'weather' in query:
            query = query.replace("weather")
            print("Locate the device first or location of the weather")

        elif 'verify' in query or "valid" in query:
            newQuery = query.replace("verify","").replace("valid","")

            print("Check if the phone number or email is valid")

        elif 'analyze' in query:
            query = query.replace("analyze","")
            if 'text' in query:
                print("analyze the text in some way.")
                print("This can be by test, text anaylzer or if needed category prediction")
            elif 'video' in query:
                print("Doing the estimate pose")


        elif 'transcribe' in query:
            if 'audio to text' in query:
                query = query.replace("trascribe audio to text", "")
                print("Do the scripting for Transcribe")

        elif 'scan' in query:
            if 'url' in query:
                
                print("scan urls or something")
                print("Do the detect or URL intel")

        elif 'image' in query and 'text' in query:
            
            print("Image to text OCRLY")

        elif 'youtube' in query:
            if 'search' in query:
                
                print("Search and pull up the youtube video")
            elif 'download' in query:
                
                print("Download the youtube video. this may require searching for it")

        elif 'locate' in query:
            
            print("go through ip address")


        elif 'more commands' in query:
            
            print("Made some more commands here")




        else: # check if it is a command to run on terminal
            print("Check here if it is a command or not")
