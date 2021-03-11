import requests


r =  requests.get('https://www.metaweather.com/api/location/2455920')
d = r.json()
weather = d['consolidated_weather']

for days in weather:
    date = days['applicable_date']
    humidity = days['humidity']
    print(f'The date of {date} will has a humidity of {humidity}.')
