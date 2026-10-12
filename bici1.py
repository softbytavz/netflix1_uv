import pandas as pd
import streamlit as st 
import matplotlib.pyplot as plt

@st.cache_data
def load_data(nrows=500):
    return pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/movies.csv",nrows=nrows,encoding="latin-1")

bici_data = load_data()