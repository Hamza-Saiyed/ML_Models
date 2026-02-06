import streamlit as st
import pandas as pd
import pickle 

model = pickle.load(open('house_model.pkl',"rb"))

st.title("House Price Prediction App")

area = st.number_input("Enter Area(sqft)",min_value = 200, max_value = 5000)
bed = st.number_input("Enter Number of Bedrooms", min_value = 1, max_value = 10)
age = st.number_input("Enter Age of House (years)",min_value = 0, max_value = 80)

if st.button("Predict Price"):
    data = pd.DataFrame({
        "area" : [area],
        "bedrooms" : [bed],
        "age" : [age]
    })
    
    # pred = model.predict(data)[0]
    # st.success(f"Estimated House Price: ₹ {round(pred,2)}")
    pred = model.predict(data)[0]
    st.success(f" Estimated House Price: ₹ {pred:,.2f}")
