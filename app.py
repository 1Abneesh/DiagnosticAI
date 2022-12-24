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
#stroke model
stroke_model = pickle.load(open('heart_stroke.sav','rb'))
scaler_stroke = pickle.load(open('scaler_heart.sav','rb'))

st.set_page_config(page_title='Mdps', page_icon="🖖")
# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['About',
                           'Diabetes Prediction',
                           'Stroke Prediction',
                           'Contact'],
                          icons=['house','heart','brain','person'],
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

if (selected == 'Stroke Prediction'):
    
    
    # page title
    st.title('Stroke Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Gender = st.selectbox('Select you gender',
                              ('Male','Female')
                              )
        if Gender == 'Male':
            Gender = 1
        else :
            Gender = 0
        
    with col2:
        Age = st.slider('Select your age',min_value=(0.0),max_value=(100.0),value=50.0,step=(0.01))
    
    with col3:
        Hypertension = st.selectbox('Are you suffering from hypertension?',
                                    ('Yes','NO')
                                    )
        if Hypertension == 'Yes':
            Hypertension = 1
        else :
            Hypertension = 0
    
    with col1:
        heart_disease =  st.selectbox('Are you suffering from any heart disease?',
                                    ('Yes','NO')
                                    )
        if heart_disease == 'Yes':
            heart_disease = 1
        else :
            heart_disease = 0
            
    with col2:
        married_status =  st.selectbox('Are you Married?',
                                    ('Yes','NO')
                                    )
        if married_status == 'Yes':
            married_status = 1
        else :
            married_status = 0
    
    with col3:
        Residence_type =  st.selectbox('Select your residence type',
                                    ('Rural','Urban')
                                    )
        if Residence_type == 'Urban':
            Residence_type = 1
        else :
            Residence_type = 0
    
    with col1:
        avg_glucose_level = st.number_input(label='Enter your glucose level',step=1.,format="%.2f")
        #avg_glucose_level = st.text_input('Enter your glucose level')
    
    with col2:
        bmi = st.number_input(label='enter your BMI',step=1.,format="%.2f")
        #bmi = st.text_input('Enter your BMI')
    
    with col3:
        work_type_Never_worked=0
        work_type_Private=0
        work_type_Self_employed=0
        work_type_children=0
        Work_type =  st.selectbox('Select your Work type',
                                    ('Never_worked','Private','Self-employed','Children')
                                    )
        if Work_type == 'Never_worked':
            work_type_Never_worked=1
        elif Work_type == 'Private':
            work_type_Private=1
        elif Work_type == 'Self-employed':
            work_type_Self_employed=1
        else:
            work_type_children=1
    with col1:
        smoking_status_formerly_smoked=0
        smoking_status_never_smoked=0
        smoking_status_smokes=0
        smoking_status =  st.selectbox('Select your smoking status',
                                    ('Formely smokes','Never smokes','Regular smokes')
                                    )
        if smoking_status == 'Formely smokes':
            smoking_status_formerly_smoked=1
        elif  smoking_status == 'Never smokes':
            smoking_status_never_smoked=1
        else:
            smoking_status_smokes=1
    
    # code for Prediction
    stroke_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Stroke Test Result'):
        
        
        
        data_stroke = [[Gender,Age,Hypertension,heart_disease,married_status,Residence_type,avg_glucose_level,bmi,work_type_Never_worked,work_type_Private,work_type_Self_employed,work_type_children,smoking_status_formerly_smoked,smoking_status_never_smoked,smoking_status_smokes]]
        lst = scaler_stroke.transform([[Age,avg_glucose_level,bmi]])
        print(data_stroke,lst)
        data_stroke[0][1],data_stroke[0][6],data_stroke[0][7] = lst[0][0],lst[0][1],lst[0][2]
        stroke_prediction = stroke_model.predict(data_stroke)
        
        if (stroke_prediction[0] >= 0.5):
          stroke_diagnosis = 'The patient has high chances of stroke'
        else:
          stroke_diagnosis = 'The patient has no chances of stroke'
        
    st.success(stroke_diagnosis)
    image = Image.open('stroke.jpg')
    st.image(image,caption='Stroke')
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
    
    
    local_css("style.css")











