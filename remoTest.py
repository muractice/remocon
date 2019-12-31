#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import json
import os
import time
import sys

def execGetApi(url,headers):
    res = requests.get(url,headers=headers)
    print(res.url+":"+str(res.status_code))
    print(res.headers.get('X-Rate-Limit-Remaining'))
    return res

def executeSignalApi(signalKey,headers):
    url = 'https://api.nature.global/1/signals/'+signalKey+'/send'
    res = requests.post(url,headers=headers)
    print(res.url+":"+str(res.status_code))
    print(res.headers.get('X-Rate-Limit-Remaining'))
    return res
'''
    if res.status_code != 200:
        sys.exit("Error")
'''

def printResToJson(res):
    data = res.json()
    jsonText = json.dumps(data,indent=4)
    print(jsonText)

token = os.environ["REMO_API_TOKEN"]
headers = {
'accept':'application/json',
'Authorization': 'Bearer ' + token
}

hyojiSignal = '7bfd3bbb-5521-4bd5-9d44-90f17274298a'
res = executeSignalApi(hyojiSignal,headers)
if (res.status_code != 200):
    sys.exit()

url = 'https://api.nature.global//1/devices'
res = execGetApi(url,headers)
#res = requests.post(url,headers=headers)
if (res.status_code != 200):
    sys.exit("get error")
data = res.json()
jsonText = json.dumps(data,indent=4)
print(jsonText)

#printResToJson(res)

'''
urlRecoding = 'https://api.nature.global/1/signals/'+buttonKey+'/send'
res = requests.post(urlRecoding,headers=headers)
#print(res.headers)
print(res.url)
print(res.status_code)
print(res.headers.get('X-Rate-Limit-Remaining'))

data = res.json()
jsonText = json.dumps(data,indent=4)
print(jsonText)
'''


"""
urlGet = 'https://api.nature.global/1/appliances'
response = requests.get(urlGet,headers=headers)
data = response.json()
jsonText = json.dumps(data,indent=4)
"""
