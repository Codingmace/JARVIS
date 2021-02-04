import requests
from variable import rapidApiKey

def downloadVideo(videoId):
    url = "https://youtube-to-mp32.p.rapidapi.com/yt_to_mp3"

    querystring = {"video_id":videoId}

    headers = {
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "youtube-to-mp32.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    if response['Status_Code'] == "200":
        return response['Download_url']
    else:
        return response['Warining']
