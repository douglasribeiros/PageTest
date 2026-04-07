import streamlit as st

st.set_page_config(page_title="Sistema de Gestão", layout="wide")

# CSS para manter sua cor padrão 007e7a
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #007e7a; }
    [data-testid="stSidebar"] * { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏛️ Portal de Gestão Contratual")
st.write("Bem-vindo ao sistema. Utilize o menu ao lado para navegar entre as funcionalidades.")

# Card de resumo rápido
st.info("Selecione uma das opções na barra lateral para começar a fiscalização.")