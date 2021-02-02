import requests
from variables import rapidApiKey

class YoutubeDownload():
    def __init__(self):
        self.id = videoId
        
    def downloadVideo(self):
        url = "https://youtube-to-mp32.p.rapidapi.com/yt_to_mp3"

        querystring = {"video_id": self.id}

        headers = {
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "youtube-to-mp32.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        if response['Status_Code'] == "200":
            return response['Download_url']
        else:
            return response['Warining']
