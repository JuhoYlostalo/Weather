from tkinter import *
import tkinter.font as tkFont
import os
from dotenv import load_dotenv
import requests
# weather app
#gets weather data from api and shows it using tkinter

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
    
data = getWeatherData(api_key,lat,lon)

weatherLabel=Label(root,text=f"{data}°C",font=custom_font) 
weatherLabel.place(width=300,height=25)
print(data)

root.mainloop()