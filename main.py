"""" 
36e4086e5553fcc23dc6f3b3dab91113
"""
import requests, json

api_key = "36e4086e5553fcc23dc6f3b3dab91113"
base_url="http://api.openweathermap.org/data/2.5/weather?"
city_name = input("ingresa el nombre de la ciudad: ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response=requests.get(complete_url)
x=response.json()
temperature =x["main"]["temp"]
presion=x["main"]["pressure"]
humedad=x["main"]["humidity"]

print(temperature - 273.15," grados celcius en la ciudad de " + city_name,",un presion de",presion," hPa y una humedad del",humedad,"%")
          

import webbrowser

f = open('helloworld.html','w')

message = """<html>
<head></head>
<body><p>Hello World!</p></body>
</html>"""

f.write(message)
f.close()

webbrowser.open_new_tab('openweatherAPI.html')