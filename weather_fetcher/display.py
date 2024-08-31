
def display_weather(data):
    print(data)
    city=data["name"]
    temp=data["main"]["temp"]
    description=data["weather"][0]["description"]
    humidity=data["main"]["humidity"]
    pressure=data["main"]["pressure"]

    print(f"weather in {city}")
    print(f"temperature: {temp}")
    print(f"condition: {description}")
    print(f"Humidity: {humidity}")
    print(f"pressure: {pressure}")
    