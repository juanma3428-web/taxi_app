import streamlit as st
import requests
from datetime import datetime

st.set_page_config(layout="centered", page_title="Taxi Bilbao")

# --- ESTILO PARA QUE LOS BOTONES REALES SEAN INVISIBLES Y SE AJUSTEN AL DISEÑO ---
st.markdown("""
    <style>
    .block-container { padding: 10px 5px !important; }
    header, footer { visibility: hidden; }

    /* Contenedor de la rejilla visual */
    .contenedor-visual {
        display: grid; grid-template-columns: 1fr 1fr; gap: 10px; padding: 5px;
        position: absolute; width: 100%; z-index: 1;
    }
    .casilla {
        height: 160px; border-radius: 15px; display: flex; align-items: center;
        justify-content: center; color: white; font-size: 22px; font-weight: bold;
    }
    .azul { background-color: #0000FF; } .verde { background-color: #008000; }
    .naranja { background-color: #FFA500; } .gris { background-color: #808080; }

    /* Hacer que los botones de Streamlit sean transparentes y cubran el dibujo */
    .stButton > button {
        height: 160px !important;
        background: transparent !important;
        color: transparent !important;
        border: none !important;
        z-index: 2;
        position: relative;
    }
    
    /* Para los botones pequeños de abajo */
    .fila-pequena-visual {
        display: grid; grid-template-columns: repeat(4, 1fr); gap: 5px; margin-top: 10px;
    }
    .mini {
        height: 70px; background-color: #333; color: white; border-radius: 10px;
        display: flex; align-items: center; justify-content: center; font-size: 12px;
    }
    .small-btns .stButton > button { height: 70px !important; }
    </style>

    <div class="contenedor-visual">
        <div class="casilla azul">PARADA</div>
        <div class="casilla verde">MANILLA</div>
        <div class="casilla naranja">EMISORA</div>
        <div class="casilla gris">LIBRE</div>
    </div>
    """, unsafe_allow_html=True)

# --- BOTONES REALES (LOGICA) ---
def registrar(evento):
    st.toast(f"✅ {evento} enviado correctamente")

col1, col2 = st.columns(2)
with col1:
    if st.button("P", key="p"): registrar("PARADA")
    if st.button("E", key="e"): registrar("EMISORA")
with col2:
    if st.button("M", key="m"): registrar("MANILLA")
    if st.button("L", key="l"): registrar("LIBRE")

st.markdown('<div class="fila-pequena-visual"><div class="mini">FOTO</div><div class="mini">MIC</div><div class="mini">CAFE</div><div class="mini">FIN</div></div>', unsafe_allow_html=True)

st.markdown('<div class="small-btns">', unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
with c1: 
    if st.button("F"): registrar("FOTO")
with c2: 
    if st.button("MI"): registrar("MIC")
with c3: 
    if st.button("C"): registrar("CAFE")
with c4: 
    if st.button("FI"): registrar("FIN")
st.markdown('</div>', unsafe_allow_html=True)
