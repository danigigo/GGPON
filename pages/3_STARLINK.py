import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="AGROSAT",
    page_icon="👋",
)

st.write("# :red[STARLINK]💻 ")

st.sidebar.success("DANIEL SANTIAGO CAMACHO CALVO \n \n SANTIAGO JOSE HERRERA TORRES \n \n JEAN PAUL JUNIOR LOPEZ CERVANTES ")



st.markdown("""<p style='text-align: justify;'>Durante el desarrolo de este proyecto se usaron diversos equipos basicos como ARDUINO UNO y herramientas de software, pero aca vemo los equipos mas relevantes que se usaron.</p>""",unsafe_allow_html=True)

# OLT (Optical Line Terminal)
st.markdown('<h3 style="color:green">CONECTIVIDAD DONDE MENOS SE ESPERA</h3>', unsafe_allow_html=True)

st.markdown("""<p style='text-align: justify;'><br>Hacer streaming, las videollamadas, juegos en línea, el trabajo 
            remoto y más ahora son posibles incluso en los lugares más remotos gracias al sistema de Internet más 
            avanzado del mundo.</br><br></br></p>""",unsafe_allow_html=True)
            

video_url = "https://www.starlink.com/assets/videos/SpaceX%20Starlink%20Explainer%20Video%201080p%20desktop.mp4"
st.video(video_url)
        

image9 = Image.open('mapa.png')
st.image(image9)

st.markdown("""<p style='text-align: justify;'><br>Los soportes diseñados para instalarse permanentemente en un techo,
            poste o pared para evitar obstrucciones, estarán disponibles en la tienda de Starlink una vez que su Starlink
            esté listo para enviarse. También hay kits de enrutamiento de cables, longitudes de cable adicionales, nodos
            en malla y adaptadores Ethernet disponibles.</br><br></br></p>""",unsafe_allow_html=True)
# Colocar las imágenes en una lista
images = ['star.jpg',
          'router.jpg',
          'adaptador.jpg',
          'soporte.jpg']

# Mostrar las imágenes en una disposición en mosaico
image_index = st.slider('Mueve la barra para ver mas enemigos', 0, len(images)-1)

# Mostrar la imagen seleccionada
st.image(images[image_index], use_column_width=True)