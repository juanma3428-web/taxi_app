import streamlit as st

st.set_page_config(layout="centered", page_title="Panel Trabajo")

# Este es el estilo que funcionó para tener 2 columnas y colores en el iPhone
st.markdown("""
    <style>
    /* Forzar que las columnas no se apilen en el móvil */
    [data-testid="column"] {
        width: 48% !important;
        flex: 1 1 45% !important;
        min-width: 45% !important;
    }
    
    /* Estilo general de los botones */
    .stButton > button {
        height: 140px !important;
        width: 100% !important;
        font-size: 22px !important;
        font-weight: bold !important;
        color: white !important;
        border-radius: 15px !important;
        margin-bottom: 10px !important;
        border: none !important;
    }

    /* Colores exactos de tu diseño */
    /* Fila 1 */
    div.stButton:nth-child(1) button { background-color: #0000FF !important; } /* PARADA - Azul */
    div.stButton:nth-child(2) button { background-color: #008000 !important; } /* MANILLA - Verde */
    
    /* Fila 2 */
    div.stButton:nth-child(3) button { background-color: #FFA500 !important; } /* EMISORA - Naranja */
    div.stButton:nth-child(4) button { background-color: #808080 !important; } /* LIBRE - Gris */

    /* Botones pequeños de abajo */
    .bot-row .stButton > button {
        height: 60px !important;
        font-size: 14px !important;
        background-color: #333333 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Estructura de botones
col1, col2 = st.columns(2)
with col1:
    st.button("PARADA")
    st.button("EMISORA")

with col2:
    st.button("MANILLA")
    st.button("LIBRE")

st.markdown('<div class="bot-row">', unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
with c1: st.button("FOTO")
with c2: st.button("MIC")
with c3: st.button("CAFE")
with c4: st.button("FIN")
st.markdown('</div>', unsafe_allow_html=True)
