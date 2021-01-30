import os, sys
import requests
import re

def createUrl():
    baseUrl = "https://www.whitepages.com/phone/1-"
    extendUrl = "200-200-2000

    r = requests.get((baseUrl + extendUrl), allow_redirects=True)
    print(len(r.content))
    open(extendUrl + '.html', 'wb').write(r.content)
    if(len(r.content)< 65000):
        print("that is a bad number")
    else:
        print("That is a good number")


createUrl()


