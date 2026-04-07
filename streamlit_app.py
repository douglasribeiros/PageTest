import streamlit as st

# Configuração da página
st.set_page_config(page_title="Teste de Acesso - Gestão", page_icon="✅")

# CSS customizado para usar a sua cor 007e7a
st.markdown(f"""
    <style>
    .main-header {{
        background-color: #007e7a;
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
    }}
    .status-card {{
        background-color: #f0f2f6;
        border-left: 5px solid #007e7a;
        padding: 15px;
        margin: 10px 0;
    }}
    </style>
    """, unsafe_allow_html=True)

# Cabeçalho no estilo dos seus cards
st.markdown('<div class="main-header"><h1>Página Equipe Gestão Contratual</h1></div>', unsafe_allow_html=True)

st.success("🚀 O sistema está online e acessível!")

# Simulação de funcionalidades
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="status-card"><h3>Dashboard</h3><p>Conexão com banco de dados: <b>OK</b></p></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="status-card"><h3>Notificações</h3><p>Módulo de alertas: <b>Ativo</b></p></div>', unsafe_allow_html=True)

# Botão de teste de interação
if st.button('Registrar Notificação (Teste)'):
    st.balloons()
    st.info("Botão pressionado com sucesso no servidor!")

st.sidebar.title("Configurações")
st.sidebar.write("Versão de Teste: 1.0.0")