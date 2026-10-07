import streamlit as st
import pandas as pd

@st.cache_data
def load_data(nrows=500):
    return pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/movies.csv",nrows=nrows,encoding="latin-1")

movies_data = load_data()

st.header("Data Description")
st.dataframe(movies_data)