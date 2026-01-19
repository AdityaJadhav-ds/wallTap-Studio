import streamlit as st
import os

def inject_css():
st.markdown(""" <style>
html, body, [class*="css"] {
background-color: #0e1117;
color: #f2f2f2;
font-family: 'Segoe UI', sans-serif;
}
#MainMenu, footer, header {
visibility: hidden;
}
.nav-bar {
display: flex;
justify-content: space-between;
align-items: center;
padding: 1.2rem 3rem;
background: #0e1117;
position: sticky;
top: 0;
z-index: 100;
}
.nav-brand {
font-size: 1.6rem;
font-weight: 700;
color: #ffffff;
}
.nav-links button {
background: transparent;
border: none;
color: #cccccc;
font-size: 1rem;
margin-left: 1.2rem;
cursor: pointer;
transition: all 0.3s ease;
}
.nav-links button:hover {
color: #ff4b4b;
transform: translateY(-2px);
}
.hero {
padding: 5rem 3rem 3rem 3rem;
text-align: center;
}
.hero-title {
font-size: 3.5rem;
font-weight: 800;
letter-spacing: 1px;
}
.hero-subtitle {
font-size: 1.4rem;
margin-top: 1rem;
color: #bbbbbb;
}
.cta-button {
margin-top: 2rem;
background: #ff4b4b;
border: none;
color: #ffffff;
padding: 0.9rem 2.2rem;
font-size: 1rem;
border-radius: 30px;
cursor: pointer;
transition: all 0.3s ease;
}
.cta-button:hover {
background: #ff6b6b;
transform: translateY(-3px);
}
.section {
padding: 3rem;
}
.section-divider {
height: 1px;
background: #222;
margin: 3rem 0;
}
.card {
background: #141922;
border-radius: 18px;
padding: 2rem;
box-shadow: 0 12px 30px rgba(0,0,0,0.4);
transition: all 0.3s ease;
height: 100%;
}
.card:hover {
transform: translateY(-6px);
box-shadow: 0 20px 50px rgba(0,0,0,0.6);
}
.card-title {
font-size: 1.3rem;
font-weight: 700;
margin-bottom: 0.5rem;
}
.card-desc {
font-size: 1rem;
color: #b0b0b0;
}
.portfolio-image {
width: 100%;
height: 200px;
object-fit: cover;
border-radius: 12px;
margin-bottom: 1rem;
background: #1e1e1e;
}
.service-icon {
font-size: 2.5rem;
margin-bottom: 1rem;
}
.about-text {
max-width: 900px;
font-size: 1.1rem;
line-height: 1.8;
color: #cccccc;
}
.contact-container {
max-width: 700px;
margin: auto;
background: #141922;
padding: 2.5rem;
border-radius: 20px;
box-shadow: 0 15px 40px rgba(0,0,0,0.5);
}
.footer {
background: #0b0e13;
padding: 2rem;
text-align: center;
color: #888888;
font-size: 0.9rem;
}
.footer-brand {
font-weight: 700;
color: #ffffff;
margin-bottom: 0.5rem;
} </style>
""", unsafe_allow_html=True)

def render_nav():
if "page" not in st.session_state:
st.session_state.page = "Home"
col1, col2 = st.columns([3, 7])
with col1:
st.markdown('<div class="nav-brand">Aditya Creative Studio</div>', unsafe_allow_html=True)
with col2:
c1, c2, c3, c4, c5 = st.columns(5)
with c1:
if st.button("Home", key="nav_home"):
st.session_state.page = "Home"
with c2:
if st.button("Portfolio", key="nav_portfolio"):
st.session_state.page = "Portfolio"
with c3:
if st.button("Services", key="nav_services"):
st.session_state.page = "Services"
with c4:
if st.button("About", key="nav_about"):
st.session_state.page = "About"
with c5:
if st.button("Contact", key="nav_contact"):
st.session_state.page = "Contact"

def render_home():
st.markdown(""" <div class="hero"> <div class="hero-title">Aditya Creative Studio</div> <div class="hero-subtitle">We craft cinematic digital experiences.</div> </div>
""", unsafe_allow_html=True)
if st.button("View Our Work", key="cta_home"):
st.session_state.page = "Portfolio"
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown(""" <div class="section"> <p class="about-text">
We are a modern creative studio blending cinematic storytelling, intelligent systems, and refined design to build unforgettable digital experiences. </p> </div>
""", unsafe_allow_html=True)
cols = st.columns(3)
features = [
("Design", "High-end visual identity and UI design crafted for impact."),
("Storytelling", "Cinematic narratives that emotionally engage audiences."),
("AI", "Intelligent automation and AI-powered creative solutions.")
]
for col, feature in zip(cols, features):
with col:
st.markdown(f""" <div class="card"> <div class="card-title">{feature[0]}</div> <div class="card-desc">{feature[1]}</div> </div>
""", unsafe_allow_html=True)

def render_portfolio():
st.markdown('<div class="section"><div class="card-title">Portfolio</div></div>', unsafe_allow_html=True)
projects = [
("Cinematic Website", "A premium cinematic landing page experience.", "project1.jpg"),
("Brand Identity", "Complete branding system for a startup.", "project2.jpg"),
("AI Assistant", "Conversational AI for business automation.", "project3.jpg"),
("Product Launch", "High-impact visual launch campaign.", "project4.jpg"),
("Film Teaser", "Cinematic teaser production.", "project5.jpg"),
("Web App UI", "Dark-mode SaaS interface design.", "project6.jpg")
]
cols = st.columns(3)
for i, project in enumerate(projects):
title, desc, image_file = project
image_path = os.path.join("assets", image_file)
with cols[i % 3]:
if os.path.exists(image_path):
st.markdown(f""" <div class="card"> <img src="data:image/png;base64,{st.image(image_path, use_container_width=True)._repr_png_().decode('latin1') if False else ''}" class="portfolio-image"/> <div class="card-title">{title}</div> <div class="card-desc">{desc}</div> </div>
""", unsafe_allow_html=True)
st.image(image_path, use_container_width=True)
st.markdown(f""" <div class="card-title">{title}</div> <div class="card-desc">{desc}</div>
""", unsafe_allow_html=True)
else:
st.markdown(f""" <div class="card"> <div class="portfolio-image"></div> <div class="card-title">{title}</div> <div class="card-desc">{desc}</div> </div>
""", unsafe_allow_html=True)

def render_services():
st.markdown('<div class="section"><div class="card-title">Services</div></div>', unsafe_allow_html=True)
services = [
("🎨", "Branding & Identity", "Visual identity systems and brand storytelling."),
("🎥", "Video Production", "Cinematic videos and promotional content."),
("💻", "Web Design", "High-end websites and UI/UX design."),
("🤖", "AI Solutions", "Automation, chatbots, and intelligent systems."),
("🧠", "Content Strategy", "Strategic content planning and execution.")
]
cols = st.columns(3)
for i, service in enumerate(services):
icon, title, desc = service
with cols[i % 3]:
st.markdown(f""" <div class="card"> <div class="service-icon">{icon}</div> <div class="card-title">{title}</div> <div class="card-desc">{desc}</div> </div>
""", unsafe_allow_html=True)

def render_about():
st.markdown('<div class="section"><div class="card-title">About</div></div>', unsafe_allow_html=True)
st.markdown(""" <div class="section"> <p class="about-text">
Aditya Creative Studio is a modern digital studio focused on storytelling, design, and intelligent solutions.
We merge creativity with technology to craft premium digital experiences that elevate brands and inspire audiences. </p> <div class="section-divider"></div> <p class="about-text">
Our vision is to redefine digital storytelling through cinematic design, emotional engagement, and future-ready AI solutions. </p> </div>
""", unsafe_allow_html=True)

def render_contact():
st.markdown('<div class="section"><div class="card-title">Contact</div></div>', unsafe_allow_html=True)
with st.container():
st.markdown('<div class="contact-container">', unsafe_allow_html=True)
name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")
if st.button("Submit"):
if not name or not email or not message:
st.error("Please fill in all fields.")
else:
st.success("Thank you for reaching out. We will get back to you soon.")
st.markdown('</div>', unsafe_allow_html=True)

def render_footer():
st.markdown(""" <div class="footer"> <div class="footer-brand">Aditya Creative Studio</div> <div>© 2026 Aditya Creative Studio. All rights reserved.</div> <div>Instagram • LinkedIn • YouTube</div> </div>
""", unsafe_allow_html=True)

def main():
st.set_page_config(
page_title="Aditya Creative Studio",
page_icon="🎬",
layout="wide",
initial_sidebar_state="collapsed"
)
inject_css()
render_nav()
page = st.session_state.get("page", "Home")
if page == "Home":
render_home()
elif page == "Portfolio":
render_portfolio()
elif page == "Services":
render_services()
elif page == "About":
render_about()
elif page == "Contact":
render_contact()
render_footer()

if **name** == "**main**":
main()
