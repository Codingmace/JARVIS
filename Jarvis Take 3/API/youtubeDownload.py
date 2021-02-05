import requests
from variables import rapidApiKey
import json

def downloadVideo(videoId):
    url = "https://youtube-to-mp32.p.rapidapi.com/yt_to_mp3"

    querystring = {"video_id":videoId}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "youtube-to-mp32.p.rapidapi.com"
        }

    response1 = requests.request("GET", url, headers=headers, params=querystring)
#    print(response.text)
    response = response1.json()
    if response['Status'] == "Success":
        return response['Download_url']
    else:
        return response1.text
#        return response['Warning']
