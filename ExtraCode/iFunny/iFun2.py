import os, sys
import requests
import re
from lxml import html, etree
basePath = "downloads1/"

def downloadFile(AFileName):
    # extract file name from AFileName
    filename = AFileName.split("/")[-1] 
    # download image using GET
    rawImage = requests.get(AFileName, stream=True)
    # save the image recieved into the file
    with open(basePath + filename, 'wb') as fd:
        for chunk in rawImage.iter_content(chunk_size=1024):
            fd.write(chunk)
    return


def downloadingPage(webpageLink):
    # Get the original webpage html content
    page = requests.get(webpageLink)
    try:
#        print(page.text.index('content="https://img.ifunny.co/videos/'))
        startIndex = page.text.index('content="https://img.ifunny.co/videos/')
        substrinx = page.text[startIndex:]
        endIndex = substrinx.index(".mp4")
        substrinx = substrinx[9:endIndex + 4] # Url Link
        downloadFile(substrinx)    
        print(substrinx)
    except:
        print("Something fucked up with the webpage " + webpageLink)

def cleanLinks(filename):
    f = open(filename, "r")
    g = open("videos.txt", "w")
    lines = f.readlines()
    f.close()
    for line in lines:
        if "https://ifunny.co/video/" in line:
            g.write(line)
        else:
            g.flush()
    g.close()

def main():
    cleanLinks("funnyLinks.txt")
    # downloadingPage("https://ifunny.co/video/aYnpdvtO8")
    f = open("videos.txt", "r")
    lines = f.readlines()
    for line in lines:
        downloadingPage(line.strip())



def iFunny():
    testUrl = "https://ifunny.co/video/aYnpdvtO8"

    try:
        r = requests.get((testUrl), allow_redirects=True, headers=headers)
        
    except:
        print("Going to fast. Slowing Down")



"""    headers = {
        'authority': 'npnr.org',
        'method': 'GET',
        'path': extendUrl,
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'cookie': '__cfduid=d32854e1edac80db0fbc24174584bacb51611896395; __RequestVerificationToken=a2X5YPcosSAUPvLu5RY25dCKPpKmYQLxlFkbHgRbsOrtbUMVWn90_kH3WmeYH7EwZYmoq_izPar_5TVzoL7QFyPTIOyDaY1RmgNrs3jWRzU1',
        'pragma': 'no-cache',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
               }
               """
