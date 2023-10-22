# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:11:33 2023

@author: camac
"""

import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="AGROSAT",
    page_icon="👋",
)

st.write("# :red[¿QUE ES AGROSAT?]📡🖥️🌱 ")

st.sidebar.success("DANIEL SANTIAGO CAMACHO CALVO \n \n SANTIAGO JOSE HERRERA TORRES \n \n JEAN PAUL JUNIOR LOPEZ CERVANTES ")

st.markdown("""<p style='text-align: justify;'>En el siempre cambiante panorama de la agroindustria, el aprovechamiento de tecnología de vanguardia es fundamental para un crecimiento sostenible. "AGROSAT" surge como una iniciativa pionera, comprometida con mejorar la conectividad y las comunicaciones en el ámbito agroindustrial. Nuestro proyecto tiene como objetivo implementar una red de acceso a Internet vía satélite, diseñada específicamente para fortalecer las operaciones de las redes de sensores en el ecosistema de Internet de las Cosas (IoT). Este póster ofrece una visión de los objetivos centrales y las actividades de "AGROSAT", que incluyen explorar los últimos avances en tecnología de acceso satelital, desplegar un sistema de Internet satelital completamente integrado y evaluar el rendimiento en la transmisión de datos. Únase a nosotros en este viaje mientras nos esforzamos por revolucionar la conectividad en el sector de la agroindustria, garantizando un flujo óptimo de datos y la exitosa implementación de soluciones de conectividad basadas en satélites.</p>""",unsafe_allow_html=True)

# :red[""]


image = Image.open('agroo.jpg')

st.image(image)




