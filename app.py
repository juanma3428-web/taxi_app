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

<div class="grid-small">
    <a href="/?button=FOTO" class="btn-s">FOTO</a>
    <a href="/?button=MIC" class="btn-s">MIC</a>
    <a href="/?button=CAFE" class="btn-s">CAFE</a>
    <a href="/?button=FIN" class="btn-s">FIN</a>
</div>
"""

st.write(botonera_html, unsafe_allow_html=True)

# Lógica de detección de pulsación (la que ya tenías con Make)
query_params = st.query_params
if "button" in query_params:
    boton_pulsado = query_params["button"]
    st.info(f"Registrando: {boton_pulsado}...")
    # Aquí va tu link de Make que ya funcionaba
# --- LÍNEA 70: CONEXIÓN REAL CON MAKE (FOTO) ---
st.divider()

if st.checkbox("📷 Activar Cámara para el Informe"):
    foto = st.camera_input("Captura de parada o incidencia")
    
    if foto:
        if st.button("🚀 ENVIAR AHORA"):
            try:
                # 1. Preparar la imagen
                bytes_data = foto.getvalue()
                
                # 2. Tu URL de Webhook de Make (Servidor EU1)
                # IMPORTANTE: Esta URL es la que recibe los datos en tu escenario
                url_webhook = "https://hook.eu1.make.com/zBmH53wgdaq"
                
                # 3. Enviar el archivo
                res = requests.post(url_webhook, files={"archivo": bytes_data})
                
                if res.status_code == 200:
                    st.success("✅ ¡Recibido! Foto registrada en el sistema.")
                else:
                    st.error(f"❌ Error {res.status_code}: Revisa si el escenario en Make está 'ON'.")
            except Exception as e:
                st.error("⚠️ Error: Asegúrate de tener 'import requests' en la Línea 1.")

# --- FIN DEL BLOQUE ---

