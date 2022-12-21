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



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Disease_2',
                           'Disease_3'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies','insert a value')
        
    with col2:
        Glucose = st.text_input('Glucose Level','insert a value')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value','insert a value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value','insert a value')
    
    with col2:
        Insulin = st.text_input('Insulin Level','insert a value')
    
    with col3:
        BMI = st.text_input('BMI value','insert a value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value','insert a value')
    
    with col2:
        Age = st.text_input('Age of the Person','insert a value')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        scaled_data = scaler.transform([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        diab_prediction = diabetes_model.predict(scaled_data)
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)
    image = Image.open('dia.jpg')
    st.image(image,caption='Diabetes')


# Heart Disease Prediction Page
if (selected == 'Disease_2'):
    
    st.title('Heart Disease Prediction using ML coming soon')

# # Parkinson's Prediction Page
if (selected == "Disease_3"):
    
#     # page title
    st.title("Parkinson's Disease Prediction using ML coming soon")















