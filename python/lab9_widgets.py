import json
import requests

# Pull in json data from node.js server running on same system.
r = requests.get('http://localhost:3000/')
data = r.json()

print()  # formatting

# Iterate through each element of the json data.
for i in data:
    print(i['name']+" is "+i['color']+".")

print() # formatting
    