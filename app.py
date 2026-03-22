import streamlit as st
import requests
from streamlit_components_dot_com import html # Solo si usas componentes, si no, usamos st.components.v1

# 1. Configuración de Estilo y Script de GPS Directo
st.set_page_config(page_title="Trabajo Taxi", layout="centered")

# Script para capturar GPS y mandarlo a Make
st.components.v1.html("""
<script>
    function enviarUbicacion(evento) {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                const lat = position.coords.latitude;
                const lon = position.coords.longitude;
                const url = "https://hook.eu1.make.com/jgvj7anrmyxyu621vmpueo814k8wa1ue";
                
                fetch(url, {
                    method: 'POST',
                    body: JSON.stringify({
                        "evento": evento,
                        "latitud": lat,
                        "longitud": lon,
                        "timestamp": new Date().toISOString()
                    }),
                    headers: { 'Content-Type': 'application/json' }
                });
                alert(evento + " registrado con GPS ✅");
            });
        } else {
            alert("El GPS no está disponible");
        }
    }
</script>

<style>
    .grid-container {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 15px;
    }
    .btn-taxi {
        border: none;
        color: white;
        padding: 25px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 18px;
        font-weight: bold;
        border-radius: 15px;
        cursor: pointer;
        width: 100%;
    }
</style>

<div class="grid-container">
    <button class="btn-taxi" style="background-color: #2ecc71;" onclick="enviarUbicacion('LIBRE')">LIBRE</button>
    <button class="btn-taxi" style="background-color: #e67e22;" onclick="enviarUbicacion('PARADA')">PARADA</button>
    <button class="btn-taxi" style="background-color: #e74c3c;" onclick="enviarUbicacion('EMISORA')">EMISORA</button>
    <button class="btn-taxi" style="background-color: #34495e;" onclick="enviarUbicacion('MANILLA')">MANILLA</button>
</div>
""", height=250)

# 2. Botones CAFE y FIN (Directos a Make)
URL_MAKE = "https://hook.eu1.make.com/jgvj7anrmyxyu621vmpueo814k8wa1ue"

st.write("") 
col_c, col_f = st.columns(2)
with col_c:
    if st.button("☕️ CAFE", use_container_width=True):
        requests.post(URL_MAKE, json={"evento": "CAFE"})
        st.toast("Café registrado")

with col_f:
    if st.button("🏁 FIN", use_container_width=True):
        requests.post(URL_MAKE, json={"evento": "FIN"})
        st.toast("Jornada finalizada")

st.divider()

# 3. Cámara y Micro (Tus funciones que ya funcionan)
col1, col2 = st.columns(2)
with col1:
    if st.checkbox("📷 Cámara"):
        foto = st.camera_input("Foto")
        if foto and st.button("🚀 ENVIAR FOTO"):
            requests.post(URL_MAKE, files={"archivo": foto.getvalue()})
            st.success("Foto enviada")

with col2:
    if st.checkbox("🎙️ Micro"):
        audio = st.audio_input("Audio")
        if audio and st.button("🚀 ENVIAR AUDIO"):
            requests.post(URL_MAKE, files={"archivo": audio.getvalue()})
            st.success("Audio enviado")
