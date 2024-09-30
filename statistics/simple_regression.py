import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

st.markdown(""" 
            ## Simple Linear Regression
            - sample question
            1. What is the effect of income on longevity?
            """)

rng = np.random.default_rng()

x = rng.random(10)
y = 1.6*x + rng.random(10)

st.text("x")
st.text(x)
st.text("y")
st.text(y)

res = stats.linregress(x, y)

st.text(f"R-squared: {res.rvalue**2:.6f}")

fig, ax = plt.subplots()
plt.plot(x, y, 'o', label='original data')
plt.plot(x, res.intercept + res.slope*x, 'r', label='fitted line')
plt.legend()

st.pyplot(fig)



 
