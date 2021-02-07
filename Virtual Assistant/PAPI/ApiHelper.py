
from PAPI.openCam import findWebCamera
#from PAPI.quickstart import main

def gmailCleanup():
    print("This one is for google")

def imageCleanup():
    print("For compressing images")

def incrementCleanup():
    print("Turning zip into incremental Backups")

def trafficCamera(query):
    from PAPI.openCam import findWebCamera
    return findWebCamera(query)

def unique(query):
    from uniqueLines import lineSort, line
    if "sort" in query:
        query = query.replace("sort","")
        return lineSort(query)
    else:
        return line(query)


def phoneLookup(query):
    print("This is for the one that looks up phones")
    
