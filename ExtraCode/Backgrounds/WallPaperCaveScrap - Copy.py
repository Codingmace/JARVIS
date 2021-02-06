import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
# from time import sleep
import hashlib
from send2trash import send2trash


""" Checks that the url is valid """
def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

""" Returns all the images from the url """
def get_all_images(url):
    soup = bs(requests.get(url).content, "html.parser")
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
    del soup
    return urls


""" Downloads the URL into the folder 'pathname' """
def download(url, pathname):
    if not os.path.isdir(pathname): # Creating folder if it doesn't exist
        os.makedirs(pathname)
    # download the body of response by chunk, not immediately
    response = requests.get(url, stream=True)

    # get the total file size
    file_size = int(response.headers.get("Content-Length", 0))

    # get the file name
    filename = os.path.join(pathname, url.split("/")[-1])

    vE = ["png", "gif", "jpg", "jpeg"]# Valid extensions
    goodFile = vE[0] in filename or vE[1] in filename or vE[2] in filename or vE[3] in filename
    if file_size > 1000000 and goodFile: # Bigger than 16kb
        # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
        progress = tqdm(response.iter_content(1024))
        with open(filename, "wb") as f:
            for data in progress:
                # write data read to the file
                f.write(data)
                # update the progress bar manually
                progress.update(len(data))
        del progress



def hashFile(filename):
    hasher = hashlib.md5()
    with open(filename, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()


def paths(path):
    #we shall store all the file names in this list
    filelist = []

    for root, dirs, files in os.walk(path):
            for file in files:
            #append the file name to the list
                    filelist.append(os.path.join(root,file))
    return filelist

def fileSize(path):
    with open(path, 'r') as f:
        size = f.seek(0, os.SEEK_END)
        return size


def cleanup(path):
    print("Cleaning up")
    ar = paths(path)
    fileList = []
    for name in ar:
        curStr = str(hashFile(name))+ str(fileSize(name))
        if curStr in fileList:
            send2trash(name)
        else:
            fileList.append(curStr)




def main(url, path):
    # get all images
    try:
        imgs = get_all_images(url)
        for img in imgs:
            # for each img, download it
            download(img, path)
    except:
        print("The path ", url, " is done. Moving on")
 #       time.sleep(1)


if __name__ == "__main__":
    """ BRUTE FORCE WALLPaper CAVE"""
    baseUrl = 'https://wallpapercave.com/w/uwp'
    for i in range(98835, 490000, 1):
#    for i in range(66800, 490000, 1):
        if i % 100 == 99:
            # Cleanup
            print("Cleaning Up Folder " + str((int) (i/100)))
            cleanup("brute-force/" + str((int)(i/100)))

        main(baseUrl + str(i),"brute-force/" + str((int)(i / 100)) + "/" + str(i))
