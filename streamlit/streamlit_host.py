import streamlit as st
import pickle
import numpy as np
import os

# # Set up the page configuration
st.set_page_config(page_title="Crop Recommendation", layout="centered")

# Load the model
model_path = os.path.join(os.path.dirname(__file__), "..", "model", "NBClassifier.pkl")
with open(model_path, "rb") as f_in:
    model = pickle.load(f_in)


st.title("Crop Recommendation")

col1, col2 = st.columns(2)

with st.form(key='crop_form'):
    with col1:
        N = st.number_input("N (Nitrogen content in soil):", min_value=0, max_value=250)
        P = st.number_input("P (Phosphorus content in soil):", min_value=0, max_value=250)
        K = st.number_input("K (Potassium content in soil):", min_value=0, max_value=250)
        temperature = st.number_input("Temperature (in Celsius):", min_value=5, max_value=50)

    with col2:
        humidity = st.number_input("Humidity (in %):", min_value=5, max_value=100)
        ph = st.number_input("pH level of soil:", min_value=1, max_value=14)
        rainfall = st.number_input("Rainfall (in mm):", min_value=0, max_value=300)
        
    submit_button = st.form_submit_button(label="Predict") 


# Handle form submission
if submit_button:
    # Ensure all inputs are filled
    if N and P and K and temperature and humidity and ph and rainfall:
        # Convert inputs to float and prepare for prediction
        form_values = [float(N), float(P), float(K), float(temperature), float(humidity), float(ph), float(rainfall)]
        data = np.array([form_values])
        
        # Get prediction from the model
        prediction = model.predict(data)
        output = prediction[0]
        
        # Display prediction result
        st.markdown(f"<h2>Recommended crop is {output}</h2>", unsafe_allow_html=True)
    else:
        st.markdown("<h2>Please fill in all fields.</h2>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)