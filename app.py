import streamlit as st
import requests

# 1. Configuración de Estilo y Script de Geoposicionamiento Directo
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">

<script>
    function registrarEvento(nombreEvento) {
        if (navigator.geolocation) {
            // Pedimos la ubicación con alta precisión para el taxi
            navigator.geolocation.getCurrentPosition(function(position) {
                const lat = position.coords.latitude;
                const lon = position.coords.longitude;
                const url = "https://hook.eu1.make.com/jgvj7anrmyxyu621vmpueo814k8wa1ue";
                
                // Enviamos los datos a tu Webhook de Make
                fetch(url, {
                    method: 'POST',
                    body: JSON.stringify({
                        "evento": nombreEvento,
                        "latitud": lat,
                        "longitud": lon,
                        "timestamp": new Date().toISOString()
                    }),
                    headers: { 'Content-Type': 'application/json' }
                }).then(() => {
                    alert("✅ " + nombreEvento + " registrado con ubicación exacta.");
                }).catch(() => {
                    alert("❌ Error al enviar los datos a Make.");
                });
            }, function(error) {
                alert("⚠️ Error: No se pudo obtener la ubicación. Revisa los permisos de Safari/iPhone.");
            }, { enableHighAccuracy: true });
        } else {
            alert("Tu iPhone no soporta geolocalización en este navegador.");
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
    <button onclick="registrarEvento('LIBRE')" class="btn-taxi" style="background-color: #2ecc71;">
        <i class="fas fa-check"></i>LIBRE
    </button>
    <button onclick="registrarEvento('PARADA')" class="btn-taxi" style="background-color: #e67e22;">
        <i class="fas fa-map-marker-alt"></i>PARADA
    </button>
    <button onclick="registrarEvento('EMISORA')" class="btn-taxi" style="background-color: #e74c3c;">
        <i class="fas fa-headset"></i>EMISORA
    </button>
    <button onclick="registrarEvento('MANILLA')" class="btn-taxi" style="background-color: #34495e;">
        <i class="fas fa-hand-paper"></i>MANILLA
    </button>
</div>
""", unsafe_allow_html=True)

# 2. URL de tu Webhook de Make
URL_MAKE = "https://hook.eu1.make.com/jgvj7anrmyxyu621vmpueo814k8wa1ue"

# 3. Botones CAFE y FIN (Mantienen tu lógica original de Streamlit)
st.write("") 
col_c, col_f = st.columns(2)

with col_c:
    if st.button("☕️ CAFE", use_container_width=True):
        try:
            requests.post(URL_MAKE, json={"evento": "CAFE", "mensaje": "Inicio de pausa café"})
            st.toast("Aviso de CAFÉ enviado ✅")
        except:
            st.error("Error al enviar")

with col_f:
    if st.button("🏁 FIN", use_container_width=True):
        try:
            requests.post(URL_MAKE, json={"evento": "FIN", "mensaje": "Fin de jornada"})
            st.toast("Aviso de FIN enviado ✅")
        except:
            st.error("Error al enviar")

st.divider()

# 4. Sistema de Cámara y Micro (Intacto como querías)
col1, col2 = st.columns(2)

with col1:
    if st.checkbox("📷 Cámara"):
        foto = st.camera_input("Captura")
        if foto:
            if st.button("🚀 ENVIAR FOTO"):
                try:
                    res = requests.post(URL_MAKE, files={"archivo": foto.getvalue()})
                    if res.status_code == 200:
                        st.success("✅ Foto enviada")
                except:
                    st.error("⚠️ Error")

with col2:
    if st.checkbox("🎙️ Micro"):
        audio = st.audio_input("Graba")
        if audio:
            if st.button("🚀 ENVIAR AUDIO"):
                try:
                    res = requests.post(URL_MAKE, files={"archivo": audio.getvalue()})
                    if res.status_code == 200:
                        st.success("✅ Audio enviado")
                except:
                    st.error("⚠️ Error")
