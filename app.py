import streamlit as st

# Configuração da página
st.set_page_config(page_title="Portal Pro", page_icon="🚀")

# Injeção de CSS para mudar as cores de fundo e fontes
st.markdown("""
    <style>
    /* Cor de fundo do app */
    .stApp {
        background: linear-gradient(to right, #1e1e2f, #2d2d44);
        color: white;
    }
    
    /* Estilização dos inputs */
    .stNumberInput div div input {
        background-color: #3d3d5c !important;
        color: #00ffcc !important;
        border-radius: 10px !important;
    }

    /* Botão com gradiente */
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #00f2fe 0%, #4facfe 100%);
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 15px;
        font-weight: bold;
        transition: 0.3s;
    }
    
    div.stButton > button:first-child:hover {
        transform: scale(1.02);
        box-shadow: 0px 4px 15px rgba(79, 172, 254, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# Título com emoji e cor
st.markdown("<h1 style='text-align: center; color: #00f2fe;'>🎓 Simulador de Notas</h1>", unsafe_allow_html=True)
st.write("---")

# Layout em colunas
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📝 Bimestre 1")
    n1 = st.number_input("Digite a primeira nota:", min_value=0.0, max_value=10.0, step=0.5, key="n1")

with col2:
    st.markdown("### 📝 Bimestre 2")
    n2 = st.number_input("Digite a segunda nota:", min_value=0.0, max_value=10.0, step=0.5, key="n2")

st.write("") # Espaçador

if st.button("CALCULAR MÉDIA FINAL", use_container_width=True):
    media = (n1 + n2) / 2
    
    # Área de Resultado Colorida
    st.markdown(f"<h2 style='text-align: center;'>Média: {media:.1f}</h2>", unsafe_allow_html=True)
    
    if media >= 6.0:
        st.success(f"🔥 **AP
