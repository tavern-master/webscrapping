# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 19:23:09 2020

@author: hamel
"""


import urllib.request
import urllib.parse

url = 'https://www.dalkos.ru/catalog/'
values = {'catalog/': ''}

data = urllib.parse.urlencode(values)
print("urlencode - " + data)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)