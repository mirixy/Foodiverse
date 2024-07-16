import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from backend.modules.llm import foodgpt
from backend.main import FoodGPT
import pandas as pd

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

food_data = st.Page(
    "webpages/food_items.py",
    title="Food Data",
    icon=":material/database:"
)

analysis = st.Page(
    "webpages/analysis.py",
    title="Recipe Analysis",
    icon=":material/database:"
)

# Navigation
pg = st.navigation({"Menu": [home, about, food_data], "Analysis": [analysis]})

pg.run()




# Get LLM Response
