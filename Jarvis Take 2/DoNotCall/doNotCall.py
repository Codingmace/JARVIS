import requests
import json
import time
# https://www.ftc.gov/developer


def main():
    baseUrl = "https://api.ftc.gov/v0/dnc-complaints?api_key="
    extendUrl = "offset="
    extendUrl2 = "area_code="
    areaCode = "243"
    apiDoc = open("APIKey.txt", "r")
    apiKey = apiDoc.readline() # Fix this by getting more keys
    #apiKey = apiDoc.readline()
    apiKey = "1MIqfBRshPMveerYAHsjso0BMUuRFP2GwpfXLpfW"
    # NEED TO REMOVE BECAUSE YOU CANNOT HAVE MORE THAN 1 VALID KEY AT A TIME

    errors = open("log.txt","a") # Adjust to be correct folder and not override eachother

    # Read in from the API
    for offset in range(0,200, 50):
        response = requests.get(baseUrl+apiKey + "&" + extendUrl + str(offset))

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





def mergeJson():
    print("Started Reading JSON file")
    dex = []
    for i in range(0,20):
        try:
            with open(("Data\output" +str(i) + ".json"), "r") as read_file:
                print(i)
                developer = json.load(read_file)
                for x in developer['data']:
                    dex.append(x)
        except:
            print("the file " + str(i)+ "")

    # Turning dict to file
    with open('result.json', 'w') as fp:
        json.dump(dex, fp)
