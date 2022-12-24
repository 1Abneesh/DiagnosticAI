# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 00:43:11 2022

@author: 01abn
"""

from pathlib import Path

import streamlit as st
from PIL import Image


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