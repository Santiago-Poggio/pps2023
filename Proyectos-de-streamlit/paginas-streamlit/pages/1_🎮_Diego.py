import streamlit as st

f = open ('./hobbys-todos/mihobby-diego.md', 'r')
hobby = f.read()
st.write(hobby)
f.close()