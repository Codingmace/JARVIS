import requests

def validEmail(email):
    url = "https://email-validator8.p.rapidapi.com/api/v2.0/email"

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'x-rapidapi-key': "8614ca8be7msh26e5b0d5c58e075p134f84jsn178e24818b36",
        'x-rapidapi-host': "email-validator8.p.rapidapi.com"
        }

    response = requests.request("POST", url, data=email, headers=headers)

    print(response.text)

"""
{"email":"masnathan@mail.com",
"valid":true,
"disposable":false,
"mx_records":true,
"exists":null}
"""
