import streamlit as st

# Page Title
st.title('Alishba Data Analyst Pakistan')

# Page Subtitle
st.header('Welcome to the Streamlit Application')

# Description
st.write("This is a simple Streamlit application created by Alishba, a data analyst from Pakistan. "
         "Feel free to explore the features!")

# Interactive Logo
st.image("alishba_logo.png", use_column_width=True)

# Picture Uploader Button
uploaded_file = st.file_uploader("Upload a picture", type=["jpg", "jpeg", "png"])

# Display uploaded picture
if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Image Uploaded Successfully!")
