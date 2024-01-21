import streamlit as st
import csv

st.set_page_config(page_title="Cetch-up", page_icon="Logo-e.png", layout='wide')


def local_css(file_name):
    with open(file_name) as ff:
        st.markdown(f"<style>{ff.read()}</style>", unsafe_allow_html=True)


local_css("style.css")

session_state = {}
saved = False
with st.container():
    st.title('Welcome Seller!!!')

    if 'Image' not in session_state.keys():
        session_state['Image'] = None

    with st.container():
        picture = st.camera_input("Take a picture :camera_with_flash:")

        if picture:
            session_state['Image'] = picture

        if session_state['Image']:
            cl1, cl2 = st.columns(2)
            with cl1:
                st.image(session_state['Image'])

            colA, colB = st.columns(2)
            ncol1, ncol2 = st.columns(2)
            fileName = session_state['Image'].name

            with colA:
                save = st.button("Save Image", help="Save Image as Your Product Image")
                if save:
                    with open(fileName, "wb") as imageFile:
                        imageFile.write(session_state['Image'].getbuffer())
                        st.success("The Image Has Been Added to The DataBase as " + fileName)

            with ncol1:
                with st.form("Product Details"):
                    det = st.text_input("Enter Product Name: ")
                    rate = st.text_input("Enter Price Of the Product: ")
                    off_rate = st.text_input("Enter Offer Price of the Product: ")
                    off_per = st.text_input("Enter the Offer Percentage of the Product: ")
                    submitted = st.form_submit_button('Submit')
                    if det != '' and rate != '' and off_rate != '' and off_per != '':
                        with open('All_Products-db.csv', 'a', newline='') as o:
                            wr = csv.writer(o)
                            wr.writerow([det, fileName, off_rate, rate, off_per])

                    if submitted and (det != '' and rate != '' and off_rate != '' and off_per != ''):
                        st.success("The Form Has Been Added to the Data Base")
                    elif submitted and not (det != '' and rate != '' and off_rate != '' and off_per != ''):
                        st.warning('Please Fill all the Details', icon="⚠️")
