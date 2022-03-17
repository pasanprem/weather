import requests

API_KEY = "d9a00b2ecdf7dfb77fb9a94ed27f28d7"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print("Weather is: ", weather )
    temperature = round(data["main"]["temp"] - 273.15, 2) # Kelvin to celcius conversion
    print("Temperature is :", temperature, "celcius")
else:
    print("An error occured.")
