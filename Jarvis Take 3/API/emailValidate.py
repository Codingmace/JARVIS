import requests
from variables import rapidApiKey

def validEmail(email):
    url = "https://email-validator8.p.rapidapi.com/api/v2.0/email"

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'x-rapidapi-key': rapidApiKey,
        'x-rapidapi-host': "email-validator8.p.rapidapi.com"
        }

    response = requests.request("POST", url, data=email, headers=headers)
    return response

"""
{"email":"masnathan@mail.com",
"valid":true,
"disposable":false,
"mx_records":true,
"exists":null}
"""
