import streamlit as st
import requests


# Estilo y Botonera Original (Punto de restauración seguro)
botonera_html = """
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
<style>
    .grid-container {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 10px;
        padding: 10px;
    }
    .grid-small {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 5px;
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
    .btn-s {
        display: flex;
        align-items: center;
        justify-content: center;
        text-decoration: none;
        color: white;
        background-color: #7f8c8d;
        font-family: Arial, sans-serif;
        font-size: 12px;
        border-radius: 8px;
        height: 40px;
    }
    .fas { margin-bottom: 5px; font-size: 24px; }
</style>

<div class="grid-container">
    <a href="/?button=LIBRE" class="btn-taxi" style="background-color: #2ecc71;"><i class="fas fa-check"></i>LIBRE</a>
    <a href="/?button=PARADA" class="btn-taxi" style="background-color: #e67e22;"><i class="fas fa-map-marker-alt"></i>PARADA</a>
    <a href="/?button=EMISORA" class="btn-taxi" style="background-color: #e74c3c;"><i class="fas fa-headset"></i>EMISORA</a>
    <a href="/?button=MANILLA" class="btn-taxi" style="background-color: #34495e;"><i class="fas fa-hand-paper"></i>MANILLA</a>
</div>

<div style="display: flex; justify-content: center; gap: 10px;">
  • <button class="grey-button" id="btn-cafe">CAFE</button>
• <button class="grey-button" id="btn-fin">FIN</button>

</div>

"""

st.write(botonera_html, unsafe_allow_html=True)

# Lógica de detección de pulsación (la que ya tenías con Make)
query_params = st.query_params
if "button" in query_params:
    boton_pulsado = query_params["button"]
    st.info(f"Registrando: {boton_pulsado}...")
    # Aquí va tu link de Make que ya funcionaba
# --- LÍNEA 70: CÓDIGO ACTUALIZADO PARA EVITAR ERRORES DE DRIVE ---
st.divider()

col1, col2 = st.columns(2)

with col1:
    if st.checkbox("📷 Cámara"):
        foto = st.camera_input("Captura")
        if foto:
            if st.button("🚀 ENVIAR FOTO"):
                try:
                    res = requests.post("https://hook.eu1.make.com/jgvj7anrmyxyu621vmpueo814k8wa1ue", 
                                      files={"archivo": foto.getvalue()})
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
                    res = requests.post("https://hook.eu1.make.com/jgvj7anrmyxyu621vmpueo814k8wa1ue", 
                                      files={"archivo": audio.getvalue()})
                    if res.status_code == 200:
                        st.success("✅ Audio enviado")
                except:
                    st.error("⚠️ Error")

