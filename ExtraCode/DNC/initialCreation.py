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
