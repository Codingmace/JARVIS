import webbrowser

def openCamera(state):
    f = open("stateMap.txt", "r")
    lines = f.readlines()
    stateList = []
    linkList = []
    for line in lines:
        split = line.split(" - ")
        stateList.append(split[0].strip().lower())
        linkList.append(split[1].strip())
    if state in stateList:
        ind = stateList.index(state)
        return linkList[ind]
    else:
        return "NONE"



def findWebCamera(state):
    state = state.lower()
    cameraLink = openCamera(state)
    if "NONE" in cameraLink:
        return state + " is not a valid state")
    else:
        webbrowser.open(cameraLink)
        return "I have opened up " + state + " cameras"

