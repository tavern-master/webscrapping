# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 17:36:17 2020

@author: hamel
"""


from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

def parse_page(url):
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    return page_soup

            
my_domain = 'https://www.dalkos.ru'
my_url = 'https://www.dalkos.ru/catalog/'

catalog = parse_page(my_url)
catalog_divs = catalog.findAll("div", {"class": "categoreProduct__row__item"})
catalog_urls = catalog_divs.a["href"]

print(catalog_urls)

