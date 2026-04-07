import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="App de Notificações - Login", layout="centered")

# 2. CSS Avançado (Injeção de Estilo no Contêiner Nativo)
st.markdown("""
    <style>
    /* Fundo Gradiente */
    .stApp {
        background: linear-gradient(135deg, #0e1117 0%, #1a1c23 100%);
    }

    /* Esconder Header e Footer */
    header, footer, #MainMenu {visibility: hidden;}

    /* ESTILO DO CARD (Aplicado ao container que contém a classe login-card) */
    [data-testid="stVerticalBlock"]:has(div.login-card) {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        padding: 40px !important;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
    }

    /* Título Centralizado */
    .title-text {
        color: #007e7a;
        font-weight: 800;
        font-size: 2.2rem;
        text-align: center;
        margin-bottom: 25px;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Inputs Estilizados */
    .stTextInput input {
        background-color: rgba(0, 0, 0, 0.3) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
    }

    /* Botão Logar (Principal) */
    div[data-testid="stButton"] button {
        border-radius: 10px !important;
        height: 3.5rem;
        font-weight: bold;
        transition: 0.3s;
    }

    /* Customização específica do botão LOGAR */
    div.stButton > button:first-child:not(.limpar-btn button) {
        background-color: #007e7a !important;
        color: white !important;
        border: none !important;
    }

    /* Customização específica do botão LIMPAR */
    div.limpar-btn button {
        background-color: transparent !important;
        color: #888 !important;
        border: 1px solid #444 !important;
    }
    
    div.limpar-btn button:hover {
        border-color: #007e7a !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Lógica de Login
if 'auth' not in st.session_state:
    st.session_state.auth = False

def login():
    if st.session_state.usr == "admin" and st.session_state.pwd == "1234":
        st.session_state.auth = True
    else:
        st.error("Usuário ou senha incorretos")

def reset():
    st.session_state.usr = ""
    st.session_state.pwd = ""

# --- TELA DE LOGIN ---
if not st.session_state.auth:
    # Espaçador superior
    st.markdown("<div style='height: 15vh;'></div>", unsafe_allow_html=True)

    # CRIANDO O CONTEINER ÚNICO
    # Usamos o st.container para agrupar tudo visualmente
    with st.container():
        # A classe login-card serve como 'âncora' para o nosso CSS lá de cima
        st.markdown('<div class="login-card"></div>', unsafe_allow_html=True)
        
        st.markdown('<div class="title-text">App de Notificações</div>', unsafe_allow_html=True)
        
        st.text_input("Usuário", key="usr", placeholder="Digite seu usuário")
        st.text_input("Senha", type="password", key="pwd", placeholder="••••")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.button("LOGAR", on_click=login, use_container_width=True)
        with col2:
            # Envolvemos este botão em uma div específica para mudar a cor via CSS
            st.markdown('<div class="limpar-btn">', unsafe_allow_html=True)
            st.button("LIMPAR", on_click=reset, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

# --- TELA PÓS LOGIN ---
else:
    st.sidebar.success("Conectado")
    if st.sidebar.button("Logout"):
        st.session_state.auth = False
        st.rerun()
    
    st.title("🚀 Dashboard Principal")
    st.write("Bem-vindo ao sistema de notificações.")