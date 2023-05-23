import streamlit as st
import pandas as pd
import plotly.express as px
conexiones = ""
conexiones = pd.read_csv("./ciencia_de_datos_en_escuelas/conectividad_argentina/Conectividad_Internet.csv")
conexiones.head(20)
st.write(conexiones.head(20))
SATELITAL=conexiones['SATELITAL'].value_counts().rename_axis('SATELITAL').reset_index(name='Localidades')
SATELITAL.style.hide(axis='index') 
st.write(SATELITAL)