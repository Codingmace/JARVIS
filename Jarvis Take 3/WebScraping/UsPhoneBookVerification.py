import os, sys
import requests
import re

def USPhonebook():
    baseUrl = "https://www.usphonebook.com/"
    extendUrl = "100-200-2000"

    r = requests.get((baseUrl + extendUrl), allow_redirects=True, headers=headers)

    headers = {
    'authority': 'www.usphonebook.com',
    'path': '/'+extendUrl,
    'method': 'GET',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'cookie': '_pxhd=0b17d6e4da300c2e4e52cc763de4112d78f1a29c46bc72cd337c3d46429c6684:5c44fa40-61a3-11eb-a8cf-8d52630b620d; _gcl_au=1.1.193380554.1611863983; _ga=GA1.2.1729908157.1611863983; _gid=GA1.2.204002864.1611863983; _pxvid=5c44fa40-61a3-11eb-a8cf-8d52630b620d; laravel_session=eyJpdiI6InR4WndGVlRzczF5aitBcDk1b2k4RlE9PSIsInZhbHVlIjoidStZWVlBV0FKMzAzdVZxVHNFeUtHYlBxeTNUclpqSGtQSXNMNEwwTm1mbnM2b1U5eERFcXRCZVFjMTV0YnBuQSIsIm1hYyI6IjVmOGM2ZWIwMTcxZTk4YTVlZTQ5YmE3Y2Y4NTJhMGI1NGY4MzFhZTA0YWM2MjUzNTUwYmFmZmMyYWU4NGJjOWIifQ%3D%3D; _gat_UA-85194803-1=1; __gads=ID=7d9af765b447ca0f:T=1611874818:S=ALNI_Mbm8KK480R4wU7U5hnPSwru6UNRsA; _px2=eyJ1IjoiOTk1NzNmYjAtNjFiYy0xMWViLWI1N2MtYWY4ZmRmNTc3NjliIiwidiI6IjVjNDRmYTQwLTYxYTMtMTFlYi1hOGNmLThkNTI2MzBiNjIwZCIsInQiOjE2MTE4NzUxMjI3NDAsImgiOiJkNmFjMDIzMTc2MGM0NDQ2MDdkMzY5M2Q3NDIzNzg0N2Y1ZWE4ZmM0YTE4ZjMxZTM3NDNmZGFiNzU0ZTI2NjkwIn0=',
    'pragma': 'no-cache',
    'referer': 'https://www.usphonebook.com/',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4324.104 Safari/537.36',
    }
    print(len(r.content))
    open(extendUrl + '.html', 'wb').write(r.content)
    if(len(r.content)< 65000):
        print("That number is bad")
    else:
        print("That number is good")

USPhonebook()


