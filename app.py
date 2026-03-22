import streamlit as st
import requests

# 1. Configuración de Estilo y Script de Geoposicionamiento
# He quitado la librería que daba error y lo he hecho con HTML directo
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">

<script>
    function registrarConGPS(nombreEvento) {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                const lat = position.coords.latitude;
                const lon = position.coords.longitude;
                const url = "https://hook.eu1.make.com/jgvj7anrmyxyu621vmpueo814k8wa1ue";
                
                fetch(url, {
                    method: 'POST',
                    body: JSON.stringify({
                        "evento": nombreEvento,
                        "latitud": lat,
                        "longitud": lon,
                        "detalle": "Enviado desde el taxi"
                    }),
                    headers: { 'Content-Type': 'application/json' }
                }).then(() => {
                    alert("✅ " + nombreEvento + " registrado con ubicación");
                });
            }, function(error) {
                alert("⚠️ Error: Activa el GPS en tu iPhone");
            });
        }
    }
</script>

<style>
    .grid-container {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 10px;
        padding: 10px;
    }
    .btn-taxi {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        border: none;
        color: white;
        font-family: Arial, sans-serif;
        font-weight: bold;
        border-radius: 15px;
        height: 100px;
        font-size: 16px;
        cursor: pointer;
    }
    .fas { margin-bottom: 5px; font-size: 24px; }
    .stButton>button {
        border-radius: 10px;
        height: 50px;
        font-weight: bold;
    }
</style>

<div class="grid-container">
    <button onclick="registrarConGPS('LIBRE')" class="btn-taxi" style="background-color: #2ecc71;">
        <i class="fas fa-check"></i>LIBRE
    </button>
    <button onclick="registrarConGPS('PARADA')" class="btn-taxi" style="background-color: #e67e22;">
        <i class="fas fa-map-marker-alt"></i>PARADA
    </button>
    <button onclick="registrarConGPS('EMISORA')" class="btn-taxi" style="background-color: #e74c3c;">
        <i class="fas fa-headset"></i>EMISORA
    </button>
    <button onclick="registrarConGPS('MANILLA')" class="btn-taxi" style="background-color: #34495e;">
        <i class="fas fa-hand-paper"></i>MANILLA
    </button>
</div>
""", unsafe_allow_html=True)

# 2. URL de tu Webhook
URL_MAKE = "https://hook.eu1.make.com/jgvj7anrmyxyu621vmpueo814k8wa1ue"

# 3. Botones CAFE y FIN (Funcionan como siempre)
st.write("") 
col_c, col_f = st.columns(2)

with col_c:
    if st.button("☕️ CAFE", use_container_width=True):
        requests.post(URL_MAKE, json={"evento": "CAFE"})
        st.toast("Café registrado")

with col_f:
    if st.button("🏁 FIN", use_container_width=True):
        requests.post(URL_MAKE, json={"evento": "FIN"})
        st.toast("Jornada terminada")

st.divider()

# 4. Cámara y Micro (Tu código original que funciona perfecto)
col1, col2 = st.columns(2)

with col1:
    if st.checkbox("📷 Cámara"):
        foto = st.camera_input("Captura")
        if foto and st.button("🚀 ENVIAR FOTO"):
            requests.post(URL_MAKE, files={"archivo": foto.getvalue()})
            st.success("✅ Foto enviada")

with col2:
    if st.checkbox("🎙️ Micro"):
        audio = st.audio_input("Graba")
        if audio and st.button("🚀 ENVIAR AUDIO"):
            requests.post(URL_MAKE, files={"archivo": audio.getvalue()})
            st.success("✅ Audio enviado")
