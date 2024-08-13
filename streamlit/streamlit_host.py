import numpy as np

import streamlit as st
from mlops.crop_data import crop_info as crop_data
from mlops.utility_functions import load_model

# Get model
model = load_model("SVM")

# Set up the page configuration
st.set_page_config(page_title='Crop Recommendation', layout='centered')

st.title('Crop Recommendation')

# Initialize session state
if 'recommendation' not in st.session_state:
    st.session_state.recommendation = None
if 'show_more' not in st.session_state:
    st.session_state.show_more = False

col_input_1, col_input_2, col_input_3 = st.columns(3)

with st.form(key='crop_form'):
    with col_input_1:
        N = st.number_input(
            'N (Nitrogen content in soil):',
            min_value=0,
            max_value=150,
            value=None,
            placeholder='0',
            help='Insert values between 0 and 150',
        )
        P = st.number_input(
            'P (Phosphorus content in soil):',
            min_value=0,
            max_value=155,
            value=None,
            placeholder='0',
            help='Insert values between 0 and 155',
        )
        K = st.number_input(
            'K (Potassium content in soil):',
            min_value=0,
            max_value=210,
            value=None,
            placeholder='0',
            help='Insert values between 0 and 210',
        )

    with col_input_2:
        temperature = st.number_input(
            'Temperature (in Celsius):',
            min_value=5.0,
            max_value=50.0,
            value=None,
            placeholder='0.0',
            help='Insert values between 5.0 and 50.0',
        )
        humidity = st.number_input(
            'Humidity (in %):',
            min_value=10.00,
            max_value=100.00,
            value=None,
            placeholder='0.00',
            help='Insert values between 10.0 and 100.0',
        )
    with col_input_3:
        ph = st.number_input(
            'pH level of soil:',
            min_value=3.0,
            max_value=10.5,
            value=None,
            placeholder='0.0',
            help='Insert values between 0 and 10.5',
        )
        rainfall = st.number_input(
            'Rainfall (in mm):',
            min_value=19.5,
            max_value=300.0,
            value=None,
            placeholder='0.0',
            help='Insert values between 19.5 and 300.0',
        )

    submit_button = st.form_submit_button(label='Predict')

# Handle form submission
if submit_button:
    required_inputs = [N, P, K, temperature, humidity, ph, rainfall]

    if all(required_inputs):
        try:
            form_values = [float(value) for value in required_inputs]
            data = np.array([form_values])

            prediction = model.predict(data)
            output = prediction[0]

            st.session_state.recommendation = output
            st.session_state.show_more = False

        except ValueError:
            st.error('Please ensure all inputs are valid numbers.')
    else:
        st.warning('Please fill in all fields.')

# Display recommendation and growing conditions
if st.session_state.recommendation:
    st.write(f'Recommended crop is {st.session_state.recommendation}')

    # "Show More Suggestions" button
    if st.button("Show More Suggestions"):
        st.session_state.show_more = True

# Display more suggestions if button was clicked
if st.session_state.show_more:
    if st.session_state.recommendation.lower() in crop_data:
        info = crop_data[st.session_state.recommendation.lower()]
        st.subheader(
            f"Additional Growing Conditions for {st.session_state.recommendation.capitalize()}:"
        )
        for key, value in info.items():
            st.markdown(f"**{key}:** {value}")
    else:
        st.warning("No specific growing information available for this crop.")
