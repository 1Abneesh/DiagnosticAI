# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 16:55:45 2022

@author: 01abn
"""
import streamlit as st
import pickle
from streamlit_option_menu import option_menu
from PIL import Image
st.set_page_config(
    page_title="Contact us",
    page_icon="👨‍⚕️",
)
st.header(":mailbox: Get In Touch With Me!")
contact_form = """
<form action="https://formsubmit.co/01abneeshkumar@gmail.com" method="POST">
 <input type="text" name="name" placeholder = "Your name" required>
 <input type="email" name="email" placeholder = "Your email" required>
 <textarea name="message" name="subject" placeholder="Your message here"></textarea>
 <button type="submit">Send</button>
 </form>"""

st.markdown(contact_form,unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")