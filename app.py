# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 16:45:55 2022

@author: 01abn
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
scaler = pickle.load(open('scaler.sav','rb'))
#[theme]


st.set_page_config(page_title='Mdps', page_icon="🖖")
# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['About',
                           'Diabetes Prediction',
                           'Contact'],
                          icons=['house','heart','person'],
                          default_index=0,
    styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
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
    
    if st.button('Diabetes Test Result'):
        scaled_data = scaler.transform([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        diab_prediction = diabetes_model.predict(scaled_data)
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The patient is diabetic'
        else:
          diab_diagnosis = 'The patient is not diabetic'
        
    st.success(diab_diagnosis)
    image = Image.open('dia.jpg')
    st.image(image,caption='Diabetes')


# Heart Disease Prediction Page
if (selected == 'About'):
    st.balloons()
    st.title('🧑‍🎓 About us')
    st.header('Mission')
    st.write("We are making various model with high accuracy to predict diseases easily and fast.Our app is free of cost which take various patient data as input and predict what disease patient.our model is trained on verified lab dataset with high accuracy.Currently Diabetes prediction is fully working and many others to come.")
    image = Image.open('about.jpg')
    st.image(image,caption='AI in medical')

# # Parkinson's Prediction Page
if (selected == "Contact"):


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


local_css("style\style.css")











