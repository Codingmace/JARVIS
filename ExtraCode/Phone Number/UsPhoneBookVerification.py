import os, sys
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import re
import urllib
import numpy as np
import time

def savePage(url, pagefilename='page'):
    def soupfindnSave(pagefolder, tag2find='img', inner='src'):
        """saves on specified `pagefolder` all tag2find objects"""
        if not os.path.exists(pagefolder): # create only once
            os.mkdir(pagefolder)
        for res in soup.findAll(tag2find):   # images, css, etc..
            try:         
                if not res.has_attr(inner): # check if inner tag (file object) exists
                    continue # may or may not exist
                filename = re.sub('\W+', '', os.path.basename(res[inner])) # clean special chars
                fileurl = urljoin(url, res.get(inner))
                filepath = os.path.join(pagefolder, filename)
                # rename html ref so can move html and folder of files anywhere
                res[inner] = os.path.join(os.path.basename(pagefolder), filename)
                if not os.path.isfile(filepath): # was not downloaded
                    with open(filepath, 'wb') as file:
                        filebin = session.get(fileurl)
                        file.write(filebin.content)
            except Exception as exc:
                print(exc, file=sys.stderr)
        return soup
    
    session = requests.Session()
    #... whatever other requests config you need here
    response = session.get(url)
    soup = BeautifulSoup(response.text, features="html.parser")
    pagefolder = pagefilename+'_files' # page contents
    soup = soupfindnSave(pagefolder, 'img', 'src')
    soup = soupfindnSave(pagefolder, 'link', 'href')
    soup = soupfindnSave(pagefolder, 'script', 'src')
    with open(pagefilename+'.html', 'wb') as file:
        file.write(soup.prettify('utf-8'))
    return soup

def getHeader(urlExtend):
    pathU= "\'/" + urlExtend + "\'" 
    headers = {
    'authority': 'www.usphonebook.com',
    'path': '/214-844-6427',
    'method': 'GET',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'cookie': '_pxhd=0b17d6e4da300c2e4e52cc763de4112d78f1a29c46bc72cd337c3d46429c6684:5c44fa40-61a3-11eb-a8cf-8d52630b620d; _gcl_au=1.1.193380554.1611863983; _ga=GA1.2.1729908157.1611863983; _gid=GA1.2.204002864.1611863983; _pxvid=5c44fa40-61a3-11eb-a8cf-8d52630b620d; laravel_session=eyJpdiI6InR4WndGVlRzczF5aitBcDk1b2k4RlE9PSIsInZhbHVlIjoidStZWVlBV0FKMzAzdVZxVHNFeUtHYlBxeTNUclpqSGtQSXNMNEwwTm1mbnM2b1U5eERFcXRCZVFjMTV0YnBuQSIsIm1hYyI6IjVmOGM2ZWIwMTcxZTk4YTVlZTQ5YmE3Y2Y4NTJhMGI1NGY4MzFhZTA0YWM2MjUzNTUwYmFmZmMyYWU4NGJjOWIifQ%3D%3D; _gat_UA-85194803-1=1; __gads=ID=7d9af765b447ca0f:T=1611874818:S=ALNI_Mbm8KK480R4wU7U5hnPSwru6UNRsA; _px2=eyJ1IjoiOTk1NzNmYjAtNjFiYy0xMWViLWI1N2MtYWY4ZmRmNTc3NjliIiwidiI6IjVjNDRmYTQwLTYxYTMtMTFlYi1hOGNmLThkNTI2MzBiNjIwZCIsInQiOjE2MTE4NzUxMjI3NDAsImgiOiJkNmFjMDIzMTc2MGM0NDQ2MDdkMzY5M2Q3NDIzNzg0N2Y1ZWE4ZmM0YTE4ZjMxZTM3NDNmZGFiNzU0ZTI2NjkwIn0=',
    'pragma': 'no-cache',
    'referer': 'https://www.usphonebook.com/',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
    }


def createUrl():
#    https://www.usphonebook.com/000-000-0001
    baseUrl = "https://www.usphonebook.com/"
    con = 0
    validArea = open("areaCodes.txt", "r")
    areaCodes = validArea.readlines()
    delays = [1, 2,3,4,5]
    validArea.close()
    goodNumb = open("goodNumbers.txt", "a")
    badNumb = open("badNumbers.txt","a")
#    print('%3.0x-%3.0f-%3.0f' % (loc,mid,end))
    for code in areaCodes:
        i = int(code)
        fir = f"{i:03}"
        for j in range(000, 999):
            mid = f"{j:03}"
            for k in range(0000, 9999):
                end = f"{k:04}"
                # print(baseUrl + fir + "-" + mid + "-" + end + "")
                extendUrl = str(i) + "-" + str(j) + "-" + str(k)
                print(baseUrl + extendUrl)
#                req = urllib.request.Request(url, method='GET')
                headers = {
    'authority': 'www.usphonebook.com',
    'path': '/'+extendUrl,
    'method': 'GET',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'cookie': '_pxhd=0b17d6e4da300c2e4e52cc763de4112d78f1a29c46bc72cd337c3d46429c6684:5c44fa40-61a3-11eb-a8cf-8d52630b620d; _gcl_au=1.1.193380554.1611863983; _ga=GA1.2.1729908157.1611863983; _gid=GA1.2.204002864.1611863983; _pxvid=5c44fa40-61a3-11eb-a8cf-8d52630b620d; laravel_session=eyJpdiI6InR4WndGVlRzczF5aitBcDk1b2k4RlE9PSIsInZhbHVlIjoidStZWVlBV0FKMzAzdVZxVHNFeUtHYlBxeTNUclpqSGtQSXNMNEwwTm1mbnM2b1U5eERFcXRCZVFjMTV0YnBuQSIsIm1hYyI6IjVmOGM2ZWIwMTcxZTk4YTVlZTQ5YmE3Y2Y4NTJhMGI1NGY4MzFhZTA0YWM2MjUzNTUwYmFmZmMyYWU4NGJjOWIifQ%3D%3D; _gat_UA-85194803-1=1; __gads=ID=7d9af765b447ca0f:T=1611874818:S=ALNI_Mbm8KK480R4wU7U5hnPSwru6UNRsA; _px2=eyJ1IjoiOTk1NzNmYjAtNjFiYy0xMWViLWI1N2MtYWY4ZmRmNTc3NjliIiwidiI6IjVjNDRmYTQwLTYxYTMtMTFlYi1hOGNmLThkNTI2MzBiNjIwZCIsInQiOjE2MTE4NzUxMjI3NDAsImgiOiJkNmFjMDIzMTc2MGM0NDQ2MDdkMzY5M2Q3NDIzNzg0N2Y1ZWE4ZmM0YTE4ZjMxZTM3NDNmZGFiNzU0ZTI2NjkwIn0=',
    'pragma': 'no-cache',
    'referer': 'https://www.usphonebook.com/',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
    }
                r = requests.get((baseUrl + extendUrl), allow_redirects=True, headers=headers)
                print(len(r.content))
                open(extendUrl + '.html', 'wb').write(r.content)
                if(len(r.content)< 65000):
                    badNumb.write(extendUrl + "\n")
                else:
                    goodNumb.write(extendUrl + "\n")
                con += 1
                delay = np.random.choice(delays)
                time.sleep(delay)
                if(con % 20 == 0):
                    goodNumb.flush()
                    badNumb.flush()

    goodNumb.close()
    badNumb.close()

#url = 'https://www.usphonebook.com/972-898-8473'





def main1():
    req = urllib.request.Request("https://www.usphonebook.com/", method='HEAD')
    f = urllib.request.urlopen(req)
    print(f.status)
    print(f.headers['Content-Length'])

    
# savePage("https://www.cs.unm.edu/~rudym/Running+Quagga+On+Ubuntu+16.04.html")
createUrl()


