import streamlit as st 
from PIL import Image

st.title("Mi Primera App!!")#titulo o head de la pagina

st.header("benveniue")
st.write("l'importante n'est pas la chute, mais l'aterrisage)
image = Image.open('Interfaces multimodales')

st.image(image,caption='Interfaces multimodales')
