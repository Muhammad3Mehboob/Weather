import uvicorn
import streamlit as st
import requests
from dotenv import load_dotenv
import os


# OpenWeather API key (replace with your own API key)
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Function to get weather data
def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Streamlit UI
st.title("Weather Web App ☁️")
city = st.text_input("Enter City Name:")

if st.button("Get Weather"):
    if city:
        data = get_weather(city)
        if data:
            st.write(f"**City:** {data['name']}, {data['sys']['country']}")
            st.write(f"**Temperature:** {data['main']['temp']}°C")
            st.write(f"**Weather:** {data['weather'][0]['description'].capitalize()}")
            st.write(f"**Humidity:** {data['main']['humidity']}%")
            st.write(f"**Wind Speed:** {data['wind']['speed']} m/s")
        else:
            st.error("City not found! Please try again.")
    else:
        st.warning("Please enter a city name.")

# Run the Streamlit app using UV
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8501, reload=True)


