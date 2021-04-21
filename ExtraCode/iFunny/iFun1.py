import os, sys
import requests
import re







def dud():
    import urllib.request
    fid=urllib.request.urlopen('https://ifunny.co/video/aYnpdvtO8')
    webpage=fid.read().decode('utf-8')
    print(webpage)





def downloadFile(AFileName):
    # extract file name from AFileName
    filename = AFileName.split("/")[-1] 
    # download image using GET
    rawImage = requests.get(AFileName, stream=True)
    # save the image recieved into the file
    with open(filename, 'wb') as fd:
        for chunk in rawImage.iter_content(chunk_size=1024):
            fd.write(chunk)
    return


def downloadingPage(webpageLink):
    from lxml import html, etree
    import requests
    # Get the original webpage html content
#    webpageLink = 'http://www.howtowebscrape.com/examples/simplescrape1.html'
    page = requests.get(webpageLink)
#    downloadFile('http://www.howtowebscrape.com/examples/simplescrape1.html')
    # convert the data received into searchable HTML
    extractedHtml = html.fromstring(page.content)
#    f = open('testpage.html', 'w')
#    f.write(page.text)
    print(page.text.index('content="https://img.ifunny.co/videos/'))
    startIndex = page.text.index('content="https://img.ifunny.co/videos/')
    substrinx = page.text[startIndex:]
    endIndex = substrinx.index(".mp4")
    substrinx = substrinx[9:endIndex +4] # Url Link
    downloadFile(substrinx)    
    print(substrinx)
    input()
    # <meta property="og:video:secure_url" content="https://img.ifunny.co/videos/2973216916ceb2031a0fb4e1fe7467d647ef813d376a3b56438e1857be294e93_1.mp4"/>
    # content="https://img.ifunny.co/videos/2973216916ceb2031a0fb4e1fe7467d647ef813d376a3b56438e1857be294e93_1.mp4"/> 
#    f.flush()
#    f.close()
###    buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#    print(extractedHtml.xpath("/"))
    # use an XPath query to find the image link (the 'src' attribute of the 'img' tag).
    imageSrc = extractedHtml.xpath("/videos/@src") # in our example, result = ‘/images/GrokkingAlgorithms.jpg’
    # strip off the actual *page* being called as we only want to base url
    imageDomain = webpageLink.rsplit('/', 1) # in our example, result = http://www.howtowebscrape.com/examples/
    imageLink = ""
    for x in imageSrc:
        if "imageproxy" in x or "gif" in x:
            continue
            #print("not working")
        elif x.startswith("http"):
            imageLink = x
        else:
            imageLink = str(imageDomain[0]) + x
        print(imageLink)
    print(imageSrc)
#    print(extractedHtml)
#    print(page.text)
    # test if this is an absolute link or relative
    if imageSrc[0].startswith("http"):
        # start with http, therefore take this as the full link
        imageLink = imageSrc[0]
    else:
        # does not start with http, therefore construct the full url from the base url plus the absolute image link
        imageLink = str(imageDomain[0]) + str(imageSrc[0])
    print(imageLink)



#downloadingPage("")
downloadingPage("https://ifunny.co/video/aYnpdvtO8")




"""
from pywebcopy import save_webpage

url = 'https://ifunny.co/video/aYnpdvtO8'
download_folder = 'C:/Users/JMW180004/Documents/GitHub/JARVIS/ExtraCode/ifUnny/'    

kwargs = {'project_name': 'recognisable-name'}
while(True):
    try:
        save_webpage(url, download_folder, **kwargs)
    except:
        print("Something went wrong")
"""



def iFunny():
    testUrl = "https://ifunny.co/video/aYnpdvtO8"
#    baseUrl = "https://npnr.org/"
#    con = 0

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
