## This is to help with importing the API only when needed
## Will read in all the keys here though
import sys
import json
from variable import weatherInfo
from IPAddress import getMyIPv4Address, getMyIPv6Address
# rapidApiKey = "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36"
# Add variable for location


#sys.path.append("API/")
def readData(filename):
    f = open(filename, "rb")
    fin = f.readline()
    lines = f.readlines()
    for line in lines:
        fin += line
    return fin

# Urban Dictionary : To define words
def wordDefinition(word):
    from API.urbanDictionary import defineWord
#    response = defineWord(word, rapidApiKey)
    dataResponse = defineWord(word).json()
    return dataResponse['list'][0]['definition'] # First word definition
# Possible improvements : Go through the list and choose the best one. Display all of them

# Encdoing for the google
def googleEncode(term):
    return term.replace("+", "%2B").replace(" ", "+")

# Google Search : Look up things on google
def google(query):
    from API.googleSearch import search, images, crawl, news
    if "search" in query:
        query = query.replace("search ","")
        resultCount = 10
        split = query.split(" ")
        lastResult = split[:-1]
        if(lastResult.isdigit()):
            resultCount = int(lastResult)
            query = query.replace(lastResult,"")
        return search(googleEncode(query), resultCount)
        # So much can be done with this
    elif "image" in query:
        query = query.replace("image ","")
        return image(googleEncode(query))
        # Show the images Maybe
    elif "crawl" in query:
        query = query.replace("crawl","")
        resultCount = 10
        split = query.split(" ")
        lastResult = split[:-1]
        if(lastResult.isdigit()):
            resultCount = int(lastResult)
            query = query.replace(lastResult,"")
        return crawl(googleEncode(query), resultCount)
    elif "news" in query:
        query = query.replace("news","")
        return news(googleEncode(query))

# Revese Image : Google Reverse Image Search
def reverseImageSearch(query):
    from API.reverseImage import reverseImage
    print("Check that the file exists")
    print("Remove and add in the file name")
    imageUrl = query # Modify for the actual file URL
    return reverseImage(imageUrl)

# Open Proxy : Reports all open proxies at that moment
def proxyCheck():
    from API.openProxies import openProxy
    return openProxy().text

# Cat Facts : Returns random cat facts
def randomCatFact(query):
    from API.catFacts import catFact
    if "random" in query:
        print("How many facts would you like")
        numberFacts = 10
        print("Would you like to add a length to that?")
        split = query.split(" ")
        maxLength = -1
        if split[1].lower() == "yes":
            print("Ask for the length")
            maxLength = int(split[2])

        if (numberFacts == 1):
            print(catFact(maxLength))
        else:
            facts = catFacts(numberFacts, maxLength)
    else:
        return catFacts(1000, -1)
    print("Print the number of results")
    print("Choose from those results a random one because they always come in same order")
    return facts # return a fact and maybe could make this offline
#    return catFact(rapidApiKey)
    # catFact(rapidApiKey)
    

# Open Weather : Reports back the weather
""" NEEDS: have to sort out how I am going to do location """
def openWeather(query):
    from openWeather import currentWeather, forecast, searchWeatherData, historicalWeather, climateForcast30, forecast5d3h
    from API.ip2Location import ip2location
    ipv4 = getMyIPv4Address()
    callback = weatherInfo['callback']
    mode = weatherInfo['mode']
    types = weatherInfo['types']
    measurement = weatherInfo['measurement']
    units = weatherInfo['units']
    lang = weatherInfo['lang']
    count = weatherInfo['count']
    geoInfo = ip2location(ipv4, "demo")
    latitude = geoInfo['latitude']
    longitude = geoInfo['longitude']
    city = geoInfo['city_name']
    country = geoInfo['country_code']
    zipcode = geoInfo['zipcode']
    location = city + "," + country
    # Location example San francisco,us
    if "current weather" in query:
        return currentWeather(location, latitude, longitude, callback, lang, units, mode)
    elif "forecast today" in query:
        return forecast(location, latitude, longitude, count, units, mode, lang)
    elif "search" in query:
        return searchWeatherData(location, latitude, longitude, count, mode, types, units)
    elif "historical data" in query:
        return historicalWeather(latitude, longitude)
    elif "climate forecast" in query:
        return climateForecast30(city)
    elif "5 day forecast" in query:
        return forecast5d3h(location, latitude, longitude, lang, count, zipcode)
    else:
        print("That is not a valid one")
        return ""
# from openWeather import *

# Weather.com : Reports back weather
def weather(query):
    # Cannot do * Have to add all of them
    from API.weatherCom import covid19, forecastDaily, forecastHourly, historical30d
    currentWeather = weatherInfo
    language = weatherInfo['language']
    if "covid" in query:
        return covid19(language)
    lang = weatherInfo['lang']
    geocode = "100, 20" # Get this from somewhere else
    units = weatherInfo['units']
    if "daily forecast" in query:
        return forecastDaily(geocode, units, lang)
    elif "hourly forecast" in query:
        return forecastHourly(geocode, units, lang)
    elif "historical records" in query:
        return historical30d(geocode, units, lang)
    else:
        return openWeather(query)

# Email Validate : Check if email is valid or not
def validateEmailAddress(query):
    from API.emailValidate import validEmail
    # Could need to extract the text for email when trying this voice to text
    return validEmail(query)

# Verifone : Verifies a phone is valid (Default Country is US)
def verifyPhoneNumber(query):
    from API.veriphone import verifyPhone
    # Must be entered the 10 nubmer digits. My require conversion when doing voice to text
    return verifyPhone(query)

# Pose Estimate : Takes a photo or video and estimates the posture
def estimatePose(query):
    from API.poseEstimate import video, image
    print("Need to read in this data and encode it through base64 I think")
    if 'image' in query:
        query = query.replace("image", "")
        imageData = readData(query)
        return image(imageData)
    elif 'video' in query:
        query = query.replace("video", "")
        videoData = readData(query)
        return video(videoData)
    else:
        return ""
    
# Transcribe : Turns audio into text
def transcribeAudio(query):
    from API.transcribe import transcribeUrl, getTask, serviceStatus, getTasks, transcribe
    if "url" in query:
        query = query.replace("url", "")
        return transcribeUrl(query)
    elif "get task" in query:
        query = query.replace("get task" , "")
        return getTask()
    elif "status" in query:
        return serviceStatus()
    elif "tasks" in query:
        return getTasks()
    elif "file" in query:
        query = query.replace("file","")
        fileData = readData(query)
        return transcribe(fileData)
    else:
        return ""

def encode(term): # URL Encoding
    return term.replace(" ", "%20")

# Trulia :
def propertySearch(query):
    from API.trulia import searching, propertyDetail
    print("Have no fucking clue how I am going to get this information")    
    

# COST MONEY
# Category Prediction : Prints out catagories the text matches
def predictCategory(query):
    from API.categoryPrediction import categoryPrediction
    print("Could take this from the text")

# Text Analyzer : Analyzes the contents of a URL
def analyzeUrlText(query):
    from API.textAnalyzer import contentExtract, namedExtract, partOfSpeech
    if "content" in query:
        query = query.replace("content", "")
        return contentExtract(query)
    elif "named" in query:
        query= query.replace("named","")
        return namedExtract(query)
    elif "part of speech" in query:
        query = query.replace("part of speech", "")
        return portOfSpeech(query)
    else:
        return ""

# Test : To grab text, identify parts of speech, identify name of entities
def analyzeText(query):
    from API.testTextHelp import fetchText, namedEntity, pos
    if "fetch" in query:
        query = query.replace("fetch", "")
        return fetchText(query)
    elif "named" in query:
        query= query.replace("named","")
        return namedEntity(query)
    elif "part of speech" in query:
        query = query.replace("part of speech", "")
        return pos(query)
    else:
        return ""

# Summarize API : Summarize the text of a URL link
def summarizeUrlText(query):
    from API.summarizeApi import summarize
    return summarize(query)

# Plate Recognition :
def plateRecognition(query):
    from API.plateRecognition import recognizeByUrl , recognizeByImage
    if "url" in query:
        query = query.replace('url', "")
        return recognizeByUrl(query)
    elif "file" in query:
        query = query.replace("file", "")
        imageData = readData(query)
        return recognizeByImage(imageData)
    else:
        return ""

# OCRLY : URL Image to text
def urlImage2Text(query): # Uses true url encoding
    from API.OCRLY import OImage2Text
    split = query.split(" ")
    if len(split) == 2:
        return OImage2Text(split[0], split[1])
    else:
        return OImage2Text(split[0], "testFilename.txt")
    
# Youtube Download : Download Youtube Video by VideoID
def downloadYoutube(query):
    from API.youtubeDownload import downloadVideo
    return downloadVideo(query)
    
# Threat Detect :
def detectUrlThreats(query):
    from API.threatDetector import detectThreat
    print("if url must translate to an ip address")
    print("If Ip address don't need to do anything which is the basis")
    return detectThreat(query)
    
# URL Intel : Extracts Links from a URL
def IntelligentUrl(query):
    from API.urlIntel import urlIntel
    return urlIntel(query)

# IP2Location : Well Turns an IP Address into a Location
def ip2Location(query):
    from API.ip2Location import ip2location
    return ip2location(query)

# Find any Ip address world wide : IPv6 and IPv4
def ipLocWW(query):
    from API.ipWorldWide import ipWorldWide
    return ipWorldWide(query) # Not sure if this one will work

# IP Geolocation Web Service : IP Geolocate
def ipGeoLocate(query):
    from API.ipGeoLocation import ipLocation
    return ipLocation(query)
