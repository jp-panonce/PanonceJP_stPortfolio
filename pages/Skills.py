import streamlit as st
import os

st.set_page_config(page_title="JP's Portfolio",page_icon="📃",layout="wide")

st.markdown("# 🤵 MY SKILLS")

# To get only files present in a path
images_list = os.listdir(path=r"images")
 
# Loop through each value in the list_2
for val in images_list:
   
    # Remove the value from list_2 if the "." is 
    # not present in value
    if "." not in val:
        images_list.remove(val)


st.image( ["images/" + x for x in images_list],width=50)



st.divider()

# === SOFTWARE/WEB DEVELOPMENT
st.markdown("## Programming")

# === ENGINEERING
st.markdown("## Engineering")

# === DATA
st.markdown("## Data")

# === Skills
st.markdown("## Design")

# === HOBBIES
st.markdown("## Methods")