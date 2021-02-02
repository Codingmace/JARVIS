## This is to help with importing the API only when needed
## Will read in all the keys here though
import sys
import json

rapidApiKey = "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36"
# Add variable for location


#sys.path.append("API/")

def responses(response, neededData):
    dataResponse = response.json()

#    neededData = ['region_name','city_name','latitude','longitude','zip_code']
    importantData = []

    for data in neededData:
        importantData.append(dataResponse[data])

    print(neededData)
    print(importantData)



# Urban Dictionary : To define words
def wordDefinition(word):
    from API.urbanDictionary import defineWord
#    response = defineWord(word, rapidApiKey)
    dataResponse = defineWord(word,rapidApiKey).json()
    return dataResponse['list'][0]['definition'] # First word definition

#    return defineWord(word,rapidApiKey)
    # Example of it


# Encdoing for the google
def encode(term):
    return term.replace("+", "%2B").replace(" ", "+")

# Google Search : Look up things on google
def google(query):
    from API.googleSearch import search, images, crawl, news
    if "search" in query:
        search("that term", "more" , rapidApiKey)
    elif "image" in query:
        image()
    elif "crawl" in query:
        crawl()
    elif "news" in query:
        news()


# Revese Image : Google Reverse Image Search
def reverseImageSearch(query):
    from API.reverseImage import reverseImage
    
    print("Check that the file exists")
    print("Remove and add in the file name")
    imageUrl = query # Modify for the actual file URL
    reverseImage(imageUrl,rapidApiKey)

# Open Proxy : Reports all open proxies at that moment
def proxyCheck():
    from API.openProxies import openProxy    
    return openProxy(rapidApiKey)


# Cat Facts : Returns random cat facts
def randomCatFact():
    from API.catFacts import catFact
    print("gets the random cat fact and will choose one")
    facts = catFact(rapidApiKey).json()
    return facts[0]['text'] # Have to do random because their are only 5 available
#    return catFact(rapidApiKey)
    # catFact(rapidApiKey)
    





# Open Weather : Reports back the weather
""" NEEDS: have to sort out how I am going to do location """
# from openWeather import *

# Weather.com : Reports back weather
""" Just Need Geocode """
def weather(query, location):
    # Cannot do * Have to add all of them
    from API.weatherCom import covid19
    print("Add the geocode to most of these because I don't know this far")





# Email Validate : Check if email is valid or not
def validateEmailAddress(query):
    from API.emailValidate import validEmail
    


# Verifone : Verifies a phone is valid (Default Country is US)
def verifyPhoneNumber(query):
    from API.veriphone import verifyPhone
    

# Pose Estimate : Takes a photo or video and estimates the posture
def estimatePose(query):
    from API.poseEstimate import video, image
    
    
# Transcribe : Turns audio into text
def transcribeAudio(query):
    from API.transcribe import transcribeUrl, getTask, serviceStatus, getTasks, transcribe
    

def encode(term): # URL Encoding
    return term.replace(" ", "%20")

# Trulia :
def propertySearch(query):
    from API.trulia import searching, propertyDetail
    
    

# COST MONEY
# Category Prediction : Prints out catagories the text matches
def predictCategory(query):
    from API.categoryPrediction import categoryPrediction
    print("Could take this from the text")
    

# Text Analyzer : Analyzes the contents of a URL
def analyzeUrlText(query):
    from API.textAnalyzer import contentExtract, namedExtract, partOfSpeech
    

# Test : To grab text, identify parts of speech, identify name of entities
def analyzeText(query):
    from API.testTextHelp import fetchText, pos, namedEntity
    

# Summarize API : Summarize the text of a URL link
def summarizeUrlText(query):
    from API.summarizeApi import summarize
    

# Plate Recognition :
def plateRecognition(query):
    from API.plateRecognition import recognizeByUrl , recognizeByImage
    

### USES TRUE URL ENCODING

# OCRLY : URL Image to text
def urlImage2Text(query):
    from API.OCRLY import OImage2Text
    

# Youtube Download : Download Youtube Video by VideoID
def downloadYoutube(query):
    from API.youtubeDownload import downloadVideo
    print("Send it and it will return a warning or a download link to go to")
    


# Threat Detect :
def detectUrlThreats(query):
    from API.threatDetector import detectThreat
    

# URL Intel : Extracts Links from a URL
def IntelligentUrl(query):
    from API.urlIntel import urlIntel


# IP2Location : Well Turns an IP Address into a Location
def ip2Location(query):
    from API.ip2Location import ip2location
    

# Find any Ip address world wide : IPv6 and IPv4
def ipLocWW(query):
    from API.ipWorldWide import ipWorldWide
    


# IP Geolocation Web Service : IP Geolocate
def ipGeoLocate(query):
    from API.ipGeoLocation import ipLocation
    