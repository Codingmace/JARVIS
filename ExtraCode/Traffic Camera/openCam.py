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



def main(state):
    state = state.lower()
    if state == "none":
        state = input("Input the state you would like to access")
    cameraLink = openCamera(state)
    if "NONE" in cameraLink:
        print(state + " is not a valid state")
    else:
        webbrowser.open(cameraLink)

main("Texas2")
