import streamlit as st

st.set_page_config(layout="centered", page_title="Taxi Bilbao")

# CSS para forzar el diseño de 2 columnas en iPhone y los colores
st.markdown("""
    <style>
    .block-container { padding: 10px 5px !important; }
    header, footer { visibility: hidden; }

    /* Forzar 2 columnas en móvil */
    [data-testid="column"] {
        width: 49% !important;
        flex: 1 1 49% !important;
        min-width: 49% !important;
    }

    /* Estilo de los botones */
    .stButton > button {
        height: 160px !important;
        width: 100% !important;
        border-radius: 15px !important;
        font-size: 22px !important;
        font-weight: bold !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2) !important;
    }

    /* Colores por botón individual */
    /* PARADA */
    div[data-testid="column"]:nth-of-type(1) div.stButton:nth-of-type(1) > button { background-color: #0000FF !important; }
    /* EMISORA */
    div[data-testid="column"]:nth-of-type(1) div.stButton:nth-of-type(2) > button { background-color: #FFA500 !important; }
    /* MANILLA */
    div[data-testid="column"]:nth-of-type(2) div.stButton:nth-of-type(1) > button { background-color: #008000 !important; }
    /* LIBRE */
    div[data-testid="column"]:nth-of-type(2) div.stButton:nth-of-type(2) > button { background-color: #808080 !important; }

    /* Botones pequeños de abajo */
    .small-btn .stButton > button {
        height: 75px !important;
        background-color: #333333 !important;
        font-size: 14px !important;
    }

    /* El parpadeo verde al pulsar */
    .stButton > button:active {
        background-color: #00FF00 !important;
        color: black !important;
    }
    </style>
    """, unsafe_allow_html=True)

def registrar(nombre):
    st.toast(f"✅ {nombre} registrado")

# --- CUERPO DE LA APP ---
col1, col2 = st.columns(2)

with col1:
    if st.button("PARADA"): registrar("PARADA")
    if st.button("EMISORA"): registrar("EMISORA")

with col2:
    if st.button("MANILLA"): registrar("MANILLA")
    if st.button("LIBRE"): registrar("LIBRE")

st.markdown('<div class="small-btn">', unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
with c1: 
    if st.button("FOTO"): registrar("FOTO")
with c2: 
    if st.button("MIC"): registrar("MIC")
with c3: 
    if st.button("CAFE"): registrar("CAFE")
with c4: 
    if st.button("FIN"): registrar("FIN")
st.markdown('</div>', unsafe_allow_html=True)
