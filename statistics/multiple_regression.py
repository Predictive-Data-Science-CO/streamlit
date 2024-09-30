import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

st.markdown(""" 
            ## Multiple Regression
            - sample question
            1. predict the exam score based on hours studied and hours slept
            """)

# Independent variables
X1 = np.array([2, 3, 5, 7, 9])
X2 = np.array([8, 7, 6, 5, 4])

# Dependent variable
Y = np.array([81, 89, 93, 91, 97])

st.text("X1: Hours studied")
st.text(X1)
st.text("X2: Hours slept")
st.text(X2)
st.text("Y: Exam score")
st.text(Y)

# Add a column of ones to include the intercept in the model
X = np.column_stack((np.ones(len(X1)), X1, X2))

# Calculate the coefficients
beta, _, _, _ = np.linalg.lstsq(X, Y, rcond=None)
st.text(f"Coefficients: {beta}")

# Predict the exam scores
Y_pred = X @ beta
st.text(f"Predicted scores: {Y_pred}")

# Calculate R-squared
ss_res = np.sum((Y - Y_pred) ** 2)
ss_tot = np.sum((Y - np.mean(Y)) ** 2)
r_squared = 1 - (ss_res / ss_tot)
st.text(f"R-squared: {r_squared}")

fig, ax = plt.subplots()
ax.scatter(Y, Y_pred)
ax.set_xlabel('Actual Values')
ax.set_ylabel('Predicted Values')
ax.set_title('Actual vs Predicted Values')

st.pyplot(fig)


