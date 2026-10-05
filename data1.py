import pandas as pd
import str
netflix_data = pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/movies.csv", encoding='utf-8')
st.dataframe(netflix_data)


