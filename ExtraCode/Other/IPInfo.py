import requests
import json

url = "https://find-any-ip-address-or-domain-location-world-wide.p.rapidapi.com/iplocation"

querystring = {"apikey":"873dbe322aea47f89dcf729dcc8f60e8"}

headers = {
    'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
    'x-rapidapi-host': "find-any-ip-address-or-domain-location-world-wide.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
dataResponse = response.json()

# Needed Data
neededData = ['zipCode', 'accuracyRadius','city','timezone','latitude','longitude','ip','stateCode','status']
importantData = []

for data in neededData:
    importantData.append(dataResponse[data])

print(neededData)
print(importantData)
"""zipCode = data['zipCode']
radius = data['accuracyRadius']



{"zipCode":"75071"
"accuracyRadius":10
"city":"McKinney"
"timezone":"America/Chicago"
"latitude":33.1974
"longitude":-96.6177
"ip":"45.16.197.205"
"stateCode":"TX"
"status":200}
"""
