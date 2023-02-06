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

st.set_page_config(
    page_title="Stroke Data analysis",
    page_icon="📊",
)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_download = "https://assets6.lottiefiles.com/packages/lf20_22mjkcbb.json"

lottie_download = load_lottieurl(lottie_url_download)
st.title('Data analysis of Stroke Data')

st_lottie(lottie_download, key="hello",speed=1, loop=True, quality="medium", width=700,height=400)

df = pd.read_csv('Datasets\Heart stroke.csv')
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
