import json
import requests

print('Please enter your zip code:')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=1543bf2e4a545f844b2e63d35589df9e' % zip)
data = r.json()

print(data['weather'][0]['description'])