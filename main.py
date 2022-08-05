
import tkinter as tk
import requests


 

def getWeather(root):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=36e4086e5553fcc23dc6f3b3dab91113"
    
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    

    final_info = condition + "\n" + str(temp) + "°C" 
    final_data = "\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) 
    label1.config(text = final_info)
    label2.config(text = final_data)


root = tk.Tk()
root.geometry("600x500")
root.title("Clima app")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(root, justify='center', width = 20, font = t)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(root, font=t)
label1.pack()
label2 = tk.Label(root, font=f)
label2.pack()
root.mainloop()