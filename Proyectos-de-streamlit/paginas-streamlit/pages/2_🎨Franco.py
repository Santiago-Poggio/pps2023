import streamlit as st

f = open ('./hobbys-todos/myhobby-franco.md', 'r')
hobby = f.read()
st.write(hobby)
f.close()