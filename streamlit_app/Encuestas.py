import requests
import json
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title = "Viva Aerobus Manager",
    page_icon = '✈️',
)

st.title('Queremos saber tu opinión 📝')
st.sidebar.success('¿Cómo funciona el modelo en tiempo real?')

# Muestra el contenido de la pestaña seleccionada

encuesta = st.selectbox('¿Qué experiencia nos quieres compartir hoy?', ['Booking', 'Check In', 'Manage my booking', 'Feedback'])
respuesta = ""

with st.form(key="mi_formulario"):
        if encuesta == 'Booking':
            st.header('Booking 🧳')
            st.write('¿Qué tanto recomendarías nuestra página web al reservar un vuelo de Viva Aerobús?')
            nps = st.slider('Nada ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ Muy probable', 1, 10, 5)
            texto = st.text_input('¿Cuál es el motivo?')
            boton = st.form_submit_button("Enviar")
            if boton:
                data = data={"feedback": str(texto)}
                res = requests.post("http://20.85.237.99/analyze-feedback", data=json.dumps(data))
                respuesta = res.json()["message"]
        elif encuesta == 'Check In':
            st.header('Check In 🎫')
            st.write('¿Qué tan probable es que recomiendes el proceso de Check-in en nuestra página web?')
            nps = st.slider('Nada ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ Muy probable', 1, 10, 5)
            texto = st.text_input('¿Cuál es el motivo?')
            boton = st.form_submit_button("Enviar")
            if boton:
                data = data={"feedback": str(texto)}
                res = requests.post("http://20.85.237.99/analyze-feedback", data=json.dumps(data))
                respuesta = res.json()["message"]
        elif encuesta == 'Manage my booking':
            st.header('Manage my booking 💺')
            st.write('¿Qué tan probable es que recomiendes el proceso de \'Administrar tu reservación\'?')
            nps = st.slider('Nada ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ Muy probable', 1, 10, 5)
            texto = st.text_input('¿Cuál es el motivo?')
            boton = st.form_submit_button("Enviar")
            if boton:
                data = data={"feedback": str(texto)}
                res = requests.post("http://20.85.237.99/analyze-feedback", data=json.dumps(data))
                respuesta = res.json()["message"]
        elif encuesta == 'Feedback':
            st.header('Feedback 📈')
            st.write('¿Cómo calificas tu experiencia con Viva Aerobús?')
            nps = st.slider('Nada ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ Muy probable', 1, 10, 5)
            texto = st.text_input('¿Alguna recomendación? Tus comentarios son muy importantes para nosotros')
            boton = st.form_submit_button("Enviar")
            if boton:
                data = data={"feedback": str(texto)}
                res = requests.post("http://20.85.237.99/analyze-feedback", data=json.dumps(data))
                respuesta = res.json()["message"]

        

if(respuesta != ""):
     st.info(respuesta)

st.write('_No visible para el cliente:_')

st.write('**Sentimiento:** ', 'Positivo')
st.write('**Tema:** ', 'Servicio')



