import streamlit as st
import requests
from datetime import datetime

st.set_page_config(layout="centered", page_title="Taxi Bilbao")

# --- CONFIGURACIÓN DEL PUENTE (Lo rellenaremos en el paso B) ---
WEBHOOK_URL = "AQUÍ_PONDREMOS_LA_URL_LUEGO"

def enviar_registro(evento):
    ahora = datetime.now().strftime("%H:%M:%S")
    datos = {"evento": evento, "hora": ahora, "dispositivo": "iPhone"}
    try:
        # Esto envía la señal al puente
        requests.post(WEBHOOK_URL, json=datos, timeout=2)
        return True
    except:
        return False

# --- DISEÑO VISUAL ---
st.markdown("""
    <style>
    .block-container { padding: 10px 5px !important; }
    header, footer { visibility: hidden; }

    .main-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 8px;
        margin-top: 10px;
    }

    .btn-big {
        height: 160px; border-radius: 12px; display: flex; align-items: center;
        justify-content: center; color: white; font-size: 20px; font-weight: bold;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); cursor: pointer;
    }

    .azul { background-color: #0000FF; }
    .verde { background-color: #008000; }
    .naranja { background-color: #FFA500; }
    .gris { background-color: #808080; }

    /* Parpadeo verde y vibración simulada */
    .btn-big:active {
        background-color: #00FF00 !important;
        color: black !important;
        transform: scale(0.95);
    }

    .small-grid {
        display: grid; grid-template-columns: repeat(4, 1fr);
        gap: 5px; margin-top: 15px;
    }

    .btn-small {
        height: 70px; background-color: #333333; border-radius: 8px;
        display: flex; align-items: center; justify-content: center;
        color: white; font-size: 13px; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BOTONES CON LÓGICA ---
col1, col2 = st.columns(2)

with col1:
    if st.button("PARADA", use_container_width=True):
        enviar_registro("PARADA")
        st.toast("✅ PARADA registrada")
        
    if st.button("EMISORA", use_container_width=True):
        enviar_registro("EMISORA")
        st.toast("✅ EMISORA registrada")

with col2:
    if st.button("MANILLA", use_container_width=True):
        enviar_registro("MANILLA")
        st.toast("✅ MANILLA registrada")
        
    if st.button("LIBRE", use_container_width=True):
        enviar_registro("LIBRE")
        st.toast("✅ LIBRE registrado")

st.divider()

c1, c2, c3, c4 = st.columns(4)
with c1: 
    if st.button("FOTO"): enviar_registro("FOTO")
with c2: 
    if st.button("MIC"): enviar_registro("MIC")
with c3: 
    if st.button("CAFE"): enviar_registro("CAFE")
with c4: 
    if st.button("FIN"): enviar_registro("FIN")
