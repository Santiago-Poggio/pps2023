import streamlit as st
import pandas as pd
import plotly.express as px

conexiones = ""
conexiones = pd.read_csv("./ciencia_de_datos_en_escuelas/conectividad_argentina/Conectividad_Internet.csv")

C4G=conexiones['4G'].value_counts().rename_axis('4G').reset_index(name='Localidades')
C4G.style.hide(axis='index') 
st.write (C4G)

torta = px.pie(C4G, values='Localidades', names='Localidades', title='Cantidad de localidades con 4G', width=800, height=800)
st.write (torta)