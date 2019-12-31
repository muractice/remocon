#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import json
import os
import time
import sys

def executeSignalApi(signalKey,headers):
    url = 'https://api.nature.global/1/signals/'+signalKey+'/send'
    res = requests.post(url,headers=headers)
    print(res.url+":"+str(res.status_code))
    print(res.headers.get('X-Rate-Limit-Remaining'))
    return res

token = os.environ["REMO_API_TOKEN"]
headers = {
'accept':'application/json',
'Authorization': 'Bearer ' + token
}

signalChannel = {
1:'725369f5-5f75-489e-aaab-3030c76b1656',
2:'94da9227-84f8-4af1-a9ae-d317e0bb9bc6',
4:'fa9763a0-5c5c-4010-a41e-bd6af7598e6d',
5:'21830228-9a61-4247-904d-69390bb2228d',
6:'4685d8e4-fc50-4a82-b42f-b12e68c9a06d',
7:'3939c448-eb28-4668-8bc4-8652ed59c65d',
8:'9f8e1113-f789-4563-ab76-7d84e507c765'
}

urlBoot = 'https://api.nature.global/1/signals/496ec97f-c627-4cba-be68-444cb3751789/send'
res = requests.post(urlBoot,headers=headers)
if (res.status_code != 200):
    sys.exit("boot error")

time.sleep(10)
channel = sys.argv[1]
urlChangeChannel = 'https://api.nature.global/1/signals/'+signalChannel[int(channel)]+'/send'
res = requests.post(urlChangeChannel,headers=headers)
if (res.status_code != 200):
    sys.exit("change channel error")

time.sleep(3)
urlRecoding = 'https://api.nature.global/1/signals/19c641cb-fec8-4b94-b3f2-dc3013f88584/send'
res = requests.post(urlRecoding,headers=headers)
if (res.status_code != 200):
    sys.exit("recoding error")

time.sleep(1)
urlDecision = 'https://api.nature.global/1/signals/90efd112-44b6-4da6-b123-e71cde96838a/send'
res = requests.post(urlDecision,headers=headers)
if (res.status_code != 200):
    sys.exit("decision error")

print("Done")
