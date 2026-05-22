import streamlit as st
import requests
import pandas as pd
import folium
from streamlit_folium import st_folium

# =========================
# HEADER
# =========================
def show_header(text_title: str):
    col1, col2 = st.columns([1, 6])
    
    with col1:
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/3/32/Universidad_Panamericana_Logo_Dorado.jpg",
            width=90
        )
        
    with col2:
        st.title(text_title)
        st.caption("📘 Business Intelligence - Streamlit Dashboard")
        st.caption("Universidad Panamericana")


# =========================
# DATA LOAD FUNCTION
# =========================
@st.cache_data
def load_data(url):
    pagina = requests.get(url).json()
    ligas = pagina['data']['es']['feeds']

    # Filtrar estaciones
    ligas_estaciones = [l for l in ligas if 'station' in l['name']]

    liga1 = ligas_estaciones[0]
    liga2 = ligas_estaciones[1]

    data1 = requests.get(liga1['url']).json()['data']['stations']
    data2 = requests.get(liga2['url']).json()['data']['stations']

    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)

    cols = ['station_id', 'name', 'lat', 'lon', 'capacity']
    df1 = df1.reindex(columns=cols)
    df2 = df2.reindex(columns=cols)

    df = pd.concat([df1, df2], ignore_index=True)
    df = df.dropna(subset=['lat', 'lon'])

    return df


# =========================
# UI
# =========================
head_c = st.container()
main_c = st.container()

with head_c:
    show_header("Mi Dashboard de Estaciones")

# URL base (la que ya usas tú)
url = st.text_input("Ingresa URL del dataset", "")

if url:
    df = load_data(url)

    with main_c:
        st.subheader("📊 Datos cargados")
        st.dataframe(df)

        st.subheader("🗺️ Mapa de estaciones")

        centro_lat = df['lat'].mean()
        centro_lon = df['lon'].mean()

        mapa = folium.Map(location=[centro_lat, centro_lon], zoom_start=12)

        for _, row in df.iterrows():
            folium.Marker(
                location=[row['lat'], row['lon']],
                popup=row['name']
            ).add_to(mapa)

        st_folium(mapa, width=700, height=500)
