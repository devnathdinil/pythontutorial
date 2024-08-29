from fetch import get_weather_data
from display import display_weather
import requests

def main():
    city = input("Enter the name of city to get weather: ")
    
    try:
        weather_data = get_weather_data(city)
        display_weather(weather_data)
    except requests.exceptions.HTTPError as err:
        print("HTTP error occured: ",err)
    except requests.exceptions.RequestException as err:
        print("Request exception occured: ",err)


if __name__ == "__main__":
    main()