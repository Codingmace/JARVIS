import os, sys
import requests
import re
import time

def createUrl():
    baseUrl = "https://npnr.org/"
    con = 0
    validArea = open("areaCodes1.txt", "r")
    areaCodes = validArea.readlines()
    validArea.close()
    goodNumb = open("goodNumbers.txt", "a")
    badNumb = open("badNumbers.txt","a")
    nonWork = open("Nonworking.txt", "a")
    for code in areaCodes:
        i = int(code)
        for j in range(0, 999):
            mid = f"{j:03}"
            extendUrl = str(i) + "/" + str(mid)
            headers = {
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
            try:
                r = requests.get((baseUrl + extendUrl), allow_redirects=True, headers=headers)
                if ("does not have a location" in str(r.content)):
                    badNumb.write(str(i) + "" + str(mid) + "\n")
                else:
#                        open("Data/"+ str(i) + "" + str(mid) + "" + '.html', 'wb').write(r.content)
                    goodNumb.write(str(i) + "" + str(mid) + "" + "\n")
                con += 1
                if(con % 20 == 0):
                    goodNumb.flush()
                    badNumb.flush()
                    nonWork.flush()
            except:
                nonWork.write(str(i)+""+str(mid)+""+"\n")
                print(str(i)+""+str(mid)+"")
                time.delay(60)
    goodNumb.close()
    badNumb.close()
    nonWork.close()
#        exit()

createUrl()
