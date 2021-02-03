import webbrowser
import datetime
import os
import sys
import smtplib
import platform
import getpass



def takeCommand(query): # Will be implemented that this is voice instead of cmd line
    return query

def greetings():
    hour = int(datetime.datetime.now().hour)
    response = "Good Evening "+ name
    if hour >= 0 and hour < 12:
        response = "Good Morning "+ name

    elif hour >= 12 and hour < 18:
        response = "Good Afternoon"+name

    print(response)
    print('I am Tobias. Please tell me how can I help you Master?')


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
        print("Ummm. I don't know where it is. Could you specify where it is ")
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


    print("This is a list of the Basic Commands")
    for line in basicCommands:
        print(line)

    print("This is a list of the API Commands")
    for line in ApiCommands:
        print(line)
        
    cont = True
    from BasicFunctions.basicHelper import *
    from API.apiHandler import *
    while cont:
        query = "cat fact"
        cont = not cont # To only test once

        """ BASIC HELPER SECTION """
        if 'sleep' in query:
            print("Going to sleep " +name)
            sleep()

        elif 'shutdown' in query:
            print("Shutting down")
            shutdown(platform)

        elif 'your name' in query:
            print("My name is "+ machineName)
            if 'stand for' in query:
                print("which stands for " + machineMean)

        elif 'screenshot' in query:
            status = screenshot("screenshot")
            print(status)
            
        elif 'are you there' in query:
            print(str("Yes " + name + ", " + machineName+ " at your service"))

        elif 'what time is it' in query:
            print("The time is ")
            print(getTime(militaryTime))

        elif 'change voice' in query:
            voiceId = changeVoice(voiceId)
            print(str("Voice changed to " +("female" if voiceId == 0 else "male")))
            
        elif 'wikipedia' in query:
            print('Searching Wikipedia....')
            results = searchWiki(query)
            print('According to Wikipedia')
            print(results)

        elif 'diagnostics' in query:
            print('Running Diagnostics')
            print(diagnostics())

            
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
            print(randomCatFact()) # Add to this getting more than 1 back

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
            print("go through the ip address of mine or of someone else")

        elif 'property search' in query:
            print("Call Trulia on searching a property. Could be an issue.")
            

        elif 'more commands' in query:
            print("Made some more commands here")

        


        else: # check if it is a command to run on terminal
            print("Check here if it is a command or not")

