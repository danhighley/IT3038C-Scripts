from bs4 import BeautifulSoup
import requests, re

r = requests.get("http://webscraper.io/test-sites/e-commerce/allinone/phones").content
soup = BeautifulSoup(r, "lxml")
tags = soup.findAll("div", {"class":re.compile('(ratings)')})
for p in tags:
    a = p.findAll("p",{"class":"float-end review-count"})
    print(a[0].string)