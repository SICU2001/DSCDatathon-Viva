import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title = "Viva Aerobus", page_icon='✈️')

# Crea una barra lateral con los botones de las pestañas
sections = st.sidebar.radio("",
            ("Pestaña 1", "Pestaña 2"))


def encuesta():
    st.write('Por favor, responde las siguientes preguntas:')
    respuesta1 = st.radio('¿Cuál es tu color favorito?', ['Rojo', 'Azul', 'Verde'])
    respuesta2 = st.selectbox('¿Cuál es tu sabor de helado favorito?', ['Vainilla', 'Chocolate', 'Fresa', 'Menta'])
    return respuesta1, respuesta2

# Muestra el contenido de la pestaña seleccionada
if sections == "Pestaña 1":

    st.title('Queremos saber tu opinión')
    encuesta = st.selectbox('¿Qué experiencia nos quieres compartir hoy?', ['Booking', 'CheckIn', 'Manage Booking', 'Feedback'])
    st.header(encuesta)

    with st.form(key="mi_formulario"):
        if encuesta == 'Booking':
            st.write('¿Qué tanto recomendarías nuestra página web al reservar un vuelo de Viva Aerobús?')
            nps = st.slider('Nada ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ Muy probable', 1, 10, 5)
            texto = st.text_input('¿Cuál es el motivo?')
            boton = st.form_submit_button("Enviar")
            
elif sections == "Pestaña 2":
    st.header("Contenido de la Pestaña 2")
    st.write("Otro texto de ejemplo")

    respuesta1, respuesta2 = encuesta()

    df = pd.DataFrame({
        'Color favorito': [respuesta1],
        'Sabor de helado favorito': [respuesta2]
    })

