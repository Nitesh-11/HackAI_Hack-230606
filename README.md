TEMPERATURE AGENT

#DESCRIPTION
The "Temperature Agent" project is a simple software tool designed to monitor and notify users when the temperature falls outside a specified user-defined range. It operates by continuously checking the current temperature and comparing it to the predefined minimum and maximum temperature values set by the user.

#USE-CASE
The "Photovoltaic Power Predictor" is designed for forecasting solar power generation from photovoltaic (PV) systems. This prediction model utilizes a wide range of dynamic environmental parameters, including temperature, temperature range, wind speed, longitude, and latitude, among others, to provide highly accurate estimates of PV system output.

Table of Contents

About 
Installation
Usage
Contributing
License

#ABOUT

Overview
The "Photovoltaic Power Predictor" is an innovative software solution designed to accurately forecast and predict solar power generation from photovoltaic (PV) systems. This powerful tool leverages dynamic environmental parameters, including temperature, temperature range, wind speed, longitude, and latitude, to provide real-time and precise estimates of PV system output.

Main Features
Environmental Data Integration: The predictor collects and integrates a wide range of dynamic environmental data, such as real-time temperature, temperature range, wind speed, and geographical coordinates, to create a comprehensive and up-to-date picture of the conditions affecting solar power generation.

Accurate Solar Energy Forecasts: By processing this wealth of data, the tool generates highly accurate and reliable forecasts of photovoltaic power generation. These forecasts empower users to make informed decisions regarding energy consumption, storage, and distribution.

Energy Optimization: The "Photovoltaic Power Predictor" assists in optimizing the performance and efficiency of PV systems by considering various factors that impact solar power generation. This leads to better resource utilization and enhanced energy management.


#Exceution Command
python modelAgent.py
python temperatureAgent.py
python webAgent.py
streamlit run front2.py

 To run type the following command in the terminal:-
env\Scripts\activate.bat
python webAgent.py

#LIBRARIES
1.numpy
2.pandas
3. matplotlib
4.sklearn
5.XGBoostRegressor- Regression Model
5.streamlit

API :-
1. https://open-meteo.com/
2. https://github.com/OpenBMB/AgentVerse

Training Model-:
1. https://www.kaggle.com/code/aryandeshpande/solar-energy-prediction
2. https://colab.research.google.com/drive/13TGW0gZs7j8uxnX4n4fvbJ2ZWiOwdIGB








