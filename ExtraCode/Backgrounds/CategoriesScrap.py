import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
import time
import re

def getTitle(entry):
    split = entry.split("!")
    #print(len(split))
    #print(split)
    starts = split[1].strip().replace("title=\"","").replace("\">","")
    return starts.replace("wallpapers in","")

def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_images(url):
    """
    Returns all image URLs on a single `url`
    """

    response = requests.get(url).content

    ind = response.index(b'<h2><span>Recent Wallpapers by Our Community</span></h2>')
    response = response[0:ind]
#    print(response)
#    print(ind)
#    input()
#    soup = bs(requests.get(url).content, "html.parser")
    soup = bs(response, "html.parser")
    urls = []
    for img in tqdm(soup.find_all("img"), "Extracting images"):
        img_url = img.attrs.get("src")
        if not img_url:
            # if img does not contain src attribute, just skip
            continue
        # make the URL absolute by joining domain with the URL that is just extracted
        img_url = urljoin(url, img_url)
        # remove URLs like '/hsts-pixel.gif?c=3.2.5'
        try:
            pos = img_url.index("?")
            img_url = img_url[:pos]
        except ValueError:
            pass
        # finally, if the url is valid
        if is_valid(img_url):
            urls.append(img_url)
    return urls


def download(url, filename):
    """
    Downloads a file given an URL and puts it in the folder `pathname`
    """
    # download the body of response by chunk, not immediately
    response = requests.get(url, stream=True)

    # get the total file size
    file_size = int(response.headers.get("Content-Length", 0))
    vE = ["png", "gif", "jpg", "jpeg"]# Valid extensions
    goodFile = vE[0] in filename or vE[1] in filename or vE[2] in filename or vE[3] in filename
    if file_size > 20000 and goodFile: # Bigger than 20kb
        # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
        progress = tqdm(response.iter_content(1024), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)

        with open(filename, "wb") as f:
            for data in progress:
                # write data read to the file
                f.write(data)
                # update the progress bar manually
                progress.update(len(data))


def main(baseUrl, path):
    # get all images
    url = baseUrl
    try:
        imgs = get_all_images(url)
        for img in imgs:
            # for each img, download it
            download(img, path)
            time.sleep(1)
    except:
        print("The path ", url, " is done. Moving on")
        time.sleep(3)


if __name__ == "__main__":
    url = 'https://wallpapercave.com'
    categoriesUrl = url + '/categories/'
    categoriesList = ["Animals","Anime","Brands","Cars","Cartoons","Celebrities","Devices","Fortnite","Games","Geography","Holidays","Motor","Movies","Music","Nature","Other","Pokemon","Religion","Resolutions","Space","Sports","Superheroes","TV Shows"]
    categoriesSubDir = ["animals","anime","brands","cars","cartoons","celebrities","devices","fortnite","games","geography","holidays","motor","movies","music","nature","other","pokemon","religion","resolutions","space","sports","superheroes","tv-shows"]
    numberOfCategories = len(categoriesList)
    for i in range (0, numberOfCategories):
        print(str(i + 1) + ". " + categoriesList[i])

#    categorySelection = input("Select a category : ")
    categorySelection = 1
    selection = categoriesSubDir[categorySelection]
    filename = selection + ".html"
    download(categoriesUrl + selection, filename)
    startLine = "<h1>" + categoriesList[categorySelection] +" Wallpapers</h1>"
    endLine = "<script>"
    entries = []
    f = open(filename,"r")
    line = f.readline()
    while not (startLine in line):
        line = f.readline()
#           print(line)

    while not (startLine in line):
        line = f.readline()
    while not (endLine in line):
        if ("<a href=\"/" in line):
            line = line.replace(" class=\"albumthumbnail\" ","!")
            line = line.replace("<a href=","")
            entries.append(line)
        try:
            line = f.readline()
            #print(line)
        except:
            print("That line doesn't work.")

    entriesSize = len(entries)
    for i in range(0, entriesSize):
        print(str(i) + ". " + getTitle(entries[i]))

#    personSelection = int(input("Input the category you would like to download "))
    personSelection = 110
    if personSelection > entriesSize or personSelection < 0:
        print("That is not valid thus I will not continue")
    else:
        link = entries[personSelection].split("!")[0].replace("\"","")
        disInclude = ['comment.png','download.png','fav.png','instagram.png','logo.png','twitter.png']
#        print(link)
        imagesUrl = get_all_images(url + link)
        for iU in imagesUrl:
            validDownload = True
            for d in disInclude:
                if d in iU:
                    validDownload = False
#                    print(iU)                    
                    break
#            print(iU)
            if validDownload:
                newTitle = getTitle(entries[personSelection]).replace("Wallpapers","")
                newTitle = re.sub("[^a-zA-Z0-9 ]","",newTitle).strip()
#                print(newTitle) # NEED TO MAKE THE FOLDER
                ind = newTitle.index(" ")+2
                indr = iU.rindex("/")
                pathname = newTitle[ind::]
                if not os.path.isdir(pathname): # Creating folder if it doesn't exist
                    os.makedirs(pathname)
                try:
                    download(iU, (pathname + (iU[indr::])))
                except:
                    print("Something went wrong")
        print(imagesUrl)

#    main("https://wallpapercave.com/", "background-images")
