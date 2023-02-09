# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 23:43:03 2023

@author: 01abn
"""

#Import the required Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_lottie import st_lottie
import plotly.express as px
import requests
import base64
from streamlit.components.v1 import html

st.set_page_config(
    page_title="Stroke Data analysis",
    page_icon="📊",
)

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

lottie_url_download = "https://assets6.lottiefiles.com/packages/lf20_22mjkcbb.json"

lottie_download = load_lottieurl(lottie_url_download)
st.title('Data analysis of Stroke Data')

st_lottie(lottie_download, key="hello",speed=1, loop=True, quality="medium", width=700,height=400)

df = pd.read_csv('Heart stroke.csv')
df.drop(columns="id",inplace=True)

st.write('Studying data is amongst the everyday chores of researchers. It’s not a big deal for them to go through hundreds of pages per day to extract useful information from it. However, recent times have seen a massive jump in the amount of data available. While it’s certainly good news for researchers to get their hands on more data that could result in better studies, it’s also no less than a headache.')

def hist_plot(x_val):
    plt.suptitle('Visualising the Distribution of Numerical features based on target variable', fontsize = 25, color = 'mediumblue')
    fig = px.histogram(df,x = x_val, color = 'stroke')
    st.plotly_chart(fig, use_container_width=True)


option = df.drop(columns="stroke") 
st.write('')
x_axis_val = st.selectbox('Select the value to get stroke information', options=option.columns)
hist_plot(x_axis_val)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("pages.css")


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
    nav_page("Contact_me")