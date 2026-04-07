import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="App de Notificações - Login", layout="centered")

# 2. CSS Moderno e Centralização Total
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0e1117 0%, #1a1c23 100%);
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Container de Login Único */
    .login-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        padding: 40px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
        text-align: center;
        color: white;
    }

    .login-title {
        color: #007e7a;
        font-weight: 700;
        font-size: 2rem;
        margin-bottom: 20px;
    }

    /* Estilo dos Inputs dentro do Card */
    .stTextInput > div > div > input {
        background-color: rgba(0, 0, 0, 0.2) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        height: 3rem;
    }

    /* Botão de Logar (Destaque) */
    .btn-login > div > button {
        background-color: #007e7a !important;
        color: white !important;
        width: 100%;
        font-weight: bold;
        border: none;
        height: 3rem;
    }

    /* Botão de Limpar (Sutil) */
    .btn-limpar > div > button {
        background-color: transparent !important;
        color: #888 !important;
        border: 1px solid #444 !important;
        width: 100%;
        height: 3rem;
    }
    
    .btn-limpar > div > button:hover {
        color: white !important;
        border-color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Lógica de Sessão e Funções
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def try_login():
    if st.session_state.user_input == "admin" and st.session_state.pass_input == "1234":
        st.session_state.logged_in = True
    else:
        st.error("❌ Usuário ou senha inválidos")

def limpar_campos():
    st.session_state.user_input = ""
    st.session_state.pass_input = ""

# --- INTERFACE DE LOGIN ---
if not st.session_state.logged_in:
    st.markdown("<div style='padding-top: 10vh;'></div>", unsafe_allow_html=True)
    
    # O container começa aqui
    with st.container():
        st.markdown('<div class="login-card">', unsafe_allow_html=True)
        st.markdown('<div class="login-title">App de Notificações</div>', unsafe_allow_html=True)
        
        # Inputs dentro do container
        st.text_input("Usuário", key="user_input", placeholder="Ex: admin")
        st.text_input("Senha", type="password", key="pass_input", placeholder="••••")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Botões centralizados lado a lado
        col_btn1, col_btn2 = st.columns(2)
        
        with col_btn1:
            st.markdown('<div class="btn-login">', unsafe_allow_html=True)
            st.button("LOGAR", on_click=try_login)
            st.markdown('</div>', unsafe_allow_html=True)
            
        with col_btn2:
            st.markdown('<div class="btn-limpar">', unsafe_allow_html=True)
            st.button("LIMPAR", on_click=limpar_campos)
            st.markdown('</div>', unsafe_allow_html=True)
            
        st.markdown('</div>', unsafe_allow_html=True)

# --- INTERFACE DO SISTEMA ---
else:
    st.title("✅ Sistema Acessado")
    st.write(f"Bem-vindo, **{st.session_state.user_input}**!")
    if st.button("Sair"):
        st.session_state.logged_in = False
        st.rerun()