import streamlit as st
import joblib

st.set_option('client.showErrorDetails', True)
st.set_page_config(page_title="House Price Prediction", layout="centered")

model = joblib.load('model.pkl')

st.markdown("""<h1 style='text-align:center; font-size:40px; color:darkblue;'>🏡 House Price Predictor </h1>
            <p style='text-align:center; font-size:25px; color:darkblue'> Fill the detail below</p>""",unsafe_allow_html=True)

st.markdown("<p style='font-size:20px;'>Enter House Size </p>",unsafe_allow_html=True)
size = st.number_input(min_value=500, max_value=5000000, step=100)

st.markdown("<p style='font-size:20px;'>Number of Bedroom</p>",unsafe_allow_html=True)
bed = st.slider( 2, 10, 2)

st.markdown("<p style='font-size:20px;'>Number of Bathroom</p>",unsafe_allow_html=True)
bath = st.slider( 1, 5, 2)

st.markdown("<p style='font-size:20px;'>Age of House(years)</p>",unsafe_allow_html=True)
age = st.slider( 0, 30, 5)


if st.button("🔍Predict Price"):
    data = [[size, bed, bath, age]]
    prediction = model.predict(data)
    st.markdown(f"""<h3 style='text-align:center; color:green;'>🔘 Estimated Price: ₹{int(prediction[0]):,}</h3>""", unsafe_allow_html=True)


