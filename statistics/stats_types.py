import streamlit_mermaid as stmd
import streamlit as st

st.title("Statistics Types")

code = """
graph TD
    A[Predictor variable] --> B[Categorical or quantitative?]
    B -- Categorical --> C[Outcome variable: categorical or quantitative?]
    B -- Quantitative --> D[Outcome variable: categorical or quantitative?]
    C -- Categorical --> E[Non-parametric test]
    C -- Quantitative --> F[Comparision of mean test]
    D -- Categorical --> G[Logistic regression]
    D -- Quantitative --> H[How many predictor variables?]    
"""

mermaid = stmd.st_mermaid(code)
st.write(mermaid)
