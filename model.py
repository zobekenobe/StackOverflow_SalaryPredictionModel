import streamlit as st
import numpy as np
import pandas as pd
import pickle

# import the model
with open('project.pkl', 'rb') as file:
    data = pickle.load(file)

model = data[0]
country_encoder = data[1]
ethnicity_encoder = data[2]
educational_mapping = data[3]

# read in data
def show_predict():
    with st.form('Enter the variables here'):
        experience = st.slider(label = 'Years of Coding Experience', min_value = 0.5, max_value = 50.0, step = 1.0, value = 6.0)
        country = st.selectbox(label = 'Country', options = country_encoder.classes_)
        ethinicity = st.selectbox(label = 'Ethnicity', options = ethnicity_encoder.classes_)
        education  = st.selectbox(label = 'Educational Qualification', options = 
        ['Bachelor’s degree (B.A., B.S., B.Eng., etc.)',
       'Master’s degree (M.A., M.S., M.Eng., MBA, etc.)',
       'Some college/university study without earning a degree',
       'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)',
       'Associate degree (A.A., A.S., etc.)',
       'Professional degree (JD, MD, etc.)',
       'Other doctoral degree (Ph.D., Ed.D., etc.)',
       'I never completed any formal education',
       'Primary/elementary school'])

        #    encoding all the values
        c  = country_encoder.transform([country])
        ex = experience
        et = ethnicity_encoder.transform([ethinicity])
        ed = educational_mapping[education]

        x = np.array([[c, ex, et, ed]])
        
        submitted = st.form_submit_button('Calculate')
    if submitted:
        prediction = model.predict(x)
        st.markdown(f'The estimated salary is **€{prediction[0] : 0.4f}**')
