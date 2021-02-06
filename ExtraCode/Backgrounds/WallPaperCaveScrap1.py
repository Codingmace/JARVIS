import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
from time import sleep
#import time

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
    return urls


def download(url, pathname):
    """
    Downloads a file given an URL and puts it in the folder `pathname`
    """
    # if path doesn't exist, make that path dir
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    # download the body of response by chunk, not immediately
    response = requests.get(url, stream=True)

    # get the total file size
    file_size = int(response.headers.get("Content-Length", 0))

    # get the file name
    filename = os.path.join(pathname, url.split("/")[-1])

    print(file_size, " ", filename)

    # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
    progress = tqdm(response.iter_content(1024))
    with open(filename, "wb") as f:
        for data in progress:
            # write data read to the file
            f.write(data)
            # update the progress bar manually
#            progress.update(len(data))


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
    for i in range(11027, 11028, 1):
    #for i in range(11027, 490000, 1):
#    for i in range(9234, 490000, 1):
#    for i in range(1012, 1013, 1):
        main(baseUrl + str(i),"brute-force1/" + str(i))
