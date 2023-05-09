import streamlit as st

f = open ('./hobbys-todos/mihobby-saigua.md', 'r')
hobby = f.read()
st.write(hobby)
f.close()