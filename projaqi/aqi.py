import streamlit as st
import pickle
filename1='aqi.pkl'
loaded_model1=pickle.load(open(filename1,'rb'))
filename1s='scale.pkl'
loaded_scale1=pickle.load(open(filename1s,'rb'))
st.write("AQI Prediction for Karyavattom")
PM10=st.number_input("enter PM10 (Particulate Matter<=10 microns)")
PM2_5=st.number_input("enter PM2.5 (Particulate Matter <=2.5 microns)")
NO2=st.number_input("enter NO₂ (Nitrogen Dioxide)")
SO2=st.number_input("SO₂ (Sulfur Dioxide)")	
CO=st.number_input("enter CO (Carbon Monoxide)")
O3=st.number_input("enter O₃ (Ozone)")
NH3=st.number_input("enter NH3(Ammonia)")
new=[[PM10,PM2_5,NO2,SO2,CO,O3,NH3]]
predicted_class1=loaded_model1.predict(loaded_scale1.transform(new))
if st.button('predict'):
    st.write(predicted_class1)