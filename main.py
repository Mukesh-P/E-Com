import streamlit as st
from PIL import Image
import csv
from autocorrect import Speller

st.set_page_config(page_title="Cetch-up", page_icon="Logo-e.png", layout='wide')


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def strike(text):
    return ''.join([u'\u0336{}'.format(c) for c in text])


def insert_(word):
    split_l = []
    insert_list = []

    # Making pairs of the split words
    for i in range(len(word) + 1):
        split_l.append((word[0:i], word[i:]))

    # Storing new words in a list
    # But one new character at each location
    alphs = 'abcdefghijklmnopqrstuvwxyz'
    insert_list = [a + l + b for a, b in split_l for l in alphs]
    return insert_list


local_css("style.css")
with st.container():
    st.title("Welcome to Cetch-up :wave:")
    spell = Speller()
    Product = spell(st.text_input('Enter Product Name'))
    if Product:
        st.write('The Results for the Product', Product)
        with open('All_Products-db.csv', 'r', newline='') as s:
            a = csv.reader(s)
            r = list(a)
            for i in r:
                if i[0].lower() in Product.lower():
                    with st.container():
                        img = Image.open(str(i[1]))
                        img_cl, txt_cl = st.columns((1, 2))
                        with txt_cl:
                            st.header(i[0])
                            st.subheader(i[2])
                            st.write(strike(i[3]), i[4])

                        with img_cl:
                            st.image(img)

with st.sidebar:
    st.write("Categories")
    st.link_button('Toys & School Supplies',
                   "https://www.flipkart.com/toysclp-store?fm=neo%2Fmerchandising&iid=M_d8ce983a-97c2-4812-83dc-30003d836e86_1_372UD5BXDFYS_MC.A6A2ZZGHEZUT&otracker=hp_rich_navigation_6_1.navigationCard.RICH_NAVIGATION_Beauty%252C%2BToys%2B%2526%2BMore~Toys%2B%2526%2BSchool%2BSupplies_A6A2ZZGHEZUT&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_6_L1_view-all&cid=A6A2ZZGHEZUT")
    st.link_button("Fashion & Essentials",
                   'https://www.flipkart.com/fashion-ss23-trendy-store?fm=neo%2Fmerchandising&iid=M_3c971f6a-80e9-4f4c-81e2-512d872afbf7_1_372UD5BXDFYS_MC.GXQPTNACQ6S3&otracker=hp_rich_navigation_10_1.navigationCard.RICH_NAVIGATION_Fashion~Essentials_GXQPTNACQ6S3&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_10_L1_view-all&cid=GXQPTNACQ6S3')
