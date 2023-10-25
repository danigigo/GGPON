# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:32:07 2023

@author: camac
"""

import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="AGROSAT",
    page_icon="👋",
)

st.write("# :red[EQUIPOS Y MONTAJE DE MONITOREO]💻 ")

st.sidebar.success("DANIEL SANTIAGO CAMACHO CALVO \n \n SANTIAGO JOSE HERRERA TORRES \n \n JEAN PAUL JUNIOR LOPEZ CERVANTES ")



st.markdown("""<p style='text-align: justify;'>Durante el desarrolo de este proyecto se usaron diversos equipos basicos como ARDUINO UNO y herramientas de software, pero aca vemo los equipos mas relevantes que se usaron.</p>""",unsafe_allow_html=True)

# OLT (Optical Line Terminal)
st.markdown('<h3 style="color:green">ESTACION METEOROOGICA y weather shield SPARKFUN</h3>', unsafe_allow_html=True)

st.markdown("""<p style='text-align: justify;'><br>El Weather Shield de SparkFun es un accesorio diseñado para placas Arduino que proporciona una solución compacta para medir y
         monitorear diversas condiciones meteorológicas. Este shield está equipado con sensores que permiten medir la temperatura, 
         la humedad relativa, la presión atmosférica y la velocidad y dirección del viento. Estos datos son útiles para crear estaciones 
         meteorológicas personales, proyectos de IoT relacionados con el clima, o para monitorear y registrar las condiciones ambientales 
         en tiempo real.El Weather Shield incluye sensores como el BMP180 para la presión atmosférica, el HTU21D para la temperatura y la 
         humedad, y un sensor de anemómetro y veleta para medir la velocidad y dirección del viento. La información capturada por estos 
         sensores se puede utilizar para realizar pronósticos del tiempo, estudios climáticos y más. Es una herramienta versátil para proyectos
         relacionados con la meteorología y el monitoreo ambiental.</br><br></br></p>""",unsafe_allow_html=True)
            

         
image3 = Image.open('esta.jpg')
st.image(image3)
image4 = Image.open('siono.jpg')
st.image(image4)

st.markdown('<h3 style="color:green">ANTENA DE INTERNET SATELITAL Y MODEN DE STARLINK) ):</h3>', unsafe_allow_html=True)

st.markdown("""<p style='text-align: justify;'><br>El internet satelital de Starlink utiliza una antena parabólica de 23 pulgadas para recibir
            señales de una constelación de satélites de órbita terrestre baja. La antena está conectada a un módem que convierte las señales satelitales en una conexión
         Wi-Fi.La antena parabólica es el componente más importante del sistema Starlink. Está diseñada para apuntar al cielo y recibir
         señales de los satélites. La antena está equipada con un motor que la mantiene apuntando en la dirección correcta, incluso si 
         el cielo está nublado o hay obstáculos en el camino.El módem es el componente que convierte las señales satelitales en una conexión
         Wi-Fi. El módem está conectado a la antena parabólica y a un router Wi-Fi. El router Wi-Fi distribuye la conexión a otros dispositivos
         en la casa.Starlink ofrece velocidades de descarga de hasta 200 Mbps y velocidades de subida de hasta 10 Mbps. El servicio está
         disponible en zonas rurales y urbanas de todo el mundo.En resumen, el internet satelital de Starlink utiliza una antena parabólica y 
         un módem para proporcionar una conexión a Internet de alta velocidad a zonas rurales y urbanas de todo el mundo.</br><br></br></p>""",unsafe_allow_html=True)
         

image9 = Image.open('star.jpg')
st.image(image9)

