###############################################################
# +=========================================================+ #
# |     Python / Streamlit Sample Web Page - Portifolio     | #
# +=========================================================+ #
# | Author   : JOSE TEOTONIO DA SILVA NETO [TEO]            | #
# | Objective: Build a simple web page                      | #
# | Version  : 1.0.0.0                                      | #
# +=========================================================+ #
# | Name   | Changed At | Description                       | #
# +=========================================================+ #
# | Teo    | 15/11/2023 | Build Starter Version             | #
# +=========================================================+ #
###############################################################

# +=========================================================+ #
# | Libraries necessaries to execute current project        | #
# +=========================================================+ #
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

# +=========================================================+ #
# | For more emojis search at:                              | #
# | https://www.webfx.com/tools/emoji-cheat-sheet/          | #
# +=========================================================+ #

# +=========================================================+ #
# | Page Title of current project                           | #
# +=========================================================+ #
st.set_page_config(
    page_title = "Portifolio Teo", 
    page_icon=":floppy_disk:",
    layout="wide")

# +=========================================================+ #
# | Animated Charater from lottie                           | #
# +=========================================================+ #
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# +=========================================================+ #
# | CSS configuration from file                             | #
# +=========================================================+ #
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles/style.css")

# +=========================================================+ #
# | Header Section - Social Media Links                     | #
# +=========================================================+ #
"""
[![Star](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/teonett)
[![Follow](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/teo-jose-teotonio-9840a4a/)

# Hy, I am Teo :wave:

"""

# +=========================================================+ #
# | Load Section - Images on current Project                | #
# +=========================================================+ #
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_coding = Image.open("images/coding.jpg")
img_frontend = Image.open("images/frontend.gif")
img_contact = Image.open("images/contact.jpg")

# +=========================================================+ #
# | Sidebar Section                                         | #
# +=========================================================+ #
st.markdown('---')
st.sidebar.image('https://teonett.github.io/assets/img/about-img.jpg', width=200)
st.sidebar.markdown("# A System Analyst from Brazil")
st.sidebar.markdown("I am passionate about finding ways to be more efficient and effective in building solutions of an immersive way, and in moments of great pressure, I always try to convert in opportunities to make the best solutions or decision.")
st.sidebar.markdown("[More about me](https://teonett.github.io)")
st.sidebar.markdown('---')
st.sidebar.write('Developed by Jose Teotonio')
st.sidebar.write('[![Star](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](teonett@gmail.com)')

# +=========================================================+ #
# |Soft Skills - What I do                                  | #
# +=========================================================+ #
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            Enthusiastic about new technologies, managing projects (processes, costs, deadlines and documentation identifying opportunities and enhancing the delivery of results.

            Working in a large variety of projects and different departments, integration data, flexibility, expansion of capacity of current  resources, adopting the solution to real context of reality.

            My commitment consists to add value to work done and features building solutions using C#, Visual Basic, VBA, HTML, CSS, Javascript, PHP, Java, C++, Python and COBOL.
            """
        )

    with right_column:
        st_lottie(lottie_coding,  key="coding")

# +=========================================================+ #
# |Soft Skills - Soft Skills                                | #
# +=========================================================+ #
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.image(img_frontend, width=550)
    with right_column:
        st.subheader("Full Stack Developer")
        st.write(
            """
            Sprint goals planning, refinement, daily retrospectives, peer code reviews, write automated unit/integration tests, documentation and release notes to support, effectively communicate technical concepts to both technical and non-technical audiences.
            """
        )
        st.subheader("Business Analyst")
        st.write(
            """
            Immersive analysis, functional and technical specification, planning, survey, modeling, creation, implementation, evolution and documentation, acting as a translator between the user's need and the creation of the solution.
            """
        )

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Stock Markets and Insure")
        st.write(
            """
            Working in a brokerage house for more than 18 years in the IT area, where I also obtained certifications as a Broker adquire expertise in banking products mainly in Treasury, Fixed Income, Variable Income, Equities, Currency, Futures, Swap.
            """
        )
        st.subheader("Data Base Analyst (DBA)")
        st.write(
            """
            Administration of Relational Databases (Oracle, SQL Server, MySQL, PostgreSQL). Instation, configuration, identifying and solving problems, maintaining data security and integrity, analyzing and devising new ways to boost the environment.
            """
        )
    with right_column:
        st.image(img_coding, width=450)

# +=========================================================+ #
# | Contact Form                                            | #
# | # Documention: https://formsubmit.co/                   | #
# +=========================================================+ #
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/teonett@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Nome" required>
        <input type="email" name="email" placeholder="E-mail" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.image(img_contact, width=440)
    with right_column:
        st.markdown(contact_form, unsafe_allow_html=True)