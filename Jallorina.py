import streamlit as st
from PIL import Image
import os
import base64

# Function to convert image to base64
def get_image_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Setting the page configuration (this must be the first Streamlit command)
st.set_page_config(page_title="John Joshua Jallorina - Portfolio & Blog", page_icon=":camera:", layout="centered")

# Custom CSS for fonts, styling, and animations
st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Lora:ital@1&family=Raleway:wght@300&display=swap');
    
    /* Apply general body font */
    html, body, [class*="css"]  {
        font-family: 'Raleway', sans-serif;
        background-color: white;  /* White background */
        color: #333333;  /* Dark text for readability */
        scroll-behavior: smooth;
    }

    /* Header font */
    .stTitle {
        font-family: 'Lora', serif;
        text-align: center;
        color: #C0392B;  /* Red color */
        margin-top: 20px;
        animation: fadeIn 2s ease-in-out;
    }

    /* Subheader font */
    .stSubheader {
        font-family: 'Lora', serif;
        color: #C0392B;  /* Red color */
        text-align: center;
        margin-bottom: 30px;
        animation: fadeIn 2s ease-in-out;
    }

    /* Profile picture styling */
    .profile-pic {
        display: block;
        margin-left: auto;
        margin-right: auto;
        border-radius: 50%;
        margin-bottom: 1rem;
        width: 150px;
        height: 150px;
        object-fit: cover;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
        animation: bounceIn 2s ease-in-out;
    }

    /* Container for autobiography */
    .autobiography-container {
        padding: 20px;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        margin-bottom: 30px;
        animation: slideInLeft 1s ease-in-out;
    }

    /* Spacing between images */
    .image-container {
        display: flex;
        justify-content: space-between;
        margin-bottom: 2rem; /* Adds spacing below the images */
        animation: fadeInUp 2s ease-in-out;
    }

    /* Image captions styling */
    .image-caption {
        font-style: italic;
        color: #C0392B;  /* Red color */
        text-align: center;
        margin-top: 1rem;
    }

    /* Project section styling */
    .project-container {
        padding: 20px;
        background-color: #f8f8f8;
        border-radius: 10px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        margin-bottom: 30px;
        animation: slideInRight 1s ease-in-out;
    }

    /* Blog post styling */
    .blog-container {
        padding: 20px;
        background-color: #fefefe;
        border-radius: 10px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        margin-bottom: 30px;
        animation: fadeIn 2s ease-in-out;
    }

    /* Call-to-Action section */
    .cta-section {
        text-align: center;
        padding: 40px;
        background-color: #333333;  /* Black background */
        color: white;
        border-radius: 10px;
        margin-bottom: 30px;
        animation: zoomIn 2s ease-in-out;
    }

    /* Button styling */
    .stButton > button {
        background-color: #C0392B;  /* Red button */
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-family: 'Raleway', sans-serif;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.3s ease;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    .stButton > button:hover {
        background-color: #A93226;  /* Darker red on hover */
        transform: scale(1.05);
    }

    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes bounceIn {
        from { transform: scale(0.5); opacity: 0; }
        to { transform: scale(1); opacity: 1; }
    }

    @keyframes slideInLeft {
        from { transform: translateX(-100%); }
        to { transform: translateX(0); }
    }

    @keyframes slideInRight {
        from { transform: translateX(100%); }
        to { transform: translateX(0); }
    }

    @keyframes fadeInUp {
        from { transform: translateY(20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }

    @keyframes zoomIn {
        from { transform: scale(0.5); opacity: 0; }
        to { transform: scale(1); opacity: 1; }
    }
    
    </style>
""", unsafe_allow_html=True)

# Convert your image and prepare the HTML image tag
image_path = 'C:\\Users\\johnj\\Desktop\\Streamlit\\profile.jpg'  # Adjust the path as necessary
image_base64 = get_image_base64(image_path)
image_html = f'<img src="data:image/jpeg;base64,{image_base64}" class="profile-pic">'

# Header
st.markdown(image_html, unsafe_allow_html=True)
st.title("John Joshua Jallorina 📚💼")
st.subheader("Cebu Institute of Technology - University 🎓")

# About Me Section
st.markdown('<div class="autobiography-container">', unsafe_allow_html=True)
st.markdown("### About Me 💬")
st.write("""
Hi, I am John Joshua Jallorina and I am interested in business and technology. I started developing an interest in these fields to better understand the world around me and how various systems operate. 
I aim to combine my IT knowledge with my passion for business and technology to create innovative solutions and contribute to meaningful discussions.
         
         I am currently a BSIT - 4 student in Cebu Institute of Technology - University
    Currently residing in Tisa, Cebu city
    22 years old
""")
st.markdown('</div>', unsafe_allow_html=True)

# Hobbies Section
st.markdown('<div class="project-container">', unsafe_allow_html=True)
st.markdown("### Hobbies 🚀")
st.write("""
Here are some of my hobbies and interests:
1. Basketball 🏀
2. Riding 🏍️
3. Coding 💻
""")
st.markdown('</div>', unsafe_allow_html=True)

# Projects Section
st.markdown('<div class="project-container">', unsafe_allow_html=True)
st.markdown("### Projects 📝")
st.write("""
Here are some of the projects I've been involved with:
1. **FindNest**: A Lost and Found app website for CIT-U as a capstone project using React and Sprinboot.
2. **NoteEaze**: Created a notes app with an edgy design using django framework. The website featured a responsive design with different features such as posting notes, adding photos and rich text and etc using Django.
""")
# Optionally add images or links to the projects if you have any
# st.image('path_to_project_image.jpg', caption='FindNest App Interface', width=300)
st.markdown('</div>', unsafe_allow_html=True)
