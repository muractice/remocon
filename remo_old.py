#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import json
import os
import time
import sys

hoge = input()
print(hoge)

token = os.environ["REMO_API_TOKEN"]
headers = {
'accept':'application/json',
'Authorization': 'Bearer ' + token
}


dictChannel = {
1:'725369f5-5f75-489e-aaab-3030c76b1656',
2:'94da9227-84f8-4af1-a9ae-d317e0bb9bc6',
4:'fa9763a0-5c5c-4010-a41e-bd6af7598e6d',
5:'21830228-9a61-4247-904d-69390bb2228d',
6:'4685d8e4-fc50-4a82-b42f-b12e68c9a06d',
7:'3939c448-eb28-4668-8bc4-8652ed59c65d',
8:'9f8e1113-f789-4563-ab76-7d84e507c765'
}

#def changeChannel(channel):
#    urlChangeChannel = 'https://api.nature.global/1/signals/'+channel+'/send'
#    res = requests.post(urlChangeChannel,headers=headers)

#channel = input("input recoding channel:")
#channel = 5
channel = input()

#changeChannel(dictChannel[int(channel)])
#urlChangeChannel = 'https://api.nature.global/1/signals/'+dictChannel[5]+'/send'
urlChangeChannel = 'https://api.nature.global/1/signals/'+dictChannel[int(channel)]+'/send'
res = requests.post(urlChangeChannel,headers=headers)

time.sleep(3)
urlRecoding = 'https://api.nature.global/1/signals/19c641cb-fec8-4b94-b3f2-dc3013f88584/send'
res = requests.post(urlRecoding,headers=headers)

time.sleep(1)
#urlDecison = 'https://api.nature.global/1/signals/90efd112-44b6-4da6-b123-e71cde96838a/send'
#res = requests.post(urlDecison,headers=headers)


"""
urlGet = 'https://api.nature.global/1/appliances'
response = requests.get(urlGet,headers=headers)
data = response.json()
jsonText = json.dumps(data,indent=4)
"""
