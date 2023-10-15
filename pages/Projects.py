import streamlit as st

st.set_page_config(page_title="JP's Projects",page_icon="📃",layout="wide")


project_list = [
    {
        "project_name": "KANRI",
        "project_type": "excel",
        "project_image":"https://static.streamlit.io/examples/dog.jpg", 
        "project_links":[
            ["Github", "https://github.com/jpasensi/kanri"]
        ], 
        "description":"An excel tool for Project Managers. This tool provides the basic needs of a project manager such as: \n - Budget \n - Contact Lists \n - Gantt \n - Dashboard", 
        "used_platform": ["Excel, VBA"]
    },
    {
        "project_name": "2023 Popular Songs in Spotify | Streamlit",
        "project_type": "data",
        "project_image": "https://static.streamlit.io/examples/dog.jpg", 
        "project_links": [
            ["Github", "https://github.com/jpasensi/spotify2023_streamlitViz"],
            ["Streamlit", "https://spotify2023appviz-jpanonce.streamlit.app"],
        ], 
        "description": "This project is for something chuchuchu", 
        "used_platform": ["Streamlit", "Python", "Pandas", "Altair"]
    },
    {
        "project_name": "Trigonometric Functions Visualizer | Processing",
        "project_type": "programming",
        "project_image":"https://static.streamlit.io/examples/dog.jpg", 
        "project_links":[
            ["Github", "https://github.com/jpasensi/TrigFXinUnitCircle"]
        ], 
        "description":"An interactive simulation which visualizes all the basic Trigonometric Functions. This is useful for learning the basic Trigonometric concepts", 
        "used_platform": ["Processing"]
    },
    {
        "project_name": "How Many Digits of Pi do you know? | Processing",
        "project_type": "programming",
        "project_image":"https://static.streamlit.io/examples/dog.jpg", 
        "project_links":[
            ["Khan Academy", "https://www.khanacademy.org/computer-programming/how-many-digits-of-pi-do-you-know/4986016234"]
        ], 
        "description":"A mini game which checks how many digits of the irrational number, Pi you memorized.", 
        "used_platform": ["JavaScript","ProcessingJS"]
    },
    {
        "project_name": "Finance Management Tool",
        "project_type": "programming",
        "project_image":"https://static.streamlit.io/examples/dog.jpg", 
        "project_links":[
            ["Khan Academy", "https://www.khanacademy.org/computer-programming/how-many-digits-of-pi-do-you-know/4986016234"]
        ], 
        "description":"A mini game which checks how many digits of the irrational number, Pi you memorized.", 
        "used_platform": ["JavaScript","ProcessingJS"]
    },

]

def setProjectView(tab_name,project_name, project_image, project_links, description, used_platform):
    # with st.expander("## PROJECT 1"):   
    tab_name.header(project_name)

    col_prog_1, colSpac1, col_prog_2, col_prog_3,colSpac2 = tab_name.columns([1.5,0.1,3,0.8,0.2]) 

    with col_prog_1:
        st.image(project_image)

    with col_prog_2:
        st.markdown("Languages/Platform: __" + (", ".join(used_platform)) + "__")
        st.markdown(description)
    
    with col_prog_3:
        # PROJECT LINK BUTTONS
        for projLink in project_links:
            st.link_button("View in " + projLink[0], projLink[1])

    tab_name.divider()
    pass

# Create tab per category
tab_prog, tab_data, tab_excel = st.tabs(["PROGRAMMING", "DATA", "EXCEL"])

# Dictionary of Tabs according to project_type
dict_projectType = {
    "programming": tab_prog,
    "data": tab_data,
    "excel": tab_excel,
}

# Adds a Filter for Languages/Platforms for Programming Projects
filter_programming = tab_prog.multiselect(
    'Filter according to Language/Platform',
    ["Web","Mobile","C","Android","Swift","Web","Excel","VBA"]
)

# SET PROJECTS
for project in project_list:

    # if project["project_type"] == "programming":
    toDisplay = 1

    if bool(toDisplay):
        setProjectView(
            tab_name = dict_projectType[project["project_type"]], 
            project_name = project["project_name"],
            project_image = project["project_image"], 
            project_links = project["project_links"],
            description = project["description"], 
            used_platform = project["used_platform"]
        )    
