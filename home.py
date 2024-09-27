import streamlit as st

if "role" not in st.session_state:
    st.session_state.role = None

ROLES = [None, "Classification", "Regression", "ML"]


def login():

    st.header("Log in")
    role = st.selectbox("Choose your role", ROLES)

    if st.button("Log in"):
        st.session_state.role = role
        st.rerun()


def logout():
    st.session_state.role = None
    st.rerun()


role = st.session_state.role

logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
settings = st.Page("settings.py", title="Settings", icon=":material/settings:")
outlier_detection = st.Page(
    "classification/outlier_detection.py",
    title="Outlier Detection",
    icon=":material/help:",
    default=(role == "Classification"),
)
classification_2 = st.Page(
    "classification/classification_2.py", title="classification 2", icon=":material/bug_report:"
)
regression_1 = st.Page(
    "regression/regression_1.py",
    title="Regression 1",
    icon=":material/healing:",
    default=(role == "Regression"),
)
regression_2 = st.Page(
    "regression/regression_2.py", title="regression 2", icon=":material/handyman:"
)
ml_1 = st.Page(
    "ml/ml_1.py",
    title="ml 1",
    icon=":material/person_add:",
    default=(role == "ML"),
)
ml_2 = st.Page("ml/ml_2.py", title="ml 2", icon=":material/security:")

account_pages = [logout_page, settings]
classification_pages = [outlier_detection, classification_2]
regression_pages = [regression_1, regression_2]
ml_pages = [ml_1, ml_2]

# st.title("Select Project")
st.logo("images/horizontal_blue.png", icon_image="images/icon_blue.png")

page_dict = {}
if st.session_state.role in ["Classification"]:
    page_dict["classification"] = classification_pages
if st.session_state.role in ["Regression"]:
    page_dict["regression"] = regression_pages
if st.session_state.role == "ML":
    page_dict["ml"] = ml_pages

if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()