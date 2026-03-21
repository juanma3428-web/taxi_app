import streamlit as st
import requests
from datetime import datetime

st.set_page_config(layout="centered", page_title="Taxi Bilbao")

# --- DISEÑO RADICAL PARA IPHONE VERTICAL ---
st.markdown("""
    <style>
    .block-container { padding: 10px 5px !important; }
    header, footer { visibility: hidden; }

    /* Rejilla manual 2x2 */
    .contenedor-taxi {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
        padding: 5px;
    }

    /* Estilo de los botones visuales */
    .casilla {
        height: 160px;
        border-radius: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 22px;
        font-weight: bold;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        transition: 0.1s;
    }

    /* Colores */
    .azul { background-color: #0000FF; }
    .verde { background-color: #008000; }
    .naranja { background-color: #FFA500; }
    .gris { background-color: #808080; }

    /* Efecto al tocar */
    .casilla:active {
        background-color: #00FF00 !important;
        color: black;
        transform: scale(0.95);
    }

    /* Botones pequeños abajo */
    .fila-pequena {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 5px;
        margin-top: 15px;
        padding: 5px;
    }
    .mini {
        height: 70px;
        background-color: #333;
        color: white;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 12px;
        font-weight: bold;
    }
    </style>

    <div class="contenedor-taxi">
        <div class="casilla azul">PARADA</div>
        <div class="casilla verde">MANILLA</div>
        <div class="casilla naranja">EMISORA</div>
        <div class="casilla gris">LIBRE</div>
    </div>

    <div class="fila-pequena">
        <div class="mini">FOTO</div>
        <div class="mini">MIC</div>
        <div class="mini">CAFE</div>
        <div class="mini">FIN</div>
    </div>
    """, unsafe_allow_html=True)

# --- BOTÓN INVISIBLE PARA LA LÓGICA ---
# Esto es para que Streamlit detecte actividad sin romper el diseño
if st.button("ACTUALIZAR DATOS", use_container_width=True):
    st.toast("✅ Sistema listo y conectado")
