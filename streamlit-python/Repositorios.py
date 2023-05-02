import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title="Repositorios",
        options=["Diego","Franco","Toto","Santiago","Saigua","Orlando","Enzo","Milagros"],
        icons=["controller","brush-fill","bicycle","controller","circle-fill","emoji-wink","bicycle","circle-half"],
        menu_icon="layout-sidebar-inset",
        default_index=0,
    )
if selected == "Diego":
    f = open ('./hobbys-todos/mihobby-diego.md', 'r')
    hobby = f.read()
    st.write(hobby)
if selected == "Franco":
    f = open ('./hobbys-todos/myhobby-franco.md', 'r')
    hobby = f.read()
    st.write(hobby)
if selected == "Toto":
    f = open ('./hobbys-todos/mihobby-toto.md', 'r')
    hobby = f.read()
    st.write(hobby)
if selected == "Santiago":
    f = open ('./hobbys-todos/mihobby-santiago.md', 'r')
    hobby = f.read()
    st.write(hobby)
if selected == "Saigua":
    f = open ('./hobbys-todos/mihobby-saigua.md', 'r')
    hobby = f.read()
    st.write(hobby)
if selected == "Orlando":
    f = open ('./hobbys-todos/mihobby-orlando.md', 'r')
    hobby = f.read()
    st.write(hobby)
if selected == "Enzo":
    f = open ('./hobbys-todos/mihobby-enzo.md', 'r')
    hobby = f.read()
    st.write(hobby)
if selected == "Milagros":
    f = open ('./hobbys-todos/mihobby-milagros.md', 'r')
    hobby = f.read()
    st.write(hobby)


