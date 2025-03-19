import streamlit as st
import requests
from dotenv import load_dotenv
import os

API_KEY = st.secrets["weather"]["API_KEY"]
load_dotenv()
BASE_URI = "http://api.openweathermap.org/data/2.5/weather"

#  Function to get weather data

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URI, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None

# Streamlit UI

st.title("Weather Web App")
city = st.text_input("Enter City Name:")

if st.button("Get Weather"):
    if city:  
        data = get_weather(city)
        if data:
            st.subheader(f"Weather in {data['name']}, {data['sys']['country']}")
            st.write(f"🌡️ Temperature: {data['main']['temp']}°C")
            st.write(f"🌤️ Weather: {data['weather'][0]['description'].capitalize()}")
            st.write(f"💨 Wind Speed: {data['wind']['speed']} m/s")
            st.write(f"🌍 Latitude: {data['coord']['lat']}, Longitude: {data['coord']['lon']}")

            
            icon_code = data['weather'][0]['icon']
            icon_url = f"http://openweathermap.org/img/w/{icon_code}.png"
            st.image(icon_url, caption="Weather Icon", width=100)
        else:
            st.error("City not found! Please try again.")
    else:
        st.warning("Please enter a city name.")
