# pylint: disable=no-member
import streamlit as st

st.title("The Crop Recommendation App")

st.markdown(
    """
### About the App!

This application is designed to assist farmers and agricultural professionals in making
informed decisions about which crops to plant based on specific environmental conditions.

### Features:

- Enter soil nutrient levels (Nitrogen, Phosphorus, Potassium) and environmental factors
(Temperature, Humidity, pH, Rainfall).
- Get a recommendation for the best crop to plant.
- View detailed growing conditions and related pests and diseases for the recommended crop.

*Use the sidebar to navigate to the "Toolkit" page and start using the app.*

### Disclaimer

*This is a proof of concept application in which the recommendations provided are based
on data and models that analyze specific environmental factors such as soil content, temperature, 
humidity, and rainfall. Therefore, the outputs are intended for informational purposes
only and should not be considered as professional agricultural guidance.*
"""
)
