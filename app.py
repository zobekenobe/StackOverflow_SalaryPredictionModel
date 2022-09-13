import streamlit as st
from model import show_predict


st.set_page_config(page_title = 'Stackoverflow Salary (2022) Prediction', layout = 'centered')
page = st.sidebar.selectbox(label = 'Page', options = ['About', 'Predict', 'about me'])
if page == 'Predict':
    show_predict()
