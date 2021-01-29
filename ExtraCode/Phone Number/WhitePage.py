import os, sys
import requests
import re
import numpy as np
import time

def createUrl():
    baseUrl = "https://www.whitepages.com/phone/1-"
    con = 0
    validArea = open("areaCodes.txt", "r")
    areaCodes = validArea.readlines()
    delays = [1, 2,3,4,5]
    validArea.close()
    goodNumb = open("goodNumbers.txt", "a")
    badNumb = open("badNumbers.txt","a")

    for code in areaCodes:
        i = int(code)
#        fir = f"{i:03}"
        for j in range(000, 999):
            mid = f"{j:03}"
            for k in range(0000, 9999):
                end = f"{k:04}"
                # print(baseUrl + fir + "-" + mid + "-" + end + "")
                extendUrl = str(i) + "-" + str(mid) + "-" + str(end)
                print(baseUrl + extendUrl)
#                req = urllib.request.Request(url, method='GET')
                
                r = requests.get((baseUrl + extendUrl), allow_redirects=True)
                print(len(r.content))
                open(extendUrl + '.html', 'wb').write(r.content)
                if(len(r.content)< 65000):
                    badNumb.write(extendUrl + "\n")
                else:
                    goodNumb.write(extendUrl + "\n")
                con += 1
                delay = np.random.choice(delays)
                time.sleep(delay)
                if (con > 1):
                    exit()
                if(con % 20 == 0):
                    goodNumb.flush()
                    badNumb.flush()

    goodNumb.close()
    badNumb.close()

# "https://api.telnyx.com/anonymous/v2/number_lookup/1426930512"


    

createUrl()


