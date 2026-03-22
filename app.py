import streamlit as st
import requests
import streamlit.components.v1 as components

# 1. Configuración de la página
st.set_page_config(page_title="Trabajo Taxi", layout="centered")

# 2. URL de tu Webhook de Make
URL_MAKE = "https://hook.eu1.make.com/jgvj7anrmyxyu621vmpueo814k8wa1ue"

# 3. Bloque de Botones con GPS Integrado
# Usamos un componente de HTML dedicado para que el iPhone no bloquee el GPS
components.html(f"""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
<script>
    function enviarDato(evento) {{
        if (navigator.geolocation) {{
            navigator.geolocation.getCurrentPosition(function(position) {{
                const lat = position.coords.latitude;
                const lon = position.coords.longitude;
                
                fetch("{URL_MAKE}", {{
                    method: 'POST',
                    body: JSON.stringify({{
                        "evento": evento,
                        "latitud": lat,
                        "longitud": lon,
                        "detalle": "Enviado desde el iPhone"
                    }}),
                    headers: {{ 'Content-Type': 'application/json' }}
                }}).then(() => {{
                    alert("✅ " + evento + " registrado con GPS");
                }}).catch(() => {{
                    alert("❌ Error al conectar con el servidor");
                }});
            }}, function(error) {{
                alert("⚠️ Error: Activa la ubicación en Safari/Ajustes.");
            }}, {{ enableHighAccuracy: true }});
        }} else {{
            alert("Tu navegador no soporta GPS");
        }}
    }}
</script>

<style>
    .grid-container {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
        padding: 5px;
    }}
    .btn-taxi {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        border: none;
        color: white;
        font-family: sans-serif;
        font-weight: bold;
        border-radius: 15px;
        height: 100px;
        font-size: 16px;
        cursor: pointer;
    }}
    .fas {{ margin-bottom: 8px; font-size: 24px; }}
</style>

<div class="grid-container">
    <button onclick="enviarDato('LIBRE')" class="btn-taxi" style="background-color: #2ecc71;"><i class="fas fa-check"></i>LIBRE</button>
    <button onclick="enviarDato('PARADA')" class="btn-taxi" style="background-color: #e67e22;"><i class="fas fa-map-marker-alt"></i>PARADA</button>
    <button onclick="enviarDato('EMISORA')" class="btn-taxi" style="background-color: #e74c3c;"><i class="fas fa-headset"></i>EMISORA</button>
    <button onclick="enviarDato('MANILLA')" class="btn-taxi" style="background-color: #34495e;"><i class="fas fa-hand-paper"></i>MANILLA</button>
</div>
""", height=230)

# 4. Botones CAFE y FIN (Streamlit nativo)
st.write("") 
col_c, col_f = st.columns(2)

with col_c:
    if st.button("☕️ CAFE", use_container_width=True):
        try:
            requests.post(URL_MAKE, json={"evento": "CAFE", "mensaje": "Pausa"})
            st.toast("CAFÉ enviado ✅")
        except: st.error("Error")

with col_f:
    if st.button("🏁 FIN", use_container_width=True):
        try:
            requests.post(URL_MAKE, json={"evento": "FIN", "mensaje": "Fin jornada"})
            st.toast("FIN enviado ✅")
        except: st.error("Error")

st.divider()

# 5. Cámara y Micro (Tu código que ya funciona)
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
