import pandas as pd
import streamlit as st
import pickle

model = pickle.load(open('car_model.pkl',"rb"))

st.title("Car Price Prediction")

engine = st.number_input("Engine Size(cc)",600, 8000)
weight = st.number_input("Weight (kg)",500, 2000)
power = st.number_input("Horsepower",40,2000)

if st.button("Predic Mileage"):
    data = pd.DataFrame({
        "engine_size":[engine],
        "weight":[weight],
        "horsepower":[power]
    })
    
    pred = model.predict(data)[0]
    st.success(f"Estimated Mileage: {pred}")