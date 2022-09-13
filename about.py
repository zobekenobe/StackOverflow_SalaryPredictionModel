import streamlit as st

def show_about():
    st.title('Predicting Salaries of Software Developers')
    st.subheader('The StackOverflow Dataset for 2020 was used')
    st.write('https://insights.stackoverflow.com/survey/2020')

    st.write('The user enters the Years of Experience, the country they have worked in, their ethnicity and their highest educational qualification')
    st.write('The model then predicts the salary in euros')

    st.write('Select the "Predict" page to make predictions')
    st.write('To know more about me, go to the "About me" page')