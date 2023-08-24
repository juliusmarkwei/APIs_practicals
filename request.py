import requests

key = 'b1128cc40237ba85a36baec505b7bfc5'
url = f'https://api.openweathermap.org/data/2.5/weather?q=London&APPID={key}'
r = requests.get(url)

print(r.json()['main']['humidity'])
