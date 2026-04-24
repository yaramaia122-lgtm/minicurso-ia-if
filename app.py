import streamlit as st

# 1. Configurações Iniciais
st.set_page_config(page_title="Portal Dev IA", page_icon="⚡", layout="centered")

# 2. Estilização Visual (Cores e Design)
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
    }
    h1 {
        color: #00FFAA;
        text-shadow: 2px 2px #000000;
    }
    .stButton>button {
        background: linear-gradient(45deg, #00FFAA, #00A8FF);
        color: black;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar
with st.sidebar:
    st.title("🚀 IF Minicurso")
    st.info("Instrutor: Yara")
    st.write("---")
    st.markdown("**Status do Servidor:** 🟢 Online")

# 4. Interface Principal
st.title("📊 Simulador de Desempenho")
st.write("Calcule a média dos alunos de forma rápida.")

# Criando as colunas - AGORA SEM ERROS DE INDENTAÇÃO
col1, col2 = st.columns(2)

with col1:
    n1 = st.number_input("Nota 01", min_value=0.0, max_value=10.0, value=0.0, step=0.1)

with col2:
    n2 = st.number_input("Nota 02", min_value=0.0, max_value=10.0, value=0.0, step=0.1)

st.divider()

# 5. Lógica do Botão
if st.button("ANALISAR RESULTADO", use_container_width=True):
    media = (n1 + n2) / 2
    
    st.markdown(f"<h2 style='text-align: center;'>Média: {media:.1f}</h2>", unsafe_allow_html=True)
    
    if media >= 6.0:
        st.success(f"✅ APROVADO! Excelente trabalho.")
        st.balloons()
    elif media >= 4.0:
        st.warning(f"⚠️ RECUPERAÇÃO! Precisa estudar mais um pouco.")
    else:
        st.error(f"❌ REPROVADO! Procure a coordenação.")
