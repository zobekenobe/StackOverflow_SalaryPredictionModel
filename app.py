import streamlit as st
import numpy as np
from about import show_about
from model import show_predict
from aboutme import show_me


st.set_page_config(page_title = 'Stackoverflow Salary (2022) Prediction', layout = 'centered')


page = st.sidebar.selectbox(label = 'Page', options = ['About', 'Predict', 'About Me'])
if page == 'About':
    show_about()
elif page == 'Predict':
    show_predict()
elif page == 'About Me':
    show_me()
