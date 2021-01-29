import requests

h = requests.get('https://npnr.org/201/000/0000/2010000000.html')
print(h.headers)
# print(h.headers['Content-Length'])