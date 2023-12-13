import streamlit as st  
import tensorflow as tf
import random
from PIL import Image, ImageOps
import numpy as np
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="Batik classification",
    initial_sidebar_state = 'auto'
)

hide_streamlit_style = """
	<style>
  #MainMenu {visibility: hidden;}
	footer {visibility: hidden;}
  </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


with st.sidebar:
        st.subheader("#TakKenalMakaTakSayang")

st.write("""
         # Naratika 
         """
         )

st.set_option('deprecation.showfileUploaderEncoding', False)
@st.cache_data
def load_model():
    model=tf.keras.models.load_model("batikclassifier3.h5")
    return model
with st.spinner('Model is being loaded..'):
    model=load_model()

file = st.file_uploader("", type=["jpg", "png","jpeg"])
def import_and_predict(image_data, model):
        size = (256,256)    
        image = ImageOps.fit(image_data, size)
        img = np.asarray(image) / 255.0
        img_reshape = img[np.newaxis,...]
        prediction = model.predict(img_reshape)
        return prediction

        
if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    predictions = import_and_predict(image, model)

    class_names = {
    0: 'Gajah Oling',
    1: 'Kawung',
    2: 'Mega Mendung',
    3: 'Parang',
    4: 'Pucuk Rebung'
}
    batik_index = np.argmax(predictions)
    batik_key = list(class_names.keys())[list(class_names.values()).index(class_names[batik_index])]
    string = "Pattern: " + class_names[batik_key]
    if class_names[np.argmax(predictions)] == 'Kawung':
        st.info("Kawung : Motif kawung bermakna kesempurnaan, kemurnian dan kesucian. Motif ini berasal dari daerah DI Yogyakarta")
    elif class_names[np.argmax(predictions)] == 'Gajah Oling':
        st.info('Gajah Oling : Motif Gajah Oling memiliki makna selalu mengingat yang maha Agung. Motif ini berasal dari Jawa Timur')
    elif class_names[np.argmax(predictions)] == 'Mega Mendung':
        st.info("Mega Mendung : Motif batik Mega Mendung melambangkan pemberian harapan akan turunnya hujan yang penting untuk menyuburkan pertanian. Motif ini berasal dari Jawa Barat")
    elif class_names[np.argmax(predictions)] == 'Parang':
        st.info("Parang : Batik parang memiliki makna petuah untuk tidak pernah menyerah, ibarat ombak laut yang tak pernah berhenti bergerak. Batik parang juga menggambarkan jalinan yang tidak pernah putus, baik dalam arti upaya untuk memperbaiki diri, upaya memperjuangkan kesejahteraan, maupun bentuk pertalian keluarga. Motif ini berasal dari Jawa Tengah")
    elif class_names[np.argmax(predictions)] == 'Pucuk Rebung':
        st.info("Pucuk Rebung : Motif Pucuk Rebung melambangkan kekuatan yang muncul dari dalam. Motif ini berasal dari Jakarta")
