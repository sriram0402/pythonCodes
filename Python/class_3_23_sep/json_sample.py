
import json, requests, sys

location=input("enter location:")
if len(sys.argv)>1:
    locaton=''.json(sys.argv[1:])
    
url='https://api.openweathermap.org/data/2.5/weather?q='+location+'&appid=81db19b25f202bfde975b1de71c20387'

res=requests.get(url)
pyObj=json.loads(res.text)



main=pyObj['weather'][0]['main']
temp=pyObj['main']['temp']
minTemp=pyObj['main']['temp_min']
maxTemp=pyObj['main']['temp_max']
feelsLike=pyObj['main']['feels_like']
humidity=pyObj['main']['humidity']
print('Main:',main)
print('Current temp:',temp)
print('Min temp:',minTemp)
print('Max temp:',maxTemp)
print('feels like:',feelsLike)
print("Humidity:",humidity)

