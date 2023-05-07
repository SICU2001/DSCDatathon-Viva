import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title = "Viva Aerobus Manager",
    page_icon = '✈️',
)

st.title('Reporte diario 📊')
st.sidebar.success('¿Qué podemos hacer mejor hoy?')

dbBook = pd.read_csv("pages/booking_flow_processed.csv")

# Count the number of occurrences of each unique value in a column
counts = dbBook['negativo'].value_counts()

# Create a pie chart and display it in Streamlit
fig, ax = plt.subplots()
ax.pie(counts.values, labels=counts.index, autopct='%1.1f%%')
ax.axis('equal')
st.pyplot(fig)

