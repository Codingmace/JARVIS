import requests
import json
import os, sys
import re
import time

def createUrl():
    baseUrl = "https://api.telnyx.com/anonymous/v2/number_lookup/1"
    
    con = 0
    validArea = open("areaCodes.txt", "r")
    areaCodes = validArea.readlines()
    validArea.close()
    goodNumb = open("goodNumbers.txt", "a")

    for code in areaCodes:
        i = int(code)
        for j in range(843, 845):
            mid = f"{j:03}"
            for k in range(6427, 6500):
                end = f"{k:04}"

                numb = str(i) + str(mid) + str(end)
                
                r = requests.get(baseUrl + numb)
                carName = json.loads(r.content)['data']['carrier']['name']
                print(carName)
                if not(carName == ""):
                    goodNumb.write(numb + "\n")
                    print(goodNumb)
                con += 1
                time.sleep(1)
                if(con % 20 == 0):
                    goodNumb.flush()

    goodNumb.close()

    

createUrl()


