import requests

api_key = "c6b71322f6e510b0dea73d13b6b2d30c"

user_data = input("Enter the City: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_data}&APPID={api_key}"
)

if weather_data.status_code == 200:
    weather = weather_data.json()["weather"][0]["main"]
    temp = round(weather_data.json()["main"]["temp"])

    print(f"The Weather in {user_data} is: {weather}")
    print(f"The Temperature in {user_data} is: {temp}°F")
else:
    print(
        f"Error: Unable to fetch weather data for {user_data}. Please check the city name."
    )
