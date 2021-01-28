import os
import sys
import datetime

def sleep():
    print("Going to sleep")
    sys.exit()

def shutdown(platform):
    print("Shutting down")
    if platform == "win32":
        os.system("shutdown /p /f")
    if platform == "linux" or "darwin" or "linux2":
        os.system("poweroff")


def screenshot(folderPath):
    from pyautogui import screenshot
    speak("Taking screenshot")
    img = pyautogui.screenshot()
    dirExist(folderPath)
    img.save(folderPath + '/screenshot ' + datetime.datetime.now().replace(microsecond=0)+ '.png')
    
def dirExist(folderPath):
    folderCheck = os.path.isdir(folderPath)
    if not folderCheck: # Make folder if it doesn't exist
        os.makedirs(folderPath)

def getTime(military):
    if military:
        return datetime.datetime.now().strftime("%H:%M:%S")
    hour = datetime.datetime.hour
    hour = datetime.datetime.minute
    hour = datetime.datetime.second
    extend = "AM"
    if hour > 12:
        hour -= 12
        extend = "PM"
    return str(hour + ":" + minute + ":" + second+ " " + extend)

def changeVoice(curVoice):
    if voiceId == 1:
        return 0
    elif voiceId == 0:
        return 1
    

def searchWiki(query):
    import wikipedia
    query = query.replace('wikipedia', '')
    results = wikipedia.summary(query, sentences=2)
    return results

## Need to do more to this
def diagnostics():
    usage = str(psutil.cpu_percent())
    battery = psutil.sensors_battery()
    
    return str("CPU is at " + usage + " and batter is at " + battery.percent)


