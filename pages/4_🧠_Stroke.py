# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 16:48:36 2022

@author: 01abn
"""
import time
import requests
import pickle
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import base64
from streamlit.components.v1 import html

# page title
st.set_page_config(
    page_title="Stroke Prediction",
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

st.title('Stroke Prediction using ML')

stroke_model = pickle.load(open('heart_stroke3.sav','rb'))
scaler_stroke = pickle.load(open('scaler_heart3.sav','rb'))

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

lottie_url_download = "https://assets2.lottiefiles.com/packages/lf20_kvw2mn6a.json"
lottie_url_stroke = "https://assets7.lottiefiles.com/packages/lf20_pulxxm1o.json"
lottie_stroke = load_lottieurl(lottie_url_stroke)
lottie_download = load_lottieurl(lottie_url_download)


st_lottie(lottie_stroke, key="hello",speed=1, loop=True, quality="medium", width=700,height=400)
st.write('According to the World Health Organization (WHO) stroke is the 2nd leading cause of death globally, responsible for approximately 11% of total deaths.This AI model is used to predict whether a patient is likely to get stroke based on the input parameters like gender, age, various diseases, and smoking status.')
st.write("")
st.write("")
st.header("Please enter the required fields to get result.")
st.write("")
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

flag = 0

if st.button('Stroke Test Result'):
    data_stroke = [[Gender,Age,Hypertension,heart_disease,married_status,Residence_type,avg_glucose_level,bmi,work_type_Never_worked,work_type_Private,work_type_Self_employed,work_type_children,smoking_status_formerly_smoked,smoking_status_never_smoked,smoking_status_smokes]]
    lst = scaler_stroke.transform([[Age,avg_glucose_level,bmi]])
    print(data_stroke,lst)
    data_stroke[0][1],data_stroke[0][6],data_stroke[0][7] = lst[0][0],lst[0][1],lst[0][2]
    stroke_prediction = stroke_model.predict(data_stroke)
    
    if (stroke_prediction[0] >= 0.5):
      stroke_diagnosis = 'The patient has high chances of stroke'
      flag =1
    else:
      stroke_diagnosis = 'The patient has no chances of stroke'
    with st_lottie_spinner(lottie_download, key="download",height=100,width=200):
        time.sleep(5)
if flag == 1:
    st.error("You required to consult your doctor.",  icon="🚨")
st.success(stroke_diagnosis)
st.write("")
st.header('Let us see some symtomps of stroke.')
image = Image.open('stroke_sym.jpg')
st.image(image,caption='Stroke')

#applying css
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
    nav_page("Data_Analysis_stroke")