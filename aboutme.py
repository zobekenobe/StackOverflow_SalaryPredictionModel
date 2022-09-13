import streamlit as st
from PIL import Image
image = Image.open('me.jpeg')

def show_me():
    st.image(image, width = 300 )
    st.header('Zoheb Khan')
    st.markdown("Hi, Im a computational research scientist working as Post-Doctoral research Fellow at the University College Dublin in the School of Chemical and Bioprocess Engineering")
    st.markdown("I use computational fluid dynamics and artificial intelligence to simulate and study flow fields in membrane separators")
    st.markdown("I love spending time outdoors and when not in the lab, I cycle, run and play badminton")
    st.markdown("To get in touch or know more about professional work, connect with me on LinkedIn @ https://www.linkedin.com/in/zobekenobe/")