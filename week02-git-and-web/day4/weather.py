import requests

print("-" * 30)

def get_Forecast(latitude, longitude):
    try:
        response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")
    except requests.RequestException as error:
        print(f"Network error: could not reach the weather service. ({error})")
        return

    status_code = response.status_code

    if status_code == 200:
        data = response.json()
        current_weather = data.get("current", {})
        temperature = current_weather.get("temperature_2m", "N/A")
        wind_speed = current_weather.get("wind_speed_10m", "N/A")
        print(f"Current Temperature: {temperature}°C")
        print(f"Current Wind Speed: {wind_speed} m/s")
    elif status_code >= 400 and status_code < 500:
        print("Bad Request: The request was invalid. Please check the latitude and longitude values.")
    elif status_code == 500:
        print("Internal Server Error: The server encountered an error. Please try again later.")
    else:
        print(f"Unexpected status code: {status_code}. Please try again later.")

def main():
    print("=== Weather Forecast ===")
    latitude = input("Enter latitude: ")
    longitude = input("Enter longitude: ")
    get_Forecast(latitude, longitude)

main()