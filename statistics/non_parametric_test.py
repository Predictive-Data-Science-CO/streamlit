import streamlit as st
from numpy.random import seed
from numpy.random import randn
from numpy import mean
from numpy import std
from scipy.stats import mannwhitneyu
from scipy.stats import wilcoxon
from scipy.stats import kruskal
from scipy.stats import friedmanchisquare

st.header("Non-Parametric Test")
st.markdown("""
            Reasons to use non- parametric tests  
            [check out this blog post](https://blog.minitab.com/en/adventures-in-statistics-2/choosing-between-a-nonparametric-test-and-a-parametric-test)   
            (Reasons: median is preferred, very small sample size, only has ordinal data or outliers can't be removed)        
            """)

st.markdown(""" 
            | Non-parametric      | Parametric      | Apply for                          |
            |---------------------|-----------------|------------------------------------|
            | Mann-Whitney U test | Student t-test  | Comparing independent data samples |
            | Wilcoxon signed-rank test | Paired student t-test | Comparing paired data samples |
            | Kruskal-Wallis H and Friedman tests | ANOVA and repeated measures ANOVA tests | Comparing more than two data samples |
            | Spearmans's coefficient | Pearson's coefficient | Measuring linear corrleation of two data sets |
            | Chi square test |  | Measuring whether two categorical variables are related to each other|
            """)

CHOICES = {1: "Mann-Whitney U test", 2: "Wilcoxon signed-rank test", 3: "Kruskal-Wallis H Test", 4: "Friedman Test"}
option_key = st.selectbox("Select a test", CHOICES.keys(), format_func=lambda x:CHOICES[ x ])
option_value =  CHOICES[option_key]
st.write(f"You selected test: {option_value}")

st.header(f"{option_value}")

# seed the random number generator
seed(1)

st.text("generate two sets of univariate observations")

code = """
    data1 = 5 * randn(100) + 50
    data2 = 5 * randn(100) + 51
""" if option_key in (1,2) \
    else \
"""
    data1 = 5 * randn(100) + 50
    data2 = 5 * randn(100) + 50
    data3 = 5 * randn(100) + 52
"""

st.code(code)
data1 = 5 * randn(100) + 50
data2 = 5 * randn(100) + 51 
data3 = 5 * randn(100) + 52

st.text("summarize")
st.text('data1: mean=%.3f stdv=%.3f' % (mean(data1), std(data1)))
st.text('data2: mean=%.3f stdv=%.3f' % (mean(data2), std(data2)))

st.text("compare samples")

match option_key:
    case 1:
        stat, p = mannwhitneyu(data1, data2)
    case 2:
        stat, p = wilcoxon(data1, data2)
    case 3:
        stat, p = kruskal(data1, data1, data3)  
    case 4:
        stat, p = friedmanchisquare(data1, data1, data3)                   
    case _:
        "No test selected"

st.text('Statistics=%.3f, p=%.3f' % (stat, p))

st.text("interpret: alpha = 0.05")
alpha = 0.05
if p > alpha:
    st.text(f"p > {alpha} : Same distribution (fail to reject H0)")
else:
    st.text(f"p <= {alpha} : Different distribution (reject H0)")	


st.markdown("""
            References    
            - [nonparametric-statistical-significance-tests-in-python](https://machinelearningmastery.com/nonparametric-statistical-significance-tests-in-python/) 
            - [17 Statistical Hypothesis Tests in Python (Cheat Sheet)](https://machinelearningmastery.com/statistical-hypothesis-tests-in-python-cheat-sheet/) 
            """)