import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    api_key = "dfb151267aa47c93fb4855cf86885223"
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    try:
        response = requests.get(base_url, params={"q": city, "appid": api_key, "units": "metric"})
        response.raise_for_status()
        weather_data = response.json()

        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"].capitalize()
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]

        weather_result.set(f"Temperature: {temperature} °C\n"
                           f"Description: {description}\n"
                           f"Humidity: {humidity}%\n"
                           f"Wind Speed: {wind_speed} m/s")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Unable to retrieve data:\n{e}")
    except KeyError:
        messagebox.showerror("Error", "City not found. Please enter a valid city name.")

# Create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.resizable(False, False)

# Input field and label
city_label = tk.Label(root, text="Enter City:", font=("Arial", 12))
city_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 12), width=30)
city_entry.pack(pady=5)

# Button to fetch weather
fetch_button = tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather)
fetch_button.pack(pady=10)

# Label to display the weather result
weather_result = tk.StringVar()
result_label = tk.Label(root, textvariable=weather_result, font=("Arial", 12), justify="left")
result_label.pack(pady=20)

# Run the app
root.mainloop()
