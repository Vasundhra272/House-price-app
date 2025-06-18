import streamlit as st
import joblib

st.set_option('client.showErrorDetails', True)
st.set_page_config(page_title="House Price Prediction", layout="centered")

st.markdown("""
   <style>
     .main{
     background-color: ghostwhite;
   </style>""",unsafe_allow_html=True)

model = joblib.load('model.pkl')

st.markdown("""<h1 style='text-align:center; font-size:40px; color:darkblue;'>🏡 House Price Predictor </h1>
            <p style='text-align:center; font-size:25px; color:darkblue'> Please fill all required fields</p>""",unsafe_allow_html=True)

st.markdown("<p style='font-size:20px; color:navy;'><i>Enter House Size</i> </p>",unsafe_allow_html=True)
size = st.number_input("",min_value=500, max_value=5000000, step=100)

st.markdown("<p style='font-size:20px; color:navy;'><i>Number of Bedroom</i></p>",unsafe_allow_html=True)
bed = st.slider("", 2, 10, 2)

st.markdown("<p style='font-size:20px; color:navy;'><i>Number of Bathroom</i></p>",unsafe_allow_html=True)
bath = st.slider("", 1, 5, 2)

st.markdown("<p style='font-size:20px; color:navy;'><i>Age of House(years)</i></p>",unsafe_allow_html=True)
age = st.slider("", 0, 30, 5)


if st.button("🔍Predict Price"):
    data = [[size, bed, bath, age]]
    prediction = model.predict(data)
    st.markdown(f"""<h4 style='text-align:center; color:forestgreen;'>Estimated Price: ₹{int(prediction[0]):,}</h4>""", unsafe_allow_html=True)


