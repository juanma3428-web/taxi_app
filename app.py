import streamlit as st
import requests
from datetime import datetime

st.set_page_config(layout="centered", page_title="Taxi Bilbao")

# --- ESTILO QUE SÍ FUNCIONA (COLORES Y 2 COLUMNAS) ---
st.markdown("""
    <style>
    .block-container { padding: 10px 5px !important; }
    header, footer { visibility: hidden; }

    /* Forzar rejilla de 2 columnas para botones de Streamlit */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        gap: 10px !important;
    }
    div[data-testid="column"] {
        width: 100% !important;
    }

    /* Estilo de los botones */
    .stButton > button {
        height: 160px !important;
        width: 100% !important;
        border-radius: 15px !important;
        font-size: 22px !important;
        font-weight: bold !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2) !important;
    }

    /* Colores por posición */
    /* Fila 1 */
    div[data-testid="column"]:nth-of-type(1) div.stButton:nth-of-type(1) > button { background-color: #0000FF !important; } /* PARADA - Azul */
    div[data-testid="column"]:nth-of-type(1) div.stButton:nth-of-type(2) > button { background-color: #FFA500 !important; } /* EMISORA - Naranja */
    
    div[data-testid="column"]:nth-of-type(2) div.stButton:nth-of-type(1) > button { background-color: #008000 !important; } /* MANILLA - Verde */
    div[data-testid="column"]:nth-of-type(2) div.stButton:nth-of-type(2) > button { background-color: #808080 !important; } /* LIBRE - Gris */

    /* Parpadeo verde al pulsar */
    .stButton > button:active {
        background-color: #00FF00 !important;
        color: black !important;
    }

    /* Fila de abajo (Pequeños) */
    .bot-row .stButton > button {
        height: 70px !important;
        font-size: 14px !important;
        background-color: #333333 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE ENVÍO ---
def enviar(evento):
    # Por ahora solo muestra el aviso en pantalla, luego pondremos el Webhook
    st.toast(f"✅ {evento} registrado")

# --- ESTRUCTURA DE BOTONES ---
col1, col2 = st.columns(2)

with col1:
    if st.button("PARADA", key="btn_parada"): enviar("PARADA")
    if st.button("EMISORA", key="btn_emisora"): enviar("EMISORA")

with col2:
    if st.button("MANILLA", key="btn_manilla"): enviar("MANILLA")
    if st.button("LIBRE", key="btn_libre"): enviar("LIBRE")

st.markdown('<div class="bot-row">', unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
with c1: 
    if st.button("FOTO"): enviar("FOTO")
with c2: 
    if st.button("MIC"): enviar("MIC")
with c3: 
    if st.button("CAFE"): enviar("CAFE")
with c4: 
    if st.button("FIN"): enviar("FIN")
st.markdown('</div>', unsafe_allow_html=True)
