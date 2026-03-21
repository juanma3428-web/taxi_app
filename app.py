import streamlit as st

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
# --- ZONA DE PRUEBAS SEGURA (Debajo de tu botonera) ---
st.divider() # Esto crea una línea de separación visual

# Creamos un interruptor para que la cámara no esté siempre encendida
if st.checkbox("📷 Abrir Cámara para Informe"):
    foto = st.camera_input("Haz una foto de la parada o incidencia")
    
    if foto:
        # Aquí es donde Make recibirá la imagen
        st.success("Foto capturada. ¿Quieres enviarla?")
        if st.button("Confirmar Envío"):
            # Aquí pondremos el enlace a tu Webhook de Make
            st.write("Enviando a Google Sheets...")
