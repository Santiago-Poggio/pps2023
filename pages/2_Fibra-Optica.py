import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

conexiones = ""
conexiones = pd.read_csv("./ciencia_de_datos_en_escuelas/conectividad_argentina/Conectividad_Internet.csv")
FIBRAOPTICA=conexiones['FIBRAOPTICA'].value_counts().rename_axis('FIBRAOPTICA').reset_index(name='Localidades')
FIBRAOPTICA.style.hide(axis='index') 
st.write (FIBRAOPTICA)

torta = px.pie(FIBRAOPTICA, values='Localidades', names='Localidades', title='Cantidad de localidades con Fibra Optica', width=800, height=800)
st.write(torta)

mapa_Fibra = conexiones[["FIBRAOPTICA","Latitud","Longitud"]]
si = ['SI']
mask1 = mapa_Fibra[mapa_Fibra['FIBRAOPTICA'].isin(si)]

fig = go.Figure(data=go.Scattergeo(
        lon = mask1['Longitud'],
        lat = mask1['Latitud'],
        text = mask1,
        mode = 'markers',
        ))

fig.update_layout(
        title = 'Fibraoptica locations',
        geo_scope='south america',
    )
fig.update_geos(fitbounds="locations") 
st.write(fig)
