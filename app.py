import streamlit as st
import numpy as np
from model import show_predict


st.set_page_config(page_title = 'Stackoverflow Salary (2022) Prediction', layout = 'centered')

st.title('Predicting Salaries of Software Developers')
st.subheader('The StackOverflow Dataset for 2020 was used')
st.write('https://insights.stackoverflow.com/survey/2020')

st.write('The user enters the Years of Experience, the country they have worked in, their ethnicity and their highest educational qualification')
st.write('The model then predicts the salary in euros')

st.write('Select the "Predict" page to make predictions')
st.write('To know more about me, go to the "About me" page')
page = st.sidebar.selectbox(label = 'Page', options = ['About', 'Predict', 'about me'])
if page == 'Predict':
    show_predict()
