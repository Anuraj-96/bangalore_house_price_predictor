
import streamlit as st
import numpy as np
import json
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('model.joblib')

# Load the column names (feature list)
with open('columns.json', 'r') as f:
    columns = json.load(f)   

# Load the smoothed mean and global mean
with open("smooth_map.json", "r") as f:
    smooth_map = json.load(f)  

with open("global_mean.json", "r") as f:
    global_mean = json.load(f)["global_mean"]

# App title
st.set_page_config(page_title="Bangalore House Price Predictor", layout="centered")
st.title("🏠 Bangalore House Price Predictor")
st.markdown("Estimate the price of a house in Bangalore based on its features.")

# User inputs
sqft = st.number_input("Total Square Feet", min_value=300, step=50)
bath = st.selectbox("Number of Bathrooms", [1, 2, 3, 4, 5])
bhk = st.selectbox("Number of BHK", [2, 3, 4])
location = st.selectbox("Location", options=sorted(smooth_map.keys()))

# Predict button
def prepare_input(location, sqft, bath, bhk):
    # Apply smoothed mean encoding (fallback to global_mean if unseen)
    location_enc = smooth_map.get(location, global_mean)
    
    # Create dataframe with correct column order
    data_dict = {
        "location": location_enc,
        "total_sqft": sqft,
        "bath": bath,
        "bhk": bhk  }
    df = pd.DataFrame([data_dict])
    df = df[columns]  
    return df

if st.button("Predict Price"):
    if sqft > 4000:
        st.warning("⚠️ Note: Model was trained only on properties up to 4000 sqft. Predictions beyond this may be less accurate.")
    input_df = prepare_input(location,sqft, bath, bhk)
    pred_log = model.predict(input_df)[0]  # prediction in log space
    prediction = np.expm1(pred_log)  # inverse log1p transform
    st.success(f"💰 Estimated Price: ₹ {prediction:,.2f} Lakhs")
    
