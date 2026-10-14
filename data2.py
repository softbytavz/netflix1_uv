import pandas as pd
import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np

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

if st.sidebar.checkbox("Recorridos por hora"):
    hora = st.sidebar.slider("hour", 0, 23, 17)

    horas = pd.to_datetime(bici_data["started_at"]).dt.hour

   
    recorridos_por_hora = horas.value_counts().reindex(range(24), fill_value=0)

    
    colores = ["blue"] * 24
    colores[hora] = "red"

    plt.figure()
    plt.bar(recorridos_por_hora.index, recorridos_por_hora.values, color=colores)
    plt.xticks(range(0, 24))
    plt.title("Número de recorridos por hora")
    plt.xlabel("Hora del día")
    plt.ylabel("Total de recorridos")
    st.pyplot(plt)

if st.sidebar.checkbox("Mapa"):
    hora = st.sidebar.slider("hour", 0, 23, 11)
    bici_data.rename({"start_lat": 'lat', "start_lng": 'lon'}, inplace=True)
    map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [40.730610, -73.935242], columns = ['lat', 'lon'])
    st.subheader("Mapa de recorridos")
    st.map(map_data)

st.header("Integrantes del equipo")
st.write("Calderón Aquino Antonio Yaset")
st.write("González Sánchez Donovan")
st.write("Vega Romero Miguel Ángel")
st.write("Zepahua Xotlanihua Luis Enrique")
    