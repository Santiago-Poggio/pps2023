import streamlit as st
import pandas as pd
import plotly.express as px

conexiones = ""
conexiones = pd.read_csv("./ciencia_de_datos_en_escuelas/conectividad_argentina/Conectividad_Internet.csv")

SATELITAL=conexiones['SATELITAL'].value_counts().rename_axis('SATELITAL').reset_index(name='Localidades')
SATELITAL.style.hide(axis='index') 
st.write(SATELITAL)

torta = px.pie(SATELITAL, values='Localidades', names='Localidades', title='Cantidad de localidades con conectividad satelital', width=800, height=800)
st.write(torta)