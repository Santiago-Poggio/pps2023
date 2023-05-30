import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

conexiones = ""
conexiones = pd.read_csv("./ciencia_de_datos_en_escuelas/conectividad_argentina/Conectividad_Internet.csv")

C4G=conexiones['4G'].value_counts().rename_axis('4G').reset_index(name='Localidades')
C4G.style.hide(axis='index') 
st.write (C4G)

torta = px.pie(C4G, values='Localidades', names='Localidades', title='Cantidad de localidades con 4G', width=800, height=800)
st.write (torta)

mapa_4G = conexiones[["4G","Latitud","Longitud"]]
si = ['SI']
mask = mapa_4G[mapa_4G['4G'].isin(si)]


fig = go.Figure(data=go.Scattergeo(
    lon = mask['Longitud'],
    lat = mask['Latitud'],
    text = mask,
    mode = 'markers',
    ))

fig.update_layout(
        title = '4G locations',
        geo_scope='south america',
    )
fig.update_geos(fitbounds="locations") 
st.write(fig)
