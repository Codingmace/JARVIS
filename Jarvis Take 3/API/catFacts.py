import requests

def catFact(maxLength):
    url = "https://catfact.ninja/facts"
    if maxLength > 0:
        url += "?max_length=" + str(maxLength)    
        
    response = requests.request("GET", url)
    return response

def catFacts(numberFacts, maxLength):
    url = "https://catfact.ninja/facts?limit=" + str(numberFacts)
    if maxLength > 0:
        url += "&max_length=" + str(maxLength)    
        
    response = requests.request("GET", url)
    return response

print(catFact(-1).json()['data'][0]['fact'])
