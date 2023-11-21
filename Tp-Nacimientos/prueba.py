
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Nacimiento ")
nacimientos = pd.read_csv("nacidos-vivos-registrados-en-la-republica-argentina-deis-entre-los-anos-2005-2021.csv", encoding='latin-1') #si se usa windows usa latin-1, sino se debe utilizar UTF-8
st.write(nacimientos.head())
nacimientos = nacimientos[["anio","edad_madre_grupo","instruccion_madre","Sexo","nacimientos_cantidad"]]
nac_edad_madre = nacimientos[["anio","edad_madre_grupo","nacimientos_cantidad"]]
nac_edad_madre = nac_edad_madre.groupby(["anio","edad_madre_grupo"]).sum()
#st.write(nac_edad_madre.head())
nac_edad_madre2 = nac_edad_madre.groupby(["edad_madre_grupo"]).sum()
st.write(nac_edad_madre2)
nac_edad_madre = nac_edad_madre.unstack()
grafico = nac_edad_madre.plot(kind= "line",figsize= (30,15),grid=True)
plt.legend(["Menor de 15", "15 a 19", "20 a 24", "25 a 29", "30 a 34", "35 a 39", "40 a 44", "De 45 y más"])
grafico.figure
nac_madre_menor_20 = nacimientos[["edad_madre_grupo","nacimientos_cantidad"]]
nac_madre_menor_20["edad_madre_grupo"].unique()
torta = nac_madre_menor_20.groupby("edad_madre_grupo")["nacimientos_cantidad"].count().plot(kind='pie')
torta.figure
