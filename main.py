import streamlit as st
import requests

API_KEY = "5d931c3ebb308e8a3dee8ea0b1192dba"

st.title("Weather App")

# get the user's location input
location = st.text_input("Enter your city name:", "New York")

# get the current weather data
url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
response = requests.get(url).json()
if response["cod"] != "404":
    weather_data = {
        "Temperature": response["main"]["temp"],
        "Feels Like": response["main"]["feels_like"],
        "Description": response["weather"][0]["description"],
        "Icon": response["weather"][0]["icon"]
    }

    # display the current weather data
    st.subheader("Current Weather")
    st.write(f"Temperature: {weather_data['Temperature']}°C")
    st.write(f"Feels Like: {weather_data['Feels Like']}°C")
    st.write(f"Description: {weather_data['Description']}")
    icon_url = f"http://openweathermap.org/img/w/{weather_data['Icon']}.png"
    st.image(icon_url)

# get the 5-day weather forecast
url = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}&units=metric"
response = requests.get(url).json()
if response["cod"] != "404":
    forecast_data = []
    for forecast in response["list"]:
        forecast_data.append({
            "Date": forecast["dt_txt"],
            "Temperature": forecast["main"]["temp"],
            "Description": forecast["weather"][0]["description"],
            "Icon": forecast["weather"][0]["icon"]
        })

    # display the 5-day weather forecast data
    st.subheader("5-day Weather Forecast")
    for forecast in forecast_data:
        st.write(f"Date: {forecast['Date']}")
        st.write(f"Temperature: {forecast['Temperature']}°C")
        st.write(f"Description: {forecast['Description']}")
        icon_url = f"http://openweathermap.org/img/w/{forecast['Icon']}.png"
        st.image(icon_url)
        st.write("----")

