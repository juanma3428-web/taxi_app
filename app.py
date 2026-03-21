import streamlit as st

# Configuración de página
st.set_page_config(layout="centered", page_title="Trabajo")

# Estilo forzado para que se vea bien en iPhone
st.markdown("""
    <style>
    .stButton > button {
        height: 120px !important;
        width: 100% !important;
        font-size: 25px !important;
        font-weight: bold !important;
        color: white !important;
        border-radius: 15px !important;
        margin-bottom: 10px !important;
    }
    /* Colores fijos */
    div.stButton:nth-of-type(1) > button { background-color: #0047AB !important; } /* Azul */
    div.stButton:nth-of-type(2) > button { background-color: #2E7D32 !important; } /* Verde */
    
    /* Efecto parpadeo al tocar */
    .stButton > button:active {
        background-color: #00FF00 !important;
        color: black !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Panel de Trabajo")

# Botones Grandes
col1, col2 = st.columns(2)

with col1:
    if st.button("PARADA"):
        st.toast("Registrando PARADA...")
    if st.button("EMISORA"):
        st.toast("Registrando EMISORA...")

with col2:
    if st.button("MANILLA"):
        st.toast("Registrando MANILLA...")
    if st.button("LIBRE"):
        st.toast("Registrando LIBRE...")

st.divider()

# Botones Pequeños
c1, c2, c3, c4 = st.columns(4)
with c1: st.button("FOTO")
with c2: st.button("MIC")
with c3: st.button("CAFE")
with c4: st.button("FIN")
