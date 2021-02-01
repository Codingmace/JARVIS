import requests
import json
import time
# https://www.ftc.gov/developer

def doNotCallList():
    baseUrl = "https://api.ftc.gov/v0/dnc-complaints?api_key="
    areaCode = "243"
    startDate = "2020-02-06"
    endDate  = "2020-02-27"
    createdStart = "created_date_from=" + startDate
    createdEnd = "created_date_to=" + endDate
    extendUrl = "offset="
    extendUrl2 = "area_code="'
    
    apiDoc = open("APIKey.txt", "r")
    apiKey = apiDoc.readline() # Fix this by getting more keys
    apiKey = "1MIqfBRshPMveerYAHsjso0BMUuRFP2GwpfXLpfW"
    # NEED TO REMOVE BECAUSE YOU CANNOT HAVE MORE THAN 1 VALID KEY AT A TIME

    errors = open("log.txt","a") # Adjust to be correct folder and not override eachother
    print("Check the logs first for something.")
    
    # Read in from the API
    
    for offset in range(0,200, 50):
        response = requests.get(baseUrl+apiKey + "&" + extendUrl + str(offset))

        if (response.status_code == 429):
        if (response.status_code == 404):            
        if (response.status_code == 403):
        if (response.status_code == 400):
        if not (response.status_code == 200):
            print("We are out of responses. Ended on offset of " + str(offset))
            errors.write("Out of request, "+ str(offset) + "\n")
            errors.flush()
            errors.close()
            exit()

        data = response.json()
        print(response.status_code)
        output = open(str("Data\output" + str((int)(offset / 50))+".json"), "w")
        print(data)

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
            temp = element['id'] + " " + element['number'] + "\n"


        # Write it all to a file
        json.dump(data, output)
        errors.flush()
        output.flush()
        output.close()
    #    time.sleep(90)

    errors.close()


def updateLogs():
    print("merge the Json data from each")
    print("Request as much as possible at that point")
