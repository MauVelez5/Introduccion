import streamlit as st 
from PIL import Image

st.title("Mi Primera App!!")#titulo o head de la pagina

st.header("benveniue")
st.write("l'importante n'est pas la chute, mais l'aterrisage")
image = Image.open('Medieval warrior.jpeg')

st.image(image,caption='Interfaces multimodales')


texto = st.text_input('Escribe algo','Este es mi texto')
st.write('El texto esccrito es',texto)

st.subheader("Ahora usemos 2 columnas")

col1,col2 = st.columns(2) 

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran a experiencia de usuario")
  resp = st.checkbox('Estoy de acuerdo')
  if resp:
    st.write('Correcto')

with col2:
  st.subheader("Esta es la segunda columna")
  modo = st.radio("Que Modalidad es la principal en tu interfaz",('Visual','auditiva','Tactil'))
  if modo == 'Visual':
    st.write('La vista es fundamental para tu interfaz')
  if modo == 'Auditiva':
    st.write('La audicion es fundamental para tu interfaz')
  if modo == 'Tactil':
    st.write('El tacto es fundamental para tu interfaz')


  
