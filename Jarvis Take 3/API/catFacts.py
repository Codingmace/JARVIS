import requests

def catFact(maxLength):
    url = "https://catfact.ninja/facts"
    if max_length > 0:
        url += "?max_length=" + str(maxLength)    
        
    response = requests.request("GET", url, headers=headers)
    return response

def catFacts(numberFacts, maxLength):
    url = "https://catfact.ninja/facts?limit=" + str(numberFacts)
    if max_length > 0:
        url += "&max_length=" + str(maxLength)    
        
    response = requests.request("GET", url, headers=headers)
    return response
