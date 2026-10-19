import pandas as pd
import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np

@st.cache_data
def load_data(nrows=1000):
    return pd.read_csv("https://raw.githubusercontent.com/softbytavz/Bici_data/refs/heads/main/citibike-tripdata.csv")

bici_data = load_data()
horas = pd.to_datetime(bici_data["started_at"]).dt.hour
st.header("Uso de bicicletas")
st.dataframe(bici_data)


if st.sidebar.checkbox("View RAW data"):
    st.subheader("Cicles Rides in NYC")
    st.write(f"Total de registros: {len(bici_data)}")
    st.dataframe(bici_data)

if st.sidebar.checkbox("Recorridos por hora"):
    recorridos_por_hora = horas.value_counts().reindex(range(24), fill_value=0)
 
    st.subheader("Numero de recorridos por hora")
    plt.figure(figsize=(10, 4))
    plt.bar(recorridos_por_hora.index, recorridos_por_hora.values, color="#4C78A8")
    plt.xticks(range(0, 24), rotation=90)
    plt.xlabel("Hora del día")
    plt.ylabel("Número de recorridos")
    st.pyplot(plt)

if st.sidebar.checkbox("Mapa"):
    hora = st.sidebar.slider("hour", 0, 23, 11)
 
    # Solo los recorridos de la hora del slider
    filtered_data = bici_data[horas == hora]
 
    # start_lat -> lat y start_lng -> lon
    filtered_data = filtered_data.rename(columns={"start_lat": "lat", "start_lng": "lon"})
 
    st.subheader(f"Mapa de recorridos iniciados a las {hora}:00")
    st.map(filtered_data.dropna(subset=["lat", "lon"]))


st.header("Integrantes del equipo")
st.write("Calderón Aquino Antonio Yaset")
st.write("González Sánchez Donovan")
st.write("Vega Romero Miguel Ángel")
st.write("Zepahua Xotlanihua Luis Enrique")
    