import requests

try:
    r = requests.get('http://www.udacity.com')
    if r.status_code == 200 or r.status_code == 404:
        print(r.status_code)

except requests.exceptions.ConnectionError:
    print('Could not connect to server')
