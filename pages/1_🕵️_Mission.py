# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 16:26:31 2022

@author: 01abn
"""
import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import base64
from streamlit.components.v1 import html


st.set_page_config(
    page_title="Multiple Disease Prediction System",
    page_icon="👨‍⚕️",
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

st.title("Multiple Disease Prediction System")

def nav_page(page_name, timeout_secs=3):
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {
                        links[i].click();
                        return;
                    }
                }
                var elasped = new Date() - start_time;
                if (elasped < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    html(nav_script)
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

#defining styling of button
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

if st.button("Next page"):
    nav_page("About_me")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.balloons()
local_css("pages.css")