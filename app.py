import streamlit as st
import numpy as np
from about import show_about
from model import show_predict


st.set_page_config(page_title = 'Stackoverflow Salary (2022) Prediction', layout = 'centered')

show_about()
page = st.sidebar.selectbox(label = 'Page', options = ['About', 'Predict', 'about me'])
if page == 'Predict':
    show_predict()
