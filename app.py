import streamlit as st

# Configuración para evitar márgenes innecesarios
st.set_page_config(layout="centered", page_title="Taxi Bilbao")

# CSS "AGRESIVO" para iPhone Vertical
st.markdown("""
    <style>
    /* Eliminar todo el espacio sobrante de Streamlit */
    .block-container { padding: 5px !important; }
    header, footer { visibility: hidden; }
    
    /* FORZAR 2 COLUMNAS EN MÓVIL (Vertical) */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 10px !important;
    }
    div[data-testid="column"] {
        flex: 1 !important;
        width: 48% !important;
        min-width: 48% !important;
    }

    /* ESTILO DE LOS BOTONES */
    .stButton > button {
        height: 160px !important;
        width: 100% !important;
        border-radius: 15px !important;
        font-size: 20px !important;
        font-weight: bold !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3) !important;
    }

    /* ASIGNACIÓN DE COLORES POR ORDEN REAL */
    /* Columna Izquierda */
    div[data-testid="column"]:nth-of-type(1) div.stButton:nth-of-type(1) > button { background-color: #0000FF !important; } /* PARADA */
    div[data-testid="column"]:nth-of-type(1) div.stButton:nth-of-type(2) > button { background-color: #FFA500 !important; } /* EMISORA */

    /* Columna Derecha */
    div[data-testid="column"]:nth-of-type(2) div.stButton:nth-of-type(1) > button { background-color: #008000 !important; } /* MANILLA */
    div[data-testid="column"]:nth-of-type(2) div.stButton:nth-of-type(2) > button { background-color: #808080 !important; } /* LIBRE */

    /* BOTONES PEQUEÑOS INFERIORES */
    .bot-row .stButton > button {
        height: 70px !important;
        background-color: #333333 !important;
        font-size: 13px !important;
    }

    /* EFECTO FLASH VERDE AL PULSAR */
    .stButton > button:active {
        background-color: #00FF00 !important;
        color: black !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Lógica de aviso
def click(nombre):
    st.toast(f"✅ {nombre} registrado")

# --- CONSTRUCCIÓN DE LA REJILLA ---
col1, col2 = st.columns(2)

with col1:
    st.button("PARADA", on_click=click, args=("PARADA",))
    st.button("EMISORA", on_click=click, args=("EMISORA",))

with col2:
    st.button("MANILLA", on_click=click, args=("MANILLA",))
    st.button("LIBRE", on_click=click, args=("LIBRE",))

st.markdown('<div class="bot-row">', unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
with c1: st.button("FOTO", on_click=click, args=("FOTO",))
with c2: st.button("MIC", on_click=click, args=("MIC",))
with c3: st.button("CAFE", on_click=click, args=("CAFE",))
with c4: st.button("FIN", on_click=click, args=("FIN",))
st.markdown('</div>', unsafe_allow_html=True)
