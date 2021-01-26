import requests
import json
# https://www.ftc.gov/developer

testUrl = 'https://api.ftc.gov/v0/dnc-complaints?api_key=DEMO_KEY&created_date_from="2020-02-27 04:10:00"&created_date_to="2020-02-27 04:30:00"'
baseUrl = "https://api.ftc.gov/v0/dnc-complaints?api_key="
extendUrl = "offset="
apiDoc = open("APIKey.txt", "r")
apiKey = apiDoc.readline()

fileNumb = 0

# for offset in range(0 ,3186831, 50):
for offset in range(0 ,300, 50):
    response = requests.get(baseUrl+apiKey + "&" + extendUrl + str(offset))
    data = response.json()
    
    output = open(str("output" + str(fileNumb)+".json"), "w")
    json.dump(data, output)
    output.flush()
    output.close()
    fileNumb += 1
# response = requests.get(testUrl)

print(response.status_code)
print(response.json())

data = response.json()


output = open("output2.json", "w")

#output.write(response.json())
json.dump(data, output)
output.close()


"""
with open('data.json', 'r') as data_file:
    data = json.load(data_file)

for element in data:
    element.pop('hours', None)

with open('data.json', 'w') as data_file:
    data = json.dump(data, data_file)
"""



# Parse JSON
import json

with open('output.json', 'r') as data_file:
    data = json.load(data_file)
    #print(data['data'])

del data['meta']
del data['links']

states = []
abbr = []
with open('stateMap.txt','r') as map_file:
    a = map_file.readlines()
for line in a:
    split = line.split(" - ")
    states.append(split[0])
    abbr.append(split[1][:2])


print(states)
print(abbr)
for element in data['data']:
    #print(element)
    del element['type']
    del element['relationships']
    del element['meta']
    del element['links']

    element['number'] = element['attributes']['company-phone-number']

    element['date'] = element['attributes']['violation-date']

    element['subject'] = element['attributes']['subject'].replace("  ", " ")

    element['recorded-or-robo']= element['attributes']['recorded-message-or-robocall']
    
    element['city'] = element['attributes']['consumer-city']
#    del element['attributes']['consumer-city']
    curState = element['attributes']['consumer-state']
    curAbbr = abbr[states.index(curState)]
    print(curAbbr)
    element['state'] = curAbbr
#    del element['attributes']['consumer-state']
    element['area-code'] = element['attributes']['consumer-area-code']
    del element['attributes']
#    del element['attributes']['consumer-area-code']
#    if 'data' in element:
#        for element2 in element:
#            print(element2)
#print(data['data']['id'])

with open('output2.json', 'w') as data_file:
    data = json.dump(data, data_file)

