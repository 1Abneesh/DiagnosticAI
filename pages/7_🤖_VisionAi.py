# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 03:13:41 2023

@author: 01abn
"""
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import base64
import webbrowser

st.set_page_config(
    page_title="VisionAI",
    page_icon="👨‍⚕️"    
)

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(png_file):
    with open(png_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def build_markup_for_logo(
    png_file,
    background_position="50% 10%",
    margin_top="10%",
    image_width="60%",
    image_height="",
):
    binary_string = get_base64_of_bin_file(png_file)
    return """
            <style>
                [data-testid="stSidebarNav"] {
                    background-image: url("data:image/png;base64,%s");
                    background-repeat: no-repeat;
                    background-position: %s;
                    margin-top: %s;
                    background-size: %s %s;
                }
            </style>
            """ % (
        binary_string,
        background_position,
        margin_top,
        image_width,
        image_height,
    )


def add_logo(png_file):
    logo_markup = build_markup_for_logo(png_file)
    st.markdown(
        logo_markup,
        unsafe_allow_html=True,
    )

add_logo("logo1.png")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_download = "https://assets5.lottiefiles.com/private_files/lf30_NgL6jT.json"
lottie_download = load_lottieurl(lottie_url_download)
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #ce1126;
    color: white;
    height: 3em;
    width: 12em;
    border-radius:10px;
    border:3px solid #000000;
    font-size:20px;
    font-weight: bold;
    margin: auto;
    display: block;
}

div.stButton > button:hover {
	background:linear-gradient(to bottom, #ce1126 5%, #ff5a5a 100%);
	background-color:#ce1126;
}

div.stButton > button:active {
	position:relative;
	top:3px;
}

</style>""", unsafe_allow_html=True)

def open_search(search_term):
    webbrowser.open(f"{search_term}")

st.title("Flower Classifier")

st_lottie(lottie_download, key="hello",speed=1, loop=True, quality="medium", width=700,height=400)
st.write("This is a flower classification app based on the pretrained VGG19 model. It can classify 102 different species of flowers.")

st.header("How to Use")
st.write("1. Upload an image of a flower.")
st.write("2. The app will classify the flower species.")
st.write("3. You can view the results and probability scores for each species.")

st.header("Features")
st.write("-> Pretrained VGG19 model for high accuracy.")
st.write("-> Ability to classify 102 different species of flowers.")
st.write("-> User-friendly interface for easy use.")
st.write('')

st.image('logo.png',width=700)

st.write('')
st.write('')
st.header("Contact Us")
st.write("For any inquiries or questions, please contact us at 01abneeshkumar@gmail.com.")

st.write("")
if st.button('VisionAI'):
    open_search('https://visionai.onrender.com')

#applying css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("pages.css")