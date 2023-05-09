import streamlit as st

st.title("Bienvenidos a nuestros repositorios👋")

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["🎮Diego","🎨Franco","🚲Toto","🕹️Santiago","⚽Saigua","🥊Orlando","🚴Enzo","🏐Milagros"])

with tab1:
    f = open ('./hobbys-todos/mihobby-diego.md', 'r')
    hobby = f.read()
    st.write(hobby)
    f.close()

with tab2:
    f = open ('./hobbys-todos/myhobby-franco.md', 'r')
    hobby = f.read()
    st.write(hobby)
    f.close()

with tab3:
    f = open ('./hobbys-todos/mihobby-toto.md', 'r')
    hobby = f.read()
    st.write(hobby)
    f.close()

with tab4:
    f = open ('./hobbys-todos/mihobby-santiago.md', 'r')
    hobby = f.read()
    st.write(hobby)
    f.close()

with tab5:
    f = open ('./hobbys-todos/mihobby-saigua.md', 'r')
    hobby = f.read()
    st.write(hobby)
    f.close()

with tab6:
    f = open ('./hobbys-todos/mihobby-orlando.md', 'r')
    hobby = f.read()
    st.write(hobby)
    f.close()

with tab7:
    f = open ('./hobbys-todos/mihobby-enzo.md', 'r')
    hobby = f.read()
    st.write(hobby)
    f.close()

with tab8:
    f = open ('./hobbys-todos/mihobby-milagros.md', 'r')
    hobby = f.read()
    st.write(hobby)
    f.close()
