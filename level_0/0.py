#!/usr/bin/python3
import requests


payload = {'id': '1651', 'holdthedoor':'Submit'}
URL = 'http://158.69.76.135/level0.php'
votos = 0
while votos < 1024:
    r = requests.post(URL, payload)
    votos += 1
