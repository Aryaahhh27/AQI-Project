import streamlit as st
import pickle

st.set_page_config(page_title="homepage", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://cdn.wallpapersafari.com/29/15/zS9WuJ.jpg');     
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: black;
    }
    h1, h2, h3, p, label, div, span {
        color: white !important;
        font-weight: bold !important;
    }
    /* Predict Button */
    .stButton button {
        color: white !important;
        font-weight: bold !important;
        background-color: #333333 !important;
        border: 2px solid white !important;
    }
    /* Style selectbox and its label */
    div[data-baseweb="select"] {
        color: white !important;
    }
    div[data-baseweb="select"] > div {
        background-color: #333333 !important;
        color: white !important;
        border: 1px solid white !important;
    }
    div[data-baseweb="select"] div {
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("AQI Prediction")

filename1 = 'aqi.pkl'
loaded_model1 = pickle.load(open(filename1, 'rb'))
filename1s = 'scale.pkl'
loaded_scale1 = pickle.load(open(filename1s, 'rb'))
filename2 = 'aqik.pkl'
loaded_model2 = pickle.load(open(filename2, 'rb'))
filename2s = 'scalek.pkl'
loaded_scale2 = pickle.load(open(filename2s, 'rb'))
filename3 = 'aqie.pkl'
loaded_model3 = pickle.load(open(filename3, 'rb'))
filename3s = 'scalee.pkl'
loaded_scale3 = pickle.load(open(filename3s, 'rb'))

st.markdown('<p style="font-size:1.5rem; font-weight:bold; color:white;">Enter the following details</p>', unsafe_allow_html=True)

PM10 = st.number_input("enter PM10 (Particulate Matter<=10 microns)")
PM2_5 = st.number_input("enter PM2.5 (Particulate Matter <=2.5 microns)")
NO2 = st.number_input("enter NO₂ (Nitrogen Dioxide)")
SO2 = st.number_input("SO₂ (Sulfur Dioxide)")
CO = st.number_input("enter CO (Carbon Monoxide)")
O3 = st.number_input("enter O₃ (Ozone)")
NH3 = st.number_input("enter NH3(Ammonia)")

new = [[PM10, PM2_5, NO2, SO2, CO, O3, NH3]]

st.write("----------------------------------------------------------------------------------------")

if "clicked_predict" not in st.session_state:
    st.session_state.clicked_predict = False

if st.button("Predict"):
    st.session_state.clicked_predict = True

if st.session_state.clicked_predict:
    city = st.selectbox(
        "Select your City",
        ["", "Karyavattom", "Kollam", "Eloor"]
    )
    if city:
        if city == "Karyavattom":
            predicted_class = loaded_model1.predict(loaded_scale1.transform(new))
        elif city == "Kollam":
            predicted_class = loaded_model2.predict(loaded_scale2.transform(new))
        elif city == "Eloor":
            predicted_class = loaded_model3.predict(loaded_scale3.transform(new))
        st.success(f"Predicted AQI class for {city}: {predicted_class[0]}")
