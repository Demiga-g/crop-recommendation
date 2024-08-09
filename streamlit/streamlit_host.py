# You can integrate the prediction code into your Streamlit app by following the example below:

import streamlit as st
import pickle
import numpy as np
import os

# Set up the page configuration
# st.set_page_config(page_title="Crop Recommendation", layout="centered")

# Custom CSS styling
# st.markdown(
#     """
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');
#     body {
#         font-family: "Poppins", sans-serif;
#         background: #f8f3d9;
#     }
#     .container {
#         max-width: 600px;
#         margin: auto;
#         padding: 20px;
#         border: 1px solid #a8aca5;
#         border-radius: 50px;
#         background-color: #ffffff;
#     }
#     h1 {
#         text-align: center;
#     }
#     .form-group {
#         display: flex;
#         flex-wrap: wrap;
#         justify-content: space-between;
#         gap: 10px;
#     }
#     .form-group label {
#         width: 100%;
#     }
#     .form-group input {
#         width: 48%;
#         padding: 8px;
#         box-sizing: border-box;
#     }
#     .predict-btn {
#         background-color: #4CAF50;
#         color: white;
#         padding: 10px 20px;
#         border: none;
#         border-radius: 5px;
#         cursor: pointer;
#         display: block;
#         width: 50%;
#         margin: 20px auto;
#         text-align: center;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# Load the model
model_path = os.path.join(os.path.dirname(__file__), "..", "model", "NBClassifier.pkl")
with open(model_path, "rb") as f_in:
    model = pickle.load(f_in)

# Main container
with st.container():
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.title("Crop Recommendation")

    # Create form inputs
    with st.form(key='crop_form'):
        n = st.text_input("N (Nitrogen content in soil):")
        p = st.text_input("P (Phosphorus content in soil):")
        k = st.text_input("K (Potassium content in soil):")
        temperature = st.text_input("Temperature (in Celsius):")
        humidity = st.text_input("Humidity (in %):")
        ph = st.text_input("pH level of soil:")
        rainfall = st.text_input("Rainfall (in mm):")

        # Submit button
        submit_button = st.form_submit_button(label="Predict")

    # Handle form submission
    if submit_button:
        # Ensure all inputs are filled
        if n and p and k and temperature and humidity and ph and rainfall:
            # Convert inputs to float and prepare for prediction
            form_values = [float(n), float(p), float(k), float(temperature), float(humidity), float(ph), float(rainfall)]
            data = np.array([form_values])
            
            # Get prediction from the model
            prediction = model.predict(data)
            output = prediction[0]
            
            # Display prediction result
            st.markdown(f"<h2>Recommended crop is {output}</h2>", unsafe_allow_html=True)
        else:
            st.markdown("<h2>Please fill in all fields.</h2>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

