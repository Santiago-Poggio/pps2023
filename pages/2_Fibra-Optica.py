import streamlit as st
import pandas as pd
import plotly.express as px

conexiones = ""
conexiones = pd.read_csv("./ciencia_de_datos_en_escuelas/conectividad_argentina/Conectividad_Internet.csv")
FIBRAOPTICA=conexiones['FIBRAOPTICA'].value_counts().rename_axis('FIBRAOPTICA').reset_index(name='Localidades')
FIBRAOPTICA.style.hide(axis='index') 
st.write (FIBRAOPTICA)

torta = px.pie(FIBRAOPTICA, values='Localidades', names='Localidades', title='Cantidad de localidades con Fibra Optica', width=800, height=800)
st.write(torta)