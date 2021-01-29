import os, sys
import requests
import re
import numpy as np
import time

def createUrl():
    validArea = open("areaCodes.txt", "r")
    areaCodes = validArea.readlines()
    validArea.close()
    numbers = open("allNumbers.txt","w")
    for code in areaCodes:
        i = int(code)
        for j in range(000, 999):
            mid = f"{j:03}"
            for k in range(0000, 9999):
                end = f"{k:04}"
                extendUrl = str(i) + "-" + str(mid) + "-" + str(end)
                #print(extendUrl)
                numbers.write(extendUrl + "\n")
        print(str(code))
        numbers.flush()
    numbers.close()


    

createUrl()


