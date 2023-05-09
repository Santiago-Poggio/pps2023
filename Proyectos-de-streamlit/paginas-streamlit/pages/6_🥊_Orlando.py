import streamlit as st

f = open ('./hobbys-todos/mihobby-orlando.md', 'r')
hobby = f.read()
st.write(hobby)
f.close()