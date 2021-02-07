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
    from API.IPAddress import getMyIPv4Address, getMyIPv6Address
    print("Loading Config")
    machineName = "TOBIAS"
    machineMean = "Totally Obscure Intelligent Assistant System"
    platform = sys.platform
    name = "Master"
    dirExist("User")
    userPath = "User/" + name + "/"
    dirExist(userPath)
    militaryTime = True
    voiceId = 1 # Female
    musicPath = userPath + "music/" # Later verify how much we start with
#    softwareList = getSoftwares(platform) ## Will implement later
    browser= 'chrome'
    chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    webbrowser.register(browser, None, webbrowser.BackgroundBrowser(chrome_path))
    
    ## LOAD IN THE BASIC CONFIGURATIONS
    basicFile = open("data/BasicTestCommands.txt", "r")
    basicCommands = basicFile.readlines()
    ## LOAD IN THE API CONFIGURATIONS
    ApiFile = open("data/ApiCommands.txt", "r")
    ApiCommands = basicFile.readlines()
    ipv4 = getMyIPv4Address()
    ipv6 = ""
    try:
        ipv6 = getMyIPv6Address()
    except:
        print("You do not have an IPv6 Address")
##    print("Loaded config")
#    greetings()

    
##    print("This is a list of the Basic Commands")
##    for line in basicCommands:
##        print(line)
##
##    print("This is a list of the API Commands")
##    for line in ApiCommands:
##        print(line)

    queries = []
    f = open('Data/ApiCmd.txt', 'r')
    lines= f.readlines()
    for line in lines:
        queries.append(line)

    cont = True
    from basicHelper import *
    from API.apiHandler import *
    from API.IPAddress import getMyIPv4Address, getMyIPv6Address
    for q in queries:
#    while cont:
#        query = ""
#        query = "weather"
#        query = queries[3]
        query = q
        cont = not cont

#        """ BASIC HELPER SECTION """
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
            status = screenshot(userPath + "screenshot")
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

        elif 'get my ip' in query:
            if 'v4' in query:
                print(getMyIPv4Address())
            elif 'v6' in query:
                try:
                    print(getMyIPv6Address())
                except:
                    print("it seems you don't have an IPv6 Address")
        elif 'get both my ip' in query:
            print(getMyIPv4Address())
            print(getMyIPv6Address())

        elif 'play my music' in query:
            playMyMusic(musicPath)

        elif 'basic calculation' in query:
            query=query.replace("basic calculation", "")
            print("calculating: " + calculate(query))

        elif 'open google' in query:
            webbrowser.get(browser).open_new_tab("https://google.com")

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
            print(reverseImageSearch(newQuery))

        elif 'proxy' in query:
            proxies = proxyCheck()
            dateTime = (datetime.datetime.now().replace(microsecond=0).strftime('%H-%M-%S'))
            tempFile = open(userPath + "op_" + dateTime + ".txt", "w")
            tempFile.write(proxies)
            tempFile.flush()
            tempFile.close()
            print(proxies[0]) # Check this works. Wasn't able to test today
            print("Printing out top 2 and saving all of them to a file")

        elif 'cat fact' in query:
            query = query.replace("cat fact","")
            print(randomCatFact(query))

        elif 'weather' in query:
            query = query.replace("weather","")
            print(weather(query))

        elif 'verify' in query:
            query = query.replace("verify", "").strip()
            print(verifyPhoneNumber(query))
            
        elif "valid" in query: 
            query = query.replace("valid","").strip()
            print(validateEmailAddress(query))
            
        elif 'analyze' in query:
            query = query.replace("analyze","")
            if 'text' in query:
                if "url" in query:
                    if "summarize" in query:
                        query = query.replace("text url summarize" ,"")
                        print(summarizeUrlText(query))
                    elif "extract" in query:
                        query = query.replace("text url extract","")
                        print(analyzeUrlText(query))
                    elif "grab" in query:
                        query = query.replace("text url grab","")
                        print(analyzeText(query))
                else:
                    print("I dont think that is an option")
                    
            elif 'video' in query or 'image' in query:
                print("This one doesn't work at all yet")
                print(estimatePose(query)) 


        elif 'transcribe' in query:
            if 'audio to text' in query:
                query = query.replace("trascribe audio to text", "")
                print("Do the scripting for Transcribe")

        elif 'scan' in query:
            if 'url threat' in query:
                query = query.replace("scan url threat", "")
                print(detectUrlThreats(query))
            elif 'url link' in query:
                query = query.replace("scan url link", "")
                print(IntelligentUrl(query))
                
        elif 'image to text' in query:
            query = query.replace("image to text", "")
            print(urlImage2Text(query))

        elif 'youtube' in query:
            if 'search' in query:
                print("dont think I have this one yet")
                print("Search and pull up the youtube video")
            elif 'download' in query:
                query = query.replace("youtube download","")
                print(downloadYoutube(query))
            
        elif 'ip address' in query:
            if "to location" in query:
                print(ip2Location(ipv4))
            if "geolocate" in query:
                print(ipGeoLocate(ipv4))
            elif "world wide" in query:
                print(ipLocWW(ipv4))

        elif 'plate scan' in query:
            query = query.replace("plate scan","")
            print(plateRecognition(query))


#       """ Personal API Helper """
        

        elif 'more commands' in query:
            print("Print out the file with more commands")
            print("Made some more commands here")


        else: # check if it is a command to run on terminal
            print("Check here if it is a command or not")
