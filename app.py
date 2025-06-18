import streamlit as st
import joblib

# ✅ MUST BE THE VERY FIRST Streamlit command
st.set_page_config(page_title="House Price Prediction", layout="centered")

# Load trained model
model = joblib.load('model.pkl')

st.title("🏠 House Price Prediction App")

# Inputs
size = st.number_input("Area in sqft", min_value=500, max_value=500000, step=100)
bed = st.slider("Bedrooms", 1, 10, 2)
bath = st.slider("Bathrooms", 1, 5, 2)
age = st.slider("Age of house (years)", 0, 30, 5)

# Predict
if st.button("Predict Price"):
    data = [[size, bed, bath, age]]
    prediction = model.predict(data)
    st.success(f"Estimated Price: ₹{int(prediction[0]):,}")
