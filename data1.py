import streamlit as st
import pandas as pd

@st.cache_data
def load_data(nrows=500):
    return pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/movies.csv",nrows=nrows,encoding="latin-1")

movies_data = load_data()

st.header("Netflix_Data")
st.dataframe(movies_data)

# 1. Checkbox: mostrar todos los filmes
if st.sidebar.checkbox("Mostrar todos los filmes"):
    st.subheader("Todos los filmes")
    st.write(f"Total filmes: {len(movies_data)}")
    st.dataframe(movies_data)

# 2. Buscar por título (que contenga, sin importar mayúsculas)
def filtrar_por_titulo(df, texto):
    return df[df["name"].str.contains(texto, case=False, na=False, regex=False)]

titulo = st.sidebar.text_input("Título del filme:")
if st.sidebar.button("Buscar filmes"):
    resultado = filtrar_por_titulo(movies_data, titulo)
    st.subheader("Resultado de la búsqueda")
    st.write(f"Total filmes: {len(resultado)}")
    st.dataframe(resultado)

# 3. Filtrar por director
def filtrar_por_director(df, director):
    return df[df["director"] == director]

director = st.sidebar.selectbox(
    "Seleccionar Director",
    sorted(movies_data["director"].dropna().unique())
)
if st.sidebar.button("Filtrar director"):
    resultado = filtrar_por_director(movies_data, director)
    st.subheader(f"Filmes de {director}")
    st.write(f"Total filmes: {len(resultado)}")
    st.dataframe(resultado)