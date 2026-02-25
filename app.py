import streamlit as st

# Configuración elegante
st.set_page_config(page_title="Altamira Novias - Fitting Room", page_icon="✨")

st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    h1 { color: #1a1a1a; text-align: center; font-family: 'Serif'; }
    .stButton>button { background-color: #000000; color: white; border-radius: 0px; height: 50px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

st.title("✨ Altamira Novias")
st.write("### Encuentra tu talla ideal")
st.write("Ingresa tus medidas en centímetros para una recomendación precisa.")

# Columnas para las medidas
col1, col2, col3 = st.columns(3)

with col1:
    busto = st.number_input("Busto (cm)", min_value=70, max_value=130, value=90)
with col2:
    cintura = st.number_input("Cintura (cm)", min_value=50, max_value=110, value=70)
with col3:
    cadera = st.number_input("Cadera (cm)", min_value=70, max_value=140, value=95)

if st.button("CALCULAR MI TALLA"):
    talla = "Consultar Boutique"
    
    # Lógica exacta según tu tabla de medidas
    if 82 <= busto <= 86 and 62 <= cintura <= 66 and 88 <= cadera <= 92:
        talla = "XS"
    elif 87 <= busto <= 91 and 67 <= cintura <= 71 and 93 <= cadera <= 97:
        talla = "S"
    elif 92 <= busto <= 96 and 72 <= cintura <= 76 and 98 <= cadera <= 102:
        talla = "M"
    elif 97 <= busto <= 101 and 77 <= cintura <= 81 and 103 <= cadera <= 107:
        talla = "L"
    elif 102 <= busto <= 106 and 82 <= cintura <= 86 and 108 <= cadera <= 112:
        talla = "XL"
    elif 107 <= busto <= 111 and 87 <= cintura <= 91 and 113 <= cadera <= 117:
        talla = "XXL"
    else:
        # Sugerencia inteligente si está entre tallas
        if busto <= 91: talla = "S"
        elif busto <= 96: talla = "M"
        elif busto <= 101: talla = "L"
        elif busto <= 111: talla = "XL/XXL"

    st.markdown(f"<h2 style='text-align: center; color: #1a1a1a;'>Tu talla sugerida: {talla}</h2>", unsafe_allow_html=True)
    st.info("Nota: Esta es una guía. Recomendamos una prueba final en nuestra boutique.")
  
