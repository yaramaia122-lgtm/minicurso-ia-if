import streamlit as st

st.title("Calculadora de Notas do IF")

n1 = st.text_input("Introduza a Nota 1")
n2 = st.text_input("Introduza a Nota 2")

if st.button("Calcular Média"):
  media = (float(n1) + float(n2)) / 2
  st.write("A tua média é:", media)
