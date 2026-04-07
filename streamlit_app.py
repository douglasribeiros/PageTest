import streamlit as st

st.set_page_config(page_title="Sistema de Gestão - Dark Mode", layout="wide")

# CSS para forçar o Modo Escuro e manter sua cor padrão 007e7a
st.markdown("""
    <style>
    /* Fundo da aplicação principal */
    .stApp { 
        background-color: #0e1117; 
        color: #ffffff;
    }

    /* Estiliza o container da sidebar (barra lateral) */
    [data-testid="stSidebar"] {
        background-color: #007e7a;
    }

    /* Garante que os textos da sidebar sejam brancos */
    [data-testid="stSidebar"] .stMarkdown, 
    [data-testid="stSidebar"] label, 
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span {
        color: white !important;
    }

    /* Ajusta os inputs e caixas de texto para o modo escuro */
    .stTextInput>div>div>input {
        background-color: #262730;
        color: white;
    }
    
    /* Estilização de títulos */
    h1, h2, h3 {
        color: #ffffff !important;
    }

    /* Cor de fundo para mensagens de info/sucesso se necessário */
    .stAlert {
        background-color: #262730;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- MENU LATERAL ---
st.sidebar.title("Navegação")
paginas = ["🏠 Início", "📊 Painel do Fiscal", "👥 Equipe de Gestão", "📋 Contratos"]
escolha = st.sidebar.radio("Selecione a página:", paginas)

st.sidebar.markdown("---")
st.sidebar.write("Usuário: **Rafael Santos**")

# --- CONTEÚDO PRINCIPAL ---
if escolha == "🏠 Início":
    st.title("🏛️ Portal de Gestão Contratual")
    st.write("Bem-vindo ao sistema em modo escuro.")
    st.info("O layout foi ajustado para reduzir o cansaço visual.")

# Exemplo de conteúdo para visualizar o contraste
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Contratos Ativos", value="245", delta="5%")