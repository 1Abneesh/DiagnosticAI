# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 20:36:19 2022

@author: 01abn
"""

import time
import requests

import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

import streamlit as st

from streamlit_card import card

st.title("Streamlit Card - test")

res = card(
    title="Streamlit Card",
    text="This is a test card",
    image="https://placekitten.com/500/500",
    url="https://github.com/gamcoh/st-card",
)

st.write(res)
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_url_hello = "https://assets5.lottiefiles.com/packages/lf20_42B8LS.json"
lottie_url_download = "https://assets4.lottiefiles.com/private_files/lf30_t26law.json"
lottie_hello = load_lottieurl(lottie_url_hello)
lottie_download = load_lottieurl(lottie_url_download)


st_lottie(lottie_hello, key="hello",speed=1, loop=True, quality="medium", width=500,height=700)

if st.button("Download"):
    with st_lottie_spinner(lottie_download, key="download"):
        time.sleep(5)
    st.balloons()