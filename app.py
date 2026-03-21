import streamlit as st
import requests

# 1. Configuración de Estilo (Diseño de la botonera superior)
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
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
        text-decoration: none;
        color: white;
        font-family: Arial, sans-serif;
        font-weight: bold;
        border-radius: 15px;
        height: 100px;
        font-size: 16px;
    }
    .fas { margin-bottom: 5px; font-size: 24px; }
    /* Estilo para los botones de Streamlit para que se vean mejor */
    .stButton>button {
        border-radius: 10px;
        height: 50px;
        font-weight: bold;
    }
</style>

<div class="grid-container">
    <a href="/?button=LIBRE" class="btn-taxi" style="background-color: #2ecc71;"><i class="fas fa-check"></i>LIBRE</a>
    <a href="/?button=PARADA" class="btn-taxi" style="background-color: #e67e22;"><i class="fas fa-map-marker-alt"></i>PARADA</a>
    <a href="/?button=EMISORA" class="btn-taxi" style="background-color: #e74c3c;"><i class="fas fa-headset"></i>EMISORA</a>
    <a href="/?button=MANILLA" class="btn-taxi" style="background-color: #34495e;"><i class="fas fa-hand-paper"></i>MANILLA</a>
</div>
""", unsafe_allow_html=True)

# 2. URL de tu Webhook de Make
URL_MAKE = "https://hook.eu1.make.com/jgvj7anrmyxyu621vmpueo814k8wa1ue"

# 3. Lógica para los botones de colores (LIBRE, PARADA, etc.)
query_params = st.query_params
if "button" in query_params:
    boton_pulsado = query_params["button"]
    try:
        requests.post(URL_MAKE, json={"evento": boton_pulsado, "detalle": "Cambio de estado"})
        st.success(f"Registrado: {boton_pulsado}")
    except:
        st.error("Error al registrar estado")

# 4. Botones CAFE y FIN (Funcionales y centrados)
st.write("") # Espacio visual
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

# 5. Sistema de Cámara y Micro (Tu código original intacto)
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
