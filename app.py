import streamlit as st

st.title("My Webpage Built from the Browser!")
st.write("Hello world! This app was built without using a terminal.")

slider_val = st.slider("Move the slider:", 0, 100, 50)
st.write(f"The slider is at: {slider_val}")
