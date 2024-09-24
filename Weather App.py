import tkinter as tk
from tkinter import messagebox
import requests
import tkinter.font as tkFont


API_KEY = 'bc77cf770cba77986fe3a3702735d420'

def get_weather(even=None):
	city = city_entry.get()
	if city:  
		url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
		response = requests.get(url)
	

		if response.status_code == 200:
			data = response.json()
			weather_description = data ['weather'][0]['description']
			temperature = data['main']['temp']
			message = f"Weather in {city}:\nTemperature: {temperature}°C\nDescription: {weather_description}"
			messagebox.showinfo("Weather Info", message)
		else:
			messagebox.showerror("Error, city not found!")

	else:
		messagebox.showwarning("Input Error", "Please enter a city name.")

#GUI

root = tk.Tk()
root.title("Weather App")
root.configure(bg="black")
root.geometry("250x200")

font_style = tkFont.Font(family="Helvetica",size=14,weight="bold")
font_style_2 = tkFont.Font(family="Helvetica",size=16)

tk.Label(root, text="Enter City:", bg="black", fg="red", font=font_style).pack(pady=10)
city_entry = tk.Entry(root, bg="grey", fg= "red", font=font_style_2)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather!", bg="darkblue", fg="red", font=font_style, command=get_weather).pack(pady=20)
# Bind the Enter key to the get_weather function
root.bind('<Return>', get_weather)

root.mainloop()
