import streamlit as st
import time

st.set_page_config(layout="centered", page_title="Trabajo")

# Estilo para los botones grandes y el parpadeo
st.markdown("""
    <style>
    div.stButton > button {
        height: 150px; width: 100%; font-size: 30px; border-radius: 15px;
        color: white; font-weight: bold; margin-bottom: 10px;
    }
    /* Colores base */
    .btn-parada { background-color: #0000FF; }
    .btn-manilla { background-color: #008000; }
    .btn-emisora { background-color: #FFA500; }
    .btn-libre { background-color: #808080; }
    
    /* El efecto al pulsar (Flash Verde) */
    div.stButton > button:active { background-color: #00FF00 !important; }
    </style>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("PARADA", key="p"):
        st.toast("Registrado: PARADA")
        # Aquí es donde se conectará conmigo
    if st.button("EMISORA", key="e"):
        st.toast("Registrado: EMISORA")

with col2:
    if st.button("MANILLA", key="m"):
        st.toast("Registrado: MANILLA")
    if st.button("LIBRE", key="l"):
        st.toast("Registrado: LIBRE")

st.divider()
c1, c2, c3, c4 = st.columns(4)
c1.button("FOTO")
c2.button("MICRO")
c3.button("CAFE")
c4.button("FIN")
