from tkinter import *
import tkinter.font as tkFont
import os
from dotenv import load_dotenv
import requests
import time

root=Tk()
custom_font = tkFont.Font(family="Arial", size=25)
root.title("Current weather")
root.config(width=300,height=40)

load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")
lat="60.993"
lon="24.464"

def getWeatherData(Api_Key,lattitude,longitude):
    Url = f"https://api.openweathermap.org/data/2.5/weather?lat={lattitude}&lon={longitude}&appid={Api_Key}&units=metric"
    try:
        response = requests.get(Url)
        data=response.json()
        temp = data["main"]["temp"]
        return temp
    except requests.exceptions.RequestException as e:
        print(f"Error {e}")
        return None
    
weatherLabel=Label(root,font=custom_font)
weatherLabel.place(width=300,height=35)    

def updateWeather():
    data = getWeatherData(api_key,lat,lon)

    if data == None:
        return

    if int(data) < 15 and int(data) > 5:
        root.configure(bg="lightblue")
        weatherLabel.config(text=f"{data}°C",font=custom_font,bg="lightblue") 
        
    elif int(data) < 25 and int(data) > 15:
        root.configure(bg="green")
        weatherLabel.config(text=f"{data}°C",font=custom_font,bg="green") 

    elif int(data) > 25:
        root.configure(bg="red")
        weatherLabel.config(text=f"{data}°C",font=custom_font,bg="red") 

    else:
        root.configure(bg="blue")
        weatherLabel.config(text=f"{data}°C",font=custom_font,bg="blue")

    root.after(600000, updateWeather)

updateWeather()
root.mainloop()

    