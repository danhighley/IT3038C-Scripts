from bs4 import BeautifulSoup
import requests, re

data = requests.get("https://www.nike.com/t/air-force-1-07-pro-tech-mens-shoes-GG5zvd/FB8875-001").content
soup = BeautifulSoup(data, 'html.parser')
span = soup.find("h1", {"class":"headline-2 css-16cqcdq"})
title = span.text
span = soup.find("div", {"class":"product-price"})
price = span.text
print()
print("Item %s has price %s" % (title, price))
print()