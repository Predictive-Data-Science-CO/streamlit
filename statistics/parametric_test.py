import streamlit as st
from scipy.stats import pearsonr
from scipy.stats import ttest_ind
from scipy.stats import ttest_rel
from scipy.stats import f_oneway

st.header("Parametric Test")

st.markdown("""
            In summary, based on central limit theorem, parametric test is the most commonly used tests.  
            [check out this blog post](https://blog.minitab.com/en/adventures-in-statistics-2/choosing-between-a-nonparametric-test-and-a-parametric-test)   
            (Requirements: sample is size is > 20, > 50 if population is extremely skewed)        
            """)

CHOICES = {1: "Student's t-test", 2: "Paired Student's t-test", 3: "Analysis of Variance Test (ANOVA)", 4: "Pearson’s Correlation Coefficient"}
option_key = st.selectbox("Select a test", CHOICES.keys(), format_func=lambda x:CHOICES[ x ])
option_value =  CHOICES[option_key]
st.write(f"You selected test: {option_value}")

st.header(f"{option_value}")

code = """
    data1 = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
    data2 = [0.353, 3.517, 0.125, -7.545, -0.555, -1.536, 3.350, -1.578, -3.537, -1.579]    
""" if option_key !=3 \
else \
"""
    data1 = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
    data2 = [1.142, -0.432, -0.938, -0.729, -0.846, -0.157, 0.500, 1.183, -1.075, -0.169]
    data3 = [-0.208, 0.696, 0.928, -1.148, -0.213, 0.229, 0.137, 0.269, -0.870, -1.204]
"""
st.code(code)

data1 = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
data2 = [0.353, 3.517, 0.125, -7.545, -0.555, -1.536, 3.350, -1.578, -3.537, -1.579]
data3 = [1.142, -0.432, -0.938, -0.729, -0.846, -0.157, 0.500, 1.183, -1.075, -0.169]
data4 = [-0.208, 0.696, 0.928, -1.148, -0.213, 0.229, 0.137, 0.269, -0.870, -1.204]

match option_key:
    case 1:
        stat, p = ttest_ind(data1, data2)
    case 2:
        stat, p = ttest_rel(data1, data2)
    case 3:
        stat, p = f_oneway(data1, data3, data4)
    case 4:
        stat, p = pearsonr(data1, data2)    
    case _:
        ""

st.text('stat=%.3f, p=%.3f' % (stat, p))

st.text("interpret: alpha = 0.05")
alpha = 0.05
if p > alpha:
    if option_key in ({4}):
        st.text(f"p > {alpha} : Probably independent")
    else:
        st.text(f"p > {alpha} : Same distribution (fail to reject H0)")
else:
    if option_key in ({4}):
        st.text(f"p <= {alpha} : Probably dependent")
    else:
        st.text(f"p <= {alpha} : Different distribution (reject H0)")	          



 