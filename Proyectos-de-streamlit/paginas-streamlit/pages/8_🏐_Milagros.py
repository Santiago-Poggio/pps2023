import streamlit as st

f = open ('./hobbys-todos/mihobby-milagros.md', 'r')
hobby = f.read()
st.write(hobby)
f.close()