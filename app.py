import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import datetime

st.set_page_config(page_title="🌤 Weather Analysis Dashboard", layout="wide")

API_KEY = "7aebe6ac5127cd2c875b8bef60d7d1d5"

@st.cache_data(ttl=600)
def fetch_weather_data(city):
    city_query = city + ",IN"  # Ensure city is treated as an Indian location
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_query}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def parse_weather(json_data):
    if not json_data:
        return None
    return {
        "City": json_data["name"],
        "Date": datetime.datetime.now(),
        "Temperature (°C)": json_data["main"]["temp"],
        "Humidity (%)": json_data["main"]["humidity"],
        "Weather": json_data["weather"][0]["main"],
        "Wind Speed (m/s)": json_data["wind"]["speed"],
        "Air Pressure (hPa)": json_data["main"]["pressure"]
    }

st.title("📊 Weather Data Analysis Dashboard")

city_input = st.text_input("Enter Indian City Name")

if city_input:
    data_json = fetch_weather_data(city_input)
    weather_info = parse_weather(data_json)

    if weather_info:
        df_current = pd.DataFrame([weather_info])
        st.subheader(f"🌇 Weather in {weather_info['City']} on {weather_info['Date'].strftime('%Y-%m-%d %H:%M:%S')}")

        # KPIs
        col1, col2, col3 = st.columns(3)
        col1.metric("🌡 Temperature", f"{weather_info['Temperature (°C)']} °C")
        col2.metric("💧 Humidity", f"{weather_info['Humidity (%)']} %")
        col3.metric("🌬 Wind Speed", f"{weather_info['Wind Speed (m/s)']} m/s")

        # Table
        st.write("### 📋 Weather Summary")
        st.dataframe(df_current, use_container_width=True)

        # Visualization
        st.write("### 📈 Visualization")
        chart_df = df_current[["Temperature (°C)", "Humidity (%)", "Wind Speed (m/s)", "Air Pressure (hPa)"]].melt()
        fig = px.bar(chart_df, x="variable", y="value", color="variable", title="Current Weather Metrics")
        st.plotly_chart(fig, use_container_width=True)

        # Feature 1: Historical Data Comparison (simulated)
        st.write("### ⏳ Historical Comparison (Simulated)")
        hist_df = df_current.copy()
        hist_df["Temperature (°C)"] -= 2
        hist_df["Humidity (%)"] += 5
        hist_df["Date"] = weather_info["Date"] - datetime.timedelta(days=1)

        combined_df = pd.concat([hist_df, df_current])
        fig2 = px.line(combined_df, x="Date", y="Temperature (°C)", title="📉 Temperature Comparison (Today vs Yesterday)", markers=True)
        st.plotly_chart(fig2, use_container_width=True)

        # Feature 2: Download CSV
        st.download_button("⬇ Download Weather Data as CSV", data=df_current.to_csv(index=False), file_name=f"{city_input}_weather.csv", mime="text/csv")

    else:
        st.error(f"❌ Error fetching data for {city_input}. Please try a different city.")
