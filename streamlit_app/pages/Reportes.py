import streamlit as st
import pandas as pd
import numpy as np

st.title('Reporte dierio 📊')
st.sidebar.success('¿Qué podemos hacer mejor hoy?')

db = pd.read_csv("booking_flow_processed")

st.write(db)