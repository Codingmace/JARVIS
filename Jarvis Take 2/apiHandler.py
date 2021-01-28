## This is to help with importing the API only when needed
## Will read in all the keys here though

global rapidApiKey = "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36"

# Urban Dictionary : To define words
def wordDefinition(word):
    from urbanDictionary import defineWord
    return defineWord(word,rapidApiKey)


# Google Search : Look up things on google

from googleSearch import search, images, crawl, news

def encode(term):
    return term.replace("+", "%2B").replace(" ", "+")

# Revese Image : Google Reverse Image Search
from reverseImage import reverseImage


# Open Weather : Reports back the weather
""" NEEDS: have to sort out how I am going to do location """
from openWeather import *

# Weather.com : Reports back weather
""" Just Need Geocode """
from weatherCom import *

# Open Proxy : Reports all open proxies at that moment
from openProxies import openProxy

# Cat Facts : Returns random cat facts
from catFacts import catFact

# Test : To grab text, identify parts of speech, identify name of entities
from testTextHelp import fetchText, pos, namedEntity

# Email Validate : Check if email is vali or not
from emailValidate import validEmail

# Summarize API : Summarize the text of a URL link
from summarizeApi import summarize

# Verifone : Verifies a phone is valid (Default Country is US)
from veriphone import verifyPhone

# Pose Estimate : Takes a photo or video and estimates the posture
from poseEstimate import video, image

# Transcribe : Turns audio into text
from trascribe import transcribeUrl, getTask, serviceStatus, getTasks, transcribe

# Trulia : 
from trulia import searching, propertyDetail

def encode(term): # URL Encoding
    return term.replace(" ", "%20")

# COST MONEY
# Category Prediction : Prints out catagories the text matches
from categoryPrediction import categoryPrediction

# Text Analyzer : Analyzes the contents of a URL
from textAnalyzer import contentExtract, namedExtract, partOfSpeech

# URL Intel :
from urlIntel import urlIntel

# Plate Recognition :
from plateRecognition import recognizeByUrl , recognizeByImage
### USES TRUE URL ENCODING

# OCRLY : URL Image to text
from OCRLY import OImage2Text

# Youtube Download : Download Youtube Video by VideoID
from youtubeDownload import downloadVideo




