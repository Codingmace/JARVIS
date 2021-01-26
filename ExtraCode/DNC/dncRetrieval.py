import requests
import json
# https://www.ftc.gov/developer

testUrl = 'https://api.ftc.gov/v0/dnc-complaints?api_key=DEMO_KEY&created_date_from="2020-02-27 04:10:00"&created_date_to="2020-02-27 04:30:00"'
baseUrl = "https://api.ftc.gov/v0/dnc-complaints?api_key="
extendUrl = "offset="
apiDoc = open("APIKey.txt", "r")
apiKey = apiDoc.readline()

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
    corr.append(split[1])
#print(subject)

# Read in from the API
# for offset in range(0 ,3186831, 50):
for offset in range(1900 ,6000, 50):
    response = requests.get(baseUrl+apiKey + "&" + extendUrl + str(offset))
    data = response.json()
    output = open(str("Data\output" + str((int)(offset / 50))+".json"), "w")

#    print(data)
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

#        print(tempSubject)
# Modify so that we get the attributes Compressed
        if tempSubject in subject:
#            print(subject.index(tempSubject))
            tempSubject = corr[subject.index(tempSubject)]
#            print(tempSubject)
        else:
            print(tempSubject)

        
        element['subject'] = tempSubject
        
        element['recorded-or-robo']= element['attributes']['recorded-message-or-robocall']
        element['city'] = element['attributes']['consumer-city']
        curState = element['attributes']['consumer-state']
        curAbbr = abbr[states.index(curState)]
        
        element['state'] = curAbbr
        element['area-code'] = element['attributes']['consumer-area-code']

        del element['attributes']
        
    # Write it all to a file
    json.dump(data, output)
    output.flush()
    output.close()



