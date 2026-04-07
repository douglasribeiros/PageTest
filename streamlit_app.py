import streamlit as st

# Configuração da página (deve ser a primeira linha)
st.set_page_config(page_title="Gestão Contratual", layout="wide", initial_sidebar_state="expanded")

# CSS para forçar o Modo Escuro e fixar o estilo da Sidebar
st.markdown("""
    <style>
    /* Fundo principal escuro */
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }

    /* Estilização da Sidebar Fixa */
    [data-testid="stSidebar"] {
        background-color: #007e7a;
        min-width: 250px;
        max-width: 300px;
    }

    /* Cor dos textos na Sidebar */
    [data-testid="stSidebar"] section[data-testid="stSidebarNav"] span,
    [data-testid="stSidebar"] .stMarkdown, 
    [data-testid="stSidebar"] label, 
    [data-testid="stSidebar"] p {
        color: white !important;
        font-weight: 500;
    }

    /* Estilo dos Radio Buttons na Sidebar */
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] {
        gap: 10px;
    }
    
    /* Títulos da página principal */
    h1, h2, h3 {
        color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONTEÚDO DA SIDEBAR (FIXA) ---
with st.sidebar:
    st.image("https://via.placeholder.com/200x80/007e7a/ffffff?text=GESTÃO+PÚBLICA", use_container_width=True)
    st.title("Menu Principal")
    
    # Navegação por botões de rádio
    paginas = ["🏠 Home", "📊 Dashboard Fiscal", "👥 Equipe de Gestão", "📜 Lista de Contratos"]
    escolha = st.radio("Navegar para:", paginas)
    
    st.markdown("---")
    st.write("👤 **Usuário:** Rafael Santos")
    st.write("🆔 **Perfil:** Gestor Master")
    
    if st.button("Sair / Logout"):
        st.toast("Sessão encerrada (Simulação)")

# --- LÓGICA DE EXIBIÇÃO DAS TELAS ---
if escolha == "🏠 Home":
    st.title("🏛️ Portal de Gestão Contratual")
    st.subheader("Bem-vindo ao sistema de monitoramento.")
    st.info("Utilize a barra lateral à esquerda para acessar os módulos. Ela permanecerá fixa durante sua navegação.")
    
    # Exemplo de conteúdo longo para testar a rolagem
    st.write("### Resumo de Atividades")
    for i in range(10):
        st.write(f"Linha de log de atividade {i+1}: Contrato X atualizado.")

elif escolha == "📊 Dashboard Fiscal":
    st.title("📊 Dashboard do Fiscal")
    col1, col2, col3 = st.columns(3)
    col1.metric("Contratos", "128", "+2")
    col2.metric("Alertas", "14", "-5")
    col3.metric("Vencimentos", "7", "Próximos 30 dias")

elif escolha == "👥 Equipe de Gestão":
    st.title("👥 Equipe de Gestão")
    st.write("Visualize os membros da equipe e suas cargas de trabalho.")
    # Inserir aqui a tabela que criamos anteriormente