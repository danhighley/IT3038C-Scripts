from bs4 import BeautifulSoup
import requests, re

data = requests.get("https://www.reebok.com/p/100045716/reebok-flexagon-energy-3-shoes-preschool").content
soup = BeautifulSoup(data, 'html.parser')
span = soup.find("h1", {"class":"tag_h1_light--2sTWu product-wrapper-title--1ky4m"})
title = span.text
print(title)
span = soup.find("p", {"class":"tag_p--1xo5V product-price-sale--22JTh"})
price = span.text
print("Item %s has price %s" % (title, price))