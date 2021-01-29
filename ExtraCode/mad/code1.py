import os, sys
import requests
import re
import numpy as np
import time

def createUrl():
#    https://www.usphonebook.com/000-000-0001
    baseUrl = "https://npnr.org/"
    con = 0
    validArea = open("areaCodes.txt", "r")
    areaCodes = validArea.readlines()
    delays = [1, 2,3,4,5]
    validArea.close()
    goodNumb = open("goodNumbers.txt", "a")
    badNumb = open("badNumbers.txt","a")

#    for code in areaCodes:
    for code in range(817, 818):
        i = int(code)
#        fir = f"{i:03}"
        for j in range(681, 682):
            mid = f"{j:03}"
            for k in range(5833, 5845):
                end = f"{k:04}"
                # print(baseUrl + fir + "-" + mid + "-" + end + "")
                extendUrl = str(i) + "/" + str(mid) + "/" + str(end) + "/"+ str(i) + "" + str(mid) + "" + str(end) +""
                print(baseUrl + extendUrl  + ".html")
#                req = urllib.request.Request(url, method='GET')
                headers = {
'authority': 'npnr.org',
'method': 'GET',
'path': '/817/681/5833/8176815833.html',
'scheme': 'https',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
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
                r = requests.get((baseUrl + extendUrl), allow_redirects=True, headers=headers)
                print(len(r.content))
                open(str(i) + "" + str(mid) + "" + str(end) + '.html', 'wb').write(r.content)
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

createUrl()


