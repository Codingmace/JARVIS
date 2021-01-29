## This is to help with importing the API only when needed
## Will read in all the keys here though
import sys

rapidApiKey = "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36"
#sys.path.append("API/")

# Urban Dictionary : To define words
def wordDefinition(word):
    from API.urbanDictionary import defineWord
    return defineWord(word,rapidApiKey)

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
def reverseImage(query):
    from API.reverseImage import reverseImage
    print("Remove and add in the file name")


# Open Weather : Reports back the weather
""" NEEDS: have to sort out how I am going to do location """
# from openWeather import *

# Weather.com : Reports back weather
""" Just Need Geocode """
from API.weatherCom import *

# Open Proxy : Reports all open proxies at that moment
from API.openProxies import openProxy

# Cat Facts : Returns random cat facts
from API.catFacts import catFact

# Test : To grab text, identify parts of speech, identify name of entities
from API.testTextHelp import fetchText, pos, namedEntity

# Email Validate : Check if email is vali or not
from API.emailValidate import validEmail

# Summarize API : Summarize the text of a URL link
from API.summarizeApi import summarize

# Verifone : Verifies a phone is valid (Default Country is US)
from API.veriphone import verifyPhone

# Pose Estimate : Takes a photo or video and estimates the posture
from API.poseEstimate import video, image

# Transcribe : Turns audio into text
from API.transcribe import transcribeUrl, getTask, serviceStatus, getTasks, transcribe

# Trulia :
from API.trulia import searching, propertyDetail

def encode(term): # URL Encoding
    return term.replace(" ", "%20")

# COST MONEY
# Category Prediction : Prints out catagories the text matches
from API.categoryPrediction import categoryPrediction

# Text Analyzer : Analyzes the contents of a URL
from API.textAnalyzer import contentExtract, namedExtract, partOfSpeech

# URL Intel :
from API.urlIntel import urlIntel

# Plate Recognition :
from API.plateRecognition import recognizeByUrl , recognizeByImage
### USES TRUE URL ENCODING

# OCRLY : URL Image to text
from API.OCRLY import OImage2Text

# Youtube Download : Download Youtube Video by VideoID
from API.youtubeDownload import downloadVideo

# Threat Detect :
from API.threatDetector import detectThreat
