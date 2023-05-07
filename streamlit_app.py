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

    st.title('Queremos saber tu opinión 📝')
    encuesta = st.selectbox('¿Qué experiencia nos quieres compartir hoy?', ['Booking', 'Check In', 'Manage my booking', 'Feedback'])


    with st.form(key="mi_formulario"):
        if encuesta == 'Booking':
            st.header('Booking 🧳')
            st.write('¿Qué tanto recomendarías nuestra página web al reservar un vuelo de Viva Aerobús?')
            nps = st.slider('Nada ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ Muy probable', 1, 10, 5)
            texto = st.text_input('¿Cuál es el motivo?')
            boton = st.form_submit_button("Enviar")
        elif encuesta == 'Check In':
            st.header('Check In 🎫')
            st.write('¿Qué tan probable es que recomiendes el proceso de Check-in en nuestra página web?')
            nps = st.slider('Nada ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ Muy probable', 1, 10, 5)
            texto = st.text_input('¿Cuál es el motivo?')
            boton = st.form_submit_button("Enviar")
        elif encuesta == 'Manage my booking':
            st.header('Manage my booking 💺')
            st.write('¿Qué tan probable es que recomiendes el proceso de \'Administrar tu reservación\'?')
            nps = st.slider('Nada ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ Muy probable', 1, 10, 5)
            texto = st.text_input('¿Cuál es el motivo?')
            boton = st.form_submit_button("Enviar")
        elif encuesta == 'Feedback':
            st.header('Feedback 📈')
            st.write('¿Cómo calificas tu experiencia con Viva Aerobús?')
            nps = st.slider('Nada ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ Muy probable', 1, 10, 5)
            texto = st.text_input('¿Alguna recomendación? Tus comentarios son muy importantes para nosotros')
            boton = st.form_submit_button("Enviar")
            
elif sections == "Pestaña 2":
    st.header("Contenido de la Pestaña 2")
    st.write("Otro texto de ejemplo")

    respuesta1, respuesta2 = encuesta()

    df = pd.DataFrame({
        'Color favorito': [respuesta1],
        'Sabor de helado favorito': [respuesta2]
    })

