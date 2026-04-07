import streamlit as st

# Configuração da página
st.set_page_config(page_title="Menu Principal", layout="wide")

# Verificação de Segurança (Impede que acessem a página sem logar)
if 'auth' not in st.session_state or not st.session_state.auth:
    st.error("Acesso negado. Por favor, faça login.")
    st.stop() # Interrompe a execução aqui

# --- BARRA LATERAL COM LOGOUT ---
with st.sidebar:
    st.title("App de Notificações")
    st.write(f"Usuário: **admin**")
    
    if st.button("🚪 Sair / Logout"):
        st.session_state.auth = False
        # Volta para o arquivo principal (tela de login)
        st.switch_page("streamlit_app.py")

# --- CONTEÚDO DO MENU PRINCIPAL ---
st.title("🚀 Menu Principal")
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("### 📊 Dashboards\nVisualize os indicadores de contratos.")
    if st.button("Abrir Dashboards"):
        pass # Você pode criar outra página e dar switch_page aqui

with col2:
    st.success("### 📋 Notificações\nGerencie os alertas pendentes.")

with col3:
    st.warning("### 👥 Equipe\nGestão de fiscais e gestores.")