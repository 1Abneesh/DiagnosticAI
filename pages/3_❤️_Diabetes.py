# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 16:38:20 2022

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


diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
scaler = pickle.load(open('scaler.sav','rb'))

st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="👨‍⚕️",
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
    nav_page("Stroke")