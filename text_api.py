from pyowm import OWM

api_key = "f3e1216cc7e05d7e1db59db5a7ca97ec"
owm = OWM(api_key)

mgr = owm.weather_manager()
observation = mgr.weather_at_place('Hong Kong')
w = observation.weather

humidity = w.humidity
wind = w.wind()
temp = w.temperature('celsius')

print(f"Wind: {wind} \nHUmidity: {humidity} \nTemperature: {temp}")
