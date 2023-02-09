# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 00:43:11 2022

@author: 01abn
"""

from pathlib import Path
from streamlit.components.v1 import html
import streamlit as st
from PIL import Image
import base64

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent.parent if "__file__" in locals() else Path.cwd()
#print(current_dir)
css_file = current_dir / "main.css"
resume_file = current_dir / "resume.pdf"
profile_pic = current_dir / "pic.png"



DESCRIPTION = """
A positive, bold, confident, and dedicated Computer Engineering student from the Army Institute of Technology
with a keen interest in ML and AI. I actively participate in various hackathons related to machine learning. 
I have worked on various projects related to AI/ML such as object detection, Stroke prediction Using Deep Learning, Diabetes prediction ,Sonar vs Rock mine prediction and many more.
In free time I like to play 🏏cricket and 👨‍💻competative programming.
"""
EMAIL = "01abneeshkumar@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/1abneesh/",
    "GitHub": "https://github.com/1Abneesh",
    "Website": "https://multiple-disease-prediction-app.onrender.com/"
}



st.set_page_config(page_title='ABOUT ME', page_icon="👨‍⚕️")

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
# # --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# # --- header SECTION ---
col1, col2 = st.columns([1,1.5], gap="small")
with col1:
    st.image(profile_pic, width=250)

with col2:
    st.title('Abneesh Kumar')
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# # --- Education ---
st.write('\n')
st.subheader("Education")
st.write(
    """
- 👉 B.E in Computer Engineering - Army Institute of Technology (S.G.P.A = 9.44)
- 👉 12th Boards Army Public School, Lucknow (91%)
- 👉 10th Boards Army Public School, Lucknow (95%)
"""
)


# # --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write(
    """
- 👩‍💻 Programming Languages: Python , C++
- 🐍 Python packages: Numpy,Pandas,Tensorflow,Matplotlib, Seaborn,Scikit-learn,OpenCV, Streamlit
- 💻 Machine Learning
- ⌨️ OOP(C++,Python)
- 🗄️ Databases:  MongoDB, MySQL
"""
)

# # Achievements
ACHIEVEMENTS = {
    "🥇 AWS Student DeepRacer - Securing Top 30 position in semifinals":"https://drive.google.com/file/d/1zxzVvFSemIHJkXLt7ZJKayve4dFMoESA/view?usp=share_link",
    "🥇 IICC (Innovate India coding championship) - Securing 957 rank in which more than 200000+ student participate.":"https://drive.google.com/file/d/1jtbNSutENjQH4jcbu5rygzL720v-ZU-c/view?usp=share_link",
    "🥇 Udchalo scholarship - scholarship for Exemplary academic and all-round performance in first year of engineering":"https://drive.google.com/file/d/1jukLNsqfxCbW7FMmT9hLhDuPwXzSfph2/view?usp=share_link"
    }
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for achievement, link in ACHIEVEMENTS.items():
    st.write(f"[{achievement}]({link})")
# # --- Projects  ---
PROJECTS = {
    "📁 Multiple disease prediction system - Machine learning based web app to detect multiple diseases. This app is developed on streamlit.": "https://multiple-disease-prediction-app.onrender.com/",
    "📁 SONAR Rock vs Mine Prediction -  Machine learning project to detect whether an object is either Rock or Mine with SONAR Data": "https://github.com/1Abneesh/SONAR-Rock-vs-Mine-Prediction",
    "📁 Object tracking - Detecting region of intrest in video with computer vision": "https://github.com/1Abneesh/Object-tracking.git",
    "📁 Steganography - Hiding messages inside an image by using LSB steganography technique": "https://github.com/1Abneesh/Steganography.git",
}
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

flag = True
# if st.button('Magic Button'):
#     if flag:
#         st.snow()
#         flag = False
#     else :
#         st.balloons()
#         flag = True
#defining styling of button
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
    nav_page("Diabetes")