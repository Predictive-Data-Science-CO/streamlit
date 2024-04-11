import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title

st.set_page_config(
    page_title="Streamlit demo",
    page_icon="🧰"
)

# Either this or add_indentation() MUST be called on each page in your
# app to add indendation in the sidebar
add_page_title()

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("Home.py", "Home", ""),
        #Page("pages/Sales.py", "Sales", ""),
        Section("Section1", icon=""),
        Section("Section2", icon=""),
        # Pages after a section will be indented
        Page("pages/Dashboard.py", icon=""),
        Page("pages/Editing.py", icon=""),
        Section("Section3", icon=""),
        # Unless you explicitly say in_section=False
        #Page("Not in a section", in_section=False)
    ]
)