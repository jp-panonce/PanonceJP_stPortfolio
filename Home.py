import streamlit as st

st.set_page_config(page_title="JP's Portfolio",page_icon="📃",layout="wide")

st.markdown("# 🤵 MEET ENGINEER JP")

col1_home, sp_home, col2_home = st.columns([0.7,0.1,1])

with col1_home:

    st.image("images/PanonceJP_mainPic.jpg",use_column_width=True)

with col2_home:
    st.markdown("### A people-centric designer and programmer with a passion for efficiency and automation")
    st.markdown("Hello! I’m JP, a designer, programmer and engineer powered by people and problems big or small. \n My superpower is  [materialize] - materializing all your ideas, and turning them into something that can make your life easier. ")
    st.caption("Currently @ Kuehne Nagel ISC | Cebu as a RPA (Robotics & Process Automation) Specialist ")

# === PERSONAL INFO
st.markdown("## Personal Information")

# === EDUCATION JOURNEY
st.markdown("## Educational Journey")

# === CAREER JOURNEY
st.markdown("## Career")

# === Skills
st.markdown("## Skills")

# === HOBBIES
st.markdown("## Playground")

with st.sidebar:
    st.caption('Wish to connect?')
    st.text(" 📧 jpasensi13@gmail.com \n 📞 (+63) 945-340-4489")
    pdfFileObj = open('docs/Panonce, John Paul - Resume.pdf', 'rb') 
    st.sidebar.download_button('Download Resume',pdfFileObj,file_name='PanonceJohnPaul_resume.pdf',mime='pdf')