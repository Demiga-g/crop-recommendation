# pylint: disable=no-member
from st_pages import get_nav_from_toml

import streamlit as st

st.set_page_config(layout="wide")

nav = get_nav_from_toml("pages_sections.toml")

pg = st.navigation(nav)

pg.run()
