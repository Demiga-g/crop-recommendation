# pylint: disable=no-member
# from st_pages import get_nav_from_toml
from datetime import datetime

import streamlit as st

st.set_page_config(layout="centered")

# nav = get_nav_from_toml(".streamlit/pages_sections.toml")

pg = st.navigation(
    [
        st.Page("home.py", title="About", icon="🌿"),
        st.Page("app_content.py", title="Toolkit", icon="💻"),
    ]
)

# copyright section
current_year = datetime.now().year
st.sidebar.markdown(
    f"""
    <div>
        <br><br><br><br><br><br>
        <b>© {current_year} Midega George</b>
    </div>
    """,
    unsafe_allow_html=True,
)

pg.run()
