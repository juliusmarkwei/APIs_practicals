import requests

url = 'https://api.openweathermap.org/data/2.5/weather?q=London&APPID={f3e1216cc7e05d7e1db59db5a7ca97ec}'
r = requests.get(url)

print()
