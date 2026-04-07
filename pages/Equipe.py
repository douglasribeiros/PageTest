import streamlit as st
import pandas as pd

# 1. Configuração da Página
st.set_page_config(page_title="Equipe de Gestão", layout="wide")

# 2. Estilização Customizada (Cor 007e7a)
st.markdown(f"""
    <style>
    .main-header {{
        background-color: #007e7a;
        color: white;
        padding: 1.5rem;
        border-radius: 0.5rem;
        text-align: center;
        font-family: sans-serif;
        margin-bottom: 2rem;
    }}
    .metric-card {{
        background-color: #f8f9fa;
        border: 1px solid #e9ecef;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #007e7a;
    }}
    </style>
    """, unsafe_allow_html=True)

# 3. Cabeçalho Estilo Banner
st.markdown('<div class="main-header"><h1>PÁGINA EQUIPE GESTÃO CONTRATUAL</h1></div>', unsafe_allow_html=True)

# 4. Linha de Métricas (Cards Superiores)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="metric-card"><strong>Total de Membros</strong><br><h2>18</h2></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card"><strong>Contratos Ativos</strong><br><h2>245</h2></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card"><strong>Tarefas Pendentes</strong><br><h2 style="color:red;">31</h2></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="metric-card"><strong>Prazo Médio</strong><br><h2>12 dias</h2></div>', unsafe_allow_html=True)

st.write("---")

# 5. Listagem da Equipe (Dados Simulados)
st.subheader("Membros da Equipe e Responsabilidades")

data = {
    "Nome": ["Ana Silva", "Pedro Santos", "Juliana Lima", "Ricardo Oliveira", "Maria Eduarda"],
    "Cargo": ["Coordenadora", "Analista Pleno", "Fiscal de Contrato", "Gestor Pleno", "Assistente"],
    "Contratos Ativos": [45, 32, 18, 25, 12],
    "Status": ["Ativo", "Ativo", "Em Férias", "Ativo", "Ativo"],
    "Última Atualização": ["05/04/2026", "07/04/2026", "20/03/2026", "06/04/2026", "07/04/2026"]
}

df = pd.DataFrame(data)

# Exibição da Tabela com filtros
search = st.text_input("Filtrar membro da equipe por nome:")
if search:
    df = df[df['Nome'].str.contains(search, case=False)]

st.dataframe(df, use_container_width=True, hide_index=True)

# 6. Distribuição de Carga (Gráfico Simples)
st.write("---")
st.subheader("Distribuição de Carga de Trabalho")
st.bar_chart(df.set_index('Nome')['Contratos Ativos'], color="#007e7a")

# 7. Rodapé informativo
st.caption("Sistema de Gestão Contratual - Atualizado em tempo real")