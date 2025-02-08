import streamlit as st
import pandas as pd

st.title('hello this is PY SUBEER')
st.audio("D:\Bezubaan Phir Se Reprise Abcd 2 320 Kbps.mp3")
st.warning('This is a warning')

# Collect feedback from users
feedback = st.text_area('Please provide your feedback here:')
if feedback:
    st.write('Thank you for your feedback!')

st.video('https://www.youtube.com/watch?v=_p0lDxPqJiM')