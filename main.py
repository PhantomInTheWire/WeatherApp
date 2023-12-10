from datetime import datetime
import streamlit as st
from pyowm import OWM
import plotly.express as px

# Streamlit configuration
st.set_page_config(page_title="Weather Report App", layout="wide")

# App title
st.title("Weather Report App")
st.caption("~By Swarnim Goyal and Team")
# City input
city = st.text_input("Enter city name", "Gandhinagar, Gujrat")

key = '908ccbd2f6cca4ccbdea63188930b090'
owm = OWM(key)
mng = owm.weather_manager()
weather = mng.weather_at_place(city).weather

# Extract temperature data
temperature_data = [
    {"date": datetime.utcfromtimestamp(weather.reference_time()).isoformat()[0:10]},
    {"temp": weather.temperature('celsius')['temp']},
]

# Create the Plotly graph
fig = px.line(temperature_data, x="date", y="temp", title="Temperature over Time")

# Create two columns
col1, col2 = st.columns(2)

# Display weather report and graph in columns
with col1:
    st.write(f"Date: {datetime.utcfromtimestamp(weather.reference_time()).isoformat()[0:10]}")
    st.write(f"Temperature: {weather.temperature('celsius')['temp']}°C")
    st.write(f"Status: {weather.detailed_status}")

with col2:
    st.write(f"Wind direction: {weather.wind()['deg']}°")
    st.write(f"Wind: {weather.wind()['speed']} m/s")
    st.write(f"Humidity: {weather.humidity}%")

st.plotly_chart(fig)
