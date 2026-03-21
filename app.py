import streamlit as st

st.set_page_config(layout="centered", page_title="Taxi Bilbao")

# CSS Inyectado para control total del diseño vertical en iPhone
st.markdown("""
    <style>
    /* Eliminar márgenes de Streamlit para ganar espacio */
    .block-container { padding: 10px 5px !important; }
    header { visibility: hidden; }
    footer { visibility: hidden; }

    /* Contenedor principal para botones de acción */
    .main-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 8px;
        margin-top: 10px;
    }

    /* Estilo de los botones grandes (2x2) */
    .btn-big {
        height: 160px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-family: sans-serif;
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        cursor: pointer;
        user-select: none;
    }

    /* Colores específicos */
    .azul { background-color: #0000FF; }
    .verde { background-color: #008000; }
    .naranja { background-color: #FFA500; }
    .gris { background-color: #808080; }

    /* Efecto parpadeo verde intenso al tocar */
    .btn-big:active, .btn-small:active {
        background-color: #00FF00 !important;
        color: black !important;
        transform: scale(0.98);
    }

    /* Contenedor inferior (4 botones en línea) */
    .small-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 5px;
        margin-top: 15px;
    }

    .btn-small {
        height: 70px;
        background-color: #333333;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 13px;
        font-weight: bold;
    }
    </style>

    <div class="main-grid">
        <div class="btn-big azul">PARADA</div>
        <div class="btn-big verde">MANILLA</div>
        <div class="btn-big naranja">EMISORA</div>
        <div class="btn-big gris">LIBRE</div>
    </div>

    <div class="small-grid">
        <div class="btn-small">FOTO</div>
        <div class="btn-small">MIC</div>
        <div class="btn-small">CAFE</div>
        <div class="btn-small">FIN</div>
    </div>
    """, unsafe_allow_html=True)
