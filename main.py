import requests
import sys
import json

weatherApi="https://www.apiopen.top/weatherApi?city={0}"

def getWeather(city):
    response=requests.get(weatherApi.format(city))
    jsonData = json.loads(response.text)
    if(200==jsonData['code']):
        weatherData=jsonData['data']['forecast'][0]
        print(weatherData['high'])
        print(weatherData['low'])
        print(weatherData['fengxiang'])
        print(weatherData['type'])
    else:
        print("get weather error")

if "__main__" == __name__:
    if(2!=len(sys.argv)):
        print("tips:{0} <$the name of place>")
    else:
        getWeather(sys.argv[1])