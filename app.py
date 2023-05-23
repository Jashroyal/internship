import streamlit as st
import pickle
#import sklearn
import pandas as pd
import numpy as np
# from PIL import Image
import base64

model=pickle.load(open('model.sav','rb'))
# model=pickle.load(open('modelreg.sav','rb'))
st.title("UBER FARE PRICE PREDICTION")
st.sidebar.header(" Fare amount")
# image = Image.open('uber car.jpg')
# st.image(image,'uber')
# def add_bg_from_local(image_file):
#     with open(image_file, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read())
#     st.markdown(
#     f"""
#     <style>
#     .stApp {{
#         background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
#         background-attachment: fixed;
#         background-size: cover
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
#     )
# add_bg_from_local('')  

def user_report():
     pickup_longitude=st.sidebar.slider("Pickup longitude",-180.0,180.0)   
     pickup_latitude=st.sidebar.slider("Pickup Latitude",-90.0,90.0)  
     dropoff_longitude=st.sidebar.slider("Dropoff Longitude",-180.0,180.0)
     dropoff_latitude=st.sidebar.slider(" Dropoff Latitude",-90.0,90.0)
     passenger_count=st.sidebar.slider(" Passenger Count",1,8)
     Distance=st.sidebar.slider("Distance",0.010000,53.070000)
     Year=st.sidebar.slider("Year",2009,2015)
     Month=st.sidebar.slider("Month",1,12)
     Day=st.sidebar.slider("Day",1,31)
     DayofWeek_num=st.sidebar.slider("Day of Week num",0,6)
     Hour=st.sidebar.slider("Hour",0,23)
     counter=st.sidebar.slider("Counter",0,1)
    
    
     user_report_data={
        'pickup_longitude':pickup_longitude,
        'pickup_latitude':  pickup_latitude,
        'dropoff_longitude': dropoff_longitude,
        'dropoff_latitude': dropoff_latitude,
        'passenger_count':passenger_count,
        'Distance':Distance,
        'Year': Year,
        'Month': Month,
        'Day': Day,
        'Day of Week_num':DayofWeek_num,
        'Hour':Hour,
        'counter': counter
         }
     report_data=pd.DataFrame(user_report_data,index=[0])
     return report_data


user_data=user_report()
st.header('Uber data')
st.write(user_data)
  
Fare=model.predict(user_data)
st.subheader('Uber fare')
st.subheader(np.round(Fare[0],2))
    
