import streamlit as st

import requests

st.title("Bienvenidos a nuestros repositorios👋")

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["🎮Diego","🎨Franco","🚲Toto","🕹️Santiago","⚽Saigua","🥊Orlando","🚴Enzo","🏐Milagros"])

with tab1:
    request = requests.get('https://raw.githubusercontent.com/LizardyOrlando/Grupo-mi-hobby/main/streamlit-python/hobbys-todos/mihobby-diego.md')
    st.write(request.text)

with tab2:
    request = requests.get('https://raw.githubusercontent.com/LizardyOrlando/Grupo-mi-hobby/main/streamlit-python/hobbys-todos/myhobby-franco.md')
    st.write(request.text)

with tab3:
    request = requests.get('https://raw.githubusercontent.com/LizardyOrlando/Grupo-mi-hobby/main/streamlit-python/hobbys-todos/mihobby-toto.md')
    st.write(request.text)

with tab4:
    request = requests.get('https://raw.githubusercontent.com/LizardyOrlando/Grupo-mi-hobby/main/streamlit-python/hobbys-todos/mihobby-santiago.md')
    st.write(request.text)

with tab5:
    request = requests.get('https://raw.githubusercontent.com/LizardyOrlando/Grupo-mi-hobby/main/streamlit-python/hobbys-todos/mihobby-saigua.md')
    st.write(request.text)

with tab6:
    request = requests.get('https://raw.githubusercontent.com/LizardyOrlando/Grupo-mi-hobby/main/streamlit-python/hobbys-todos/mihobby-orlando.md')
    st.write(request.text)

with tab7:
    request = requests.get('https://raw.githubusercontent.com/LizardyOrlando/Grupo-mi-hobby/main/streamlit-python/hobbys-todos/mihobby-enzo.md')
    st.write(request.text)

with tab8:
    request = requests.get('https://raw.githubusercontent.com/LizardyOrlando/Grupo-mi-hobby/main/streamlit-python/hobbys-todos/mihobby-milagros.md')
    st.write(request.text)
