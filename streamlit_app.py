import streamlit as st
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
import joblib

#model = load_model("sleep_efficiency_model.h5")
#scaler = joblib.load('scaler.pkl')

st.title("Sleep Efficiency")

st.header("Input Features")

with st.form("my_form"):
    gender = st.selectbox("Gender", ["Male", "Female"])


    bedtime = st.slider("Bedtime (hour)", min_value=0, max_value=23, step=1)
    wakeup_time = st.slider("Wakeup time (hour)", min_value=0, max_value=23, step=1)


    rem_percentage = st.slider("REM sleep percentage", min_value=0, max_value=100, step=1)
    deep_percentage = st.slider("Deep sleep percentage", min_value=0, max_value=100, step=1)
    light_percentage = st.slider("Light sleep percentage", min_value=0, max_value=100, step=1)
    awakenings = st.number_input("Number of awakenings per night", min_value=0, max_value=10, step=1)
    caffeine = st.number_input("Caffeine consumption (mg/day)", min_value=0, max_value=200, step=1)
    alcohol = st.number_input("Alcohol consumption (oz/day)", min_value=0, max_value=5, step=1)

    smoking_status = st.selectbox("Smoking status", ["Non-smoker", "Smoker"])
    
    # Exercise frequency (minutes per day)
    exercise = st.number_input("Exercise frequency (weekly)", min_value=0, max_value=300, step=10)

    gender_binary = 1 if gender == "Male" else 0
    smoking_binary = 1 if smoking_status == "Smoker" else 0

    wakeup_hour = wakeup_time
    if wakeup_hour < bedtime:
        wakeup_hour += 24  # Handle wakeup time on the next day
    
    # Calculate sleep duration in hours
    sleep_duration = wakeup_hour - bedtime
    age = st.slider("Age (years)", min_value=18, max_value=100, step=1)
    data = {
        "age":age,
        "gender": gender_binary,
        "bedtime":bedtime,
        "wakeup_time": wakeup_time,
        "sleep_duration": sleep_duration,
        "rem_percentage": rem_percentage,
        "deep_percentage": deep_percentage,
        "light_percentage": light_percentage,
        "awakenings": awakenings,
        "caffeine": caffeine,
        "alcohol": alcohol,
        "smoking_status": smoking_binary,
        "exercise": exercise,
    }
    input =  pd.DataFrame(data)
    submitted = st.form_submit_button("Submit")
    

if submitted:
        st.write(input)
