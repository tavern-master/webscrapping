# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 17:20:42 2020

@author: hamel
"""


import re
import urllib.request
import urllib.parse

url = 'https://www.dalkos.ru/'
values = {'s':'basics',
          'submit':'search'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

listings = re.findall(r'<li>(.*?)</>', str(respData))

for eachLi in listings: 
    print(eachLi)