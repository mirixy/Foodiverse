import os
import sys
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st

# Pages
home = st.Page(
    "webpages/home.py",
    title="Home",
    icon=":material/home:"
)

about = st.Page(
    "webpages/about.py",
    title="About",
    icon=":material/info:"
)


analysis = st.Page(
    "webpages/analysis.py",
    title="Recipe Analysis",
    icon=":material/database:"
)

find_recipe = st.Page(
    "webpages/spoonview.py",
    title="Find Recipe",
    icon=":material/search:"
)

# Navigation
pg = st.navigation({"Menu": [home, about]})

pg.run()




# Get LLM Response

