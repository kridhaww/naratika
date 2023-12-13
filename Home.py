import streamlit as st
from PIL import Image

st.set_page_config(
    page_title = "home",
    page_icon = None

)

image = Image.open("batik.jpg")
st.image(image,caption='Batik Kawung Source Pinterest')

st.markdown("<h1 style='text-align: center; color:black;'>Naratika</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color:black;'>#TakKenalMakaTakSayang</h5>", unsafe_allow_html=True)

st.sidebar.success("Choose Page")

tab1, tab2= st.tabs(["About Naratika", "Team Member"])

with tab1:
   st.header("Naratika")
   st.write(
    "Naratika is a Data Mining II project by Team 1 of SD-A2 class. It aims to preserve Indonesian batik using technology. The project uses image classification principles to classify batik motifs according to their names. The project aims to make batik motifs more recognizable to the public, in order to preserve them."
)

with tab2:
   st.header("Introducing")
   col1, col2, col3= st.columns(3)
   col4, col5= st.columns(2)
   imagem = Image.open("mikeok.jpg")
   imagej = Image.open("ijah.jpeg")
   imagef = Image.open("farid.jpeg")
   imagek = Image.open("kridhaw.png")
   images = Image.open("sean.jpeg")

with col1:
   st.image(imagem,width=180)
   st.write("Name : Michael Adi Herryanto")
   st.write("NIM : 162112133024")

with col2:
   st.image(imagej,width=180)
   st.write("Name : Syarifah Fildzah Shahab")
   st.write("NIM : 162112133060")

with col3:
   st.image(imagek,width=180)
   st.write("Name : Kridha Mei Wulandari")
   st.write("NIM : 162112133091")

with col4:
   st.image(imagef,width=180)
   st.write("Name : Farid Ardhan")
   st.write("NIM : 162112133084")

with col5:
   st.image(images,width=180)
   st.write("Name : Sean Adam")
   st.write("NIM : 162112133101")





