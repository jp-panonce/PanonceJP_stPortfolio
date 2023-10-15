import streamlit as st

st.set_page_config(page_title="JP's Portfolio",page_icon="📃",layout="wide")

st.markdown("# 🤵 MEET ENGINEER JP")

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
    st.text(" 📧 jpasensi13@gmail.com \n 📞 (+63) 945-340-4489 \n 📌 Cebu City, Philippines")
    pdfFileObj = open('docs/Panonce, John Paul - Resume.pdf', 'rb') 
    st.sidebar.download_button('Download Resume',pdfFileObj,file_name='PanonceJohnPaul_resume.pdf',mime='pdf')