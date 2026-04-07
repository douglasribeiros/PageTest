import streamlit as st

st.set_page_config(page_title="Sistema de Gestão", layout="wide")

# CSS para manter sua cor padrão 007e7a e ajustar o menu lateral
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    /* Estiliza o container da sidebar */
    [data-testid="stSidebar"] {
        background-color: #007e7a;
    }
    /* Estiliza os textos e widgets dentro da sidebar */
    [data-testid="stSidebar"] .stMarkdown, [data-testid="stSidebar"] label, [data-testid="stSidebar"] p {
        color: white !important;
    }
    /* Estiliza o selectbox dentro da sidebar */
    div[data-baseweb="select"] > div {
        background-color: white;
        color: #007e7a;
    }
    </style>
    """, unsafe_allow_html=True)

# --- MENU LATERAL ---
st.sidebar.image("https://via.placeholder.com/150x50?text=LOGOTIPO", use_container_width=True) # Espaço para seu logo
st.sidebar.title("Navegação")

# Opções do menu
paginas = ["🏠 Início", "📊 Painel do Fiscal", "👥 Equipe de Gestão", "📋 Contratos"]
escolha = st.sidebar.radio("Selecione a página:", paginas)

st.sidebar.markdown("---")
st.sidebar.write("Usuário: **Rafael Santos**")
st.sidebar.write("Perfil: **Coordenador**")

# --- LÓGICA DE NAVEGAÇÃO ---
if escolha == "🏠 Início":
    st.title("🏛️ Portal de Gestão Contratual")
    st.write("Bem-vindo ao sistema. Utilize o menu ao lado para navegar entre as funcionalidades.")
    st.info("Selecione uma das opções na barra lateral para começar a fiscalização.")

elif escolha == "📊 Painel do Fiscal":
    st.title("📊 Painel do Fiscal ou Gestor")
    st.write("Aqui você visualiza seus indicadores de desempenho.")
    # Adicione aqui o conteúdo do Dashboard

elif escolha == "👥 Equipe de Gestão":
    st.title("👥 Equipe de Gestão Contratual")
    st.write("Gerenciamento de membros e carga de trabalho.")
    # Adicione aqui o conteúdo da Equipe que criamos anteriormente

elif escolha == "📋 Contratos":
    st.title("📋 Gestão de Contratos")
    st.write("Lista completa de contratos ativos e notificações.")