import streamlit as st
import os

st.set_page_config(page_title="JP's Portfolio",page_icon="🔨",layout="wide")
st.markdown("# 🔨 MY SKILLS")

# To get only files present in a path
images_list = os.listdir(path=r"images")

# create list of images related to a skill (by having sk_ prefix) while excluding directories (identified as having no extension)
for val in images_list:

    if (("." not in val) or ("sk_" not in val)):
        images_list.remove(val)

#Sort list alphabetically
images_list.sort()

#add the relative directory path
images_list_wRelativePath = ["images/" + x for x in images_list]
    
#Create list of Skill Names
skillName_list = [(x.replace("_"," ")[3:x.rfind('.')]) for x in images_list]

# ========================================

skill_statements = {
    "Software Development":[
        "Create VBA scripts for MS Excel, Outlook, Word and Powerpoint",
        "Develop Android applications using Android Studio wiith Javaa",
    ],
    "Engineering":[
        "Calibrate and test industry-rated sensors",
    ],
    "Design":[
        "Create UI Designs for Websites and/or applications using Adobe XD",
    ],
    "Project Management":[
        "Able to work with project management tools such as Jira, Notion, Trello",
        "Able to work with Projects using the Agile Management approach which includes Kanban, Scrum, Lean or Extreme Programming."
    ],
    "Data":[
        "Create web scraping scripts using Selenium to get large number of data from webpages",
        "Perform Data and Statistical Analysis using MS Excel, Python, R",
        "Perfrom and apply SQL queries",
    ],
    "Web Development":[
        ""
    ]
}

app_list = {
    "Adobe XD": ["Design"],
    "Android": ["Software Development"],
    "Android Studio": ["Software Development"],
    "Arduino": ["Software Development", "Engineering"],
    "HTML": ["Software Development","Web Development"],
    "Java": ["Software Development"],
    "JavaScript": ["Software Development","Web Development"],
    "Jira": ["Project Management"],
    "MS Excel": ["Data"],
    "Power BI": ["Data"],
    "Python": ["Data","Software Development","Web Development"],
    "Proteus": ["Engineering"],
    "ISO 26262":["Engineering"],
    "MATLAB": ["Data","Engineering"],
    "R": ["Data","Software Development"],
    "Raspberry Pi": ["Engineering"],
    "SQL": ["Data"],
    "MathCAD":["Engineering"],
    "AutoCAD":["Engineering"],
    "Pandas":["Data","Software Development"],
    "Adobe Photoshop":["Design"],
    "Figma":["Design"],
    "Notion":["Project Management"],
    "Agile":["Project Management"],
    "Selenium":["Data","Software Development"],
    "HTML": ["Software Development"],
    "CSS": ["Software Development","Web Development"],
    "Postman": ["Software Development"],
    "VBA": ["Software Development"],
    "C": ["Software Development"],
    "C++": ["Software Development"],
    "UIPath": ["Software Development"],
    "Trello": ["Software Development"],
    "SQL Developer": ["Data"],
    "Tableau": ["Data"],
    "Oracle Database":["Data"],
    "Processing":["Software Development"],
    "TensorFlow":["Data","Software Development"]
}

skillCategory_list = ["Software Development","Engineering","Data","Design","Project Management","Web Development"]
filter_programming = st.multiselect(
    'Select Category',
    skillCategory_list
)


# === Display skills according to selected skill category
skillCategory_todisplay = (filter_programming if filter_programming else skillCategory_list)
for skillCategory in skillCategory_todisplay:
    
    # skill category title
    st.markdown("## " + skillCategory)

    # create columnns: Structure [details, sp, 5*(skill_icon),sp] where sp - spacing
    sk_cols = st.columns([1.5,0.05,0.25,0.25,0.25,0.25,0.25,0.08])

    # Details column
    with sk_cols[0]:    
        st.markdown(" - " + " \n - ".join(skill_statements[skillCategory]))
        
    # display Skills Icons with 5 icons per row
    i = 2
    idx = 0
    for img in images_list_wRelativePath:
        
        # display only if under the current skill category
        if skillCategory in app_list[skillName_list[idx]]:
            with sk_cols[i]:
                st.image(img,width=60,caption=skillName_list[idx])
                i+=1

            # go to next row if 5 icons have been displayed in current row
            if i == 7:
                i = 2
        idx+=1
    
    st.divider()