
 AQI Prediction for KOLLAM, KARYAVATTOM, and ELOOR

 Overview

AQI Prediction is an interactive web application built using Streamlit and a pre-trained machine learning model. The project aims to predict the Air Quality Index (AQI) for three prominent cities in Kerala — Kollam, Karyavattom, and Eloor — based on input pollution parameters. The data used in training the model spans the years 2023 and 2024 for these cities, allowing the model to give accurate and region-specific AQI predictions.

 Key Features

* User-friendly interface powered by Streamlit.
* Ability to input pollutant parameters:
    PM10
    PM2.5
    CO
    NO₂
    SO₂
    NH₃
    O₃
*Single-click prediction feature with a "Predict" button.
*Dropdown menu for choosing the target city — Kollam, Karyavattom, or Eloor.
*Instant AQI value output displayed on the screen after city selection.
*Model trained on real-world historical data (2023–2024) for accurate predictions.

How It Works

1.The user enters pollution parameters.
2.Upon clicking "Predict", the application reveals a dropdown list with three cities.
3.The user selects the desired city.
4.The app passes the input parameters and city to the pre-trained machine learning model (aqi.pkl), which outputs a predicted AQI value.
5.The predicted AQI is displayed in the UI for the user.

Technologies & Tools

Frontend: Streamlit — for quick, elegant web apps in pure Python.
Backend: Python, with pickle to load the trained model.
Modeling: Regression-based ML model trained on pollution data (2023–2024) for Kollam, Karyavattom, and Eloor.
Data: Historical pollution data (PM10, PM2.5, CO, NO₂, SO₂, NH₃, O₃) used for training.




