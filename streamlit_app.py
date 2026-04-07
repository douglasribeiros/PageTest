import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Sistema de Gestão Contratual", layout="wide")

# 2. CSS Customizado para Login e Tema Escuro
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    [data-testid="stSidebar"] { background-color: #007e7a; }
    .login-box {
        max-width: 400px;
        padding: 2rem;
        border-radius: 10px;
        background-color: #1e2129;
        margin: auto;
        border: 1px solid #007e7a;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Gerenciamento de Autenticação
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False

def realizar_login(usuario, senha):
    if usuario == "admin" and senha == "1234":
        st.session_state['autenticado'] = True
        st.success("Login realizado com sucesso!")
        st.rerun() # Recarrega a página para entrar no sistema
    else:
        st.error("Usuário ou senha incorretos.")

def realizar_logout():
    st.session_state['autenticado'] = False
    st.rerun()

# --- TELA DE LOGIN ---
if not st.session_state['autenticado']:
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.title("🔐 Acesso ao Sistema")
        st.subheader("Gestão Contratual")
        
        usuario_input = st.text_input("Usuário")
        senha_input = st.text_input("Senha", type="password")
        
        if st.button("Entrar", use_container_width=True):
            realizar_login(usuario_input, senha_input)
        st.markdown('</div>', unsafe_allow_html=True)

# --- TELA INTERNA (APÓS LOGIN) ---
else:
    # Menu Lateral Fixo
    with st.sidebar:
        st.header("🏢 GESTÃO ATIVA")
        st.markdown(f"👤 **Bem-vindo, { 'Administrador' }**")
        st.markdown("---")
        
        menu = st.radio("Navegação", ["🏠 Home", "📊 Dashboard", "👥 Equipe", "📋 Contratos"])
        
        st.markdown("---")
        if st.button("🚪 Sair do Sistema"):
            realizar_logout()

    # Conteúdo das Páginas
    if menu == "🏠 Home":
        st.title("🏛️ Painel Principal")
        st.write("Bem-vindo ao Portal de Gestão Contratual.")
        st.info("Utilize o menu lateral para gerenciar as notificações e fiscais.")
        
        # Exemplo de Cards
        c1, c2, c3 = st.columns(3)
        c1.metric("Contratos Ativos", "142")
        c2.metric("Notificações Hoje", "12")
        c3.metric("Fiscais Online", "5")

    elif menu == "📊 Dashboard":
        st.title("📊 Indicadores de Desempenho")
        st.bar_chart({"Contratos": [10, 25, 15, 30], "Meses": ["Jan", "Fev", "Mar", "Abr"]})

    elif menu == "👥 Equipe":
        st.title("👥 Gestão da Equipe")
        st.write("Membros ativos no sistema de fiscalização.")

    elif menu == "📋 Contratos":
        st.title("📋 Lista de Contratos")
        st.write("Filtre e visualize detalhes de cada contrato.")