
import requests
import json
import datetime


class OpenWeatherMap:
    def __init__(self):
        self.__api_key = "NEVER PUSH KEYS TO GITHUB"
        self.__lat = 51.450832
        self.__lon = 7.013056
        self.__weather_url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (
            self.__lat, self.__lon, self.__api_key)
        self.__forecast_url = "http://api.openweathermap.org/data/2.5/forecast?lat=51.450832&lon=7.013056&appid=190a8d037ec64f8c4ca1f84cd3ee7dd7&units=metric"

    def get_weather_data(self):
        response = requests.get(self.__weather_url)
        data = json.loads(response.text)
        weather = {"temp": data["current"]["temp"], "wind_speed": data["current"]["wind_speed"],
                   "sunrise": data["current"]["sunrise"], "description": data["current"]["weather"][0]["description"],
                   "icon": data["current"]["weather"][0]["icon"], "feels_like": data["current"]["feels_like"]}

        return weather

    def get_forecast(self):
        response = requests.get(self.__forecast_url)
        data = json.loads(response.text)
        forecast = []
        for element in data["list"]:
            if datetime.datetime.fromtimestamp(element["dt"]).time() == datetime.time(14, 0, 0):
                forecast.append(Forecast(element["dt"], element["main"]["temp"], element["weather"][0]["icon"]))

        return forecast


class Forecast:
    def __init__(self, dt, temp, icon):
        self.temp = str(round(temp,1))
        self.icon = str(icon)
        self.dt = dt

    def __repr__(self):
        return str({"temp": self.temp, "icon": self.icon, "dt": datetime.datetime.fromtimestamp(self.dt).date()})


if __name__ == "__main__":
    owm = OpenWeatherMap()
    # print(owm.get_weather_data())
    print(owm.get_forecast())
    print(owm.get_weather_data())
