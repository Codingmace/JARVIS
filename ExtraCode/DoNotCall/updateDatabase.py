import datetime
import os

def updateDatabase():
    leftOff = open("Base/leftOff.txt", "r")
    leaving = leftOff.readlines()
    if leaving == "": # Finished
        print("We are now going to build from the lastDate till today")
        lastDate = open("Done/lastDate.txt", "r")
        goFrom = lastDate.readline()
        lastDate.close()
        print("Have to turn goFrom to a valid Date")
        
    else:
        print("Parse the date of leaving and continue from there")
    
    print("Move on to finishing/creating the temp folder")
    
    print("Find out where left off")
    print("Look through the folder 'Days' and go from the furthest back")
    print("Once they are done combine all the files in the temp folder")
    print("for the last one and put that in 'base' folder")
    print("Continue to next file reading it in. If a key doesn't work cycle through")
    print("Cycle through all the keys and if needed throw error")
    print("If No files are in the folder, check the done folder for the most recent one")
    print("Go from that day and create the days up to it")
    print("run process over again")

def createDatabase(dncApiKey):
    baseUrl = "https://api.ftc.gov/v0/dnc-complaints?api_key="
    os.makedir("Done") # Creating needed files
    os.makedirs("Base/temp/")
    print("We are grabbing the days all the way back to February 14, 2020")
    offset = 0
    currentDay = datetime.today()
    curDay = open("Done/lastDate.txt", "w") # Last date updated
    curDay.write(currentDat.strftime("%Y-%m-%d"))
    curDay.flush()
    curDay.close()
    moreDays = True
    while moreDays:
        d = currentDay - timedelta(days=offset)
        form = d.strftime("%Y-%m-%d")
        response = requests.get(baseUrl + dncApiKey + "&created_date=\"" + form + "\"")
        if form == "2020-02-14":
            moreDays = False
        if (response.status_code == 429):
            print("Rate has been exceeded")
        elif (response.status_code == 404):
            print("API server cannot be reached")
        elif (response.status_code == 403):
            print("Api key missing or invalid")
        elif (response.status_code == 400):
            print("URL Does not use HTTPS:")
        if not (response.status_code == 200):
            leftOff = open("Base/leftOff.txt" , "w") # Left off when going backwards
            leftOff.write(form)
            leftOff.flush()
            leftOff.close()
            print("Exiting at " + form)
            input("Press any key to close")
            exit()
        # Got successful information
        data = response.json()
        if data['meta']['record-total'] == 0:
            print("the day is invalid but still recorded. Skip")
            break
        output = open(str("Base\\" +form +".json"), "w")

        # Parse Json
        del data['meta']
        del data['links']
        for element in data['data']:
            del element['type']
            del element['relationships']
            del element['meta']
            del element['links']
            element['number'] = element['attributes']['company-phone-number']
            element['area-code'] = element['attributes']['consumer-area-code']
            del element['attributes']

        # Write it all to a file
        json.dump(data, output)
        output.flush()
        output.close()
    

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



print(os.listdir("Data/"))
# createDatabase("DNCKEY")
