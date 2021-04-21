import requests
#from lxml import html, etree
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
    f = open("videos.txt", "r")
    h = open("written.txt","w")
    lines = f.readlines()
    f.close()
    for line in lines:
        downloadingPage(line.strip())
        h.write(line)
        h.flush()
    h.close()


main()
