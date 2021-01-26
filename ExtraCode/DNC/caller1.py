import requests
import json
# https://www.ftc.gov/developer

testUrl = 'https://api.ftc.gov/v0/dnc-complaints?api_key=DEMO_KEY&created_date_from="2020-02-27 04:10:00"&created_date_to="2020-02-27 04:30:00"'
baseUrl = "https://api.ftc.gov/v0/dnc-complaints?api_key="
extendUrl = "offset=50"
apiDoc = open("APIKey.txt", "r")
apiKey = apiDoc.readline()

response = requests.get(baseUrl+apiKey + "&" + extendUrl)
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
