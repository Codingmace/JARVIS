import requests
import json
import time
# https://www.ftc.gov/developer

# testUrl = 'https://api.ftc.gov/v0/dnc-complaints?api_key=DEMO_KEY&created_date_from="2020-02-27 04:10:00"&created_date_to="2020-02-27 04:30:00"'
baseUrl = "https://api.ftc.gov/v0/dnc-complaints?api_key="
extendUrl = "offset="
apiDoc = open("APIKey.txt", "r")
apiKey = apiDoc.readline()
# apiKey = "1MIqfBRshPMveerYAHsjso0BMUuRFP2GwpfXLpfW"

### FOR UPDATING

# NEED TO REMOVE BECAUSE YOU CANNOT HAVE MORE THAN 1 VALID KEY AT A TIME

# Map States
states = ['']
abbr = ['']
with open('stateMap.txt','r') as map_file:
    a = map_file.readlines()

for line in a:
    split = line.split(" - ")
    states.append(split[0])
    abbr.append(split[1][:2])

# Map Subject
subject = ['']
corr = [''] # Correlation
with open('subjectMap.txt','r') as subject_file:
    a = subject_file.readlines()

for line in a:
    split = line.split(" - ")
    subject.append(split[0])
    corr.append(split[1].strip('\n'))

phoneMap = open("PhoneMap.txt", "a")
errors = open("log.txt","a") # Adjust to be correct folder and not override eachother

# Read in from the API
# for offset in range(7500,3186831, 50):
# for offset in range(9350,3186831, 50):
# for offset in range(9550,3186831, 50):
# for offset in range(11350,3186831, 50):
# for offset in range(13900,3186831, 50):
# for offset in range(14200,3186831, 50):
# for offset in range(14800,3186831, 50):
# for offset in range(16250,3186831, 50):
# for offset in range(16550,3186831, 50):
# for offset in range(19050,3186831, 50):
# for offset in range(21600,3186831, 50):
# for offset in range(21850,3186831, 50):
# for offset in range(24400,3186831, 50):
# for offset in range(26950,3186831, 50):
# for offset in range(29300,3186831, 50):
# for offset in range(31850,3186831, 50):
# for offset in range(34400,3186831, 50):
# for offset in range(36900,3186831, 50):
# for offset in range(37800,3186831, 50):
# for offset in range(42900,3186831, 50):
# for offset in range(45450,3186831, 50):
# for offset in range(47050,3186831, 50):
# for offset in range(47500,3186831, 50):
# for offset in range(47800,3186831, 50):
# for offset in range(50350,3186831, 50):
# for offset in range(52800,3186831, 50):
# for offset in range(55350,3186831, 50):
# for offset in range(56500,3186831, 50):
for offset in range(57850,3186831, 50):
    response = requests.get(baseUrl+apiKey + "&" + extendUrl + str(offset))

    if not (response.status_code == 200):
        print("We are out of responses. Ended on offset of " + str(offset))
        errors.write("Out of request, "+ str(offset) + "\n")
        errors.flush()
        errors.close()
        phoneMap.flush()
        phoneMap.close()
        exit()

    data = response.json()
    print(response.status_code)
    output = open(str("Data\output" + str((int)(offset / 50))+".json"), "w")
    # print(data)

# Parse Json
    del data['meta']
    del data['links']

    for element in data['data']:
        del element['type']
        del element['relationships']
        del element['meta']
        del element['links']

        element['number'] = element['attributes']['company-phone-number']
        element['date'] = element['attributes']['violation-date']
        tempSubject =  element['attributes']['subject'].replace("  ", " ")
       # element['subject'] = element['attributes']['subject'].replace("  ", " ")


# Modify so that we get the attributes Compressed
        if tempSubject in subject:
            tempSubject = corr[subject.index(tempSubject)]
        else: # If it is not mapped yet
            print(tempSubject)


        element['subject'] = tempSubject

        element['recorded-or-robo']= element['attributes']['recorded-message-or-robocall']
        element['city'] = element['attributes']['consumer-city']
        curState = element['attributes']['consumer-state']
        curAbbr = abbr[states.index(curState)]

        element['state'] = curAbbr
        element['area-code'] = element['attributes']['consumer-area-code']

        del element['attributes']
        temp = element['id'] + " " + element['number'] + "\n"
        phoneMap.write(temp)


    # Write it all to a file
    json.dump(data, output)
    phoneMap.flush()
    errors.flush()
    output.flush()
    output.close()
    time.sleep(90)

errors.close()
phoneMap.close()
