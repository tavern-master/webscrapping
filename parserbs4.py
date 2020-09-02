# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 17:36:17 2020

@author: hamel
"""


from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

my_domain = 'https://www.dalkos.ru'
my_url = 'https://www.dalkos.ru/catalog/avtomatika-i-elektronnye-komponenty/dzhojjstiki-operatora/djoystiki-bosch-rexroth/'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div",{"class":"favoriteProduct__row"})


firm_name = page_soup.findAll("h2")


filename = "products.csv"
f = open(filename, "w")

headers = "link; frima; title; contact\n"
#из далкоса взять контакты \лектронныу

f.write(headers)
links_array = []
for container in containers:
    link = container.div.div.a["href"]
    title = container.div.div.a.text
    f.write(my_domain + link + ";" + firm_name[0].text  + ";" + title.replace("|", "-") + "\n")
    links_array.append(my_domain+link)
    
f.close()
print(links_array)
    
# container = containers[0]
# print(container.div.div.a["href"])
# container.finAll("a", {"class":"", })