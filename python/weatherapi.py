import json
import requests

print('Please enter your zip code:')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=API_KEY' % zip)
data = r.json()

print(data['weather'][0]['description'])