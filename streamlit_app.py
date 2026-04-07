import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="App de Notificações - Login", layout="centered")

# 2. CSS Avançado para Forçar os Itens dentro do Card
st.markdown("""
    <style>
    /* Fundo gradiente */
    .stApp {
        background: linear-gradient(135deg, #0e1117 0%, #1a1c23 100%);
    }

    /* Esconder headers e footers */
    header, footer, #MainMenu {visibility: hidden;}

    /* ESTILO DO CONTAINER DE LOGIN (O segredo está aqui) */
    [data-testid="stVerticalBlock"] > div:has(div.login-anchor) {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        padding: 40px !important;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
        text-align: center;
    }

    /* Título personalizado */
    .login-title {
        color: #007e7a;
        font-weight: 700;
        font-size: 2.2rem;
        margin-bottom: 20px;
        text-align: center;
    }

    /* Inputs */
    .stTextInput input {
        background-color: rgba(0, 0, 0, 0.3) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
    }

    /* Botão Logar */
    div[data-testid="stButton"] > button:first-child {
        background-color: #007e7a !important;
        color: white !important;
        border: none !important;
        width: 100%;
        height: 3.5rem;
        font-weight: bold;
    }

    /* Botão Limpar */
    div[data-testid="stButton"] > button:not(:first-child), 
    .btn-secondary button {
        background-color: transparent !important;
        color: #888 !important;
        border: 1px solid #444 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Lógica de Login
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

def validar():
    if st.session_state.user == "admin" and st.session_state.password == "1234":
        st.session_state.autenticado = True
    else:
        st.error("Usuário ou senha incorretos")

def limpar():
    st.session_state.user = ""
    st.session_state.password = ""

# --- TELA DE LOGIN ---
if not st.session_state.autenticado:
    # Espaçamento superior
    st.markdown("<div style='height: 15vh;'></div>", unsafe_allow_html=True)
    
    # Esta div vazia serve como "âncora" para o CSS encontrar o container correto
    st.markdown('<div class="login-anchor"></div>', unsafe_allow_html=True)
    
    # Tudo dentro deste bloco ficará visualmente dentro do Card
    st.markdown('<div class="login-title">App de Notificações</div>', unsafe_allow_html=True)
    
    st.text_input("Usuário", key="user", placeholder="admin")
    st.text_input("Senha", type="password", key="password", placeholder="1234")
    
    col1, col2 = st.columns(2)
    with col1:
        st.button("LOGAR", on_click=validar, use_container_width=True)
    with col2:
        # Usamos uma classe auxiliar para o botão secundário
        st.markdown('<div class="btn-secondary">', unsafe_allow_html=True)
        st.button("LIMPAR", on_click=limpar, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- TELA DO SISTEMA ---
else:
    st.success("Logado com sucesso!")
    if st.button("Logout"):
        st.session_state.autenticado = False
        st.rerun()