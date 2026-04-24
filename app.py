import streamlit as st

# Configuração da página - Layout Wide fica mais moderno
st.set_page_config(page_title="Portal do Aluno", page_icon="🎓", layout="centered")

# Estilização básica para um visual mais "clean"
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        border-radius: 20px;
        height: 3em;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar - Informações do Curso
with st.sidebar:
    st.title("👨‍💻 Desenvolvedor")
    st.info("Minicurso: IA para Devs")
    st.divider()
    st.write("Versão 2.0")

# Conteúdo Principal
st.title("📊 Simulador de Desempenho")
st.caption("Insira as notas abaixo para calcular a média e verificar o status.")

# Criando um card visual com as colunas
with st.container():
    c1, c2 = st.columns(2)
    
    with c1:
        # Usei number_input para evitar erros de digitação de texto
        n1 = st.number_input("Nota do 1º Bimestre", min_value=0.0, max_value=10.0, step=0.1)
    
    with c2:
        n2 = st.number_input("Nota do 2º Bimestre", min_value=0.0, max_value=10.0, step=0.1)

    st.markdown("---") # Linha divisória

    if st.button("Analisar Desempenho", use_container_width=True, type="primary"):
        media = (n1 + n2) / 2
        
        # Exibição do resultado com métricas
        st.subheader(f"Média Final: {media:.1f}")
        
        if media >= 6.0:
            st.balloons()
            st.success("**APROVADO!** Parabéns pelo seu esforço! 🎉")
        elif media >= 4.0:
            st.warning("**RECUPERAÇÃO.** Você ainda tem uma chance! 📚")
        else:
            st.error("**REPROVADO.** Procure o apoio pedagógico. ❌")
