import streamlit as st
from PIL import Image

st.markdown("<h1 style='text-align: center; color:black;'>The Idea of Naratika</h1>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4= st.tabs(["Background", "Goals", "Dataset","Methodology"])

with tab1:
   st.header("Why Batik?")
   st.write("Batik merupakan salah satu bentuk dari karya seni khas Indonesia, dimana karya seni tersebut telah diakui sebagai warisan budaya tak benda oleh UNESCO pada tahun 2003. Perkembangan motif batik yang ada membuat jumlah motif batik bertambah, tidak terkecuali pada daerah yang ada di Pulau Jawa . Penambahan motif batik tersebut membuat budaya Indonesia semakin kaya. Hal tersebut dapat menjadi keunikan dan daya tarik bagi Indonesia. Namun hal tersebut akan menjadi sebuah tantangan yang besar dimana setiap warga negara memiliki kewajiban untuk menjaga serta melestarikan budaya tersebut. Tantangan tersebut akan membawa permasalahan yang cukup serius apabila motif batik di Indonesia tidak dikenali oleh warganya sendiri.")

with tab2:
   st.header("Goals")
   st.write("Melakukan penelitian dan melakukan klasifikasi motif batik agar motif batik dapat diketahui oleh masyarakat. Sehingga masyarakat dapat mengenali motif batik khususnya di Pulau Jawa untuk kemudian dapat melestarikannya")

with tab3:
    st.header("About the Data")
    imagem = Image.open("merge.png")
    st.image(imagem,width=500)
    st.write("Data yang digunakan dalam penelitian ini adalah jenis data tidak terstruktur, yaitu data gambar. Dimana data tidak terstruktur merupakan jenis data yang tidak memiliki format atau struktur tertentu yang dapat diorganisir dengan mudah. Data gambar yang digunakan adalah data gambar batik untuk setiap daerah di pulau Jawa yaitu DK Jakarta, Jawa Barat, DI Yogyakarta, Jawa Tengah, dan Jawa Timur. Data tersebut diperoleh dari Google Images dengan memanfaatkan Google Extension yang bernama Download All Images. Dari daerah tersebut diambil satu jenis motif batik yang menjadi khas, kemudian setiap kategori tersebut diambil 500 gambar.")
    
with tab4:
    st.header("Method")
    st.write("Berikut ini merupakan metode yang digunakan dalam penelitian ini. Melakukan data augmentation, melakukan scaling pixel, memisahahkan gambar menjadi batch, membagi batches untuk data train dan test, memodelkan data menggunakan CNN, melakukan training dan testing pada data. Preprocessing data dan pemodelan data untuk data gambar yang telah diuraikan sebelumnya dilakukan menggunakan serangkaian pemrograman menggunakan bahasa pemrograman Python dan akan dilakukan deployment menggunakan Streamlit,  platform yang memungkinkan pembuatan antarmuka pengguna yang interaktif untuk model dan aplikasi data sains. Dengan demikian, hasil dari penelitian ini dapat diakses dan digunakan dengan lebih mudah oleh pengguna akhir.")
