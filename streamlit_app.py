import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Login - Gestão Contratual", layout="centered")

# 2. CSS para Centralização Vertical e Estilo Clean
st.markdown("""
    <style>
    /* Esconde o menu padrão e o footer do Streamlit para um look mais limpo */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Centralização da caixa de login */
    .stTextInput {
        margin-bottom: 10px;
    }
    
    .stButton > button {
        background-color: #007e7a;
        color: white;
        width: 100%;
        border-radius: 5px;
        height: 3em;
    }

    .login-container {
        padding: 40px;
        border-radius: 15px;
        background-color: #1e2129;
        border: 1px solid #333;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Lógica de Autenticação
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def check_login():
    if st.session_state.user == "admin" and st.session_state.password == "1234":
        st.session_state.logged_in = True
        st.success("Acesso liberado!")
    else:
        st.error("Usuário ou senha inválidos")

# --- INTERFACE ---

if not st.session_state.logged_in:
    # Espaçamento superior para centralizar verticalmente
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    
    # Criando a caixa centralizada
    with st.container():
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.title("🔒 Login")
        
        st.text_input("Usuário", key="user")
        st.text_input("Senha", type="password", key="password")
        
        st.button("Entrar", on_click=check_login)
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # O que aparece após o login
    st.sidebar.button("Sair", on_click=lambda: st.session_state.update(logged_in=False))
    st.title("🏛️ Bem-vindo ao Sistema")
    st.write("Você está logado como Administrador.")
    st.info("Painel de Gestão Contratual Ativo.")