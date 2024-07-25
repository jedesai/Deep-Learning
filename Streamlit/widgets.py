import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your name:")

age = st.slider("Select your age:",0,100,25) # (string,lower limit, upper limit, default)

st.write(f"Your age is {age}.")

options = ['python', 'java', 'C++', 'javascript']
choice = st.selectbox("Choose your favorite language:", options)
st.write(f"You selected {choice}.")

if name:
    st.write(f"Hello, {name}")

data = {
    "Name": ['john', 'jane', 'jake', 'jill'],
    "Age": [28, 24, 35, 40],
    "City": ["New york", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)