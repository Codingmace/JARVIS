
def updateDatabase():
    print("Find out where left off")
    print("Look through the folder 'Days' and go from the furthest back")
    print("Once they are done combine all the files in the temp folder")
    print("for the last one and put that in 'base' folder")
    print("Continue to next file reading it in. If a key doesn't work cycle through")
    print("Cycle through all the keys and if needed throw error")
    print("If No files are in the folder, check the done folder for the most recent one")
    print("Go from that day and create the days up to it")
    print("run process over again")

def createDatabase():
    print("There is nothing. Do not run if files are in the folder.  Use as valid the user does want to restart")
    print("Go from the last day possible to now.")
    print("If invalid day ignore and reach current date")
    print("Write the day to a file and return the dates started and ended on")

def crushDatabase():
    print("This is to combine up to that point files.")
    print("Takes all the files in done and combines them.")

def cleanDatabase():
    print("Just want to clean up the database and catch up to current day")
    print("Updates to writting to current Day")
    print("Finishes up the temp folder")
    print("Get rid of invalid values which are....")
    print("If there is no number of if areacode does not match number")
    print("If areacode doesn't match, write it to another file") # Maybe write all infomration since we have the ID
