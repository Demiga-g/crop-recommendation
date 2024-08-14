# pylint: disable=no-member
# from st_pages import get_nav_from_toml

import streamlit as st

st.set_page_config(layout="centered")

# nav = get_nav_from_toml(".streamlit/pages_sections.toml")

pg = st.navigation(
    [
        st.Page("home.py", title="About", icon="🌿"),
        st.Page("app_content.py", title="Toolkit", icon="💻"),
    ]
)

pg.run()
