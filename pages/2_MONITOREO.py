# -- coding: utf-8 --
"""
Created on Tue May  9 15:32:07 2023

@author: camac
"""
import streamlit as st

import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title="AGROSAT",
    page_icon="👋",
)

# Definimos los datos

st.write("# :red[MONITOREO EN TIEMPO REAL]🌩️")

st.sidebar.success("DANIEL SANTIAGO CAMACHO CALVO \n \n SANTIAGO JOSE HERRERA TORRES \n \n JEAN PAUL JUNIOR LOPEZ CERVANTES ")



import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Datos de las 7 gráficas
data = [
    {
        'title': "Angulo de el aire ",
        'x_data': [2, 4, 6, 8, 10, 12, 14],
        'y_data': [57, 170, 185, 165, 170, 175, 160],
        'line_color': 'blue'
    },
    {
        'title': "Velocidad del aire Km/s",
        'x_data': [2, 4, 6, 8, 10, 12, 14],
        'y_data': [5, 18, 20, 17, 18, 16, 19 ],
        'line_color': 'green'
    },
    {
        'title': "Humedad",
        'x_data': [2, 4, 6, 8, 10, 12, 14],
        'y_data': [0, 42, 43, 45, 44, 50,47],
        'line_color': 'red'
    },
    {
        'title': "Temperatura",
        'x_data': [2, 4, 6, 8, 10, 12, 14],
        'y_data': [0, 28.4, 30.1, 29.5, 29.1, 28.8, 28.4],
        'line_color': 'purple'
    },
    {
        'title': "Nivel de lluvia (ml)",
        'x_data': [2, 4, 6, 8, 10, 12, 14],
        'y_data': [0, 0, 5, 10, 25, 26, 24],
        'line_color': 'orange'
    },
    {
        'title': "Presion (kilo-pascales )",
        'x_data': [2, 4, 6, 8, 10, 12, 14],
        'y_data': [0, 90.4, 90.4, 90.3, 90.4, 90.4, 90.3],
        'line_color': 'pink'
    },
    {
        'title': "Nivel de luz %",
        'x_data': [2, 4, 6, 8, 10, 12, 14],
        'y_data': [0, 30, 55, 65, 70, 50, 30],
        'line_color': 'brown'
    }
]


st.markdown(
    '<style>body { background-color: #0e1117; }</style>',
    unsafe_allow_html=True
)

# Crear las gráficas y mostrarlas en el dashboard
fig, axes = plt.subplots(3, 3, figsize=(10, 10), facecolor='#0e1117')

for i, grafica in enumerate(data):
    ax = axes[i // 3, i % 3]
    ax.plot(grafica['x_data'], grafica['y_data'], marker='o', color=grafica['line_color'])
    ax.set_title(grafica['title'], color='darkred', fontsize=10, fontweight='bold', alpha=0.7)  # Tamaño de letra
    ax.spines['bottom'].set_color('white')  # Eje X en blanco
    ax.spines['top'].set_color('white')  # Eje X en blanco
    ax.spines['left'].set_color('white')  # Eje Y en blanco
    ax.spines['right'].set_color('white')  # Eje Y en blanco
    ax.title.set_color('white')  # Títulos en rojo
    ax.xaxis.label.set_color('white')  # Etiqueta del eje X en blanco
    ax.yaxis.label.set_color('white')  # Etiqueta del eje Y en blanco
    ax.tick_params(axis='x', colors='white')  # Números del eje X en blanco
    ax.tick_params(axis='y', colors='white')  # Números del eje Y en blanco
    ax.grid(True, color='grey', linestyle='--', linewidth=0.5)  # Agregar cuadrícula en todas las gráficas

# Agregar espacio en blanco para las gráficas que faltan
for i in range(len(data), 9):
    ax = axes[i // 3, i % 3]
    ax.axis('off')

# Centrar la gráfica 7 en la fila inferior central
axes[2, 1].axis('off')
fig.delaxes(axes[2, 2])

st.pyplot(fig)