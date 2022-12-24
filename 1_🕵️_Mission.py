# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 16:26:31 2022

@author: 01abn
"""
import time
import requests
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner



st.set_page_config(
    page_title="Multiple Disease Prediction System",
    page_icon="👨‍⚕️",
)

st.title("Multiple Disease Prediction System")


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_url_doctor = "https://assets5.lottiefiles.com/packages/lf20_42B8LS.json"
lottie_doctor = load_lottieurl(lottie_url_doctor)

col1,  col2 = st.columns([10,5])
with col1:
    st.write("We are making various model with high accuracy to predict diseases easily and fast.Our app is free of cost which take various patient data as input and predict what disease patient is suffering from.our model is trained on verified lab dataset and have high accuracy.Currently Diabetes prediction and stroke prediction is fully working is fully working and many others to come.Fell free to contact from contact form for any suggestion.🙂")
with col2:
    st_lottie(lottie_doctor, key="hello",speed=1, loop=True, quality="medium", width=300,height=200)
st.write("")
col1,col2,col3 = st.columns([1,2,1])
with col2:
    st.markdown("""**_"Eat fruits plenty, keep body wealthy."_**<br>""",True)

st.header('Lets look below how the system would work')

# st.markdown(""" # h1 tag
# ## h2 tag
# ### h3 tag
# :moon:<br>
# :sunglasses:
# ** bold **
# _ italics _
# """,True)


image = Image.open('about.jpg')
st.image(image,caption='AI in medical')

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("pages.css")