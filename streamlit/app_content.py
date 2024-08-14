# pylint: disable=no-member
import warnings

import numpy as np

import streamlit as st
from mlops.crop_data import crop_info as crop_data
from mlops.utility_functions import load_model

warnings.filterwarnings('ignore')


st.title("Recommendation Toolkit")

st.markdown('---')

# Initialize session state
if 'recommendation' not in st.session_state:
    st.session_state.recommendation = None

col_input_1, col_input_2, col_input_3 = st.columns(3)

with st.form(key='crop_form', border=False):
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

    submit_button = st.form_submit_button(
        label='Recommend', type='primary', use_container_width=True
    )

st.markdown('---')

# get model
model = load_model("SVM")

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

        except ValueError:
            st.error('Please ensure all inputs are valid numbers.')
    else:
        st.warning('Please fill in all fields.')

# show recommended crop and other growth conditions
if st.session_state.recommendation:
    st.markdown(
        f"""
        <h3>
            Recommended crop is
            <span style="color:yellow">
                {st.session_state.recommendation}
            </span>
        </h3>
        """,
        unsafe_allow_html=True,
    )

    with st.expander("Expand for more"):
        if st.session_state.recommendation.lower() in crop_data:
            info = crop_data[st.session_state.recommendation.lower()]
            st.subheader(
                f"Optimal Harvest of {st.session_state.recommendation.capitalize()} may require:"
            )
            for key, value in info.items():
                st.markdown(f"**{key}:** {value}")
        else:
            st.warning(
                "No specific growing information available for this crop."
            )
