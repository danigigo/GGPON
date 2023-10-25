import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="AGROSAT",
    page_icon="👋",
)

st.write("# :red[STARLINK]💻 ")

st.sidebar.success("DANIEL SANTIAGO CAMACHO CALVO \n \n SANTIAGO JOSE HERRERA TORRES \n \n JEAN PAUL JUNIOR LOPEZ CERVANTES ")



st.markdown("""<p style='text-align: justify;'>Starlink es una empresa que nació como proyecto de SpaceX para la creación
            de una constelación de satélites de internet​ con el objetivo de brindar un servicio de internet de banda ancha,
            baja latencia y cobertura mundial a bajo costo.​​ SpaceX comenzó a lanzar satélites Starlink en 2019</p>""",unsafe_allow_html=True)

# OLT (Optical Line Terminal)
st.markdown('<h3 style="color:green">CONECTIVIDAD DONDE MENOS SE ESPERA</h3>', unsafe_allow_html=True)

st.markdown("""<p style='text-align: justify;'><br>Hacer streaming, las videollamadas, juegos en línea, el trabajo 
            remoto y más ahora son posibles incluso en los lugares más remotos gracias al sistema de Internet más 
            avanzado del mundo.</br><br></br></p>""",unsafe_allow_html=True)
            

video_url = "https://www.starlink.com/assets/videos/SpaceX%20Starlink%20Explainer%20Video%201080p%20desktop.mp4"
st.video(video_url)
        

st.markdown("""<p style='text-align: justify;'><br>Los soportes diseñados para instalarse permanentemente en un techo,
            poste o pared para evitar obstrucciones, estarán disponibles en la tienda de Starlink una vez que su Starlink
            esté listo para enviarse. También hay kits de enrutamiento de cables, longitudes de cable adicionales, nodos
            en malla y adaptadores Ethernet disponibles.</br><br></br></p>""",unsafe_allow_html=True)
# Colocar las imágenes en una lista
images = ['antena.jpg',
          'router.jpg',
          'adaptador.jpg',
          'soporte.jpg']

# Mostrar las imágenes en una disposición en mosaico
image_index = st.slider('Mueve la barra para ver los accesorios', 0, len(images)-1)

# Mostrar la imagen seleccionada
st.image(images[image_index], use_column_width=True)

st.markdown("""<p style='text-align: justify;'><br>Starlink envía sus kits de instalación desde Estados 
            Unidos, y actualmente el tiempo de entrega se estima entre una y dos semanas. La antena se
            debe instalar en un lugar despejado a continuacion podras observar la cobertura del servicio
            resaltada en azul</br><br></br></p>""",unsafe_allow_html=True)
            
image9 = Image.open('mapa.png')
st.image(image9)
