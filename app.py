import streamlit as st

st.set_page_config(layout="centered", page_title="Panel Taxi")

# Estilo blindado para iPhone (Copia fiel de la imagen 19:35)
st.markdown("""
    <style>
    .block-container { padding: 10px 5px !important; }
    header, footer { visibility: hidden; }

    /* La rejilla mágica que no se rompe */
    .grid-taxi {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
        padding: 5px;
    }

    /* Diseño de los botones grandes */
    .btn {
        height: 150px;
        border-radius: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-family: sans-serif;
        font-size: 22px;
        font-weight: bold;
        text-decoration: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    }

    /* Colores exactos */
    .azul { background-color: #0000FF; }
    .verde { background-color: #38761d; }
    .naranja { background-color: #f6b26b; }
    .gris { background-color: #7f7f7f; }

    /* Fila de abajo */
    .grid-small {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 5px;
        margin-top: 15px;
        padding: 5px;
    }
    .btn-s {
        height: 70px;
        background-color: #333;
        border-radius: 10px;
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 12px;
        font-weight: bold;
        text-decoration: none;
    }
    </style>

    <div class="grid-taxi">
        <a href="/?button=PARADA" class="btn azul">PARADA</a>
        <a href="/?button=MANILLA" class="btn verde">MANILLA</a>
        <a href="/?button=EMISORA" class="btn naranja">EMISORA</a>
        <a href="/?button=LIBRE" class="btn gris">LIBRE</a>
    </div>

    <div class="grid-small">
        <a href="/?button=FOTO" class="btn-s">FOTO</a>
        <a href="/?button=MIC" class="btn-s">MIC</a>
        <a href="/?button=CAFE" class="btn-s">CAFE</a>
        <a href="/?button=FIN" class="btn-s">FIN</a>
    </div>
    """, unsafe_allow_html=True)

# Lógica para detectar qué botón has pulsado
query_params = st.query_params
if "button" in query_params:
    boton_pulsado = query_params["button"]
    st.toast(f"✅ {boton_pulsado} registrado")
    # Limpiar la URL para el próximo toque
    st.query_params.clear()
