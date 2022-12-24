# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 16:38:20 2022

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



diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
scaler = pickle.load(open('scaler.sav','rb'))

st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="👨‍⚕️",
)

st.title('Diabetes Prediction using ML')

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_download = "https://assets2.lottiefiles.com/packages/lf20_kvw2mn6a.json"
lottie_url_doctor = "https://assets2.lottiefiles.com/packages/lf20_n08ryckr.json"
lottie_doctor = load_lottieurl(lottie_url_doctor)
lottie_download = load_lottieurl(lottie_url_download)


st_lottie(lottie_doctor, key="hello",speed=1, loop=True, quality="medium", width=700,height=400)
# getting the input data from the user

st.write(('Diabetes is a disease that occurs when your blood glucose, also called blood sugar, is too high. Blood glucose is your main source of energy and comes from the food you eat. Insulin, a hormone made by the pancreas, helps glucose from food get into your cells to be used for energy. Sometimes your body doesn’t make enough—or any—insulin or doesn’t use insulin well. Glucose then stays in your blood and doesn’t reach your cells.'))
st.write('About 422 million people worldwide have diabetes, the majority living in low-and middle-income countries, and 1.5 million deaths are directly attributed to diabetes each year. Both the number of cases and the prevalence of diabetes have been steadily increasing over the past few decades. ')



st.write("")
st.header('Please enter the reuired fields to get result.')
st.write("")
col1, col2, col3 = st.columns(3)

with col1:
    Pregnancies = st.text_input('Number of Pregnancies')
    
with col2:
    Glucose = st.text_input('Glucose Level')

with col3:
    BloodPressure = st.text_input('Blood Pressure value')

with col1:
    SkinThickness = st.text_input('Skin Thickness value')

with col2:
    Insulin = st.text_input('Insulin Level')

with col3:
    BMI = st.text_input('BMI value')

with col1:
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

with col2:
    Age = st.text_input('Age of the Person')


# code for Prediction
diab_diagnosis = ''

# creating a button for Prediction
flag =0

if st.button('Diabetes Test Result'):
    scaled_data = scaler.transform([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    diab_prediction = diabetes_model.predict(scaled_data)
    
    if (diab_prediction[0] == 1):
      diab_diagnosis = 'The patient is diabetic'
      flag=1
    else:
      diab_diagnosis = 'The patient is not diabetic'
    with st_lottie_spinner(lottie_download, key="download",height=100,width=200):
        time.sleep(5)
st.success(diab_diagnosis)

st.header('Let us see some symtomps of diabetes.')
if flag == 1:
    st.error("You required to consult your doctor.",  icon="🚨")
image = Image.open('dia.jpg')
st.image(image,caption='Diabetes')

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("pages.css")