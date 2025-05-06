## 📊 Weather Dashboard with Alerts and Forecast

This is a Weather Dashboard web application that provides real-time weather data for cities across the world. The application fetches weather data from the OpenWeatherMap API and visualizes key weather metrics such as temperature, humidity, and weather conditions. It also generates alerts for extreme weather conditions like heatwaves and cold waves
.
## 🚀 Features

    Real-time Weather Data: Fetches weather information for any city in the world.

    5-Day Forecast: Displays a 5-day weather forecast, showing temperature, humidity, and weather conditions for each day.

    Weather Alerts: Generates alerts based on temperature thresholds (e.g., heatwaves and cold waves).

    Responsive Interface: Clean and responsive user interface built using Streamlit.

## ☁️Prerequisites

Before running the project, make sure you have the following installed on your machine:

      Python 3.x

      pip (Python package manager)

## ✅ Installation

1.Clone this repository to your local machine:

git clone https://github.com/yourusername/weather-dashboard.git

cd weather-dashboard

2. Create and activate a virtual environment (optional but recommended):

python -m venv venv

source venv/bin/activate   # On Windows use `venv\Scripts\activate`

3. Install the required dependencies:

pip install -r requirements.txt

4.Set up your OpenWeatherMap API Key:

                  1.Sign up for a free API key at OpenWeatherMap.

                  2.  Replace API_KEY in app.py with your actual API key.

## 📈 Usage

1.	Run the Streamlit app:
        
        streamlit run app.py

2.	Open the provided link (usually http://localhost:8501) in your browser.

3.	Enter a city name in the input field to fetch the weather data and 5-day forecast.

4.	The dashboard will display:

         1.Current Weather: Temperature, humidity, and weather condition.
  	
         2.5-Day Forecast: Weather details for the next five days.
  	
         3.Weather Alerts: Alerts for extreme weather conditions like heatwaves and cold    waves.
         
## 🛠️ Dependencies

 •	Streamlit: For building the web app.

 •	Requests: To make API calls to the OpenWeatherMap API.

 •	Pandas: For data handling and processing.

 •	Plotly: For visualizing weather data (optional).





