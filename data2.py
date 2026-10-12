import pandas as pd
import streamlit as st 
import matplotlib.pyplot as plt

@st.cache_data
def load_data(nrows=1000):
    return pd.read_csv("https://raw.githubusercontent.com/softbytavz/Bici_data/refs/heads/main/citibike-tripdata.csv")

bici_data = load_data()

st.header("Uso de bicicletas")
st.dataframe(bici_data)


if st.sidebar.checkbox("View RAW data"):
    st.subheader("Cicles Rides in NYC")
    st.write(f"Total de registros: {len(bici_data)}")
    st.dataframe(bici_data)