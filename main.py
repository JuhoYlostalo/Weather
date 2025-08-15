from tkinter import *
import tkinter.font as tkFont
import os

# weather app
#gets weather data from api and shows it using tkinter

root=Tk()
custom_font = tkFont.Font(family="Arial", size=25)
root.title("Current weather")
root.config(width=300,height=40)
weatherLabel=Label(root,text="37C",font=custom_font) 
weatherLabel.place(width=300,height=25)

root.mainloop()