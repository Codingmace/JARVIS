#import urllib
#import re
#from urllib2 import urlopen

print("we will try to open this url, in order to get IP Address")

"""
url = "http://checkip.dyndns.org"

print(url)

request = urllib.requests.urlopen(url).read()

theIP = re.findall(r"d{1,3}.d{1,3}.d{1,3}.d{1,3}", request)

print("your IP Address is: ",  theIP)
"""

import requests

public_IP = requests.get("https://www.wikipedia.org").headers["X-Client-IP"]
print(public_IP)

#print(requests.get('http://ip.42.pl/raw').text)
"""
my_ip = urllib.urlopen('http://ip.42.pl/raw').read()
print(my_ip)
"""
