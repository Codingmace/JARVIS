import requests
from variables import rapidApiKey

class Trulia():
    def __init__(self):
	self.city = "frisco"
	self.state = "texas"
	self.pageNum = str(1)
        self.propertyUrl = "https%3A%2F%2Fwww.trulia.com%2Fp%2Fny%2Fnew-york%2F150-central-park-s-new-york-ny-10019--689699"
        
    def searching(self):
        url = "https://trulia1.p.rapidapi.com/search"
	payload = "city="+ self.city + "&state_code=" + self.state + "&page=" + self.pageNum
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "trulia1.p.rapidapi.com"
            }

        response = requests.request("POST", url, data=payload, headers=headers)
        return response

# Not going to work because I don't know the property to put in the payload
    def propertyDetail(self):
        url = "https://trulia1.p.rapidapi.com/property"

        payload = "property_url=" + self.propertyUrl
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'x-rapidapi-key': rapidApiKey,
            'x-rapidapi-host': "trulia1.p.rapidapi.com"
            }

        response = requests.request("POST", url, data=payload, headers=headers)
        return response
