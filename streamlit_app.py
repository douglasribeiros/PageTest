import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="App de Notificações - Login", layout="centered")

# 2. CSS Moderno (Glassmorphism + Custom Colors)
st.markdown(f"""
    <style>
    /* Fundo com gradiente sutil */
    .stApp {{
        background: linear-gradient(135deg, #0e1117 0%, #1a1c23 100%);
    }}

    /* Esconder elementos padrão do Streamlit */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}

    /* Container de Login Moderno */
    .login-card {{
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        padding: 50px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        text-align: center;
        margin-top: 50px;
    }}

    /* Título Estilizado */
    .login-title {{
        color: #007e7a;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 700;
        font-size: 2.2rem;
        margin-bottom: 5px;
    }}
    
    .login-subtitle {{
        color: #888;
        font-size: 0.9rem;
        margin-bottom: 30px;
    }}

    /* Botão Customizado */
    .stButton > button {{
        background-color: #007e7a;
        color: white;
        width: 100%;
        border-radius: 10px;
        height: 3.5rem;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }}
    
    .stButton > button:hover {{
        background-color: #00afaa;
        border: none;
        color: white;
        transform: translateY(-2px);
    }}

    /* Estilo dos Inputs */
    .stTextInput > div > div > input {{
        background-color: rgba(255, 255, 255, 0.07) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
        height: 3rem;
    }}
    </style>
    """, unsafe_allow_html=True)

# 3. Lógica de Sessão
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def try_login():
    if st.session_state.user == "admin" and st.session_state.password == "1234":
        st.session_state.logged_in = True
    else:
        st.error("Credenciais inválidas. Tente novamente.")

# --- INTERFACE DE LOGIN ---
if not st.session_state.logged_in:
    # Centralizador vertical manual
    st.markdown("<div style='padding-top: 5vh;'></div>", unsafe_allow_html=True)
    
    with st.container():
        # HTML do Card de Login
        st.markdown(f"""
            <div class="login-card">
                <div class="login-title">App de Notificações</div>
                <div class="login-subtitle">Gestão Contratual e Fiscalização</div>
            </div>
        """, unsafe_allow_html=True)
        
        # Inputs (posicionados logo abaixo do card via colunas para ajuste fino)
        col1, col2, col3 = st.columns([1, 4, 1])
        with col2:
            st.text_input("Usuário", key="user", placeholder="Digite seu usuário")
            st.text_input("Senha", type="password", key="password", placeholder="••••••••")
            st.markdown("<br>", unsafe_allow_html=True)
            st.button("ACESSAR SISTEMA", on_click=try_login)
            
        st.markdown("</div>", unsafe_allow_html=True)

# --- INTERFACE PÓS-LOGIN ---
else:
    st.sidebar.title("App de Notificações")
    st.sidebar.write(f"Conectado como: **admin**")
    if st.sidebar.button("Encerrar Sessão"):
        st.session_state.logged_in = False
        st.rerun()

    st.title("🚀 Painel de Notificações")
    st.write("Bem-vindo ao novo ambiente de gestão.")
    
    # Exemplo de conteúdo moderno
    tabs = st.tabs(["Notificações Ativas", "Histórico", "Configurações"])
    with tabs[0]:
        st.info("Você tem 3 novas notificações de contratos aguardando revisão.")