import streamlit as st
import requests
import pandas as pd
import folium
from streamlit_folium import st_folium


# =========================
# HEADER
# =========================
def show_header(title):
    col1, col2 = st.columns([1, 6])

    with col1:
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/3/32/Universidad_Panamericana_Logo_Dorado.jpg",
            width=90
        )

    with col2:
        st.title(title)
        st.caption("📘 Ecobici Dashboard - Business Intelligence")


# =========================
# CARGA DE DATOS GBFS
# =========================
@st.cache_data
def load_ecobici():

    url = "https://gbfs.mex.lyftbikes.com/gbfs/gbfs.json"

    data = requests.get(url).json()
    feeds = data["data"]

    # idioma dinámico
    lang = list(feeds.keys())[0]
    feeds_list = feeds[lang]["feeds"]

    station_info_url = None
    station_status_url = None

    for f in feeds_list:
        if "station_information" in f["name"]:
            station_info_url = f["url"]
        if "station_status" in f["name"]:
            station_status_url = f["url"]

    # descargar datos
    info = requests.get(station_info_url).json()["data"]["stations"]
    status = requests.get(station_status_url).json()["data"]["stations"]

    df_info = pd.DataFrame(info)
    df_status = pd.DataFrame(status)

    # merge
    df = df_info.merge(df_status, on="station_id")

    return df


# =========================
# APP UI
# =========================
head = st.container()
main = st.container()

with head:
    show_header("🚲 Ecobici CDMX Dashboard")

df = load_ecobici()

with main:

    st.subheader("📊 Datos de estaciones")
    st.dataframe(df)

    st.subheader("🗺️ Mapa de estaciones")

    # centro mapa
    centro_lat = df["lat"].mean()
    centro_lon = df["lon"].mean()

    mapa = folium.Map(location=[centro_lat, centro_lon], zoom_start=12)

    for _, row in df.iterrows():
        folium.Marker(
            location=[row["lat"], row["lon"]],
            popup=f"{row['name']}"
        ).add_to(mapa)

    st_folium(mapa, width=700, height=500)
    
